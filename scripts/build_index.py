#!/usr/bin/env python3
"""Build INDEX.md from the frontmatter of every document under docs/.

Human readable and agent readable. Run after adding or changing any document.
Requires pyyaml.
"""
import pathlib, re, yaml, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

def read_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    return yaml.safe_load(m.group(1))

entries = []
for path in sorted(DOCS.rglob("*.md")):
    fm = read_frontmatter(path)
    if not fm:
        continue
    fm["path"] = str(path.relative_to(ROOT))
    entries.append(fm)

lines = ["# INDEX", "",
         "Map of every document, generated from frontmatter by `scripts/build_index.py`.",
         "Humans: scan the summaries. Agents: load `AGENTS.md`, then only the documents whose tags or summary match your task.", "",
         "| Part | Id | Title | Status | Audience | Tags | Summary |", "|---|---|---|---|---|---|---|"]
for e in entries:
    lines.append("| {part} | `{id}` | [{title}]({path}) | {status} | {aud} | {tags} | {summary} |".format(
        part=e.get("part", ""), id=e.get("id", ""), title=e.get("title", ""), path=e["path"],
        status=e.get("status", ""), aud=", ".join(e.get("audience", [])),
        tags=", ".join(e.get("tags", [])), summary=e.get("summary", "").replace("|", "/")))

lines += ["", "## Open questions across the project", ""]
for e in entries:
    qs = e.get("open_questions") or []
    for q in qs:
        lines.append(f"- `{e.get('id')}`: {q}")

lines += ["", "## Machine-readable", "", "```json",
          json.dumps([{k: v for k, v in e.items() if k != "agent_guidance"} for e in entries], indent=1, ensure_ascii=False),
          "```", ""]
(ROOT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Indexed {len(entries)} documents.")
