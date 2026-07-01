# SE Roofing — Brand Guidelines

Single source of truth for SE Roofing's brand, marketing, and website design system. Anyone (or any AI tool) working on SE Roofing materials should start here.

## Repo map

| Folder | What lives here |
|---|---|
| [`brand/logos`](brand/logos) | The SE logo and its usage rules (clear space, minimum size, do/don't) |
| [`brand/typography`](brand/typography) | Approved typefaces, weights, and hierarchy |
| [`brand/color`](brand/color) | Brand color palette (hex/RGB/CMYK) and usage |
| [`brand/voice-and-messaging`](brand/voice-and-messaging) | Brand voice, tone, taglines, core messaging pillars |
| [`marketing/assets`](marketing/assets) | Existing marketing materials (flyers, ads, one-pagers, etc.) |
| [`marketing/playbook`](marketing/playbook) | The marketing playbook — how we position and market SE Roofing |
| [`marketing/campaigns`](marketing/campaigns) | Campaign-specific assets and briefs |
| [`website/design-system`](website/design-system) | Design tokens/components used on the SE Roofing website |
| [`website/content`](website/content) | Website copy and content guidelines |
| [`ai`](ai) | Reference doc for AI tools/agents generating SE Roofing content |
| [`docs`](docs) | Contribution guidelines for this repo |

## Status

- [x] Standing SE logo files (PNG + print-ready EPS, both color variants) → `brand/logos/`
- [x] Brand colors — exact Pantone/CMYK + sampled digital hex → `brand/color/`
- [x] Typography — confirmed typeface system + a flagged inconsistency to resolve → `brand/typography/`
- [x] Messaging/voice — taglines, pillars, boilerplate pulled from real collateral + roofingse.com → `brand/voice-and-messaging/`
- [x] Two marketing materials (Capabilities Statement, Gio Becerril bio) → `marketing/assets/`
- [ ] Marketing playbook — not yet located/provided → `marketing/playbook/`
- [ ] Decide whether to import the rest of the existing marketing library (proposal template, second bio, photos, video, folder artwork) — see `marketing/assets/README.md`
- [ ] Resolve the Bio-template font inconsistency — see `brand/typography/README.md`
- [ ] Author `ai/brand-brief.md` once the playbook is in and the open items above are resolved

## Conventions

- File names: lowercase, hyphen-separated (`se-logo-primary.svg`, not `SE Logo Final(2).svg`).
- Keep source/editable files (`.ai`, `.psd`, `.fig`) alongside exported/final files (`.svg`, `.png`, `.pdf`) — note which is which in the folder's README.
- Update the relevant `README.md` whenever you add or retire an asset — this repo is only useful if it stays current.
