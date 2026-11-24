# SE Roofing white-knockout lockup (derived)

Location: `/home/box/creative-dept/se-roofing/brand/`

**Status: derived knockout, pending Hayden approval of reversed usage.** 24 Nov 2026, America/Chicago.

| File | What |
|---|---|
| `se-lockup-white.svg` | Vector. Horizontal lockup ("SE" mark + ROOFING wordmark), every fill set to `#FFFFFF`, transparent background. viewBox 0 0 461.25 61.6. |
| `se-lockup-white@2x.png` | 922×122, RGBA, transparent |
| `se-lockup-white@4x.png` | 1844×244, RGBA, transparent |

## Source and method

- Source: `haydenclayne-ctrl/SE-Roofing-` `brand/logos/se-roofing-full-lockup-pms.eps` (Adobe Illustrator 30.3 EPS, 4 May 2026). It's the official vector, with real paths and not an embedded raster.
- Steps: EPS → PDF (Ghostscript 10.05, `-dEPSCrop`) → SVG (pdftocairo). Then the 9 fill values were swapped for `#FFFFFF`. No paths were edited, redrawn, simplified or moved. The clip paths and the S/E separation gap come straight from the artwork, and that gap renders as background on dark grounds.
- PNGs are rendered from that SVG in Chromium with a transparent background.

## Approval status

- The repo has **no reversed or white logo file**, and `brand/logos/README.md` **does not explicitly approve** a reversed version. It only says: "On dark photo backgrounds, use a white-knockout version if available, or place on a white/light plate." The live marketing site uses a white SE emblem, but that isn't a repo master.
- So this is a **derived knockout, pending Hayden approval of reversed usage.** Until he approves it, the fallback on dark grounds is the color lockup on a white plate.
- Use it on SE Navy `#203A47`, SE Slate `#456977`, or a dark, quiet area of a photo. Minimum width is 120px on screen. Clear space equals the height of the "S".

## Note

The EPS → RGB conversion turns the spot colors into approximate RGB values (around `#243241` / `#4B708C`), which are **not** the brand hexes. Don't use a color SVG made this way without resetting the fills to `#203A47` / `#456977`. Only the white version is delivered here.
