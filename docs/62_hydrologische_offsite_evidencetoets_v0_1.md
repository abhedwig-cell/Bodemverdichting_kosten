# Hydrologische off-site routes: evidence-toets en onderzoekskeuze v0.1

**Datum:** 2026-10-12. **Status:** RESEARCH_REVIEW_ONLY, niet gekwalificeerd voor nationale schadeberekeningen. Aansluiting op F1–F5, O3 en de bestaande evidence-governance. Geen nieuwe empirische parameters.

## Getoetste bestaande repositorybronnen

- `docs/02_theoretical_framework.md`: matched current/reference, respons onder dezelfde forcing, afzonderlijke transfer- en waarderingsstappen; occurrence en magnitude van runoff scheiden.
- `docs/49_project_effect_pathway_matrix_v0_1.md`: F1 heeft lokale/modelmatige bronrespons, F2 mist generieke delivery, F3 is vooral Tollebeek-pilot, F4 heeft uitsluitend benchmark voor schade, F5 mist overgang van potentiële behoefte naar feitelijke levering.
- `docs/50_evidence_ensemble_protocol_v0_1.md`: bronleden met verschillende context niet middelen; DIRECT_CANDIDATE/PROXY/BOUND/SCENARIO/BENCHMARK/GUARDRAIL en intended-use onderscheiden.
- `docs/07_evidence_and_qualification.md`: bron, evidence-item, claim en intended-use-qualification gescheiden.
- `docs/58_project_architecture_status_v0_1.md`: kleine watersysteemtypologie als eerstvolgende off-site-stap; Tollebeek is geen nationaal model.

**Reikwijdte van deze toets:** documentatie- en bewijsarchitectuur plus de in bovenstaande documenten vastgelegde samenvattingen. Geen heranalyse van oorspronkelijke meetreeksen of numerieke herberekening; daarmee kunnen we nog geen onafhankelijke kwantitatieve validatie claimen.

## Beoordeling per hydrologische schakel

| Schakel | Huidige onderbouwing in Git | Wat is verantwoord | Blokkade voor geldbedrag |
|---|---|---|---|
| S0: toestand/referentie | Diepte- en ernstafhankelijkheid expliciet; actuele landelijke exposure ontbreekt | Gedefinieerde matched scenario's | Representativiteit en actuele verdichtingsomvang |
| F1: bodem → runoff/drainage | Lokale empirische/modelvoorbeelden, contextafhankelijk | Conditionele bronrespons en gevoeligheidsgrenzen, mits bronmatch | Niet elke lokale respons is nationaal overdraagbaar |
| F2: bron → perceelsrand/netwerk | Causale route bekend, generieke delivery ontbreekt | Transfer als afzonderlijke te toetsen relatie | Connectiviteit, opslag, timing en ontvangend systeem |
| F3: netwerk → bemaling | Tollebeek architectuur en bounded checks | Pilottoetsing en expliciete scenario's | Feitelijke operationele gegevens en schaaloverdracht |
| F4: netwerk → overlast/schade | Defra/Graves uitsluitend benchmark | Mechanisme en relevante receptor vastleggen | Overschrijdingskans, blootstelling en schadefunctie |
| O3/F5: waterstress → regionale watervraag | Fysieke scenario's; levering onbekend | Potentiële vraag apart rapporteren | Gedrag, bron, beschikbaarheid, daadwerkelijke levering en schaarste |

**Voorlopig oordeel:** grootste methodische lacune bij wateroverlast ligt **niet** in de definitie van runoff maar in F2 en vervolgens F4; bij droogte ligt ze in de overgang O3 → feitelijke vraag/levering → F5. Dit is een oordeel over de keten, geen kwantitatieve rangorde van maatschappelijke schade.

## Kleine typologie voor toetsing, niet voor landelijke classificatie

| Voorlopig systeemtype | Kenmerkende vraag | Noodzakelijke toets |
|---|---|---|
| A. Peilbeheerst bemalen poldergebied | Wanneer wordt extra aangevoerd water daadwerkelijk extra verpompt of veroorzaakt het capaciteitsspanning? | Routing, berging, regeling, pompbelasting; Tollebeek als één pilot |
| B. Vrij afwaterend gebied | Verandert extra perceelsafvoer de benedenstroomse piek en blootstelling? | Reistijd, berging, synchronisatie van pieken, drempels |
| C. Gedraineerd landbouwgebied met watergangen | Hoe verschuift afvoer tussen drainage, oppervlakkige route en tijd? | Drainageconfiguratie, uitlaat, lokale retentie, ontvangend systeem |
| D. Wateraanvoergebied met beperkte beschikbaarheid | Leidt potentiële extra watervraag tot werkelijke aanvoer, onttrekking of onvervuld tekort? | Beregeningsgedrag, waterbeschikbaarheid, allocatieregels en kosten |

Dit zijn **onderzoekshypothesen voor een systeemtypologie**, geen bewezen uitputtende of onderling exclusieve Nederlandse gebiedsklassen. Een gebied kan meer dan één typekenmerk hebben.

## Beslisvolgorde 2026

1. **Kies eerst het te waarderen eindpunt:** extra bemalingsenergie, wateroverlastschade, daadwerkelijke extra aanvoer of onvervuld tekort. Niet al deze eindpunten zijn automatisch optelbaar.
2. **Identificeer per eindpunt de eerstvolgende ontbrekende causale schakel.** F2 voor regionale wateroverlast, vraag/levering voor F5.
3. **Selecteer per systeemtype maximaal één concrete toetscase** waarvoor actuele data en een matched bodemreferentie beschikbaar kunnen zijn; Tollebeek mag alleen zijn eigen klasse/pilot onderbouwen.
4. **Zoek eerst empirische gegevens en eenvoudige grenzen.** Gebruik SWAP of routingmodellen alleen als ze een voor de eindkosten bepalende onzekerheid aantoonbaar kunnen verkleinen.
5. **Leg een stopregel vast:** als bron- of transferattributie niet kan worden gekwalificeerd, rapporteer de fysieke indicatie en blokkade, niet een fictief eurobedrag.
6. **Rapporteer ook niet-monetair:** gewijzigde timing, pieken, waterstress en mogelijk ecologische gevolgen, inclusief onzekerheden.

## Concrete toetsvragen aan Ab en expertgroep

- Is het doel van de eerste waterpilot vooral bemalingskosten, wateroverlastschade of de vergelijkbaarheid van bronrespons tussen soilscapes?
- Welke bestaande gebieds- en operationele gegevens maken één F2-transferrelatie toetsbaar zonder een nationaal hydrologisch model?
- Welke beregeningsgegevens onderscheiden behoefte, aanvraag, daadwerkelijke levering en niet-geleverde vraag?
- Hoe voorkomen we dat dezelfde extra waterhoeveelheid via zowel extra pompen als overstromingsschade onterecht dubbel wordt gewaardeerd?
- Zijn de voorgestelde vier systeemtypen bruikbaar, of ontbreekt een belangrijk Nederlands watersysteemtype?

## Vervolg en toelatingsgrens

De volgende inhoudelijke stap is **bronspecifieke verificatie**: open de oorspronkelijke hydrologische studies, meetreeksen en pilotgegevens en vul per schakel het bestaande evidence-register met expliciete intended use. Dit document mag niet als zelfstandig bewijs voor numerieke factoren worden gebruikt. Na review kan de typologie worden vastgelegd in de bestaande pathway-/evidence-structuur; tot dan geen nieuwe canonieke datasets, coefficients of schemawijzigingen.
