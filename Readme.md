# studentencodex
Een statische website voor verschillende codices van Antwerpen. 

Het is een statische site gemaakt met het Jekyll framework. De site is te vinden op https://arnodeceuninck.github.io/studentencodex/.

Alle liederen van de oude rode codex zijn te vinden (en indien nodig te bewerken) in de `_rodex_oud` folder, die van de Antwerpse codex in de `_antwerpse` folder. 

De bestanden beginnen telkens met een paar keywords, met daaronder een blok markdown. De teksten zijn dus telkens geschreven in markdown. Jekyll zet dit dan om naar html (en een json die gebruikt kan worden voor de mobiele app).

Enkele dingen waar je rekening mee moet houden:
- Als de keywords een aanhalingsteken bevatten, moet je heel het keyword tussen aanhalingstekens zetten en indien nodig het aanhalingsteken ook escapen (dus `\"` ipv `"`). Bv. 'title: 't Ros Beyaert' -> 'title: "'t Ros Beyaert"' (escapen is hier niet nodig om dat ' een ander aanhalingsteken is dan ").
- Nieuwe alineas in markdown worden aangegeven met twee lege regels. Eén lege regel geeft dus geen nieuwe alinea!
- Nieuwe regels in markdown worden ofwel aangegeven met één lege regel tussen, ofwel twee spaties op het einde van de voorgaande regel. Het scriptje `automation/space_addr/convert.py` voegt dit overal toe waar dat niet het geval is. 

## Lokaal draaien
Om de site lokaal te draaien, moet je eerst Jekyll installeren. Dit kan je doen met `gem install jekyll bundler`. Daarna kan je de site lokaal draaien met `bundle exec jekyll serve`. De site is dan te vinden op http://localhost:4000/studentencodex/. Dit genereert de nodiges statische bestanden, waaronder de `codices.json` die gebruikt wordt door de mobiele app.

Als je naar github pusht, wordt de site automatisch gegenereerd en gepusht naar de `gh-pages` branch.

## Mobiele app
Er bestaat ook een mobiele app, gemaakt in Flutter. Hiervoor moet je de gegenereerde `codices.json` in de assets folder van de app repo zetten. 

De repo van de app: https://github.com/arnodeceuninck/studentencodex-app

## TODO's
- Antwerpse codex: Alle liedjes vanaf p. 515
- Nummering: het refrein reset de nummering. Nummers staan wel juist in de markdown files, maar markdown nummert bv. 9. ook vanzelf en past het cijfer dus aan.

## Liedjes toevoegen
Gewoon een nieuw bestand toevoegen, bv. in de `_antwerpse` folder. Neem een kijkje naar de andere bestanden in die folder om te weten hoe je het bestand moet opbouwen. 

## Andere codices toevoegen
Als je een andere codices wil toevoegen, maak je een nieuwe folder `_{codex_naam}` en voeg je deze ook toe in de `_config.yml` file. Vergeet ook niet `codices.json` en `_layouts/home.html` aan te passen. In de mobiele app ga je ook nog iets klein moeten aanpassen. 

## Zoekfunctie
- Old search: https://blog.webjeda.com/instant-jekyll-search/ (didn't allow show all by default, allowed searchin in content)\
- Current search: https://www.w3schools.com/howto/howto_js_filter_table.asp (only searches title and page number (voorkomt dat we alle liedjes moeten inladen om de pagina te laden (gebruikt veel 4g anders)))
