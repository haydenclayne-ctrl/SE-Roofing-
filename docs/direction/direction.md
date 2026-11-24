# SE Roofing website: design direction (v1)

**Status: Approved by Z, Nov 24 2026 (branding items still pending Hayden).** Direction A "Field Manual". Jeremy (Creative Designer), America/Chicago. Branding changes still go to Hayden via Ari. Nothing is deployed, and no repo `main` was touched.

**Read with:** `research.md` (references and live-site inventory), `CLAUDE-DESIGN-BRIEF.md` (paste-ready build brief), `../COPY-DECK.md` (copy, owned by Z / Copy Humanizer), `../BUILD-PLAN.md` and `../TECH-DISCOVERY.md` (Website Developer).

## 0. Inputs applied

| Source | Applied |
|---|---|
| Hayden via Z | The public name is **SE Roofing**. **SE Roofing Solutions LLC** is used only where it's legally required (footer copyright per COPY-DECK, privacy). "Southeast Roofing Solutions" is retired. The one phone number is **713-814-5251**, everywhere. |
| Z structure (1:02 PM) | Projects stays hidden until there are 3+ verified photo jobs. The case study is a **future template** only. No Blog, no Careers, no Manufacturer Partners band. How we work lives at `/capabilities#how-we-work`. |
| COPY-DECK.md (Z) | All Home copy comes verbatim from the deck, except for the HQ and city removals below. Header nav is **Capabilities, Safety, About, Contact**. Government is a **single footer link** to seroofinggov.com (href in config); there's no Government nav item and no `/government` page. "In-house crews" and "self-performed" are held. RoofCo appears only in the footer and in about.story. |
| Z approval (1:14 PM) | Direction A approved. The main CTA is **"Invite us to bid"** everywhere (header button, hero primary, CTA bands, mobile menu, form submit). The secondary is always **"Call 713-814-5251"**. The contact form gets the optional bid-invite fields after the deck's five. **HQ is unconfirmed:** no address, city or "Based in" claim anywhere in the mocks or brief. The phone stays. The mobile header uses a 44px hamburger icon button. Build files carry no mock banner or verify labels. |
| Still open (Hayden) | The orange accent, the web fonts, the domain. |

> **Resolved (Z, 1:14 PM):** nav follows COPY-DECK. Government is a footer link only.

## 1. Concepts

### A. "Field Manual" (recommended)
A structured, technical layout that reads like a spec sheet. Each section opens on a 4px navy rule with a numbered slate label ("02 · How we work"). Hairline slate dividers separate the content. There's a fact strip under the hero (Role / We work with / Scopes). A single cut corner echoes the parallelogram frame in the logo, used on primary buttons and the hero photo. Grounds are white and light gray, and navy is used for emphasis bands. Photos support the copy instead of carrying the page.

### B. "Jobsite Documentary"
A full-bleed jobsite photo with very large white type over a navy gradient. It's photo-led and cinematic. See `concept-b-hero.html` and `screenshots/concept-b-hero-1440.png` / `-390.png`.

### Why A
1. **It works with the photography we actually have.** B needs a library of verified, high-res SE job photos, and today only the box-truck shot is provably SE's. A holds up with one photo, or with none.
2. **It fits the audience.** GC PMs, estimators and precon scan for facts: role, scope, who's accountable. A's labeled rules and fact strip put those facts first, which is the "calm, competent, proof-led" tone.
3. **It's closer to the brand.** The print capabilities statement is navy and slate on white with short heads and a cut-corner frame. A is that system on the web. B's dark photo washes push the two-color palette into the background.
4. **Contrast and robustness.** Type over photos (B) is hard to keep AA across crops. The B mock shows it: the headline collides with the truck's logo. A's text always sits on flat brand grounds.
5. **It's easy to build as static HTML/CSS** on the existing tokens, which matches BUILD-PLAN.

**What B contributes to A:** once verified job photos exist, A can use one full-bleed "documentary" photo band per page (with no type on it).

## 2. Site map (v1, per Z + COPY-DECK)

| Page | URL | Sections (COPY-DECK IDs) |
|---|---|---|
| Home | `/` | `home.hero` → `home.who-we-are` → `home.how-we-work` → `home.capabilities` → `home.cta` |
| Capabilities | `/capabilities` | hero → overview → 4 service blocks (`#commercial-roofing`, `#new-construction`, `#overlay-restoration`, `#tear-off-replacement`) → **`#how-we-work`** (full: body + 4 stages) → cta |
| Safety | `/safety` | hero → body → (`safety.proof` omitted until EMR / program are verified) → cta |
| About / Team | `/about` | hero → story → positioning → team (Gio bio template; others only if provided) → cta |
| Contact | `/contact` | hero → contact details (phone; no address until HQ is confirmed) → form (deck's 5 fields + optional bid details) → FAQ (2 Qs) → cta |
| Privacy | `/privacy` | legal body |
| Government | footer link "Government work ↗" → https://seroofinggov.com | No nav item, no page in v1 (Z + COPY-DECK) |
| Projects | **hidden** | Ships only with 3+ verified jobs with photos. Template: `mock-case-study-FUTURE-TEMPLATE.html` |

**Roof systems** (TPO, PVC, EPDM, modified bitumen, metal) are the only list the current site names, on `/services/commercial-roofing`. COPY-DECK holds the systems table until ops confirms it, so there's no systems row in v1. The Capabilities layout has room for a chip row under the service blocks once ops confirms the list.

**Case-study template (future):** breadcrumb → eyebrow (market) → H1 (project name + scope phrase) → "Our role: roofing subcontractor to [GC]" side note → hero photo (cut corner) → **spec sheet** (Location, Building type, Roof system, Roof area, Scope, Duration, General contractor, Warranty; fields without facts are hidden) → body with sticky TOC (The scope / Site constraints / How we executed / Closeout, mirroring the 4 stages) → photo gallery (before / in-progress / detail) → GC quote (written approval only) → next project + CTA. Photo slots are neutral in the template, as COPY-DECK requires.

## 3. Grid and spacing

- **Desktop (≥1101px):** 12 columns, max content width 1240px, 24px gutters, 48px side margins. Section heads: the label sits in columns 1–3 and the heading in 4–12.
- **Tablet (721–1100px):** 12 columns, 32px margins. The nav collapses into a Menu button. Capability tiles go to 2 columns.
- **Phone (≤720px):** 4 columns, 16px gutters, 20px margins. Everything stacks to full width.
- **Spacing scale (4px base):** `--s1` 4 · `--s2` 8 · `--s3` 12 · `--s4` 16 · `--s5` 24 · `--s6` 32 · `--s7` 48 · `--s8` 64 · `--s9` 96 · `--s10` 128.
- **Section padding:** `--s9` (96) top and bottom on desktop, `--s8` (64) on phone. Head to content: `--s7` (48), or `--s6` on phone.
- **Header height:** 76px desktop, 64px phone. The header is sticky.

## 4. Type

Font tokens are swappable. Change only `--se-font-body` and `--se-font-display` in `tokens.web.css`.

| Role | Interim web face (Google Fonts, verified 200 OK 24 Nov) | Print face it stands in for | Weight |
|---|---|---|---|
| Body / UI | **Figtree** (400–900) | Proxima Nova | 400 body, 600 nav, 700 labels/buttons |
| Display (H1–H3) | **Outfit** (800–900) | Museo Sans 900 | 800 |

Figtree (Proxima-like humanist-geometric), Outfit (heavy geometric), Mulish, Red Hat Display, Urbanist and Lexend all resolved on fonts.googleapis.com. Figtree + Outfit is the pick: they're the closest proportions, both have full weight ranges, and both are OFL. Fallback stacks continue to Proxima Nova / Museo Sans / Avenir Next, so licensed faces take over automatically once they're installed.

| Token | Desktop | Phone |
|---|---|---|
| H1 `--se-fs-h1` | 72 / 1.02 | 42 / 1.04 (60 on tablet) |
| H2 `--se-fs-h2` | 44 / 1.06 (who-we-are quote 52) | 30 (quote 34) |
| H3 `--se-fs-h3` | 22 / 1.2 | 20 |
| Lead `--se-fs-lead` | 21 / 1.5 | 18 |
| Body `--se-fs-body` | 18 / 1.55 | 17 |
| Small | 15 | 15 |
| Label / eyebrow `--se-fs-label` | 13, 700, +0.14em, uppercase | same |

Display headings use letter-spacing −0.01em and word-spacing +0.06em, because Outfit sets tight. Body measure is about 36–38em max.

### Headline case: DECISION, sentence case
**All headings are sentence case. Title case is not used anywhere, and headings are never CSS-uppercased.** Uppercase is reserved for small labels and eyebrows, buttons, and spec-sheet keys. The tokens are `--se-heading-case: none` and `--se-label-case: uppercase` (in `tokens.web.css`).

Rationale:
1. COPY-DECK and the messaging framework write every line in sentence case and ask that they not be set as stacked slogans. All caps turns "Your project. Our roofing expertise." into a slogan.
2. The headlines are full sentences ("The team doing the work stays accountable for the outcome."). Sentence case reads faster and calmer for a GC audience. It's the proof-led register, not the shouted one.
3. Title case adds arbitrary capitalization decisions and fights the plainspoken voice.
4. The brand's all-caps DNA survives where it's strongest: the logo, the eyebrows, the buttons and the spec keys. That keeps the print look (Museo caps) recognizable without caps headlines.
5. Accessibility and SEO: the authored text is the displayed text, with no transform surprises for screen readers or snippets.

(Print can keep all-caps headline fragments. This is a web rule.)

## 5. Color usage

**Two-color brand plus neutrals. Nothing else ships by default.**

| Token | Hex | Use | Contrast |
|---|---|---|---|
| `--se-navy` | #203A47 | Text, headings, primary buttons, rules, CTA band, footer | 11.95:1 on white |
| `--se-slate` | #456977 | Labels, step numbers, accent words, the government/secondary panel, focus ring | 5.93:1 on white (AA body), 5.47 on paper |
| `--se-white` | #FFFFFF | Grounds, reverse text | — |
| `--se-mist` | #E7E9EA | Brand light gray (print). Optional ground | navy 9.81:1 |
| `--se-paper` | #F4F6F7 | Alternate section ground | navy 11.02:1 |
| `--se-ink-2` | #3A4E58 | Secondary body text | 8.71:1 |
| `--se-on-navy-2` | #C9D6DC | Secondary text on navy | 8.04:1 |
| `--se-line` / `--se-line-strong` | #C9D1D5 / #8FA1AA | Hairlines and rules only, **never text** | — |

Rules:
- Never put navy type on slate, or slate on navy (2.01:1).
- Slate stays an accent. It's never a large text field and never the CTA fill.
- No Roof Co gold, no live-site near-navies (#16272F / #1A1A2E / #182B33), and no gradients on text grounds.
- Photos never carry type in A.

**BRANDING (pending Hayden), optional accent:** the live orange `#D4762C` can be switched on as `--se-accent` with **#111 labels (5.78:1)**, never white (3.27:1 fails). It's used only for the primary button fill. It's off by default. Screenshots: `screenshots/home-1440-BRANDING-orange-accent.png` and `…-cta.png`. My recommendation is to keep it off. The brand is two-color, and orange also reads as the "urgent roofer" trope we're avoiding.

## 6. Components

- **Header (`site.header`):** a sticky white bar with a 1px bottom line. Color lockup 26px tall (20px on phone, still ≥120px wide). **Desktop (>1100):** nav Capabilities, Safety, About, Contact, then the phone number (`tel:`), then the persistent primary button **"Invite us to bid" → /contact** (navy, cut corner, nowrap). **Tablet (721–1100):** the nav and phone hide, and the header shows the logo, the "Invite us to bid" button and a **44×44 hamburger icon button** (`aria-label` "Open menu" / "Close menu", `aria-expanded`, `aria-controls="mnav"`; the icon swaps to an X). **Phone (≤720):** logo + hamburger only. The CTA moves into the menu as a full-width primary button, because a compact "Invite us to bid" plus the logo and hamburger doesn't fit 390 without shrinking the logo below 120px. The hero primary is the first thing below the header anyway. **Menu drawer:** Home, Capabilities, How we work, Safety, About, Contact (48px rows), then the "Invite us to bid" button, then "Call 713-814-5251".
- **Section head:** a 4px navy rule, then a 12-column row: label (01 · Name) in columns 1–3 and the H2 plus optional lead in columns 4–12.
- **Hero:** copy in columns 1–6 (eyebrow "Commercial roofing subcontractor", H1, lead, then the buttons **"Invite us to bid"** (primary) and **"Call 713-814-5251"** (ghost)), photo in columns 7–12 with the cut corner at bottom-left (48px, 28px on phone), min height 540. A **3-cell fact strip** sits below it (Role / We work with / Scopes, columns 1fr 1fr 2fr) with a 4px navy top rule. On phone, Role and We work with share a row and Scopes spans full width.
- **Stage bar (how we work teaser):** 4 cells, each a slate number (Outfit 36) plus a stage name (Figtree 700, 19px), with hairline separators. 2×2 on phone. The full version on Capabilities adds the deck's one-line description under each stage.
- **Capability tile:** white with a 1px line border, 4px navy top, 24px padding. Label "Scope 0N", H3, body (16px, ink-2), then "View scope →". On hover, the border and top switch to slate. The whole card is the link. Grid is 4 / 2 / 1.
- **Project card (future):** a 4:3 photo, a market eyebrow, an H3 project name, and a definition list (Location / System / GC). The whole card is the link. No card ships without a verified job.
- **Stat block (future, conditional):** an Outfit 56 figure, an uppercase label, and a source line ("From [document], [date]"). It ships only with 2+ verified figures. The intended first use is EMR on /safety. It isn't on Home (COPY-DECK: no `home.stats`).
- **Buttons:** 48px min height (44 in the header on phone), 700, 15px, uppercase, +0.06em. Primary is a navy fill with a 14px cut corner. Ghost is a 2px navy outline. On navy grounds they invert (white fill with navy text, or white outline). The focus ring is 3px slate, or white on navy, with 3px offset.
- **CTA band (`home.cta`, reused on every page):** a navy band with an H2 and lead in columns 1–7 and two buttons (**"Invite us to bid"**, white fill; **"Call 713-814-5251"**, white outline) right-aligned in columns 9–12. They stack full width on phone.
- **Form (`contact.form`, approved by Z):** labels above fields (13px uppercase, 700), 48px inputs with square corners, a 2px border and a 3px focus ring. Errors are inline text plus an icon, never color alone. Field order: the deck's five, **Name\* · Phone · Company · Email\* · Message**, then a **"Bid details (all optional)"** fieldset with **Project name · General contractor · Bid due date (date) · Plans & specs link (url, hint "BuildingConnected, Procore, Dropbox or any share link.") · Roofing scope** (checkbox chips for the four services). The submit is **"Invite us to bid"**, full width on phone. Netlify Forms `name="bid-invite"` with a honeypot. Markup: `src/snippets/bid-invite-form.html`. (\* Required fields are my proposal; the deck doesn't specify any.)
- **Footer (`site.footer`):** SE Navy ground. The **white knockout lockup** (`../brand/se-lockup-white.svg`, 28px tall). The RoofCo line. Company: Capabilities, Safety, About, Contact, Privacy, and **"Government work ↗" → https://seroofinggov.com** (the only government link). Contact: "SE Roofing", 713-814-5251, "Invite us to bid →". **No street address or city** until HQ is confirmed. "© 2026 SE Roofing Solutions LLC".

## 7. Imagery

- **Use only real SE crews, roofs and equipment.** No stock, no AI-generated people, no hard-hat handshakes, no storm or damage drama.
- Before an image ships, confirm three things: the job is SE's, it's approved for use, and it shows no client or GC branding without permission. Every live-site photo except the box truck is unverified, and flagged VERIFY in the mock.
- Preferred shots: crews at work at mid distance (PPE visible, faces not posed), finished roofs wide (RTUs, terminations, clean lines), detail shots (seams, flashing, edge metal), and the branded truck or equipment on site.
- Treatment: natural color, no filters or duotone, no text on photos. One cut corner per photo, max. 4:3 for cards, about 21:9 for case-study heroes, about 1:1.05 for the home hero.
- Requested shoot list for Hayden/ops: 3 completed roofs (wide + detail), 2 crews in progress, the truck and equipment staging, and a team portrait for About.

### Photo provenance (kept here, not in the build files)
- `crew-roof.jpg` (home hero) comes from the current site's /projects page (card "Sheridan, AR"). **It's unverified as an SE job.** Confirm it's SE's and approved, or swap in an approved photo, before launch.
- `truck.jpg` (Concept B) shows the SE logo on the truck, so it's SE equipment, but usage approval is still needed.
- The other current-site photos (`tpo-roof`, `crew-insulation`, `crew-board`, `gravel-roof`) are tied to placeholder project slugs. Don't use them until they're verified.
- Build files (`static/`, `mock-home.html`, the brief) carry **no** banner or verify labels. This list is the record.

## 8. Motion
Minimal. 150–300ms ease-out on hover color and border changes, and a 1.02 image scale on card hover. No scroll-jacking, parallax, autoplay video, counters or marquees. The live site's scroll-driven sections are dropped. Everything is disabled under `prefers-reduced-motion` (already in CSS).

## 9. Accessibility (WCAG 2.2 AA)
- All text pairs listed in §5 pass AA, and most pass AAA. Hairline colors are never used for text.
- A skip link, one H1 per page, logical H2/H3 order, landmarks (header / nav / main / footer), and `aria-current` on the active nav item.
- Visible focus everywhere (3px). Targets are ≥44×44. The menu button uses `aria-expanded` / `aria-controls`.
- Forms use real `<label>` elements, `autocomplete` attributes, `type=tel/email/url/date`, and errors that are announced (`aria-describedby`).
- Images get meaningful alt text from COPY-DECK. The logo alt is "SE Roofing". Decorative rules are CSS only.
- No content on hover only. Text resizes to 200% without loss. No horizontal scroll at 320px (checked to 390: scrollWidth = viewport).

## 10. Mobile behavior (≤720)
- The header becomes logo + a 44px hamburger icon button. "Invite us to bid" moves into the drawer as a full-width primary button above the phone row. The drawer pushes down under the header with 48px rows.
- The hero stacks: eyebrow, H1 (42), lead, two full-width buttons, then the photo (4:3).
- The fact strip becomes Role | We work with on one row, with Scopes full width below. Section heads stack (label above heading).
- The stage bar goes 2×2. Capability tiles become 1 column with no min height.
- The CTA band buttons go full width. The footer becomes a single column.
- The Phone link is a primary path on mobile (hero secondary CTA, CTA band, drawer, footer).

## 11. Layout questions from the copy lead: recommendations

1. **Sentence case for headings: yes.** I decided this in §4: sentence case on every heading, uppercase only for labels and buttons, and never title case.
2. **A Manufacturer Partners section: no, not in v1.** It's cut per Z and COPY-DECK. The live band shows GAF / Elevate / FiberTite / Soprema logos with no confirmed relationship or status level, and a logo wall of unverified partners is a credibility risk with estimators. If ops later supplies **approved marks and the exact program/status wording**, it returns as a single quiet row on Capabilities (monochrome marks, the label "Manufacturer programs", and status text under each mark), not on Home.
3. **Where "How we work" lives:** **a homepage section (short: body + 4 stage names + a link) and the full version at `/capabilities#how-we-work`** (body + 4 described stages). It isn't a standalone page or a fifth service. It also appears in the mobile drawer as "How we work", so GCs can jump straight to it. The case-study template mirrors the same 4 stages so the story stays consistent.

## 12. BRANDING questions (Hayden, via Ari)
1. **Orange accent:** keep `#D4762C` as an optional web accent (with black labels), or drop it so the site is strictly navy and slate? I recommend dropping it.
2. **Web fonts:** license Proxima Nova + Museo Sans for web (Adobe Fonts / MyFonts), or approve Figtree + Outfit as the permanent web pair?
3. **Domain:** which canonical host goes on the new site (roofingse.com, seroofingteam.com, or another)?
4. **Reversed logo:** approve white-knockout use of the lockup on navy and dark photos. `../brand/se-lockup-white.svg` is a derived recolor of the official EPS, and the guidelines don't explicitly approve reversed use.
5. **Photography:** confirm which current-site photos are SE jobs, and approve a short shoot (§7).
6. **HQ (business fact, not branding):** confirm the public address. Until then, no address or city appears on the site. It goes back in `site.contact-block` once it's confirmed.

## 13. Live-site defects to retire (FYI for the build)
- The **Careers footer link returns a 404** (`/careers`). It's cut from v1.
- `/services/commercial-roofing` publicly shows "[Insert your real safety data here, EMR rating, safety program name…]".
- Unverified stats, testimonials, placeholder project slugs ("South, TX", EnergyOptix…), "Hydra - Modern Framer Template" titles, and "national support / scale" framing are **not carried over**.
- "Who We Are" overflow at 1440 (the new layout uses a fluid measure, checked at 1440 and 390).
- The gov microsite shows UEI / CAGE / NAICS as "TBD" (it's outside this site, but the footer link points there).

## 14. Files

| Path (under `/home/box/creative-dept/se-roofing/`) | What |
|---|---|
| `direction/CLAUDE-DESIGN-BRIEF.md` | Paste-ready brief + Home section spec |
| `direction/direction.md` | This doc |
| `direction/research.md` | References + live-site inventory |
| `direction/static/index.html` | **Home mock, static HTML** linking `css/tokens.css` (the design-system tokens, unchanged) + `css/tokens.web.css` (web tokens, incl. the headline-case decision) + `css/site.css` |
| `direction/templates/case-study-template.html` | Future case-study template (not in the v1 build; keeps its slot labels) |
| `direction/mock-home.html` | The same Home as a single self-contained file (fonts and images inlined) |
| `direction/mock-case-study-FUTURE-TEMPLATE.html` | Self-contained future template |
| `direction/concept-b-hero.html` | Concept B comparison hero |
| `direction/screenshots/` | `home-1440-viewport.png`, `home-1440-full.png`, `home-390-viewport.png`, `home-390-full.png`, `home-390-menu-open.png`, `home-1024-menu-open.png` (1440 has no menu; the nav is inline), `home-1440-BRANDING-orange-accent.png` / `-cta.png`, `concept-b-hero-1440.png` / `-390.png`, `case-study-FUTURE-TEMPLATE-1440-full.png` / `-390-full.png` |
| `direction/src/` + `direction/build.py` | Sources. `python3 build.py` regenerates both the static and the bundled mocks |
| `brand/se-lockup-white.svg`, `@2x.png`, `@4x.png`, `README.md` | White knockout (derived, pending Hayden) |
| `direction/research-shots/`, `direction/site-images/` | Reference screenshots and the original live-site images |

## 15. Paste-ready brief
See **`CLAUDE-DESIGN-BRIEF.md`**. It's written to paste straight into Claude Design, and the Website Developer can then package it into `haydenclayne-ctrl/se-roofing-site`.
