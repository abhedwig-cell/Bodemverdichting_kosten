# Besluit: volledige en eenduidige codering causale netwerkfiguur

**Datum:** 12 oktober 2026. **Status:** VASTGELEGD ONTWERPBESLUIT, uitvoering nog open. **Context:** expertgroepvoorbereiding en bespreking van `docs/75_offsite_causaal_netwerk_en_effectmatrix_v0_1.md` (huidige inhoudelijke versie 0.2).

## Aanleiding

De volledige causale figuur bevat pijlen zonder C-code. De bestaande C01–C14-matrix is daardoor geen volledige, één-op-één beschrijving van het netwerk. Bovendien omvatten C05 (bemaling en wateroverlast) en C09 (N₂O en CH₄) elk meer dan één afzonderlijk mechanisme. C14 wordt visueel slechts bij één van zes routes getoond terwijl de waarderingsstap voor alle zes geldt.

## Besloten ontwerpprincipes voor versie 0.3

1. **Elke causale procespijl krijgt een unieke code.** De code komt letterlijk op de pijl en verwijst naar precies één rij in de effectmatrix. Ook nu niet-genummerde pijlen, bijvoorbeeld waterstroming → perceelsrandafvoer, poriënstructuur → beworteling en bodemvocht → redoxprocessen, worden opgenomen.
2. **Bundels worden gesplitst.** C05a (extra bemaling) en C05b (wateroverlast) worden afzonderlijke relaties; hetzelfde geldt voor N₂O en CH₄ binnen C09. De uiteindelijke codering en eventuele hernummering worden in v0.3 vastgesteld.
3. **Fysische processen, externe gevolgen en economische waardering zijn afzonderlijke lagen.** Verbindingslijnen naar rapportagevormen (euro's, fysieke indicatoren, kwalitatieve effecten en kennislacunes) zijn geen causale bodemprocessen en krijgen daarom geen C-code van hetzelfde type. Een afzonderlijke, helder benoemde waarderings-/rapportagestap geldt voor ieder offsite-eindpunt.
4. **Eén-op-één controle:** alle causale pijlen zijn terug te vinden in de matrix; alle matrixcodes komen voor in de figuur. Geen impliciete of dubbelzinnige codebetekenis.
5. **Wetenschappelijke terughoudendheid:** codering betekent niet dat een relatie bewezen of positief is. De matrix vermeldt bewijssoort, context, mogelijke tekenwisseling, onzekerheid en verantwoordelijke expert. Het onderscheid tussen bovengrond- en ondergrondverdichting blijft expliciet.
6. **Bestaande autoriteit blijft leidend:** C-codes zijn tijdelijke analyse-identificaties, geen nieuwe canonieke F1–F6/O3-pathway-ID's. Geen nieuwe schadefactoren of evidence-admissions zonder de gebruikelijke kwalificatie.

## Uitvoeringsvolgorde

1. Inventariseer alle pijlen uit v0.2, inclusief ongenummerde relaties.
2. Splits gebundelde mechanismen en wijs stabiele codes toe met een migratietabel oud → nieuw.
3. Maak een nieuwe volledige netwerkfiguur en één-op-één effectmatrix (v0.3).
4. Controleer Mermaid-weergave, leesbaarheid en inhoudelijke samenhang.
5. Werk daarna de PowerPoint bij, niet andersom.
6. Leg de inhoudelijke keuzes en resterende kennislacunes voor aan de expertgroep.

**Acceptatiecriteria:** geen ongenummerde causale pijlen; geen code met twee verschillende causale betekenissen; niet-causale rapportagelijnen duidelijk anders aangeduid; matrix en figuur volledig herleidbaar. Tot uitvoering blijft document 75 versie 0.2 een concept.
