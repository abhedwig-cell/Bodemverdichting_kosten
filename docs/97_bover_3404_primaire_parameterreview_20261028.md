# BoVer rapport 3404: primaire tabelcontrole en SWAP-toepassing

**28 oktober 2026 | SOURCE_CHECKED / CANDIDATE_PARAMETERS_ONLY**

Gebaseerd op het door de gebruiker aangeleverde volledige primaire rapport: Bakema, Bakker, Heinen, Van Egmond en Van den Elsen (2024), *De invloed van bodemverdichting op de plantontwikkeling*, WENR-rapport 3404, DOI 10.18174/675719, vooral **appendix 1, 2, 3 en 5**. Dit document vervangt de onvolledige inhoudelijke bespreking in [broncontrole 96](96_bover_bakema_rapporten_broncontrole_v0_1.md); het verandert niet automatisch het bestaande admitted evidence-register.

## 1. Proefopzet, monsterherkomst en referentie

Appendix 1, rapport p. 33–45: de gebruikte grond was een gemengde/gezeefde bovengrond (Bornsesteeg Wageningen): matig humeus, zwak lemig matig fijn zand, gloeiverlies 2,9%. Vier behandelingstrappen, elk met 100/200/300/400 kPa compressiedruk, monsters bij circa 10–11% massawatergehalte. Er zijn verschillende ringtypen gebruikt. De kleine ringen voor de aanvullende natte-retentiemetingen hadden bij dezelfde behandeling 2,1–4,4% lagere dichtheden dan de grotere ringen voor de verdampingsmethode (appendix 3 p. 73).

De kolomproef (appendix 2, p. 48–50) bevatte een **10 cm verdichte laag op 30–40 cm** met niet-verdichte boven- en onderlagen; beworteling onder geforceerde uitdroging in de bovengrond. S0 was de beoogde referentie op 1350 kg/m³.

**Belangrijk:** appendix 3 p. 75 meldt dat S0 maar eenmaal is bepaald en anders kan zijn voorbereid; S0 wordt door de auteurs niet meegenomen in de verdere regressies voor dichtheidsafhankelijkheid. Dit is dus geen gekwalificeerde nationale REFERENCE-toestand.

## 2. Gemeten en gefitte parameters uit appendix 3

De tabellen hieronder geven **gerapporteerde gemiddelden**, niet nieuwe fits. `theta_r` en `theta_s` in m³/m³, `alpha` in cm⁻¹, `n` en `lambda` dimensieloos, `Ks_fit` in cm/dag. Bulk density voor S1–S4 uit appendix 3, tabel 3 p. 75, n=3. Parameterwaarden komen uit tabellen 4 en 5 op p. 75–76.

### Casus 0: standaardprocedure, inclusief zandbakmetingen

| Behandeling | rho_d kg/m³ | theta_r | theta_s | alpha cm⁻¹ | n | lambda | Ks_fit cm/d |
|---|---:|---:|---:|---:|---:|---:|---:|
| S0 | 1350* | 0.009970 | 0.486610 | 0.016480 | 1.522540 | 5.971230 | 150.062 |
| S1 | 1416 | 0.020954 | 0.444696 | 0.037124 | 1.491509 | 3.326122 | 360.9493 |
| S2 | 1507 | 0.025916 | 0.442840 | 0.027019 | 1.567971 | 2.273573 | 74.96801 |
| S3 | 1535 | 0.018188 | 0.415402 | 0.020156 | 1.590952 | 2.505652 | 30.46626 |
| S4 | 1573 | 0.016298 | 0.384050 | 0.016421 | 1.592376 | 3.326196 | 25.05535 |

*S0 circa 1350 kg/m³ in kolomreferentie; de gerapporteerde hydrologische S0-fit is een enkelvoudige, afwijkend voorbehandelde verkenning. Niet als volledig vergelijkbaar datapunt in de dichtheidsfit gebruiken.*

### Casus 1: zonder zandbakmetingen

| Behandeling | theta_r | theta_s | alpha cm⁻¹ | n | lambda | Ks_fit cm/d |
|---|---:|---:|---:|---:|---:|---:|
| S0 | 0.009970 | 0.486610 | 0.016480 | 1.522540 | 5.971230 | 150.062 |
| S1 | 0.024547 | 0.396667 | 0.026398 | 1.582949 | 4.644329 | 293.1506 |
| S2 | 0.019768 | 0.377333 | 0.021667 | 1.490038 | 3.785440 | 68.21504 |
| S3 | 0.021403 | 0.357333 | 0.017010 | 1.535784 | 3.807897 | 27.95798 |
| S4 | 0.012330 | 0.346000 | 0.015762 | 1.445845 | 4.119167 | 22.95615 |

### Wetenschappelijke interpretatie

- Verzadigd watergehalte/porositeit en gefitte Ks nemen in de S1–S4-reeks duidelijk af, met sterke niet-lineaire respons voor Ks. S1→S4 in casus 0: ongeveer factor 14,4 verschil in Ks, **binnen één specifieke bewerkte laboratoriumgrond**, niet als nationale factor.
- `n` verandert van trend tussen casus 0 en casus 1; `lambda` varieert niet monotoon. `theta_r` volgt niet zonder meer de theoretisch verwachte respons. Er is dus geen betrouwbare universele schaalfunctie voor alle MVG-parameters.
- De oorspronkelijke auteurs verklaren dat de proef relatief klein bereik aan relatieve bulkdichtheid onderzocht (verhoudingen circa 1,02–1,11) en adviseren herhaling voor andere bodemsoorten en een groter bereik (appendix 3 p. 77–80).
- Het gestructureerd mengen en opnieuw verdichten elimineert oorspronkelijke bioporiën en anisotropie. Extrapolatie naar jarenlang verdichte ondergronden is niet automatisch geldig.

## 3. SWAP-WOFOST is al toegepast: appendix 5, p. 108–118

Auteurs: Marius Heinen en Martin Mulder. De kolomkasproef is nagerekend met gemeten hydraulische eigenschappen uit appendix 3. Bodemverdamping werd uitgezet; transpiratievraag is in tijdstappen opgelegd. Er is **geen dynamische gewasgroei** gesimuleerd; wortelverdeling werd dag voor dag opgelegd op basis van gemeten eindverdeling en aannames over de ontwikkeling in de tijd.

- Opnameconcepten: Feddes zonder compensatie (Fe_0), Feddes met compensatie (Fe_1), procesgericht de Willigen/Van Noordwijk (dW).
- Drukhoogte net boven en watergehalte onder de laag vertonen redelijk overeenkomstige patronen met metingen (p. 112, 118), maar actuele transpiratie is niet voldoende onafhankelijk geobserveerd om één concept te kwalificeren.
- `dW` reageerde zeer sterk op de MVG-`lambda` van het niet-verdichte profiel (van circa 6 naar 3); simulaties konden grote verschillende absolute wateropnamerespons tonen.
- De modelberekeningen gaven bij verschillende verdichtingsbehandelingen **ongeveer gelijke reductie in wateropname**, terwijl bovengrondse droge biomassa wel afnam met toenemende behandeling. De totale (wortel + scheut) biomassa veranderde niet significant; verdichting verschoof assimilaten naar wortels (p. 110–111, 118).
- Opwaartse flux door de verdichte laag naar boven was in de simulatie verwaarloosbaar, in gewijzigde dW-`lambda=3` variant minder dan 0,03 mm/dag, bij een opgelegde watervraag van circa 2 mm/dag (p. 114). Geen algemene claim over capillaire opstijging in het veld.
- Gesimuleerde watertoevoer via grof zand onder de kolom circa 0,45 mm/dag, voor alle behandelingen vergelijkbaar en bepaald door de onderrand (p. 113).

**Beperking:** proefonderrand was soms minder stabiel dan beoogd, wortelontwikkeling in de tijd was niet rechtstreeks gemeten, wortels konden langs kolomwand en in grofzand terechtkomen; bodemfysische eigenschappen werden in aparte monsters bepaald en wortelinvloed op hydrauliek was niet meegenomen.

## 4. On-site effecten: appendix 2

De gemeten bovengrondse scheutdrogestof nam in de vijf behandelingen af: S0 18,758 g, S1 16,278 g, S2 15,580 g, S3 13,310 g, S4 11,613 g (appendix 2 p. 62, tabel 12). In appendix 2 p. 53 zijn S3/S4 significant lager dan S0 volgens ANOVA. De proef was **jong mais, ongeveer zes weken, onder geforceerde droogte**. Dit is geen jaarlijkse oogstopbrengstderving; de rapporttekst noemt reducties tot circa 30% in vroege groei onder experimenteel zeer droge condities.

Wortellengtedichtheid in verdichte laag daalde, wortels werden dikker en verhouding wortel:scheut nam toe. Deze mechanistische routes zijn niet door alleen SWAP-transpiratiestress gereproduceerd.

## 5. Wat kunnen we nu werkelijk met SWAP?

**Wel:** een reproduceerbare *diagnostische* H-proef voor dit ene zand, met S1–S4-casus0-profielen (of gevoeligheidsvergelijking casus0/casus1) en expliciete vastlegging van de gekozen referentie, alle parameters en hun herkomst. Ook vergelijking van volledige theta(h)/K(h) curves en parametergevoeligheid mogelijk.

**Nog niet:** zomaar het profiel S0 als bewezen niet-verdichte natuurlijke referentie toelaten; gemengde bovengrond gebruiken als universele ondergrondrelatie; H-resultaten omzetten in nationale runoff- of opbrengstschadefactoren; wortelontwikkeling voorspellen zonder aanvullende procesrelaties.

**Concreet:** bij een eerste modelproef zijn S1–S4 uit casus 0 te gebruiken als **CANDIDATE_DIAGNOSTIC_PARAMETERS**, niet als CURRENT/REFERENCE voor een Nederlandse locatie. Een gecontroleerde ondergrondprofielsimulatie blijft data-gated waar laagdiepte, textuur en waterbeheer niet zijn toegelaten.

## 6. Relevantie voor v0.7

Sterk bewijs voor het mechanisme V01–V05 / V09; concrete beperkte gegevens voor V11, V17, V21 via waterbalans. V03/V06–V07 krijgen bovendien wortel- en vroege biomassa-effecten, met de beperking dat finale opbrengst niet is gemeten. V42 blijft een meerjarige terugkoppeling, geen in deze proef bepaalde herstelparameter.

**Wetenschappelijke status:** SOURCE_CHECKED_LOCAL_EXPERIMENT / PARAMETERS_FOR_DIAGNOSTIC_ONLY. Geen ADMITTED_FOR_NATIONAL_CALCULATION. De bestaande canonical `evidence/*.csv` en het causale netwerk v0.7 blijven intact.
