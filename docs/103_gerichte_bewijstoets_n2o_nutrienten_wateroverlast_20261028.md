# Gerichte bewijstoets F1 F3 F4: ondergrondverdichting en off-site effecten

**28 oktober 2026 | source-scoped review | uitsluitend toetsbare uitspraken, geen nationale schadefactor**

Vervolg op de [centrale matrix](../evidence/offsite_results_matrix_v0_1.csv), [document 102](102_offsite_zes_categorieen_resultatenmatrix_v0_1.md) en [Defra-bronaudit 101](101_defra_appendix_h_occurrence_volledige_methodereconstructie_v0_1.md). Bronnen: aangeleverde primaire PDF's uit de Teams-collectie en aanvullende openbare publicatiepagina's. Herkomst van de nieuwe internationale studies wordt hieronder apart genoemd. **De matrix is niet aangepast omdat de kwalificatiestatus niet tot nationale monetaire admission is veranderd.**

## 1. F3 N2O: wat meten de studies echt?

| Studie | Proef/meetbasis | Kwantitatieve bevinding en grens | Toelaatbare interpretatie |
|---|---|---|---|
| Bessou et al. (2010), *Modelling soil compaction impacts on nitrous oxide emissions in arable fields*, European Journal of Soil Science 61, 348–363 | Franse suikerbietvelden 2007/2008; in nat voorjaar compactiebehandeling met beladen tractor versus conventionele bewerking; automatische kamers; temperatuur/vocht 10–20 cm, bulkdichtheid 0–30 cm | Gemeten cumulatief 944 en 977 g N2O-N/ha zonder extra verdichting, 1448 en 1382 g N2O-N/ha met behandeling; bron-kwalificatie: **veldbehandeling omvat bovenste laag en is niet als afzonderlijke 30–100 cm ondergrondcontrast geïsoleerd** | CONTEXT_EXPERIMENT_ONLY, geen Nederlandse subsoil-emissiefactor |
| Pulido-Moncada et al. (2022), *Soil compaction raises nitrous oxide emissions in managed agroecosystems* (meegeleverd review) | Review over meerdere landgebruikstypen, met expliciete topsoil-contrastbeoordeling | Factor 1,3–42 in abstract slaat op **bovengrondverdichting** | Niet gebruiken voor ondergrond-effectband |
| Pulido-Moncada et al. (2024), *Soil pore network effects on the fate of nitrous oxide as influenced by soil compaction, depth and water potential*, Soil Biology and Biochemistry 197, 109536, DOI 10.1016/j.soilbio.2024.109536 | Intacte kernen uit lysimeters met **TopComp, SubComp en NoComp**; diepten 10–20, 30–40 en 50–60 cm; gecontroleerde injectie N2O onderaan kern, diffusie en micro-CT | Lagere porieconnectiviteit, gasdoorlaatbaarheid en diffusie bij verdichting; analyse wijst porieconnectiviteit als belangrijkste predictor aan. **Geen gemeten netto seizoensveldflux door ondergrondverdichting** | DIRECT_SUBSOIL_PROCESS_EVIDENCE voor gastransport; niet als N2O-emissiecoëfficiënt |
| Bommisetty et al. (2026), *Influence of tillage intensity and soil compaction on N2O emissions under field conditions* (preprint, SSRN 6854021, online 30 mei 2026) | Twee Deense veldsites, verschillende grondbewerkingen en apart rijsporencontrast op één site | Relevant voor behandeling/landgebruik, maar geen in deze ronde gekwalificeerd afzonderlijk diep ondergrondcontrast of nationaal effect | SOURCE_CANDIDATE, verifieer volledige methode en toestand |
| Bimantara et al. (2026), *Tractor-induced soil compaction drives nitrous oxide emissions*, DOI 10.1016/j.still.2026.107323 | Deense veldwaarneming 2024–25, rijsporen en controle; bodemfysische kernen **0–5 cm**; bronpagina vermeldt publicatie **december 2026** | De webindex biedt abstractcijfers maar publicatiedatering ligt **na** deze notitiedatum 28-10-2026. **Niet als op 28 oktober beschikbaar bewijs behandelen**, totdat eventuele aantoonbare eerdere online publicatie is vastgesteld | POSTDATED / excluded for contemporaneous evidence |

**Beslissing F3:** er is een causale mechanistische basis voor V23–V29, inclusief specifieke ondergrond-processen. Het cruciale ontbrekende endpoint is **netto N2O- en CH4-veldflux als functie van aantoonbaar 30–100 cm ondergrondcontrast**, uitgesplitst naar weersituatie, bemesting, landgebruik en (bij gastransport) productie versus consumptie/retentie. Geen nationaal emissieverschil berekend.

## 2. F4 N/P: de literatuur levert geen uniforme tekenrichting

Primaire bron: Groenendijk et al., WENR rapport 2811, *Effecten van verbetering bodemkwaliteit op waterhuishouding en waterkwaliteit*. Het ten geleide en de samenvatting noemen waterkwaliteitsresultaten **niet eenduidig, soms tegenstrijdig**; de interventie combineert opheffen van verdichting, hoger organischestofgehalte en andere bodemkwaliteitsaspecten. Dit is **niet** een enkelvoudig verdichtingscontrast.

Aparte fysieke balansregels:

- `N_out = runoff_N + drainage_N + leaching_N`, alleen wanneer elke term bij dezelfde ruimtelijke systeemgrens terechtkomt; voorkom dubbeltelling wanneer drain- en leaching-doorsneden elkaar overlappen.
- Voor P apart **opgelost P en particulair P** onderscheiden, met erosie, sorptie, preferente stroming en transport via verschillende afvoerroutes.
- Een lagere oppervlaktestroming kan gepaard gaan met meer infiltratie en mogelijk andere (niet noodzakelijk lagere) nitraatflux; hydrologische verschuiving is **niet** gelijk aan een netto waterkwaliteitsverbetering.
- De CLO N/P-landbouwbijdrage uit document 100 is nationale probleembaseline, **geen compaction attributable fraction**.

**Beslissing F4:** geen uit de huidige primaire bronnen afleidbaar nationaal percentage extra of minder N/P-vracht. Geschikt vervolg is zoeken naar gepaarde, **vracht-gebaseerde** proeven per afvoerroute en bodemcontext. Een concentratieverschil zonder fluxvolumes is onvoldoende voor vrachttoerekening.

## 3. F1 Wateroverlast: waar begint feitelijke externe schade?

Primaire bron: WENR 2811, modelscenario's met grotere infiltratie bij bodemverbetering en sterk afhankelijke piekrespons per bui/vochttoestand. Het is geen geïsoleerde ondergrondverdichtingstoets. Defra Appendix H geeft de beoogde keten **perceelrespons → routing → regionale overschrijding → receptor → schade**, maar berekende uiteindelijk met de vereenvoudiging dat een gemiddelde 7% afvoerwijziging leidt tot 7% kostenschommeling.

Voor een echte Nederlandse attribution pair moeten zes opeenvolgende gegevens beschikbaar zijn:

1. **Bodemtoestand:** referentie versus huidige 30–100 cm laag, op representatieve profiel- en gebiedscontext.
2. **Bronrespons:** per gebeurtenis `ΔQ(t)` of `Δrunoff(t)` plus veranderingen drainage/berging en massabalans.
3. **Connectiviteit en routing:** welk deel van het extra water, met welke looptijd, bereikt de beheerde watergang?
4. **Beheerrespons:** pomp, stuw en opslag werken niet noodzakelijk lineair en niet iedere extra mm wordt extra bemaling.
5. **Systeempiek en blootstelling:** slechts relevante drempeloverschrijding bij receptor veroorzaakt extra overlast.
6. **Additionele economische gevolgschade:** vermijden van dubbele telling van maatregelen en resterende schade; alleen **marginale verschilkosten**.

**Beslissing F1:** een procentueel runoff-effect mag niet worden omgezet in hetzelfde procentuele bedrag schade. Tollebeek kan een lokale bewijs- en rekenomgeving zijn; nationale opschaling wacht op overdraagbaarheid.

## 4. Directe implicaties voor de centrale matrix

| Categorie | Eerste mechanisme onderbouwd? | Kwantitatief direct toepasbaar voor Nederlandse ondergrondschade? | Prioritaire toets |
|---|---|---|---|
| F3, N2O/CH4 | Ja, inclusief Deens gastransport ondergrond | **Nee**: netto veldemissie niet geïsoleerd | Separate source / gas-production / net flux study design |
| F4, N/P | Ja, hydro- en biogeochemische routes | **Nee**: routes en effecten mengen, mogelijke tegengestelde tekens | Gepaard waterbalans + N/P-vracht per route |
| F1, wateroverlast | Ja, lokale waterbalans | **Nee**: transfer, operatie en receptor ontbreken | Eén case met waargenomen `Q(t)`, routing en overschrijding |

De andere drie categorieën (waterbeschikbaarheid, middelen, bodemleven) blijven in [matrix v0.1](../evidence/offsite_results_matrix_v0_1.csv) zichtbaar. Er is nog geen argument om een van de zes categorieën weg te strepen op basis van monetariseerbaarheid.

## 5. Bronnen en provenance

- Teams PDF `TEAMS20261028_006`: Bessou et al. 2010, vooral abstract (PDF p.1), Materials and Methods (PDF p.2–4) en Table 3 (PDF p.6–7). Dichtheidsprofiel 0–30 cm en het tractorbehandelingsontwerp verhinderen de claim 'zuivere ondergrondverdichting'.
- Teams PDF `TEAMS20261028_007`: Pulido-Moncada et al. 2022, abstract/topsoilfactor.
- Teams PDF `TEAMS20261028_038`: WENR rapport 2811, ten geleide, samenvatting en hoofdstuk 5.
- Extern (open publicatie): https://doi.org/10.1016/j.soilbio.2024.109536 (Pulido-Moncada et al. 2024), gecontroleerde topsoil/subsoil-methodiek.
- Extern (preprint): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6854021 (Bommisetty et al. 2026), beschikbaar vanaf 30-05-2026.
- Extern (nog te dateren): https://doi.org/10.1016/j.still.2026.107323 (Bimantara et al. 2026), vermelde journal publication december 2026, **niet als in oktober gepubliceerde studie gebruikt**.

**Status:** BRONSCOPES_GEVALIDEERD / NATIONALE_EFFECTCOEFFICIENTEN_NIET_TOEGELATEN. Geen wijziging in causale netwerk v0.7, geen wijzigingen aan `evidence/*.csv` en geen nieuwe SWAP-run.
