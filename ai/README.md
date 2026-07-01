# AI Documentation

Reference material for AI tools/agents (Claude or otherwise) that generate or evaluate SE Roofing content — ads, social posts, emails, website copy, or design work.

## Purpose

An AI agent working on SE Roofing content won't have read this whole repo — it needs a short, concrete brief it can act on directly. This folder is that brief, not a copy of everything else. Link back to the source-of-truth docs rather than duplicating them.

## `brand-brief.md` (to author once `brand/` and `marketing/playbook/` are filled in)

Should be a single, dense doc covering:

- **Do use**: exact hex codes, approved typefaces, tagline(s), messaging pillars — pulled from `brand/color`, `brand/typography`, `brand/voice-and-messaging`
- **Don't**: banned words/phrases, competitor comparisons to avoid, tone mismatches (e.g. no fear-based storm-damage scare tactics if that's off-brand)
- **Logo usage**: link to `brand/logos` and the do/don't rules, since AI image tools regularly mishandle logo placement
- **Target audience**: pulled from `marketing/playbook`
- **Example outputs**: 2-3 short pieces of on-brand copy the agent can pattern-match against

## `prompts/`

Reusable prompt templates for common SE Roofing content tasks (e.g. "write a service-page paragraph for [service]", "write a social caption for [campaign]"). Add prompt files here as they're developed — see [`prompts/README.md`](prompts/README.md).

## Status

Not yet authored — this folder is scaffolded ahead of the underlying brand docs being filled in. Write `brand-brief.md` once `brand/` and `marketing/playbook/` have real content; a brief built on TBDs isn't useful yet.
