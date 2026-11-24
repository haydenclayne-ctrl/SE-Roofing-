# Claude Design brief: SE Roofing website v1, Home first

Prepared 24 Nov 2026 (America/Chicago) by Jeremy (Creative Designer). This is a proposal pending Z's sign-off. Any branding change goes to Hayden via Ari. Do not deploy anything.
Build order: Home at 1440 and 390 → Capabilities (with `#how-we-work`) → Safety → About → Contact → Privacy. Once Z approves, the Website Developer packages the static export into `haydenclayne-ctrl/se-roofing-site`.

**Attach to the Claude Design session:**
- `static/index.html`, `static/css/tokens.css`, `static/css/tokens.web.css`, `static/css/site.css`, `static/css/fonts.css`, and `static/assets/` (the reference Home build).
- `screenshots/home-1440-full.png`, `screenshots/home-390-full.png`, `screenshots/home-390-menu-open.png`.
- `../COPY-DECK.md`, the only copy source.
- `../brand/se-lockup-white.svg` (footer) and `static/assets/img/se-roofing-full-lockup.png` (header; official color PNG from `SE-Roofing-/brand/logos`).

---

## PASTE INTO CLAUDE DESIGN ↓

You are designing the v1 marketing site for **SE Roofing**, a **commercial roofing subcontractor** in Houston, Texas, that works **as an extension of the general contractor's team**. Readers are GC project managers, estimators, precon, and owners' reps. The tone is calm, competent and proof-led. SE Roofing is **never** a general contractor and never runs the project or other trades.

**Direction: "Field Manual."** A structured, spec-sheet layout. Each section opens with a 4px navy rule and a numbered uppercase slate label ("02 · How we work"). Slate hairlines divide the content. A fact strip sits under the hero. One cut corner (an echo of the logo's parallelogram) appears on primary buttons and on the hero photo. Grounds are white and light gray, with navy bands for the CTA and footer. Photos support the page and never carry text.

**Hard rules**
1. Copy comes **verbatim from COPY-DECK.md**. Don't write, add or "improve" claims. No stats, testimonials, certifications, guarantees, coverage areas ("nationwide", "Houston to Miami"), "free estimate", "in-house crews" or "self-performed" (those last two are held).
2. Name: **SE Roofing**. "SE Roofing Solutions LLC" appears only in the footer copyright and the privacy page. Never use "Southeast Roofing Solutions".
3. Phone: **713-814-5251** only, always as `tel:+17138145251`, read from one config value.
4. Colors: only the tokens in `tokens.css` + `tokens.web.css`. Use `--se-navy` #203A47 and `--se-slate` #456977, plus white and the neutrals. No orange (it's off by default and pending Hayden), no gold, no gradients behind text. Never put navy text on slate or slate text on navy.
5. Fonts: use `var(--se-font-body)` (Figtree, standing in for Proxima Nova) and `var(--se-font-display)` (Outfit 800, standing in for Museo Sans 900). Never hard-code a family, so the fonts can be swapped once they're licensed.
6. Headings are **sentence case**, authored and displayed as written (`text-transform: var(--se-heading-case)`, which is none). Uppercase is used only for labels, eyebrows, buttons and spec keys.
7. Nav: **Capabilities, Safety, About, Contact**. The logo goes to Home. Government is a footer link only. No Projects, Blog, Careers or Manufacturer Partners.
8. Logos: the color lockup (`se-roofing-full-lockup.png`) on white, and the white knockout (`se-lockup-white.svg`) on navy. Don't redraw, recolor, stretch or shadow them. Minimum width is 120px.
9. Images: real SE work only. The hero photo is a current-site image marked VERIFY. Keep it swappable, and use a neutral image slot if it isn't approved. Never use stock.
10. Accessibility: WCAG 2.2 AA. One H1, a skip link, 3px visible focus, targets ≥44px, labeled form fields, and alt text from the deck. Respect `prefers-reduced-motion`. Motion is limited to 150–300ms hover transitions.

**Layout tokens:** 12 columns, max 1240px, `--gutter` 24, `--margin` 48 (32 at ≤1100, 20 at ≤720 with 4 columns and 16 gutter). Spacing uses `--s1`…`--s10` = 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Section padding is `--s9` (or `--s8` on phone). Section heads have the label in columns 1–3 and the heading in 4–12 (stacked on phone).

**Type tokens:** H1 `--se-fs-h1` 72/1.02 (60 tablet, 42 phone). H2 `--se-fs-h2` 44/1.06 (30 phone). H3 `--se-fs-h3` 22/1.2 (20). Lead `--se-fs-lead` 21/1.5 (18). Body `--se-fs-body` 18/1.55 (17). Label `--se-fs-label` 13, 700, +0.14em, uppercase. Display headings use `--se-display-weight` 800, letter-spacing −0.01em, word-spacing +0.06em.

### Home: section by section

| # | Section (COPY-DECK ID) | Content blocks (verbatim from the deck) | Layout and tokens | Responsive |
|---|---|---|---|---|
| 0 | `site.header` (sticky) | Color lockup (alt "SE Roofing", link aria-label "SE Roofing home"). Nav: Capabilities · Safety · About · Contact. Phone 713-814-5251. CTA "Contact us" → /contact | White, 1px `--se-line` bottom border, height `--header-h` 76. Logo 26px tall. Nav Figtree 600/15 with a 2px slate underline on hover/current. Primary button with a `--cut` 14px corner | ≤1100: nav and phone hide, and a "MENU" 44×44 outline button appears (aria-expanded). The drawer drops below the header with 48px rows: Home, Capabilities, How we work, Safety, About, Contact, "Call 713-814-5251". ≤720: height 64, logo 20px, CTA without the arrow, nowrap |
| 1 | `home.hero` | Eyebrow "Commercial roofing subcontractor · Houston, Texas" (layout label; confirm with Copy). H1 "Your project. Our roofing expertise." Subhead "SE Roofing is a commercial roofing subcontractor. We work as an extension of the general contractor's team." Buttons: "Get in touch" (primary → /contact), "Call 713-814-5251" (ghost, tel). Photo `crew-roof.jpg`, alt per the deck, VERIFY | Copy in columns 1–6 (eyebrow → `--s4` → H1 → `--s5` → lead → `--s6` → buttons, gap `--s4`), padding top `--s8`, bottom `--s8`. Photo in columns 7–12, min-height 540, object-fit cover, bottom-left cut of `--cut-photo` 48px | ≤720: stack copy, then the photo at 4:3 with a 28px cut. Buttons go full width with the arrow pushed right |
| 2 | Fact strip (part of the hero) | Role: Commercial roofing subcontractor · We work with: General contractors · Scopes: Commercial · New construction · Restoration · Replacement · Based in: Houston, Texas | Full-width band, 4px navy top rule, 1px line bottom. 4 equal cells, each a label plus a value (Figtree 700/17), with 1px separators and 20px vertical padding | ≤720: 2×2 grid |
| 3 | `home.who-we-are` | Label "01 · Who we are". H2 "An extension of your team." (the words "your team." in slate). Subhead (navy, 600) "We plan, schedule, and install the roofing work as part of your project team." Body: the deck paragraph. Side column: `site.contact-block` + ghost button "About SE Roofing" → /about | Section head rule. The H2 runs at 52px. Main copy in columns 1–7, side in columns 9–12 with a 1px `--se-line-strong` left border and `--s5` padding. Keep the body ≤38em so it never clips at 1440 | ≤720: one column. The side panel moves under the main copy with a top border instead of a left one. H2 34px |
| 4 | `home.how-we-work` (id `how-we-work`) | Label "02 · How we work". H2 "Built to support general contractors." Subhead "Clear communication from the first site walk through closeout." Body (navy lead) from the deck. Stage bar: 01 Preconstruction coordination · 02 Scheduling · 03 Communication and installation · 04 Closeout. Ghost button "How we work with general contractors →" → /capabilities#how-we-work | `--se-paper` ground. Body in columns 4–10. The stage bar sits `--s7` below it: a 1px rule, 4 cells, each a slate number (Outfit 800/36) plus the name (Figtree 700/19), with hairline separators. Button `--s6` below | ≤720: stage bar 2×2, body full width |
| 5 | `home.capabilities` | Label "03 · Capabilities". H2 "Roofing work that fits the job." Subhead from the deck. 4 cards (title + blurb from the deck + "View scope →"), linking to `/capabilities#commercial-roofing`, `#new-construction`, `#overlay-restoration`, `#tear-off-replacement` | 4-column card grid, gap `--gutter`. Card: white, 1px line border, 4px navy top, padding `--s5`, label "Scope 0N" → `--s5` → H3 → `--s3` → body 16 `--se-ink-2` (flex 1) → link. Min height 300. Hover switches the border/top to slate | ≤1100: 2 columns. ≤720: 1 column with no min height |
| 6 | `home.cta` | Label "04 · Contact". H2 "Ready to discuss a commercial roofing scope?" Subhead "Call 713-814-5251, or send the details and we will respond with a practical next step." Buttons "Get in touch" (white fill on navy) and "Call 713-814-5251" (white outline) | `--se-navy` band, padding `--s9`. Copy in columns 1–7, buttons in columns 9–12 aligned right and to the bottom | ≤720: stack, buttons full width |
| 7 | `site.footer` | White knockout lockup (28px tall). "SE Roofing is an operating company of RoofCo Ventures." Company: Capabilities, Safety, About, Contact, Privacy, "Government work ↗" (href from config). Contact: `site.contact-block`. "© 2026 SE Roofing Solutions LLC" (year auto) | `--se-navy` ground, 1px white/22% top border (separating it from the CTA band), padding `--s8` top. Grid: brand in columns 1–5, then 3 + 3. Labels in `--se-on-navy-2`. A legal row sits under a white/25% rule | ≤720: single column |

**Do not add to Home:** stats, partners, testimonials, projects, a government panel, newsletter sign-up, chat widgets or carousels.

### Other pages (same system)
- **Capabilities:** hero (H1 + subhead) → overview → 4 service blocks (an anchor per block: label "Scope 0N", H2, body, with a 4px navy top rule) → `#how-we-work` full version (H2, subhead, 3-paragraph body, then 4 stage cells, each with a number, name and one-line description) → CTA band.
- **Safety / About:** hero → body sections on a 7-column measure → CTA band. Safety has **no** proof block until the EMR or program is verified. About team cards: photo slot 4:5, name, title, 2-line bio, only for people Hayden provides.
- **Contact:** H1 + subhead, contact block (columns 1–4) and form (columns 6–12) on navy. The deck's fields are Name, Phone, Company, Email, Message, with submit "Get in touch". The optional bid-invite fields are a proposal; see `src/snippets/bid-invite-form.html`, and use them only if Z approves. Then the 2-question FAQ as a definition list, then the phone CTA.
- **Projects / case study:** **not in v1.** The template is ready for when 3+ verified jobs exist.

### Deliverables from Claude Design
Desktop 1440 and phone 390 for each page, plus a menu-open state at 390. Export static HTML/CSS that keeps `tokens.css` and `tokens.web.css` as separate files and uses CSS variables only (no hard-coded hex or font names in components). Use semantic HTML, with titles and meta from the deck.

## END PASTE ↑

---

### Open items (not for Claude to decide)
- BRANDING (Hayden): the orange accent (off by default; if approved, `--se-accent: #D4762C` with `--se-accent-ink: #111111`), licensed web fonts vs Figtree/Outfit, the domain, approval of reversed logo use, and photo provenance.
- Z: header CTA label ("Contact us" per the deck, or "Invite us to bid"), the optional bid-invite fields, and whether Government returns as a nav page (the 1:02 structure note vs COPY-DECK).
