# SE Roofing website: design discovery and reference research

24 November 2026, America/Chicago. Prepared by Jeremy (Creative Designer) for Z and the Website Developer. Proposal only. Nothing here is approved or deployed.

## 1. What I read

- Draft design system: `/home/box/creative-dept/se-roofing/design-system/` (DESIGN_SYSTEM.md, tokens, audit.md, screenshots). Same files are in [PR #1](https://github.com/haydenclayne-ctrl/SE-Roofing-/pull/1), branch `design-system/v1`.
- Brand repo `haydenclayne-ctrl/SE-Roofing-`: `brand/logos` (full-lockup PNG, icon mark PNG, PMS/CMYK EPS), capabilities statement PDF (V.2026.1).
- DESIGN-LIBRARY.md (SE Roofing entry), DEPARTMENT.md and PROJECTS.md.
- Copy lead: `2026-11-24-design-system-voice-notes.md`, `2026-11-24-se-roofing-consistency.md` and `2026-11-24-se-roofing-messaging-framework.md` (all in `/workspace/copy-humanizer/drafts/`).
- Live sites, fetched 24 Nov around 12:50 PM CT: https://seroofingteam.com (home, /services, /services/commercial-roofing, /projects, /about, /contact) and https://seroofinggov.com. roofingse.com returned 403 from here.
- No Website Developer notes were in `/home/box/creative-dept/se-roofing/` when I started, and `BUILD-PLAN.md` hadn't been posted.

## 2. Decisions received during this pass (Hayden via Z)

- Public name: **SE Roofing**. Use **SE Roofing Solutions LLC** only where it's legally required. "Southeast Roofing Solutions" is retired.
- One phone number everywhere: **713-814-5251**.
- Still open: the orange accent, the web fonts and the domain.

## 3. What the live site gives us to work with

**Usable as is (real copy):**
- "We don't broker labor. We deliver commercial roofing with our own crews, our own project managers, and our own standards. That gives clients direct control, clear accountability, and confidence from planning through closeout."
- The four services (Commercial Roofing, New Construction, Overlay & Restoration, Tear Off & Replacement). Take the blurbs from `/services`, not from the homepage cards.
- The four-step process (Inspect, Plan, Install, "Guarantee"). The copy lead has retitled it (Preconstruction coordination, Scheduling, Communication and installation, Closeout), and the mock uses those titles.
- Roof systems named on `/services/commercial-roofing`: TPO, EPDM, modified bitumen, metal, plus "chemical-resistant PVC and TPO membranes" in the industrial section. That's the only systems list on the site, and ops should confirm it.
- Gov: "Commercial, Industrial, Municipal & Government Roofing" and the in-house crews / direct oversight paragraph.
- HQ: 5617 Campbell Rd, Houston, TX 77041.

**Photography on the site** (copied to `site-images/`, downsized copies in `assets/`): a crew walking a membrane roof, a crew laying insulation over a metal deck, a crew carrying board, a finished white single-ply roof with RTUs, a ballasted roof, an aerial of a low-rise campus, and the branded SE box truck. Only the truck photo can be shown to be SE's (the logo is on it). The rest are tied to project cards whose slugs look like template stock (EnergyOptix, PurePower and so on). **Treat every photo except the truck as "confirm it's an SE job" before it ships.**

**Do not carry over:** the stats on either page (100% / 500+ / 10+ / 25+ on Home, 40+ / "Millions" on About), the four About testimonials, the "Hydra - Modern Framer Template" titles, the placeholder project slugs and the "South, TX" location, "national support / scale" framing, coverage claims ("Houston to Miami", "nationwide"), "Get a Free Estimate", "Start a Project", "Guaranteed Results", "Certified & Insured", "Open 7 days a week", and the manufacturer logo band (GAF, Elevate, FiberTite, Soprema) until ops confirms the relationships.

**Live defects worth noting:**
- The footer Careers link goes to a 404.
- `/services/commercial-roofing` shows a visible authoring placeholder: "[Insert your real safety data here, EMR rating, safety program name…]".
- The gov page shows UEI, CAGE and NAICS as "TBD".
- The "Who We Are" paragraph overflowed at 1440 in the earlier audit.

## 4. Reference sites (patterns only, never branding)

All visited on 24 Nov 2026 at 1440 (screenshots are in `research-shots/`). I picked them for how they talk to GCs, owners' reps and facility buyers, not for how they look. **I'm borrowing patterns only.** None of their colors, logos, type, photos or wording.

| # | Site | Type | What to borrow (pattern) | What to avoid |
|---|---|---|---|---|
| 1 | [Rosendin](https://www.rosendin.com) | Specialty electrical subcontractor | A project portfolio with filters (market, location) and a "FEATURED · CITY, ST" eyebrow on each card. The location label is a quiet spec line, not a headline. Safety sits in the top nav. | Stacked three-line slogans in the hero. Heavy consent and accessibility overlays. |
| 2 | [Cupertino Electric](https://www.cei.com) | Specialty electrical subcontractor | **"Tell us about your project" is a persistent utility link above the main nav**, a direct model for "Invite us to bid". The hero says what they do in a short line. There's a "Quick facts" block. | Image-heavy carousels. |
| 3 | [Performance Contracting (PCI)](https://www.pcg.com) | Specialty subcontractor (insulation, envelope and more) | **The safety stat appears as a single figure on the homepage**, next to other numbers. This is the model for an EMR stat block once SE has a published EMR. A services mega-list grouped by trade. | Over-long service menus. Dark, low-contrast hero copy. |
| 4 | [Crown Corr](https://www.crowncorr.com) | Building-enclosure subcontractor | **Project names used as section heads** (the job is the hero). Services include "Design-Assist" and "BIM", which is how a sub speaks to precon. | Decorative serif type. A thin hero statement with no proof. |
| 5 | [Mortenson](https://www.mortenson.com) project pages | GC/developer (pattern only; SE is never positioned this way) | **A case-study anatomy:** a location eyebrow, a framing question, "Project overview", key takeaways, then a facts rail (completion date, cost, delivery method). Our case study uses this structure, with a "Our role: roofing subcontractor to [GC]" line added. | Any GC-style "we lead the program" framing. |
| 6 | [Baker Roofing](https://www.bakerroofing.com) | Commercial roofing contractor | **Systems and markets as two separate nav lists** (Single Ply, Modified, Metal… / Data Centers, Education, Government…). Insights articles answer real spec questions (for example TPO vs PVC). | Residential cross-sell in the utility bar. "Schedule an estimate" CTA. Hurricane-damage content. |
| 7 | [CentiMark](https://www.centimark.com) | Commercial/industrial roofing | **A systems taxonomy** (TPO, PVC, EPDM, SPF, Mod-Bit, BUR, Metal) with one page per system. That's a good model for Capabilities once SE confirms its list. | "24/7 emergency" urgency. Chat widgets. Lots of overlapping overlays. |
| 8 | [Tecta America](https://www.tectaamerica.com) | Commercial roofing | A dedicated **Government Services** page in the main nav, and Safety as a first-class About item. | Red "Request quote today" urgency. "Acquisition company" messaging. |
| 9 | [Nations Roof](https://www.nationsroof.com) | Commercial roofing | **Safety and Qualifications pages**, and a downloadable comparison guide (a proof asset for estimators). | "Nationwide" coverage claims, which SE can't make. A portfolio/asset-management sales pitch. |

Kalkreuth Roofing & Sheet Metal was on my list but failed SSL from here, so it isn't cited.

### Patterns to adopt, in order of value

1. **A persistent bid CTA in the header** (CEI). In SE's version, "Invite us to bid" is always visible and the phone number sits next to it on desktop.
2. **Spec-sheet facts rail on case studies** (Mortenson, Rosendin). Location, building type, system, area, scope, duration, GC, warranty. Each field is hidden if it hasn't been verified.
3. **Safety as a top-level page with one hard number** (PCI, Tecta, Nations). SE gets a slot for its EMR and program name, and the number only shows once it's published.
4. **Systems vs. markets taxonomy** (Baker, CentiMark). The Capabilities page is organized by scope (the 4 services) and lists roof systems as chips/rows, limited to what SE confirms.
5. **Government folded in as a nav item** (Tecta), with vendor identifiers shown only when verified. This replaces the separate USFCR template look.
6. **Quiet location eyebrows** on project cards (Rosendin), so photos and facts do the selling.

### Anti-patterns we're explicitly avoiding

Storm urgency, "free estimate" banners, chat pop-ups, carousels, stock photos of hard hats shaking hands, "nationwide" maps, logo walls of manufacturers SE hasn't confirmed, and unsourced stat counters.
