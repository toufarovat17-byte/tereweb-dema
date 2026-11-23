# Jak navrhnout demo web pro lead (Tereweb)

Každý lead dostane **originální web navržený od nuly**. Žádná šablona, žádné kopírování struktury jiného dema.
Klient má po otevření odkazu dojem, že někdo přemýšlel o jeho firmě, ne že dostal formulář s vyplněným jménem.

## 0. Pravidlo originality (kontroluje se)

- Před návrhem přečti `_navod/historie.json`. Je tam seznam posledních dem: písma, paleta, typ hero sekce, interaktivní prvek a layout.
- Nový web se musí od **každého z posledních 15 dem** lišit aspoň ve 4 z 5 položek. Stejná dvojice písem ani stejný typ hero nesmí být použité dvakrát po sobě nikdy.
- Po dokončení dema přidej do `historie.json` záznam (viz konec souboru).

## 1. Koncept (než napíšeš první řádek kódu)

Napiš si (jen pro sebe) krátký koncept:
- **Svět oboru:** materiály, nástroje, prostředí, slovník oboru, místo (město, krajina). Odtud se berou barvy, textury, tvary a interaktivní prvek.
- **Pro koho:** kdo je typický zákazník a co chce zjistit během 10 vteřin.
- **Jedna velká věc:** jeden zapamatovatelný prvek, kde utratíš odvahu (hero, interakce nebo typografie). Zbytek stránky zůstane klidný a disciplinovaný.

Příklady konceptů (inspirace, ne šablony):
- Pneuservis: hero s velkou pneumatikou ze SVG, která se při scrollu otáčí; interakce = výběr rozměru pneu (šířka/profil/průměr) a sezóny a rovnou objednání termínu.
- Kosmetika: jemná, papírová estetika, ručně působící nadpisy; interakce = „sestavte si ošetření“ (vyberete péči, délku, doplňky a vidíte souhrn).
- Zemní práce: technický plán, kótované čáry, žlutá výstražná páska; interakce = vyberete terén a typ práce a SVG ukáže, jaký stroj přijede.
- Instalatér: modré technické schéma potrubí; interakce = „Co se děje?“ diagnostika ve 3 klicích, na konci tlačítko zavolat.
- Truhlář: dřevo, letokruhy, přesné spoje; interakce = konfigurátor kuchyně (tvar, délka, materiál) s živým nákresem.
- Veterina: přátelské tvary, pastelové barvy; interakce = výběr zvířete a důvodu návštěvy a objednání.
- Fotograf: tmavá galerie a typografie jako ve filmových titulcích; interakce = výběr typu focení a balíčku.

## 2. Vizuální systém

- **Barvy:** 4–6 pojmenovaných hex barev odvozených z oboru. Ověř kontrast textu (WCAG AA).
- **Písma:** Google Fonts, MUSÍ mít `latin-ext` (čeština). Maximálně 2 rodiny, jasně odlišné role. Ověř, že písmo opravdu podporuje „ěščřžýáíéůú“ (seznam podporovaných subsetů na fonts.google.com nebo v CSS odpovědi).
  Vybírej různorodě, například: Bricolage Grotesque, Familjen Grotesk, Schibsted Grotesk, Onest, Manrope, Sora, Outfit, Urbanist, Unbounded, Archivo (wdth), Big Shoulders, Anybody, Fraunces, Literata, Newsreader, Young Serif, DM Serif Display, Instrument Sans, Figtree, Red Hat Display, Rubik, Space Grotesk (střídmě), Lora, Playfair Display (střídmě), Caveat (jen akcent), Montserrat Alternates, Lexend, Plus Jakarta Sans, Epilogue, Syne.
- **Layout:** střídej archetypy hero: velká typografie, split s ilustrací, plná barevná plocha, SVG scéna, interakce přímo v hero, asymetrická mřížka, horizontální pás, „karta“ přes ilustraci… a střídej rozvržení sekcí.
- **Ilustrace:** vlastní inline SVG (tvary, ikony, scény z oboru). Žádné externí obrázky kromě loga klienta (jen https).
- **Pohyb:** jedna promyšlená animace při načtení nebo při scrollu. Respektuj `prefers-reduced-motion`.

### Čemu se vyhnout (typické znaky „AI webu“)
- krémové pozadí + terakotová/hliněná barva + patkový nadpis,
- černé pozadí s jedinou neonově zelenou barvou,
- všude stejné zaoblené karty se stejným stínem a gradientovými skvrnami,
- VELKÉ ŠEDÉ ŠTÍTKY nad každým nadpisem, číslování 01/02/03 u věcí, které nejsou postup,
- zvýraznění jednoho slova nadpisu jinou barvou,
- šipky „→“ v každém tlačítku, fade-in u každé sekce.

## 3. Povinný obsah

1. Proužek nahoře: `Návrh nového webu pro <b>{Firma}</b>, připravila Tereza Toufarová z Tereweb.cz`.
2. Navigace s logem (jejich https logo, nebo vlastní znak/monogram) a tlačítkem zavolat.
3. Hero s konkrétním sdělením pro jejich obor a město.
4. **Interaktivní prvek** specifický pro obor (viz koncept). Musí opravdu fungovat a vést k poptávce.
5. Služby: jen to, co skutečně dělají (z firmy.cz, webu, FB).
6. Jak spolupráce probíhá NEBO proč právě oni (podle toho, co dává smysl).
7. Galerie / ukázky: místo fotek stylové placeholdery v duchu designu s textem „Sem přijdou fotky vašich zakázek“.
8. Kontakt: skutečný telefon, email, adresa/obec, formulář (submit = `preventDefault` a zpráva „Toto je ukázka formuláře. V hotovém webu by zpráva přišla rovnou na váš e-mail.“).
9. Patička: `© 2026 {Firma}` a `Návrh připravila Tereweb.cz`.

## 4. Pravdivost

- NIKDY nevymýšlej recenze, reference, ceny, roky praxe, počty zakázek, certifikáty, otevírací dobu ani „nonstop“, pokud to nemáš ze zdroje.
- Texty česky, přirozeně, v 1. os. mn. č. za firmu, bez pomlček „–“ a „—“, bez marketingových frází („jsme lídrem na trhu“).

## 5. Technika

- Jeden soubor `{slug}/index.html`, CSS i JS inline, bez frameworků. Externě jen Google Fonts.
- `<meta name="robots" content="noindex, nofollow">`, `lang="cs"`, viewport, `<title>{Firma} – {Město} (návrh webu)</title>`.
- Responzivní od 360 px, viditelný focus, klávesnicí ovladatelná interakce.
- Rozsah: obvykle 250–600 řádků. Kvalita > délka.

## 6. Kontrola kvality (povinná)

1. Nainstaluj si prohlížeč, pokud chybí: `pip install --break-system-packages playwright && python3 -m playwright install --with-deps chromium`.
2. Pro každé demo udělej screenshot desktop (1366×900, celá stránka) a mobil (390×844), zachyť chyby z konzole (`page.on("pageerror")`) a vyzkoušej kliknutí na interaktivní prvek.
3. Screenshoty si prohlédni (Read na PNG). Oprav: rozbitý layout, přetékající text, nečitelný kontrast, nefunkční interakci, chybějící diakritiku, prázdná místa.
4. Zeptej se sám sebe: „Vypadá to jako web, za který by firma ráda zaplatila 15 000 Kč? Liší se zřetelně od ostatních dem?“ Když ne, přepracuj.
5. Screenshoty NEcommituj.

## 7. Zápis do historie

Na konec pole v `_navod/historie.json` přidej:
```json
{"slug": "...", "datum": "YYYY-MM-DD", "obor": "...", "pisma": ["...", "..."], "paleta": ["#...", "#..."], "hero": "popis typu hero", "interakce": "popis interaktivního prvku", "layout": "krátký popis rozvržení"}
```
