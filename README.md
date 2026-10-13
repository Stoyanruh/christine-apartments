# Christine Apartments website

Live site: https://christineapartments.com (GitHub Pages, custom domain).
Building: 526 Niagara Street, Buffalo, NY 14201. Operated by 526 Niagara LLC.
Contact on site: christineapartments@outlook.com (email only, by owner's choice).

## Files
- `index.html` – the page that is served. Do not edit by hand; rebuild it.
- `hero-1899.jpg` – hero image: 1899 published engraving of the Kurtzmann piano factory (public domain), upscaled and toned.
- `favicon.svg`, `404.html`, `CNAME` (custom domain for GitHub Pages).
- `_build/` – not published (Jekyll skips folders that start with `_`).
  - `template.html` – page source (same as the claude.ai artifact version).
  - `build.py` – wraps the template into `index.html`.
  - `source/kurtzmann-1899-original.jpg` – original engraving scan.

## How to change the site
1. Edit `_build/template.html`.
2. Run `python3 _build/build.py` from the repo root.
3. Commit and push to `main`. GitHub Pages redeploys in about a minute.

## Decisions (state as of 2026-10-13)
- Purpose: website for Quo A2P 10DLC carrier registration of the 526 Niagara text line.
- Layout modeled on a typical Buffalo property-management site (navy/sand bands, full-width hero).
- Removed by owner: phone number, texting/SMS program section, texting consent, resident services section.
- Kept: privacy-policy line that mobile numbers are not shared for marketing (carriers check for it).
- Legal name shown: "526 Niagara LLC" – must match the EIN letter used for registration.
- Hosting: GitHub Pages, public repo. DNS: apex A records to GitHub Pages IPs, `www` CNAME to `stoyanruh.github.io`.
