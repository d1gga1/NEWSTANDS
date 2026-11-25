# How to translate the NEWSTANDS website

Source file: `_build/i18n/it.json` (Italian). Output: `_build/i18n/<code>.json` — the SAME JSON structure
(same keys, same list lengths, same nesting), with every string value translated. Set `"_lang"` to the language code.
Write the file as UTF-8 JSON (no comments, no trailing commas). Then run:

    python3 /mnt/user-data/outputs/nb/_build/validate.py <code>

and fix every ERROR. Warnings about length are worth fixing; "identical to Italian" is only acceptable for proper names.

## Who the reader is
NEWSTANDS is an exhibition-stand builder based in the Milan area (Italy). Readers are marketing / trade-show managers
of companies that exhibit at trade fairs. Write natural, idiomatic, persuasive B2B marketing copy — not a word-for-word
translation. Keep the tone short, confident and concrete. This is also SEO copy: use the term people actually search
for in that language for "exhibition stand / trade fair stand" (e.g. DE "Messestand", FR "stand salon / stand d'exposition",
ES "stand ferial", NL "beursstand", PL "stoisko targowe", EN "exhibition stand"), and keep "Milan" (localized city name:
Mailand, Milan, Milán, Milão, Mediolan, Μιλάνο, Милано, मिलान, 米兰, میلان …) wherever the Italian mentions Milano.
Main message to keep strong everywhere: we are based in the Milan area — Milan is one of Europe's top trade-fair hubs —
and we travel with our own crews to every exhibition centre in Europe.

## Rules
1. Never change: `NEWSTANDS`, `NEWSTANDS Allestimenti` (company name, keep as is), e-mail addresses, phone numbers, URLs,
   `WhatsApp`, names of venues and fairs (Fiera Milano Rho, Allianz MiCo, Salone del Mobile.Milano, EICMA, HostMilano,
   TUTTOFOOD, MIDO, MICAM, Messe Düsseldorf, Koelnmesse, Messe Frankfurt, Messe München, Paris Nord Villepinte,
   Paris Expo Porte de Versailles, Eurexpo Lyon, Fira de Barcelona Gran Via, IFEMA Madrid, RAI Amsterdam, Brussels Expo,
   Messe Wien, Palexpo Genève, MEDICA), the street address (Via Carlo Delcroix 12, 27020 Tromello (PV)).
   City names inside running text SHOULD be localized (Colonia → Cologne/Köln, Monaco → Munich/München, Ginevra → Geneva …).
   Country/region names in text are translated normally.
2. Placeholders like `{t}` `{c}` `{n}` `{i}` `{type}` `{sides}` `{area}` `{dim}` must appear exactly as in the Italian string.
3. HTML inside strings (`<a href="...">…</a>`, `<br>`) must be kept exactly (same tags, same attributes). Translate only the text around them.
4. `pages.*.slug`: URL slug for that page. Lowercase ASCII only: a–z, 0–9 and hyphens, no accents, unique, keyword-rich
   in the target language (e.g. DE `messestand-individuell`, FR `stands-salon-sur-mesure`). For bg, el, hi, pa, zh, ur use these
   English slugs: personalizzati `custom-exhibition-stands`, modulari `modular-exhibition-stands`, eventi `event-congress-setups`,
   showroom `showroom-temporary-store`, grafica `large-format-graphics`, americane `truss-ledwall-lighting`,
   arredi `stand-furniture-rental`, montaggio `stand-installation-dismantling`, milano `exhibition-stands-milan`,
   europa `exhibition-stands-europe`.
5. `meta.title` and `pages.*.title`: ≤ 65 characters, keep "| NEWSTANDS" at the end. `desc`: 120–160 characters.
6. `ui.langName` = the language's own name written in that language (Deutsch, Français, Español, Polski, Ελληνικά,
   हिन्दी, ਪੰਜਾਬੀ, 简体中文, اردو …).
7. `home.h025` is an animated statement split on spaces: keep 2–3 key words prefixed with `*` (e.g. `*brand*` style:
   the asterisk goes directly before and after the word, as in the Italian). For Chinese, put a normal space between
   short phrase chunks in this one string so it can be split.
8. `js.avail` is shown on a split-flap board: max 12 characters, UPPERCASE (where the script has case).
   `js.c3` strings are painted on 3D walls: UPPERCASE, keep them about as short as the Italian.
9. Short UI labels (nav items, buttons, tags, `js.ld`, `js.ty`, `js.mq`) must stay short — similar length to Italian.
10. Some Italian headings are split in two keys that are displayed one after the other as two lines of ONE heading.
    Translate the pair so that it reads naturally line 1 + line 2 (word order may move between the two lines):
    h028+h029 ("Dal nulla" / "allo stand."), h050+h051+h052+h053 ("Tu pensi / ai clienti. / Al resto / pensiamo noi."),
    h055+h056 ("Cosa / costruiamo"), h059+h060 ("Stand / realizzati"), h009+h064 ("Configura / il tuo stand" — h009 is ALSO
    the nav label "Configure", so it must work alone too), h075+h076 ("Prossima / partenza" = next departure, a
    departures-board pun), h085+h086 ("Domande / frequenti"), h089+h090 ("Hai una fiera / in calendario?").
    h022 "Configura il tuo" is a button = "Configure yours".
    h099–h103 are form checkbox labels (project type). h104–h107 are form field labels. h110 + (email link) and
    h111 + (phone link) are fragments around links: "Nothing opened? Write to …" / "or call …".
11. `works[*].t` are client/project names: keep them, but translate generic Italian words inside them
    ("Uttar Pradesh — Agricoltura" → "Uttar Pradesh — Agriculture", "Tunisia — Medica Düsseldorf" → localize "Tunisia").
    `works[*].g` are filter categories (Design, Food & Health, Turismo, Industria, Moto, Medicale): translate consistently —
    the same Italian value must always get the same translation.
12. `js.lbl` are technical drawing labels: "L"=width, "P"=depth, "H"=height; use the local initials; keep numbers.
13. Urdu (ur) is right-to-left Arabic script; Hindi = Devanagari; Punjabi = Gurmukhi script; Chinese = Simplified (zh-Hans).
    Western digits (0–9) are fine everywhere.
14. Do not add or remove keys. Do not translate key names. Keep `_lang` = the language code.
