# Typography

Extracted directly from the embedded fonts in the existing, professionally-designed collateral: the **Capabilities Statement** and **Proposal Template** (both `marketing/assets/`). These two documents agree with each other, so this is the confirmed system.

## Primary typeface system (confirmed — used in Capabilities Statement + Proposal Template)

| Role | Typeface | Weight(s) present | Where used |
|---|---|---|---|
| Headings / display | **Museo Sans** | 900 (Black) | Big stat callouts, "WHY CHOOSE SE ROOFING" icon labels |
| Primary heading | **Proxima Nova** | Bold | Section headlines ("EXECUTION-DRIVEN ROOFING") |
| Secondary heading / eyebrow | **Proxima Nova** | Light | Eyebrow text ("YOUR PARTNER IN ROOFING", "OPERATOR-OWNED") |
| Body copy | **Proxima Nova** | Regular, Light | Paragraph text, list items |
| Italic accents | **Proxima Nova** | Light Italic | Occasional emphasis/subheads |

**Proxima Nova is the workhorse** (regular/light/bold + light italic all appear); **Museo Sans 900** is the heavy display accent used sparingly for punch (icon captions, big numbers). This mirrors a lot of construction/industrial brands: a clean geometric sans for everything, one very heavy weight for emphasis.

## ⚠️ Inconsistency found — flag for a decision

The **Bio documents** (`Gio Becerril BIO.pdf`, and the shared `SE Bio Template.docx`/`.indd`) use a **completely different font set**:

- **NewScience** (Regular, Bold)
- **Rajdhani** (Bold)

Neither of these appears in the Capabilities Statement or Proposal Template. This means the Bio template was built separately (possibly earlier, or by a different designer) and was never brought in line with the primary system. **Decision needed**: either (a) restyle the Bio template to Proxima Nova/Museo Sans to match everything else, or (b) confirm NewScience/Rajdhani is an intentional secondary system for people-focused collateral and document it as such here. Left as-is for now — don't treat Rajdhani/NewScience as "the brand" until this is resolved.

## Licensing

Proxima Nova and Museo Sans are both commercial/licensed typefaces (Mark Simonson Studio and exljbris respectively, both distributed via Adobe Fonts/Monotype). Confirm the studio's license covers however you plan to use this repo (web embedding requires a webfont license distinct from the desktop/print license already in use for these PDFs). No font files are checked into this repo for that reason — license first, then add `.woff2` files here if cleared for web use.

## Web fallback stack (until licensed webfonts are confirmed)

```css
font-family: 'Proxima Nova', 'Museo Sans', 'Century Gothic', 'Avenir Next', sans-serif;
```

`Century Gothic`/`Avenir Next` are reasonable geometric-sans fallbacks that approximate Proxima Nova's character if the licensed webfont isn't loaded yet.
