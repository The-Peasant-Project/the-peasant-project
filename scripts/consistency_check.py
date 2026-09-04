#!/usr/bin/env python3
"""Consistency check: read changed documents against the design constants,
principles, glossary and index, and report contradictions.

Runs locally (`make check`) or in the GitHub Action on pull requests.
Needs ANTHROPIC_API_KEY in the environment. Exits non-zero if the model
reports any contradiction marked severe, so the PR shows a red check.

Usage:
  python scripts/consistency_check.py                # checks all docs (slow)
  python scripts/consistency_check.py file1.md ...   # checks only these
"""
import os, sys, pathlib, subprocess, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODEL = os.environ.get("PEASANT_CHECK_MODEL", "claude-sonnet-4-6")

def read(p):
    return (ROOT / p).read_text(encoding="utf-8")

def changed_files(args):
    if args:
        return [pathlib.Path(a) for a in args]
    return sorted(ROOT.joinpath("docs").rglob("*.md"))

def rule_files_changed(files):
    rules = {"AGENTS.md", "docs/01-vision-and-principles.md"}
    return any(str(f.relative_to(ROOT) if f.is_absolute() else f) in rules for f in files)

def main():
    try:
        import anthropic
    except ImportError:
        print("pip install anthropic"); sys.exit(2)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY not set; skipping check."); sys.exit(0)

    files = changed_files(sys.argv[1:])
    context = {
        "AGENTS.md": read("AGENTS.md"),
        "principles": read("docs/01-vision-and-principles.md"),
        "glossary": read("docs/12-appendices/glossary.md"),
        "decision_log": read("docs/12-appendices/decision-log.md"),
        "index": read("INDEX.md")[:20000],
    }
    changed = {str(f): pathlib.Path(f).read_text(encoding="utf-8") for f in files if pathlib.Path(f).exists()}

    prompt = f"""You are the consistency check for The Peasant Project. Read the reference material, then the changed documents, and report every place a changed document contradicts a design constant in AGENTS.md, a principle, a decision log entry, or another document summarised in the index. Also report: a rule or constant that appears to have changed without a matching decision log entry; a new mechanism or claim with no row in the hand-waving register; a term used that the glossary does not define; any text that relies on goodwill rather than mechanism; any text that borrows an Indigenous practice as a mechanic.

Respond only with JSON: {{"findings": [{{"file": str, "severity": "severe"|"minor", "issue": str, "suggestion": str}}]}}. An empty list is a valid answer. Do not invent findings.

REFERENCE
{json.dumps(context, ensure_ascii=False)}

CHANGED DOCUMENTS
{json.dumps(changed, ensure_ascii=False)}
"""
    client = anthropic.Anthropic()
    msg = client.messages.create(model=MODEL, max_tokens=4000,
                                 messages=[{"role": "user", "content": prompt}])
    text = "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")
    text = text.strip().removeprefix("```json").removesuffix("```").strip()
    try:
        findings = json.loads(text)["findings"]
    except Exception:
        print("Could not parse model output:\n", text); sys.exit(2)

    severe = [f for f in findings if f.get("severity") == "severe"]
    print(f"{len(findings)} findings, {len(severe)} severe.\n")
    for f in findings:
        print(f"[{f['severity']}] {f['file']}\n  {f['issue']}\n  -> {f['suggestion']}\n")
    if rule_files_changed(files) and not any("decision" in f.get("issue", "").lower() for f in findings):
        print("Note: a rule file changed. Confirm a decision log entry exists.")
    sys.exit(1 if severe else 0)

if __name__ == "__main__":
    main()
