# Kwantitatieve broncontrastcontrole: N₂O en begrensde off-site conclusies

**28 oktober 2026 | EXPERIMENTAL_CONTRAST_NOT_NATIONAL_FACTOR**

Gericht vervolg op [103](103_gerichte_bewijstoets_n2o_nutrienten_wateroverlast_20261028.md) en de centrale [zes-categorieënmatrix](../evidence/offsite_results_matrix_v0_1.csv). De gepubliceerde getallen in deze notitie zijn **studie-uitkomsten**; herberekende verschillen zijn expliciet aangeduid. Dit is geen nationale Nederlandse extrapolatie en geen nieuwe canonieke evidence-admission.

## 1. Bessou et al. 2010: uitgerekend verschil per groeiseizoen

**Primaire bron:** C. Bessou et al. (2010), *Modelling soil compaction impacts on nitrous oxide emissions in arable fields*, European Journal of Soil Science 61, 348–363, DOI 10.1111/j.1365-2389.2010.01243.x. De aangeleverde PDF (`TEAMS20261028_006`) is lokaal gelezen. De bron vermeldt: noord-Frankrijk, twee suikerbietpercelen in 2007 en 2008, respectievelijk 100 en 150 kg N/ha bemesting; extra verdichtingsbehandeling door berijding van natte grond met een beladen tractor. De proef is geen geïsoleerd contrast van uitsluitend 30–100 cm diepte.

| Jaar | Zonder extra verdichting, g N₂O-N/ha | Met behandeling, g N₂O-N/ha | Verschil, g N₂O-N/ha | Relatief verschil t.o.v. controle | Verhouding |
|---|---:|---:|---:|---:|---:|
| 2007 | 944 | 1448 | **+504** | **+53,4%** | 1,534 |
| 2008 | 977 | 1382 | **+405** | **+41,5%** | 1,415 |

Berekening: `delta = treatment - control`, `relative = delta/control`; **geen** geforceerd gepoolde effectschatting. In beide jaren wordt een positieve verandering gemeten, maar er zijn slechts twee percelen/jaren en de behandeling is niet puur ondergrondverdichting. Het verschil in bemesting en condities tussen jaren onderstreept dat 2007 en 2008 **niet** een statistisch onafhankelijke landschapssteekproef vormen. Gerapporteerde waarden zijn cumulatieve emissies **in N₂O-N**, niet N₂O-massa en niet CO₂-equivalenten.

**Toegestane inzet:** experimentbasis en hypothese voor V23–V27, voor een bereden akkerbouwbodem met expliciete condities. **Niet:** een Nederlandse emissiefactor per verdichte hectare of een geldelijke schadebandbreedte.

## 2. Pulido-Moncada et al. (2024): ondergrondmechanisme zonder netto emissie-effect

**Bron:** *Soil pore network effects on the fate of nitrous oxide as influenced by soil compaction, depth and water potential*, Soil Biology and Biochemistry 197, 109536, DOI 10.1016/j.soilbio.2024.109536. Open-access journalabstract en Aarhus University repository bevestigen intacte bodemkernen met `TopComp`, `SubComp`, `NoComp`; micro-CT, luchtpermeabiliteit, verbonden poriën en diffusiemetingen na injectie van N₂O in de onderzijde van de kernen. De behandelingen verschillen naar verdichte laag en monstdiepte.

**Wat werkelijk gemeten is:** de fractie van een *geïnjecteerd* N₂O-signaal die bovenin verschijnt onder gecontroleerde laboratoriumcondities, dus gastransport/retentie; plus structuur en diffusie. Lagere porieconnectiviteit en gastransport onder verdichting ondersteunen V23, V24.

**Wat hier niet uit volgt:** minder transport betekent niet automatisch minder productie en ook niet automatisch meer netto uitstoot. N₂O kan bij langere verblijftijd verder reageren, met mogelijke vorming van N₂. De studie is daarom **PROCESS_DIRECT / EMISSION_RATE_NOT_IDENTIFIED**. De auteurs geven op de journalpagina expliciet aan dat zij geen toestemming hebben om de onderliggende data te delen. Niet als nationale N₂O-coëfficiënt gebruiken.

## 3. F4 nutriëntenvracht: welke grootheid ontbreekt?

De Nederlandse WENR-rapportage 2811 bevat hydrologische mechanistische vergelijkingen, maar combineert bodemverbeteringen. Het effect op N/P-transport heeft geen eenduidige richting. Daarom kan in deze ronde **geen numerieke band** worden afgeleid voor uitsluitend ondergrondverdichting. Een volgende brontoets vereist, voor dezelfde behandeling en tijdsgrens, **zowel waterflux als N-/P-concentratie per route**, opdat `load = integral Q(t)×C(t) dt` werkelijk kan worden bepaald. Voor P opgeloste en particulaire fracties apart. Lozingspunt en grondwaterdiepte expliciet onderscheiden.

De in CLO gerapporteerde nationale N/P-landbouwbelasting is een **receptorbaseline**, niet de te berekenen `delta_load`.

## 4. F1 wateroverlast: wat ontbreekt numeriek?

Een getal voor lokale runoff zonder route, operationele ingrepen, drempeloverschrijding en getroffen objecten is geen externe schade. Defra SP1606 Appendix H heeft juist in die keten een niet-gevalideerde proportionaliteitsaanname gebruikt. De eerste vereiste databundel voor één Nederlands beheerd gebied is: gepaarde hydrogrammen op perceelsrand, ruimtelijke connectiviteit/afvoersysteem, peilen en pomp-/stuwlogica, waargenomen capaciteit/overloop en schade-receptoren. Zolang die ontbreken is de kwantitatieve off-site band **NOT_IDENTIFIED**.

## 5. Resultaatdiscipline voor het project

| Categorie | Nieuw hard kwantitatief resultaat in deze ronde | Kwalificatie |
|---|---|---|
| N₂O | Twee experimentele verschillen: +504 en +405 g N₂O-N/ha voor extra beladen tractorbehandeling van suikerbietengrond | **GEMETEN BIJ SPECIFIEKE AKKERBEHANDELING**; niet ondergrond-specifiek |
| Gastransport in ondergrond | Structurele/kwalitatieve directe vergelijking TopComp/SubComp/NoComp | **MECHANISME AANGETOOND**; netto N₂O-effect niet bepaald |
| N/P | Geen subsoil-only `delta_load` geïdentificeerd | **NIET NUMERIEK KWALIFICEERBAAR** |
| Regionale wateroverlast | Geen gekwalificeerde `delta_damage` uit bodemcontrast | **NIET NUMERIEK KWALIFICEERBAAR** |

**Aanbevolen beslissing:** stop met het zoeken naar een generiek landelijk percentage. Breng eerst de ontbrekende **ondergrond-specifieke** broncontrasten voor N₂O/CH₄ en N/P in kaart. Onderzoek voor wateroverlast één daadwerkelijk gekoppeld regionaal geval, niet de nationale totaaluitgaven.

De status van de zes effectcategorieën blijft ongewijzigd; geen landelijke schadeband, geen monetaire schadepost, geen nieuwe causale relaties en geen wijziging aan de WUR-notitie.
