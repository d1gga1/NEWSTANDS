# Generatore del sito NEWSTANDS (28 lingue)

Le pagine del sito (home, 8 servizi, Milano, Europa × 28 lingue) sono **generate**:
non modificare a mano `index.html` o le cartelle delle lingue, perché vengono riscritte.

## Dove si modificano i contenuti
- `i18n/it.json` → testi italiani (home, FAQ, pagine servizio, menu, contatti)
- `i18n/<lingua>.json` → stessi testi nelle altre lingue (en, de, fr, es, pt, nl, pl, ro, cs, sk, sl, hr, hu, bg, el,
  da, sv, fi, et, lv, lt, ga, mt, hi, pa, zh, ur)
- `home.tpl.html` → struttura grafica della home (CSS, 3D, animazioni)
- `sub.css` → grafica delle pagine servizio
- `base.json` → foto dei lavori e foto usate in ogni pagina servizio
- `build.py` → numeri di telefono, WhatsApp, email, elenco lingue

## Rigenerare il sito
Dalla cartella del sito:

    python3 _build/build.py

Il comando riscrive `index.html`, le pagine italiane (`/stand-fieristici-milano/` …), le cartelle `/en/`, `/de/` …,
`sitemap.xml`, `llms.txt`, `llms-full.txt` e `assets/sub.css`.

Se modifichi `it.json`, ricordati di aggiornare anche le altre lingue (si può chiedere a Claude:
"aggiorna le traduzioni dopo la modifica di it.json"). Per controllare un file di traduzione:

    python3 _build/validate.py de

## Pubblicare

    git add -A && git commit -m "Aggiornamento sito" && git push origin main

La cartella `_build` non viene pubblicata online (GitHub Pages ignora le cartelle che iniziano con `_`).
