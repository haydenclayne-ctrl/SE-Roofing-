# Color Palette

Sourced directly from the vector logo files (`SE-Roofing_FULL-PMS.eps`, `SE-Roofing_PATCH-PMS.eps` in [`brand/logos`](../logos)), which embed exact Pantone/CMYK color definitions — and cross-checked by sampling the actual pixels in the shipped PNG lockups, which gives the true on-screen/digital hex.

## Primary palette

| Name | Pantone (Coated) | CMYK | Digital hex (sampled from logo PNG) | Usage |
|---|---|---|---|---|
| SE Navy | PANTONE 7546 C | C86 M69 Y50 K46 | `#203A47` | Primary — "S", "ROOFING" wordmark, dark backgrounds/footers |
| SE Slate Blue | PANTONE 5405 C | C74 M47 Y33 K7 | `#456977` | Secondary — "E" bars, accent shapes, mid-tone panels |

These are the *only* two brand colors used in the logo itself — this is a two-color brand, not a broad palette. Both PNGs (`se-roofing-full-lockup.png`, `se-roofing-icon-mark.png`) are >95% just these two colors plus antialiasing.

## Where each is used in existing materials (from the Capabilities Statement)

- **SE Navy** (`#203A47`) — headlines ("IN-HOUSE CREWS / NATIONAL REACH"), the dark footer band, body text
- **SE Slate Blue** (`#456977`) — the diagonal accent panels/dividers, secondary headings ("YOUR PARTNER IN ROOFING")
- Both are also used together as a light-to-dark gradient in some renderings (see the icon mark on the Bio PDF) — a navy→slate gradient is an acceptable brand treatment, not just flat fills.

## Neutrals (used alongside the two brand colors in existing collateral)

| Name | Hex | Usage |
|---|---|---|
| White | `#FFFFFF` | Page/section backgrounds |
| Light gray | `#E7E9EA` (approx., from capabilities statement background panels) | Section backgrounds behind body copy |

*(Neutral gray is an approximation from visual inspection of the Capabilities Statement — not pulled from a vector source. Refine if you have the exact value from the InDesign file's swatches.)*

## Print vs. digital note

- **Print production**: use the Pantone spot colors above (or their CMYK builds) — pull directly from `se-roofing-full-lockup-pms.eps` / `se-roofing-icon-mark-pms.eps`, don't reconvert from the digital hex.
- **Web/digital**: use the sampled hex values above (`#203A47` / `#456977`) — these are what's actually shipping in the current logo PNGs and marketing PDFs, so they're the values to hardcode into CSS/design tokens.

## Contrast

`#203A47` on white and white text on `#203A47` both pass WCAG AA comfortably (dark navy on white is very high contrast). `#456977` on white is roughly AA for large text only — avoid small body copy in slate blue on a white background; it's better as a background panel with white/navy text on top, matching how it's used in the existing Capabilities Statement.
