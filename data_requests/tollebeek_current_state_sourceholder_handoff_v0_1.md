# Tollebeek OT.02 current-state source-holder handoff v0.1

Status: `READY_FOR_SOURCE_HOLDER_CONTACT`

Governing readiness item: `DR_SM_CURRENT_STATE`

This handoff operationalises the already qualified CURRENT-state acquisition route. It does **not** change readiness and does not imply that the requested records are public or shareable.

## 1. Target dataset

Please use all identifiers below together to avoid ambiguity:

- project: `Flevo - land in beweging`
- RAAK-PRO dossier: `RAAK.PRO02.021`
- WER project number: `5200043298`
- report: `Regionale kartering bodemverdichting in de provincie Flevoland`, WER Rapport 3382
- DOI: `10.18174/672577`
- field campaign: September 2020 through June 2021
- scientific target area: Tollebeek OT.02

The project needs source-native point records underlying the field campaign, not values digitised from a map or a regional interpolated product.

## 2. Primary request — Aeres Hogeschool / RAAK-PRO

Recipient route: Karin Pepers — `k.pepers@aeres.nl`.

Suggested subject:

`Verzoek ruwe meetdata bodemverdichting Flevoland 2020–2021 (RAAK.PRO02.021 / WER 3382)`

Suggested message:

> Beste Karin,
>
> Voor een reproduceerbare analyse van bodemverdichting en hydrologische effecten in peilgebied Tollebeek OT.02 zoek ik de brondata van de meetcampagne uit 2020–2021 die is gebruikt in WER Rapport 3382, *Regionale kartering bodemverdichting in de provincie Flevoland* (DOI 10.18174/672577; WER-project 5200043298) en samenhangt met het RAAK-PRO-project *Flevo - land in beweging* (RAAK.PRO02.021).
>
> Ik zoek bij voorkeur de source-native meettabel of een stabiele dataset-/repository-identificatie met de puntmetingen voor droge bulkdichtheid en, indien beschikbaar, de penetrologgergegevens en bijbehorende metadata/codebook.
>
> Belangrijk voor de analyse zijn met name stabiele locatie-/sample-ID's, coördinaten plus CRS, meetdatum, exacte diepte of diepte-interval, individuele ringmetingen of een traceerbare gemiddelde bulkdichtheid, meetmethode/ringvolume, QC-/statusvelden en — waar beschikbaar — vocht-, textuur- en penetratieweerstandsgegevens.
>
> De uiteindelijke selectie is alleen voor Tollebeek OT.02. Als exacte perceelscoördinaten vanwege privacy niet gedeeld kunnen worden, is een door de datahouder uitgevoerde reproduceerbare selectie op OT.02 met stabiele pseudonieme locatie-ID's en voldoende metadata om die selectie te auditen ook bruikbaar.
>
> Zou je kunnen aangeven of deze dataset bij Aeres wordt beheerd, en zo ja onder welke dataset-/versie-identificatie? Als een andere partij de formele datahouder is, hoor ik graag wie daarvoor het juiste aanspreekpunt is.
>
> Alvast veel dank.

## 3. Parallel request — Wageningen Environmental Research / WER3382

Recipient route: Fenny van Egmond through the current public WUR profile/contact route. Do not invent an email address if the profile route changes.

Suggested subject:

`Brondata bij WER Rapport 3382 – Flevoland bodemverdichting 2020–2021`

Suggested message:

> Beste Fenny,
>
> Voor een reproduceerbare Tollebeek OT.02-analyse werk ik met WER Rapport 3382, *Regionale kartering bodemverdichting in de provincie Flevoland* (DOI 10.18174/672577; projectnummer 5200043298).
>
> Ik probeer de source-native velddata van de meetcampagne uit september 2020–juni 2021 te achterhalen: met name de puntmetingen van droge bulkdichtheid en, indien beschikbaar, de penetrologgerreeksen en bijbehorende metadata/codebook.
>
> Is hiervoor binnen WUR/WER een canonieke dataset-, archive- of repository-identificatie beschikbaar? Zo niet, is een shareable export van de bronrecords mogelijk, inclusief stabiele locatie-/sample-ID's, coördinaten/CRS, meetdatum, diepte-interval, ringmetingen of traceerbare gemiddelden, methode/ringvolume en QC-/statusvelden?
>
> De toepassing is beperkt tot peilgebied Tollebeek OT.02. Als exacte coördinaten vanwege privacy niet kunnen worden gedeeld, kan de selectie eventueel door de datahouder zelf worden uitgevoerd tegen de OT.02-polygon, waarna pseudonieme locatie-ID's plus voldoende selectie-/provenancemetadata volstaan.
>
> Ik wil de data uitsluitend gebruiken met expliciete bron-, datum-, diepte- en QC-semantiek; een regionale kaart of afgeleide interpolatie is voor deze stap niet voldoende.
>
> Kun je aangeven waar de brondata worden beheerd of wie hiervoor de juiste datahouder is?
>
> Alvast veel dank.

## 4. Referral request — Actieplan Bodem & Water Flevoland

Recipient: `info@bodemenwaterflevoland.nl`.

Suggested subject:

`Datahouder gezocht voor meetdata Flevo - land in beweging / WER Rapport 3382`

Suggested message:

> Goedemiddag,
>
> Voor een reproduceerbare analyse van bodemverdichting in Tollebeek OT.02 zoek ik de brondata van de Flevolandse meetcampagne uit 2020–2021 die samenhangt met *Flevo - land in beweging* (RAAK.PRO02.021) en is gebruikt in WER Rapport 3382 (DOI 10.18174/672577; WER-project 5200043298).
>
> Via de publieke project- en rapportpagina's heb ik geen downloadbare brondata of dataset-ID kunnen vinden. Kunnen jullie aangeven welke organisatie of persoon de definitieve meetdataset beheert, of waar de projectresultaten/data zijn gearchiveerd?
>
> Het gaat specifiek om de source-native puntmetingen van onder meer droge bulkdichtheid en penetratieweerstand plus metadata, niet om een regionale kaart.
>
> Alvast bedankt voor het doorverwijzen naar de juiste datahouder.

## 5. Minimum requested content

Where available, request and retain:

- stable site/location ID;
- stable sample/replicate ID;
- coordinates and CRS;
- sampling/measurement date;
- fixed versus variable sampling-depth indicator;
- exact depth or depth interval;
- individual dry-bulk-density ring measurements and/or traceable mean;
- ring volume and ISO/method metadata;
- penetration-resistance depth series or source-native summaries;
- soil moisture/context associated with penetration measurements;
- sample/field QC and failure/status flags;
- texture/lutum/context fields used in interpretation, if shareable;
- data dictionary/codebook;
- dataset/archive/version identifier;
- data-use or privacy restrictions.

Farmer names, addresses or other personal identifiers are not required.

## 6. Privacy-preserving OT.02 fallback

If exact coordinates cannot be released:

1. provide the canonical OT.02 polygon to the holder in EPSG:28992;
2. ask the holder to intersect the source-native points internally;
3. request only records inside OT.02;
4. replace private coordinates, where necessary, with stable pseudonymous location IDs;
5. retain the holder-side selection method, polygon identifier/version, CRS, number of selected source records and any exclusion rules;
6. do not reconstruct private point locations from figures or descriptive text.

Canonical project geometry:

`data/spatial/tollebeek_ot02_current.geojson`

## 7. Receipt protocol

When a response/file is received:

1. save the original attachment/export bytes unchanged before opening or transforming them;
2. record sender/source-holder, received date, filename, dataset/version identifier and any accompanying message/terms;
3. calculate SHA-256 for every raw file;
4. preserve archive structure if ZIP or similar is supplied;
5. do not overwrite source-native missing values;
6. do not convert blanks, sentinels or unavailable fields to zero;
7. create normalized derivatives separately from raw files;
8. retain a mapping from source-native field names/IDs to canonical project fields;
9. record any privacy/generalisation applied by the holder;
10. perform OT.02 intersection only after CRS/coordinate semantics have been verified.

## 8. Acceptance sequence after receipt

Receipt is `ACQUIRED`, not `ADMITTED`.

Required later review:

`IDENTIFY → HASH → SCHEMA/QC → SPATIAL VERIFY → TEMPORAL CLASSIFY → STATE MAPPING → QUALIFY → ADMIT/CLOSE`

Specific checks:

- exact dataset/source identity;
- source-native IDs and version;
- coordinate/CRS validity or auditable holder-side spatial selection;
- reproducible OT.02 membership;
- measurement date/depth semantics;
- ring replicate and QC semantics;
- direct measurement versus derived indicators;
- sparse-point representativeness limits;
- no point-count-derived area weighting;
- explicit 2020–2021 temporal classification;
- no silent transfer to October 1998 or 2026;
- no undocumented bulk-density-to-hydraulic transformation.

## 9. Current scientific boundary

Until source-native records or a stable archive/dataset identifier are actually received:

- `DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`;
- the project has no admitted Tollebeek CURRENT compaction state;
- SoilPhys modal density remains profile context only;
- BIS-4D and DOI/public-registry recovery routes remain reviewed negative alternatives;
- no model run is authorised from this handoff.