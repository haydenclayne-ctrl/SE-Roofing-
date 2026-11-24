# SE Roofing — Design System (proposal)

Status: **proposal only**, 24 November 2026, America/Chicago. Not owner-approved.
This document codifies the SE Roofing brand as already written in `haydenclayne-ctrl/SE-Roofing-` (guidelines recorded 1 July 2026 from logo vectors and existing collateral) and as already implemented in related product code and public sites. It does not invent a new look. Do not treat this file as permission to restyle the logo, the print system, Command, or the websites.

Machine-readable tokens: `tokens.json` and `tokens.css` in this folder. Inconsistencies and a prioritized list live in `audit.md`.

---

## 1. What this is, and what it is not

- **This company** is **SE Roofing** (public name, decided by Hayden on 24 November 2026). Use “SE Roofing Solutions LLC” only where the legal entity name is required. “Southeast Roofing Solutions” is retired and should not appear on public pages. It is a **commercial roofing subcontractor**, never a general contractor (per copy lead, pending Hayden confirmation). It works as an extension of the general contractor’s team, with in-house crews, on commercial, industrial, and government work. It is a **Roof Co Ventures operating company**.
- **Canonical brand source:** `haydenclayne-ctrl/SE-Roofing-` — `brand/color`, `brand/typography`, `brand/logos`, `brand/voice-and-messaging`. The repo itself says the current material is documented accurately but “not the final word,” and invites critique. This proposal keeps that posture: it records what exists, and flags conflicts; it does not pick a new brand.
- **Two-color brand.** The logo uses only SE Navy `#203A47` (PANTONE 7546 C) and SE Slate Blue `#456977` (PANTONE 5405 C), plus white. That pair is the brand. Roof Co gold and navy are a sibling identity, not this one.
- **Not** Roof Co Ventures / Command chrome. Command already keeps a separate `seroofing` token namespace with the same navy and slate (and two Command-only extras). Document that relationship; do not merge the two brands. Do not put Roof Co gold `#D0A255` or Roof Co navy `#233746` / `#243746` on SE-only materials.
- **Not** High Cotton Capital, Cotton Co, the Cotton Foundation, Blackhorn, Founders Ranch, Rental One, or Double Creek Ranch.
- **Not** unrelated companies on nearby domains (`seroofing.com` in Southwest Florida, `se-roofing.com` in Kissimmee, `seroofingsolutions.com` / SRS Roofing in Georgia).
- **Not** a request to restyle the logo. The marks in `brand/logos/` are the current production files.

---

## 2. Sources of truth

| Layer | Where | Status |
|---|---|---|
| Written brand | `haydenclayne-ctrl/SE-Roofing-` — start at `README.md`, then `brand/` | Recorded 1 July 2026 from Hayden-provided logo files and collateral. This proposal extracts it. |
| Logo artwork | `brand/logos/` — horizontal PNG lockup, icon/patch PNG, PMS and CMYK EPS, diagonal-lockup EPS | Shipping. No SVG. No white-knockout file in the repo, though the marketing site uses one. |
| Print collateral in-repo | `marketing/assets/slicks/se-capabilities-statement.pdf` (+ print PDF); `marketing/assets/bios/gio-becerril-bio.pdf` | Capabilities (InDesign, 29 May 2026) confirm Proxima Nova + Museo Sans 900. The Gio bio uses a different type system (NewScience + Rajdhani). Proposal template and other marketing files are cited but not in this repo. |
| Command / Estimating | `Roof-Co-Command` `app/tailwind.config.js` `seroofing` namespace (draft design-system PR #14); copied into `roofco-estimating` | Navy `#203A47`, steel `#456977`, mist `#E7E9EA` match the brand. Adds `steel-light` `#7E9BA7`. Type ships as Avenir Next until Proxima/Museo are licensed for web. |
| Estimate Command | `estimate-command` `src/app/globals.css` | SE-only palette (no Roof Co gold/navy). Navy and steel match. Ground `#F4F7F9`, muted `#6D7D88`, and status hexes **do not** match Command. Last push 10 July 2026; whether the app is retired is still Unknown. |
| Marketing website | Canonical URL in the site’s own tags: `https://www.roofingse.com`. The same Framer site is reachable at `https://seroofingteam.com` (audited 24 November 2026). `roofingse.com` / `www.roofingse.com` returned **HTTP 403** from this environment (curl, WebFetch, and Playwright). | Source is **not** in this GitHub account (Framer). Visual audit at 1440 and 390 via `seroofingteam.com`. No credentials used. |
| Gov capabilities microsite | `https://seroofinggov.com` (USFCR “Online Capabilities Statement”) | Live, audited 24 November 2026 at 1440 and 390. Generic template typography and Bootstrap colors, with the official color lockup and some Slate Blue. |
| This proposal | `docs/design-system/` in `SE-Roofing-`, with copies under `/home/box/creative-dept/se-roofing/design-system/` | Proposal only |

If the written brand (logo + `brand/` docs + Capabilities Statement) disagrees with a website or an app, **the written brand and the logo vectors win on brand facts** (the two colors, the marks, Proxima/Museo as the confirmed print system). Live sites and apps are evidence of how those facts are — or are not — implemented, including drifts in `audit.md`.

The website design-system folder in this repo is still an empty checklist. There is no coded SE component library here.

---

## 3. Brand direction

SE Roofing should feel like a **direct, execution-focused, operator-owned commercial roofing subcontractor**. Copy leads with capability and control: in-house crews, self-performed work, standardized practices, safety, and responsiveness. It should not sound flowery, vague, like a general contractor, or like a broker of subcontracted labor. Do not lead with “nationwide” until that claim is verified.

**Visual default in the confirmed print system:** navy and slate on white or light gray, often with a diagonal / cut-corner parallelogram (the framed lockup), short all-caps headline fragments, and gold-free pages. A navy→slate gradient on the icon mark is an acceptable treatment.

### Voice & copy

Voice: confident and plainspoken. Headlines are short, punchy, all-caps sentence fragments (“EXECUTION-DRIVEN ROOFING,” “OPERATOR-OWNED”), not long marketing sentences.

**Company description** (per copy lead, pending Hayden confirmation):

> SE Roofing is a commercial roofing subcontractor. We work as an extension of the general contractor’s team, with in-house crews and reliable execution on commercial, industrial, and government work.

Do not use “contractor / subcontractor” or “commercial roofing contractor.” Never describe SE as a general contractor.

**Short partnership lines:** “An extension of your team.” · “Your project. Our roofing expertise.” · “Built to support general contractors.”

**Safer homepage heroes** (either is fine): “COMMERCIAL ROOFING. SELF PERFORMED.” or “COMMERCIAL ROOFING YOU CAN COUNT ON.”

**Do not lead with, until verified:** “nationwide,” “Certified & Insured,” or “Guaranteed Results.” The recorded line “Trained Crews. Proven Materials. Guaranteed Results.” can stay in this inventory of existing copy, but it should not lead a page.

**Finish or pull** from live pages: “66% Projects Completed,” “6+ Service Coverage,” and the gov site’s TBD UEI / CAGE / NAICS codes. Incomplete stats and placeholder registrations should not stay public.

**Public name (decided 24 November 2026):** **SE Roofing.** Use “SE Roofing Solutions LLC” only where the legal entity name is required. “Southeast Roofing Solutions” is retired.

**Official phone (decided 24 November 2026):** **713-814-5251**, everywhere, including the gov site. Retired numbers: 281.965.9055 (still in the brand repo, capabilities PDFs, and README) and (281) 960-5459 (still on seroofinggov.com). Swap those leftovers for 713-814-5251; do not leave both in circulation.

**Taglines (as recorded 1 July 2026, inventory only):**

| Line | Where confirmed | Notes |
|---|---|---|
| “COMMERCIAL ROOFING YOU CAN COUNT ON” | Gio bio footer **and** the website (as of the July documentation) | Primary, confirmed in two sources then |
| “YOUR PARTNER IN ROOFING” | Capabilities Statement cover eyebrow | Print |
| “Built by roofers. Powered by our crews.” | Website (July notes); gov site as “BUILT BY ROOFERS, POWERED BY CREWS.” | Was flagged as site-only, pending a print decision |
| “Trained Crews. Proven Materials. Guaranteed Results.” | Website (July notes) | Same caveat |
| “COMMERCIAL ROOFING. SELF PERFORMED.” | Current marketing homepage hero (24 November 2026) | Not in the July brand docs. Now the dominant web headline. |

**Messaging pillars** (Capabilities Statement, as recorded): self-performed / in-house execution; consistency at scale; safety and compliance; responsiveness (24/7, rapid response, emergency work); national reach, locally rooted. Do not lead marketing with the “national reach / nationwide” pillar until it is verified.

**Services** (site, still current): Commercial Roofing · New Construction · Overlay & Restoration · Tear Off & Replacement.

**Boilerplate (short):** use the company description above. Do not reuse the older “commercial roofing contractor” boilerplate.

**Contact facts:** official phone **713-814-5251** (decided 24 November 2026) · web roofingse.com · HQ 5617 Campbell Rd, Houston, Texas 77041. The brand repo, capabilities PDFs, and README still list the retired number 281.965.9055; seroofinggov.com still lists (281) 960-5459. Those leftovers should be updated to the official number (see `audit.md`).

---

## 4. Color

This is a two-color brand. Neutrals support it. Anything else (Command steel-light, Estimate Command status colors, the marketing site’s orange) is an implementation extra until Hayden says otherwise.

### 4.1 Brand (from the logo vectors and `brand/color`)

Sampled from `se-roofing-full-lockup.png` and `se-roofing-icon-mark.png`: median and mean of the dark and mid clusters are exactly the documented hexes.

| Token | Hex | Print | Role |
|---|---|---|---|
| SE Navy | `#203A47` | PANTONE 7546 C · C86 M69 Y50 K46 | Primary — “S,” “ROOFING” wordmark, dark backgrounds, footers, headlines, body in the Capabilities Statement |
| SE Slate Blue | `#456977` | PANTONE 5405 C · C74 M47 Y33 K7 | Secondary — “E” bars, accent shapes, mid-tone panels, secondary headings |
| White | `#FFFFFF` | Paper | Page and section grounds; reverse type on navy or slate |
| Light gray / mist | `#E7E9EA` | — | Section grounds behind body copy in the Capabilities Statement. Marked **approximate** (visual inspection, not a vector swatch). Command’s `seroofing.mist` and Estimate Command’s `--color-line` use this same value. |

Print work must use the Pantone spots (or the CMYK builds in the EPS files), not a reconversion from hex. Web/digital work should hardcode `#203A47` / `#456977`.

**Contrast (measured):**

| Pair | Ratio | Notes |
|---|---|---|
| Navy on white | 11.95:1 | AAA body |
| White on navy | 11.95:1 | AAA body |
| Navy on mist | 9.81:1 | AAA body |
| Slate on white | **5.93:1** | **AA for normal text**, not AAA. The written color doc says slate on white is “roughly AA for large text only.” That note is too conservative — 5.93:1 passes AA at 14px. It is still reasonable to reserve slate for accents and large type if the team wants a stricter house rule. |
| White on slate | 5.93:1 | AA body |
| Slate on mist | 4.87:1 | AA body |
| Navy on slate | **2.01:1** | Fails. Do not put navy type on a slate panel (or the reverse). Use white or navy-on-white, matching the Capabilities Statement. |

A navy→slate gradient is already documented as an acceptable brand treatment for some icon-mark renderings (including the Bio PDF).

### 4.2 Command / Estimating `seroofing` namespace (already shared)

These values live in Command’s `tailwind.config.js` (and the file-copied Estimating config). Navy, steel, and mist **match** the brand. Keep the namespace separate from `roofco.*`.

| Token | Hex | Role |
|---|---|---|
| navy | `#203A47` | Same as SE Navy |
| steel | `#456977` | Same as SE Slate Blue |
| steel-light | `#7E9BA7` | **Command-only.** Not in `brand/color`. 2.94:1 on white — not body text. 4.06:1 on navy — large-text AA only. Accent / charts only. |
| mist | `#E7E9EA` | Same as the written light gray |

Command also has its own `surface.*` and `status.*` ramps (good `#2F6F52`, warn `#9C6A1E`, bad `#943B3B`, info `#2A5F76`) and Roof Co gold/navy. Those are product chrome, not the SE brand. Use them in Command when the UI is the Roof Co app; do not import Roof Co gold into SE sales slick.

### 4.3 Estimate Command (SE-only app, conflicts)

`estimate-command` cites `brand/color` and uses navy + steel correctly, then adds a local set that **does not match Command**:

| Token | Hex | vs Command | Contrast on white |
|---|---|---|---|
| bg | `#F4F7F9` | Command ground is `#F5F5F7`; live marketing ground is `#F5F7F9` (very close to this) | — |
| card | `#FFFFFF` | Matches | — |
| line | `#E7E9EA` | Matches mist | — |
| muted | `#6D7D88` | Command mute is `#8A939B` (also failing) | **4.25:1 — fails AA** for 14px text (large-text only) |
| brand-soft | `#E9EEF0` | No Command equivalent | — |
| success | `#2F8A5B` / soft `#E7F2EB` | Command good is `#2F6F52` / `#E4EFE9` | 4.28:1 — **fails AA** for 14px (Command good is 5.97:1, passes) |
| warning | `#B07A1E` / soft `#F7EFE0` | Command warn is `#9C6A1E` / `#F6EDDC` | 3.72:1 — large-text only (Command warn is 4.67:1, AA) |
| danger | `#C0504D` / soft `#F7EBEB` | Command bad is `#943B3B` / `#F5E4E4` | 4.67:1 AA (Command bad is 7.12:1) |

Radius in that app is 14px (`--radius-card`), a product decision, not an SE brand radius.

### 4.4 Live marketing site (observed 24 November 2026 — not official brand colors)

The Framer marketing site does **not** use the two-color logo palette as its UI system. Observed:

| Observed | Hex | Use |
|---|---|---|
| Ink / header button / “Learn More” | `#16272F` | Dark UI, near but **not** SE Navy `#203A47` |
| Heading ink | `#1A1A2E` | “Delivered At Scale” etc. |
| Stats panel / footer family | `#1D2D35`, `#182B33`, `#1E343D`, `#122023` | Deep teal-navy grounds |
| Orange CTA | `#D4762C` | Primary buttons (“Contact Us,” “Get a Free Estimate”), “Who We Are” chip. **Not** Roof Co gold, **not** in `brand/color`. White type on this orange is **3.27:1** — large-text AA only; the 15px button label fails AA. Black type would be 6.43:1. |
| Page ground | `#F5F7F9` | Light sections |
| Consult band | `#EBFBFF` | “Request a Roofing Consultation” |
| “Delivered At Scale” panel | `#CADAE4` | Light blue-gray |
| Overview eyebrow | `#CCE6FF` | On a dark service card |

Do not treat this orange, or these near-navy hexes, as the SE brand until a formal decision says the web system is allowed to diverge — or is brought back to navy/slate.

### 4.5 Gov microsite

`seroofinggov.com` uses the official color lockup correctly on white. The bar under the logo reads as slate-like, and `#456977` appears in the CSS. The rest of the page is a stock USFCR / Bootstrap palette (blues `#007BFF`, greys, success/warning/danger) and is **not** the SE brand system.

### 4.6 What not to use

- Roof Co navy `#233746` / `#243746` or Roof Co gold `#D0A255` on SE-only collateral
- HCC Gold `#CEA154`, Cotton Co black, Foundation golds, Rental One orange, Blackhorn or Founders Ranch palettes
- Recoloring the logo outside navy and slate
- Navy type on slate (2.01:1)

---

## 5. Typography

### 5.1 Confirmed print system (Capabilities Statement + Proposal Template)

Extracted from embedded fonts in the Capabilities Statement (both digital and print PDFs). Verified again 24 November 2026 with `pdffonts`:

| Role | Typeface | Weight | Use |
|---|---|---|---|
| Display / punch | **Museo Sans** | 900 (Black) | Big stat callouts, “WHY CHOOSE SE ROOFING” icon labels |
| Primary heading | **Proxima Nova** | Bold | Section headlines (“EXECUTION-DRIVEN ROOFING”) |
| Eyebrow / secondary heading | **Proxima Nova** | Light | “YOUR PARTNER IN ROOFING,” “OPERATOR-OWNED” |
| Body | **Proxima Nova** | Regular, Light | Paragraphs, lists |
| Italic accent | **Proxima Nova** | Light Italic | Occasional emphasis |

Proxima Nova is the workhorse; Museo Sans 900 is used sparingly. Both are commercial fonts (Mark Simonson / exljbris, via Adobe Fonts or Monotype). **No font files are in the repo.** A webfont license is **not confirmed**. Until it is, the documented fallback is:

```css
font-family: 'Proxima Nova', 'Museo Sans', 'Century Gothic', 'Avenir Next', sans-serif;
```

The Capabilities Statement also embeds **Minion Pro Regular**, which is **not** in the typography guide. Treat it as an unexplained extra (possible InDesign default or a small unused style), not as a brand serif, until someone shows where it is used on purpose.

There is **no numeric type scale** in the written brand docs.

### 5.2 Bio documents — flagged inconsistency (already in the repo)

The Gio Becerril bio PDF (and the unimported `SE Bio Template`) uses **NewScience** (Regular, Bold) and **Rajdhani** (Bold). Neither appears in the Capabilities Statement. The typography README already asks Hayden to either restyle bios to Proxima/Museo or document a secondary people-collateral system. **Do not treat Rajdhani or NewScience as “the brand” until that is resolved.** Rajdhani is also HCC / Cotton Co’s working face; using it on SE bios is an extra reason not to normalize it here by accident.

### 5.3 Product apps

Command and Estimating cite Proxima / Museo as the licensed faces but **do not embed them**. They ship **Avenir Next** / Avenir (with Outfit as a display fallback and Andale Mono for accents) — a product substitute, called out in Command’s design-system proposal (PR #14). Avenir Next is already in SE’s fallback stack, so this is consistent as a temporary substitute, not as a replacement brand face.

Estimate Command uses the documented SE fallback stack in CSS, also without embedded files.

### 5.4 Live marketing site (observed)

The Framer site does not load Proxima Nova or Museo Sans. Computed type on 24 November 2026:

| Role | Face | Notes |
|---|---|---|
| UI / headlines / body | **Montserrat** (400/500/600) | Hero ~70px / 600, negative tracking (~-0.05em), white on photography. Section titles ~32–48px. Nav ~13px uppercase. |
| Stat numbers | **Switzer** 500, 64px | Display accent on the “Delivered At Scale” panel |
| Fallbacks also referenced | Inter, Geist, “Placeholder” companions | Framer internals; June 2026 Wayback of roofingse.com also listed PT Mono and Zalando Sans Expanded |

This is a third type system, on top of print and bios. It is the current public web look, but it is not the confirmed brand type.

---

## 6. Logo

Source: `SE Roofing/Logo/` provided by Hayden. Production files in `brand/logos/`:

| File | Use |
|---|---|
| `se-roofing-full-lockup.png` (1000×134, RGBA) | Horizontal “SE” mark + “ROOFING” wordmark. Digital, wide placements. Pixels are navy + slate only (plus antialiasing). |
| `se-roofing-icon-mark.png` (1000×517, RGBA) | Angled parallelogram “SE” emblem, no wordmark. Avatars, favicon, social. |
| `se-roofing-full-lockup-pms.eps` | Print, Pantone 7546 C + 5405 C |
| `se-roofing-icon-mark-pms.eps` | Print / embroidery / single-color signage (documented as 7546 C) |
| `se-roofing-icon-mark-cmyk.eps` | Print when the vendor cannot run spots |
| `se-roofing-diagonal-lockup.eps` | Full lockup inside the cut-corner parallelogram (letterhead / signage). No PNG export in the repo. |

**Rules already written:**

- Do not recolor outside the two brand colors, stretch, skew, add shadows or outlines, or rebuild the wordmark in another font.
- Clear space: at least the height of the “S” on all sides (rule of thumb, pending an original designer guide if one exists).
- Minimum size: do not shrink the full lockup below ~1 inch print or ~120px on screen.
- Backgrounds: navy/slate reads best on white or very light grounds. On dark photos, use a **white-knockout** if available, or a white/light plate (as in the Capabilities Statement).

**Gaps:** no SVG; no knockout/reverse file in the repo, even though the marketing hero uses a white SE emblem (and a color lockup in the nav). The source `Logo/` folder also had a COI PDF and a prequalification spreadsheet, correctly left out of this brand repo.

The gov site and the truck wrap on the marketing site use the official color lockup correctly.

---

## 7. Layout, components, and motion

There is no coded component library and no grid, radius, or motion tokens in `SE-Roofing-`. `website/design-system/README.md` is an unchecked checklist.

From existing materials, not invented as a new system:

- **Print:** letter-size capabilities slick; diagonal/cut-corner frame; navy footer with contact; all-caps headlines; icon row for “Why choose SE Roofing.”
- **Marketing site:** Framer site, sticky white nav pill with the color lockup, dark “Contact Us” chip, orange primary CTAs with a circular arrow, full-bleed jobsite photography, a light dotted consult band, deep-teal footer. A hamburger appears at 390. Scroll-driven / sticky sections are used; a full-page screenshot misses mid-page content unless the view is scrolled. Motion was not formalized.
- **Gov site:** generic top logo + slate bar + stacked body, USFCR and SAM badges. UEI / CAGE / NAICS are still “TBD” and should be finished or pulled from the live page.

Do not copy Command’s invert dark mode, gold rules, or 18px cards into SE marketing work just because the companies share a parent.

---

## 8. Imagery

No photography guide lives in this repo (`marketing/assets` has no photos folder yet; LinkedIn banner, video, and other assets are still on Hayden’s machine). The live marketing site uses jobsite photography (roofs, crews, a branded box truck). The official logo appears on the truck. That is consistent with a commercial, self-performed story. There is no written “documentary vs stock” rule here; do not invent one, and do not import Rental One’s camp rule or Cotton Co’s disaster-avoid list unless Hayden wants a shared photography standard.

---

## 9. Product relationship (Command, Estimating, Estimate Command)

SE Roofing is an operating company of Roof Co Ventures. Command is the parent CRM and already carries both identities:

- `roofco.*` for Roof Co Ventures / app chrome (navy `#233746`, gold `#D0A255`, etc.).
- `seroofing.*` for SE, matching this brand’s navy, slate, and mist, plus Command-only `steel-light`.

That split is correct and should stay. When Command shows an SE job, use the SE namespace for SE marks and tints; do not recolor the SE logo in Roof Co gold. Estimating copies the same Tailwind file and is the same product family (Command draft PR #14).

Estimate Command is a separate, older Next.js app that is **SE-only** (no Roof Co token set) and disagrees on ground, muted, and status hexes. Whether it is retired is still Unknown. Until that is decided, do not treat its extras as the SE brand, and do not silently “fix” them to Command’s status ramp without a product call.

---

## 10. Accessibility (as built)

Strengths: navy and white are AAA; slate on white actually passes AA (5.93:1); Command’s SE navy/steel inherit that; official logos have solid contrast on white.

Failures and gaps:

- Marketing orange `#D4762C` with white labels: 3.27:1, fails AA at the 15px button size.
- Command `steel-light` and Estimate Command `muted` / `success` fail or barely miss AA as 14px text (see §4).
- Navy on slate fails (2.01:1).
- The marketing “Who We Are” paragraph was observed overflowing its row (“Backed by” cut off at 1440).
- The gov site’s stock Bootstrap text is generally contrast-safe; it is just not on-brand.

---

## 11. Tokens

CSS custom properties in this proposal use the `--se-` prefix. Official brand tokens are the logo colors plus the written mist and type stack. Command, Estimate Command, and live-site values are included in `tokens.css` / `tokens.json` in clearly marked groups so they are not mistaken for approved brand additions.
