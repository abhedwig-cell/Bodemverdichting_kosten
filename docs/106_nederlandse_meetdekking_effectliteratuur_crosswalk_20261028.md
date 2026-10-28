# Nederlandse meetdekking versus bewezen effectcontext: eerste profielvergelijking

**28 oktober 2026 | COVERAGE_CROSSWALK | geen nieuwe meetwaarden / schadefactor**

Dit is de eerste controle op **feitelijke dataset-overlap** in plaats van een nieuwe literatuurreview. Gecontroleerde projectbronnen: `data/soil/tollebeek_soil_profiles.csv`, `data/soil/tollebeek_soil_layers.csv`, `data/soil/tollebeek_profile_screening_v0_1.json` en `data_requests/data_request_register.csv`. Effectbronnen: BoVer WENR 3404; Hanse (2011), WENR 2811; Bessou (2010), Pulido-Moncada (2024); Deasy (2009) en Quinton (2024). Volledige [koppeltabel](../evidence/nl_profile_effect_transfer_screen_v0_1.csv).

## 1. Wat daadwerkelijk als numerieke data aanwezig is

**Voor Tollebeek OT.02:**
- Acht SoilPhys-profielen, 117 screeningspunten waarvan 113 een modal profiel opleverden; geen gevalideerde verdichtingsmeting aan die punten. De verdeling 70/14/13/5/4/3/3/1 is een **aantal screeningshits**, geen areaalgewicht en geen percentage verdichte bodem.
- Per profiel bodemhorizonnen tussen 0 en 120 cm met textuur, organische stof, modal bulkdichtheid en Staring-klasse.
- De zes bovenste niet-veenrijke kandidaatprofielen mogen niet zonder verdere analyse als één 'zand' worden behandeld. Mineralogie, lutum/silt en laagdiepte lopen duidelijk uiteen.
- De circa 1800 ondergrondverdichtingsmeetlocaties uit het recente expertgesprek zijn een **genoemde dataset**, maar geen met locatie-ID, survey design, breedtegraad, gewas, diepte, gemeten dichtheid en QC als analysebestand in de gecontroleerde projectlocaties aanwezig. Geen landelijke prevalenties of relatieve dichtheidsklasse uit afgeleid.

**Status bestaande projectcontracten:** `DR_SM_PROFILE = ADMITTED` uitsluitend voor profielidentiteit/context; `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`, geen geauditeerde ruwe Flevoland-puntwaarden of Tollebeek-join. Deze statuses blijven gelden.

## 2. Per profiel de belangrijkste inhoudelijke verschillen

| SoilPhys ID | Bodemkaartcode | Hits | Ondergrondcontext 30–100 cm | Meest nabije literatuur | Oordeel |
|---|---|---:|---|---|---|
| 90115240 | Mn15A | 70 | 25–50 cm O9 en 50–120 cm O8; minerale zavel/zandige ondergrond | WENR 2811, Hanse | Hydrologische analogie, niet gekalibreerd |
| 15100 | Mv51A | 14 | 25–60 cm minerale lagen, 60–120 cm zeer organisch materiaal | WENR 2811 | Laagovergang vereist aparte fysica |
| 15250 | Mn15Av | 13 | 25–105 cm afwisselende minerale lagen, vanaf 105 cm organisch | WENR 2811 | Geen uniforme verdichte laag aannemen |
| 90115270 | Mn25A | 5 | 25–120 cm fijnere minerale lagen | WENR 2811 | Niet overeenkomend met BoVer-zand |
| 11020 | Zn10A | 4 | 25–120 cm zand/silt, Staring O4 | BoVer 3404 | Alleen procesanalogie; andere grond |
| 12010 | Sn13A | 3 | 25–120 cm zandig, Staring O3 | BoVer 3404 | Alleen procesanalogie |
| 11021 | Zn10Av | 3 | 25–70 cm minerale laag, vanaf 70 cm organisch | BoVer 3404 | Mineraal/organisch afzonderlijk |
| 90111050 | Zn50A | 1 | 25–120 cm zand, van O2 naar O1 | BoVer 3404 | Alleen procesanalogie; grover zand |

De stof- en textuurgegevens zijn **modal profielcontext**, niet direct gemeten op een bijbehorende verdichte locatie. De profielen zijn geen nationaal representatieve steekproef. De aanwezigheid van hoog organisch materiaal is een reden om grondsoort en classificatie te controleren, niet automatisch de vaststelling dat bodemverdichting onmogelijk is.

## 3. Directe overlap met effectonderzoek

| Effectstudie | Gemeten bodemtype/diepte | Relatie tot Nederlandse profielbasis | Toegelaten gebruik |
|---|---|---|---|
| BoVer 3404 | Gehomogeniseerde zwak lemige fijne **bovengrond**, verdicht als 30–40 cm kunstmatige laag | Enkele Tollebeek-zandprofielen hebben oppervlakkige textuurovereenkomst, maar geen identieke structuur/diepte | Hypothese, diagnostische curvevergelijking; geen directe parameteroverdracht |
| Hanse, bieten | Nederlandse akkerpercelen, ondergrond-Ks en bovengrondse luchtgevulde porositeit | Nederlandse minerale akkercontext, maar landgebruik en bodemtype moeten worden gepaard | Plausibiliteit, geen causale opbrengstfactor |
| WENR 2811 | Voornamelijk dekzand op melkveebedrijven; gecombineerd bodembeheer | Ander landgebruik en bodemcontext | Hydrologisch mechanisme en experimenteel ontwerp |
| Bessou 2010 | Noord-Franse suikerbieten, berijding, metingen vooral in bovenste 30 cm | Geen geïsoleerde ondergrondbehandeling | Topsoil/traffic context voor N₂O |
| Pulido-Moncada 2024 | Deense intacte kernen, TopComp/SubComp/NoComp 10–60 cm | Directer procesbewijs van subsoil-gastransport, geen Nederlandse netto-emissiefactor | Mechanisme gasdiffusie |
| Deasy / Quinton | Britse tramlines en oppervlakkige P-vrachten | Andere laag en hellings-/afvoercontext | Transportroute, geen NL subsoil-P-factor |

## 4. Conclusie voor stratificatie van nationale meetpunten

Een nationale analyse moet minimaal op **bodemtype × landgebruik × bemonsterde dieptelaag × meetperiode** kunnen uitsplitsen. Waar gegevens toereikend zijn ook mechanische belasting, vochtconditie, referentiedichtheid en laagdikte. De rol van *diepte* is onmisbaar: een hoog gemeten bulkdichtheid in natuurlijke zandondergrond is niet automatisch antropogene verdichting.

**Voorstel voor eerste concrete datacontrole:** vraag één datadictionary en tabeloverzicht van de genoemde ~1800 locaties op met exacte laaggrenzen, bulkdichtheid, bodemtype, landgebruik, historische meetdatum, replicaten, coördinaten en steekproef-/selectiemethode. Eerst vaststellen hoeveel records per bodem × landgebruik × diepte beschikbaar zijn en welk deel een geloofwaardig minder-verdichte referentie heeft. Geen Nederlandse kaart of schadeband zolang dit niet controleerbaar is.

## 5. Bewijs- en gebruiksstatus

`TOLLEBEEK_PROFILE_CONTEXT_PRESENT`; `NATIONAL_POINT_DATA_NOT_VERIFIED`; `SUBSOIL_EFFECT_TRANSFER_NOT_ADMITTED`; `NO_NATIONAL_DAMAGE_COEFFICIENT`.

Er zijn **8 lokale profielcontexten**, maar **0 geverifieerde gemeten CURRENT/REFERENCE-paren** die zonder voorbehoud aan de effectstudies kunnen worden gekoppeld. Dat is een vaststelling over de gecontroleerde projectbestanden, niet de bewering dat de data elders niet bestaan.

Geen wijzigingen aan v0.7, Word-notitie of bestaande admitted claim/evidence-registers.
