# SE Roofing — Design-system audit (proposal)

Status: **proposal only**, 24 November 2026, America/Chicago. Not owner-approved.
Audit of `haydenclayne-ctrl/SE-Roofing-` at `main` @ `a5951a3` (1 July 2026, 11:51 AM America/Chicago, CDT), plus Command’s `seroofing` tokens (PR #14 findings), `estimate-command`, and public sites audited the same day. No application or website code was changed.

Each recommendation is tagged **REFINEMENT** (implementation cleanup that preserves the established look) or **BRANDING** (needs Hayden’s call). This file does not authorize a restyle, a deploy, or a merge with Roof Co Ventures / Command, HCC, or any other brand.

---

## What is already in good shape

- The logo is real production artwork (PNG + PMS/CMYK EPS). Pixel samples of both PNGs match the documented hexes exactly: navy `#203A47`, slate `#456977`.
- The written brand correctly describes a strict two-color identity, with print vs. digital guidance, and already flags the bio type mismatch instead of papering over it.
- Command already keeps SE in a separate `seroofing` namespace, and navy / steel / mist **match** this brand. That split should stay.
- The official color lockup is used correctly on the gov microsite, on the marketing nav, and on the boxed truck in the site photography.
- Navy and white are AAA. Slate on white, measured at 5.93:1, actually passes AA for body text (the written “large text only” warning is stricter than the math).

---

## Findings

### 1. Three type systems are in use at once

The confirmed print system is **Proxima Nova + Museo Sans 900** (Capabilities Statement and Proposal Template; re-verified from embedded fonts). The Gio bio (and the unimported Bio template) uses **NewScience + Rajdhani**. The live Framer marketing site uses **Montserrat** for UI and headlines and **Switzer** for stat numbers (Inter/Geist also referenced; a June 2026 Wayback capture of roofingse.com also listed PT Mono and Zalando Sans Expanded). None of the web faces are the print faces. No webfont license for Proxima/Museo is confirmed, and no font files are in the repo.

Command/Estimating already substitute **Avenir Next** for the licensed pair — a documented temporary stand-in, and Avenir Next is in the SE fallback stack.

The typography README already asked for a decision on the bios in July. The live site has since added a third system.

**BRANDING** — Choose one type system for the brand (almost certainly Proxima/Museo, which two professionally designed documents already agree on), and say whether bios and/or the website are allowed to keep a variant. Do not treat Rajdhani or Montserrat as “the brand” by default. License Proxima/Museo for web if the public site should match print.

### 2. The live marketing site is not the two-color brand

`seroofingteam.com` is a Framer site whose `<link rel="canonical">` and `og:url` point at `https://www.roofingse.com`. This is Hayden’s SE Roofing site: Houston address, Roof Co Ventures in the copy, official lockup, the same service list. `roofingse.com` itself returned **HTTP 403** from this environment (curl, WebFetch, Playwright) on 24 November 2026, so the audit used the reachable host.

The current look is photography-led, with a white-knockout SE emblem, a sticky white nav, **orange `#D4762C` primary buttons**, and a family of near-navy inks (`#16272F`, `#1A1A2E`, footer `#182B33`) that are **not** SE Navy `#203A47`. White type on the orange CTA is **3.27:1** and fails AA at the 15px button size. The hero headline is now “COMMERCIAL ROOFING. SELF PERFORMED.” — not the July-confirmed “COMMERCIAL ROOFING YOU CAN COUNT ON.” Footer copyright says “Southeast Roofing Solutions.” The “Who We Are” paragraph overflows at 1440 (“Backed by” is cut off). Mid-page sections are scroll-driven and do not appear in a naive full-page screenshot.

The website design-system folder in the brand repo is still an empty checklist, and the site source is not in this GitHub account.

**BRANDING** — Either bring the marketing site back to navy/slate + Proxima/Museo, or formally adopt a web system (including whether orange is allowed) so print and web are not accidentally two brands. Add a white-knockout logo to `brand/logos/` if the hero treatment stays.

**REFINEMENT** — Fix the overflow, the 403 on the canonical domain, the orange/white contrast (black type on `#D4762C` is 6.43:1), the empty/broken YouTube slot and sparse Projects page, and leftover incomplete bits (a “Careers” footer link). **Finish or pull** stats such as “66% Projects Completed” and “6+ Service Coverage,” and the gov site’s TBD UEI / CAGE / NAICS — unfinished figures should not stay on a live page.

### 3. Command matches the brand; Estimate Command does not fully

Command’s `seroofing.navy` / `steel` / `mist` are the official hexes. That is the right relationship: shared tokens, separate namespace, no Roof Co gold on SE marks. Command also adds `steel-light` `#7E9BA7` (2.94:1 on white — not text) and uses Avenir Next as a substitute face. Estimating copies Command’s Tailwind file.

Estimate Command (last push 10 July 2026) is SE-only and cites the same brand README, but its ground `#F4F7F9`, muted `#6D7D88` (4.25:1, fails AA), and status hexes (`#2F8A5B`, `#B07A1E`, `#C0504D`) **do not match** Command’s later `status.*` (`#2F6F52`, `#9C6A1E`, `#943B3B`). Command’s status colors generally have stronger contrast. Whether Estimate Command is retired is still Unknown.

**REFINEMENT** — Keep Command’s SE namespace as the product implementation of this brand (navy/steel/mist). Do not use `steel-light` as body text. If Estimate Command is still alive, align its mute and status ramps with Command or document a deliberate SE-app exception; if it is retired, say so.

### 4. Public facts disagree: name, domain, phone, tagline

| Item | Brand repo (1 July 2026) | Live marketing (24 November) | Gov microsite | Other |
|---|---|---|---|---|
| Name | SE Roofing Solutions | “Southeast Roofing Solutions” in title and footer | SE ROOFING SOLUTIONS LLC | GAF listing: SE Roofing Solutions LLC |
| Domain | roofingse.com | Canonical is roofingse.com; site is reachable at seroofingteam.com | seroofinggov.com | — |
| Phone | 281.965.9055 | 713-814-5251 | (281) 960-5459 | Command team records also list other direct lines |
| Primary line | “COMMERCIAL ROOFING YOU CAN COUNT ON” | “COMMERCIAL ROOFING. SELF PERFORMED.” | “BUILT BY ROOFERS, POWERED BY CREWS.” | — |

`seroofinggov.com` is a stock USFCR template (Bootstrap blues, system/Lato typography, UEI/CAGE/NAICS still “TBD”). It uses the official lockup correctly and mentions Roof Co Ventures, but it is not the brand system.

**BRANDING** — Confirm the public name, the canonical domain, the public phone, and which tagline leads. Then update the brand repo and the sites so they say the same thing. The name and phone are pending Hayden; this proposal does not pick a phone among the three numbers above.

**REFINEMENT** — Correct the written contrast note for slate (it passes AA at 5.93:1). Record or remove Minion Pro from the Capabilities Statement. Export a PNG/SVG of the diagonal lockup and a knockout mark. Import, or formally defer, the rest of the marketing library listed in `marketing/assets/README.md`. Fill or retire the empty `website/design-system/` checklist.

### 5. Positioning and marketing copy need a cleanup

Existing boilerplate still calls SE a “commercial roofing contractor” or “contractor / subcontractor.” SE is a **commercial roofing subcontractor**, never a general contractor (per copy lead, pending Hayden confirmation). The marketing site and July notes also lead, or can be read as leading, with unverified lines: “nationwide,” “Certified & Insured,” and “Guaranteed Results.”

**REFINEMENT (copy)** — Use this positioning (per copy lead, pending Hayden confirmation): “SE Roofing is a commercial roofing subcontractor. We work as an extension of the general contractor’s team, with in-house crews and reliable execution on commercial, industrial, and government work.” Drop “contractor / subcontractor” and “commercial roofing contractor.” Do not lead with “nationwide,” “Certified & Insured,” or “Guaranteed Results” until they are verified. Finish or pull “66% Projects Completed,” “6+ Service Coverage,” and TBD UEI / CAGE / NAICS. Safer heroes: “COMMERCIAL ROOFING. SELF PERFORMED.” or “COMMERCIAL ROOFING YOU CAN COUNT ON.” Short partnership lines: “An extension of your team.” / “Your project. Our roofing expertise.” / “Built to support general contractors.” Leave the official phone and public name for Hayden.

---

## Top recommendations (priority)

1. **BRANDING** — Pick a single type system. Proxima Nova + Museo Sans 900 is already confirmed by two designed print pieces. Decide the fate of NewScience/Rajdhani on bios and of Montserrat/Switzer on the website, and license the print faces for web if the site should match.
2. **BRANDING** — Reconcile the live marketing look with the two-color brand. Either restyle the Framer site to navy/slate (no orange, official navy ink, official faces) or formally approve a web-only system — and put a knockout logo in the brand repo. Do not let print, web, and bios drift as three identities.
3. **REFINEMENT** — Keep Command’s `seroofing` navy/steel/mist as the product source for this brand; leave Roof Co gold out of SE materials. Align or retire Estimate Command, whose mute and status hexes disagree with Command and in several cases fail AA.
4. **REFINEMENT** — Fix shipping quality on the public sites: orange/white contrast (3.27:1), the 1440 “Backed by” overflow, 403s on roofingse.com, unfinished project/video slots, and the gov template’s off-brand Bootstrap chrome. **Finish or pull** “66% Projects Completed,” “6+ Service Coverage,” and TBD UEI / CAGE / NAICS.
5. **BRANDING** — Confirm the public identity: SE vs. Southeast, which domain and phone are official, and which tagline leads (“YOU CAN COUNT ON” vs. “SELF PERFORMED.” vs. “Built by roofers…”). The name and phone are pending Hayden; do not pick a phone in this proposal.
6. **REFINEMENT (copy)** — Position SE as a commercial roofing subcontractor, never a GC (per copy lead, pending Hayden confirmation). Drop “contractor / subcontractor” and “commercial roofing contractor.” Do not lead with “nationwide,” “Certified & Insured,” or “Guaranteed Results” until verified. Finish or pull the unfinished stats and TBD registrations noted above.

---

## BRANDING questions for Hayden

1. Is **Proxima Nova + Museo Sans 900** the only type system? If yes, should bios and the Framer site be brought in line (and licensed for web)? If the site’s Montserrat/Switzer look is intentional, should that be documented as a web-only system?
2. The marketing site’s orange `#D4762C` and near-navy inks are not the two-color logo palette. Should the site return to SE Navy / Slate Blue, or is the current Framer look approved as a web exception?
3. Which public identity is official: the name (SE Roofing Solutions vs. Southeast Roofing Solutions), the canonical domain (roofingse.com is tagged as canonical but 403s here; seroofingteam.com is what loads), the phone (the repo, the marketing footer, and the gov site all disagree — do not pick one in this proposal), and the lead tagline? The copy lead also asks Hayden to confirm SE’s positioning as a commercial roofing subcontractor (never a GC).

---

## Live sites and screenshots

Audited 24 November 2026, America/Chicago, at 1440 and 390. No logins, no forms submitted.

- **Marketing:** `https://seroofingteam.com` (Framer). Canonical/og URL is `https://www.roofingse.com`. `roofingse.com` and `www.roofingse.com` returned HTTP 403 from this environment. Viewport shots (hero, mid, footer) and 390 hero are in `/home/box/creative-dept/se-roofing/design-system/screenshots/`. Full-page PNG files exist but miss scroll-driven mid sections — use the viewport shots.
- **Gov:** `https://seroofinggov.com` (USFCR capabilities microsite), 1440 and 390 in the same folder.
- **Not this company:** `seroofing.com` (Southwest Florida), `se-roofing.com` (Kissimmee), `seroofingsolutions.com` (SRS / Georgia). Not screenshotted as SE Roofing.
- Website source is not in this GitHub account. A June 17 2026 Wayback snapshot of roofingse.com confirms it was a Framer site then (title: “Southeast Roofing Solutions, LLC — Commercial Roofing Nationwide”).
