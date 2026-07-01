# Logos

Source: `SE Roofing/Logo/` (provided by Hayden). These are the real, current production files — not placeholders.

## Files in this repo

| File | Format | What it is |
|---|---|---|
| `se-roofing-full-lockup.png` | PNG, RGBA, 1000×134 | Horizontal lockup — "SE" mark + "ROOFING" wordmark side by side. Digital/screen use. |
| `se-roofing-icon-mark.png` | PNG, RGBA, 1000×517 | Icon/patch mark only (the "SE" emblem inside the angled parallelogram), no wordmark. Digital/screen use. |
| `se-roofing-full-lockup-pms.eps` | Vector (EPS) | Full lockup, built with exact Pantone spot colors (7546 C, 5405 C) — use for print production. |
| `se-roofing-icon-mark-pms.eps` | Vector (EPS) | Icon mark only, Pantone spot color (7546 C) — use for print production (e.g. embroidered patches, single-color signage). |
| `se-roofing-icon-mark-cmyk.eps` | Vector (EPS) | Icon mark, process CMYK build (no spot colors) — use when a print vendor can't run spot colors. |
| `se-roofing-diagonal-lockup.eps` | Vector (EPS, embedded TIFF) | The full lockup inside the angled/cut-corner parallelogram frame (the "cut corner" version used on letterhead/signage). |

## Which one to use

- **Website, digital ads, social**: `se-roofing-full-lockup.png` (horizontal) for wide placements; `se-roofing-icon-mark.png` for square/avatar placements (favicon, social profile photo).
- **Print (business cards, signage, vehicle wraps, embroidery)**: the `-pms` EPS files. Use CMYK EPS only if the vendor explicitly can't run Pantone spot inks.
- **Letterhead / framed / signage with the angled cut-corner border**: `se-roofing-diagonal-lockup.eps`.

## Colors

Both marks use exactly two brand colors — see [`brand/color`](../color) for exact Pantone/CMYK/hex values (PANTONE 7546 C navy + PANTONE 5405 C slate blue). Don't recolor the logo outside these two.

## Usage rules

- **Clear space**: keep at least the height of the "S" in the icon mark as clear space on all sides (standard rule of thumb — confirm against the original brand guide if one exists from the designer).
- **Minimum size**: don't shrink the full lockup below ~1 inch wide in print or ~120px wide on screen — the wordmark becomes illegible below that.
- **Backgrounds**: the navy/slate-blue mark reads best on white or very light backgrounds. On dark photo backgrounds, use a white-knockout version if available, or place on a white/light plate (as done in the Capabilities Statement) rather than directly on a dark photo.
- **Don'ts**: don't stretch/skew, don't recolor outside the two brand colors, don't add drop shadows or outlines, don't rebuild the wordmark in a different font.

## Not brand assets (found in the same source folder, not copied here)

The source `Logo/` folder also contains `COI.pdf` (certificate of insurance) and `ROOFCO-SE_Prequalification_Packet.xlsx` — business/compliance documents, not brand assets. Left out of this repo; flag to Hayden if a `compliance/` or `documents/` section should be added to hold these separately.
