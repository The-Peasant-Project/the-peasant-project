# Explainer Build Guide

House style for anything in `learning/`, for the primers in `docs/00` to `docs/03`, and for any agent asked to explain something. Follow it as a checklist, or paste Part 6 to an AI as instructions.

Source: Rob's explainer guide, September 2026. Kept verbatim below.

---

## Part 1 — Answer these five before writing

1. Who is this for, and what do they already know? One sentence.
2. What will they be able to do afterwards that they can't do now? One sentence. If you can't write it, stop and think again.
3. Which one to three ideas unlock everything else? Build the whole thing around these. Cut anything that doesn't serve them.
4. What does this audience probably believe that's wrong? List it. If you don't know, ask three people from the audience to explain the topic and note where they go wrong.
5. What concrete case will you open with?

## Part 2 — Write it in this order

1. Open with a specific case, question or surprise. Not a definition. Not history. Not "X is important because".
2. Make them commit. Ask them to guess, predict, or choose before you explain. One line is enough.
3. Name the wrong answer and kill it. Say the common misconception out loud, then say plainly why it fails. Skip this step if the audience doesn't already hold that belief — repeating a wrong idea to people who never had it makes it stickier.
4. Explain the real thing, built directly out of the case you opened with.
5. Generalise last. State the abstract rule only after they've watched it work.
6. Give a second example that looks different on the surface but works the same way underneath.
7. End with something they do — a question, a prediction, a small problem.

## Part 3 — Rules that always apply

Language: define every term in the sentence before it first appears, or don't use it. Short sentences. Write like you'd say it out loud. Conversational, not formal. "You" and "we", not "one" and "the reader".

Analogies: one per concept. Pick analogies where the relationships match, not where the things look alike. Always state where it breaks: "This is like X — except X doesn't do Y." An analogy with no stated limit becomes the next misconception.

Cutting: delete every number that isn't doing work. Delete anything interesting but not load-bearing. If a paragraph doesn't serve one of your one-to-three core ideas, cut it.

Layout: put the picture next to the words that describe it. Don't repeat narration as on-screen text. Break into segments the reader controls.

Tone: assume capability. Never signal that you've dumbed it down. Say when something is genuinely hard, and that being stuck is normal. Aim for "I could have worked that out myself", not "that was well explained".

## Part 4 — Review checklist

Any "no" is a rewrite.

- Does it open with something concrete rather than an abstraction?
- Does the reader do or decide something in the first minute?
- Is the common misconception named and refuted explicitly?
- Is every term defined before it's used?
- Does every analogy have a stated limit?
- Could I cut 20% without losing meaning? If yes, cut it.
- Is there a second, surface-different example?
- Would a beginner who finished this be able to apply it to a new case, not just recognise it?
- Have I tested it on someone who actually didn't know the topic?

## Part 5 — Warning signs

It feels smooth and satisfying: fluency creates a false sense of understanding. You started with a definition: that's the expert's order, not the learner's. You're proud of how much you covered: coverage is the enemy of understanding. You can't name what the reader will be able to do: then neither can they. You skipped a step because it's obvious: it's obvious to you, that's the whole problem. Your test is "did they like it?": test whether they can use it a week later.

## Part 6 — Paste-ready AI prompt

> You are writing an explanation of a complex topic for people who don't already know it.
>
> First, tell me: (a) who the audience is, (b) the one thing they'll be able to do afterwards, (c) the one to three ideas that unlock the topic, (d) the most likely wrong belief they already hold, (e) the concrete example you'll open with. Wait for my confirmation before writing.
>
> Then write in this order: concrete case first → ask the reader to predict or choose → name and refute the common misconception → explain the real mechanism using the opening case → state the general rule only now → give a second, surface-different example → end with something the reader does.
>
> Rules: define every term in the sentence before it first appears. One analogy per concept, and always state where it breaks. Cut any number that isn't load-bearing. Short sentences, conversational tone. Assume the reader is capable — never signal simplification. Say plainly when something is hard and that being stuck is normal. Never open with a definition, history, or why the topic matters.
>
> Goal: the reader should finish feeling they could have worked it out themselves.

---

## Known violations in this repo

- `docs/00-one-pager.md` opens with an abstraction ("Most of what we do online..."), not a case, and never asks the reader to commit. Rewrite it against Part 2. Candidate opening case: the town pool's gas bill.
