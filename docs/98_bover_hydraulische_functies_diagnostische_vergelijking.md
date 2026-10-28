# BoVer 3404: reproduceerbare diagnostische Mualem–Van Genuchten-analyse

**28 oktober 2026 | DIAGNOSTIC_ONLY | geen uitgevoerde SWAP-berekening of parameter-admission**

Primaire bron: Bakema et al. (2024), WENR 3404, appendix 3, tabellen 3–5 (gedrukte rapportpagina's 75–76), appendix 5 voor modelcontext. Zie [broncontrole 97](97_bover_3404_primaire_parameterreview_20261028.md).

## Werkwijze

Voor S1–S4 zijn **casus 0** en **casus 1** doorgerekend met de in de publicatie gegeven `theta_r, theta_s, alpha, n, lambda, Ks_fit`. Alle waarden blijven bron-specifieke fits voor gehomogeniseerde fijne zandgrond. S0 is uitgesloten van vergelijking: afwijkend voorbereid en enkelvoudig bepaald.

Voor de diagnostische curven (geen nieuwe metingen) is de standaard MVG-formulering gebruikt: `m = 1 - 1/n`, `Se = (1+(alpha*|h|)^n)^(-m)`, `theta = theta_r+(theta_s-theta_r)*Se`, `K = Ks*Se^lambda * [1-(1-Se^(1/m))^m]^2`. Drukhoogte `|h|` in cm, `K` in cm/dag. De analyse bevat h = 0, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000 en 100000 cm.

## Brongegevens casus 0

| S | rho kg/m3 | theta_r | theta_s | alpha 1/cm | n | lambda | Ks cm/d |
|---|---:|---:|---:|---:|---:|---:|---:|
| S1 | 1416 | .020954 | .444696 | .037124 | 1.491509 | 3.326122 | 360.9493 |
| S2 | 1507 | .025916 | .442840 | .027019 | 1.567971 | 2.273573 | 74.96801 |
| S3 | 1535 | .018188 | .415402 | .020156 | 1.590952 | 2.505652 | 30.46626 |
| S4 | 1573 | .016298 | .384050 | .016421 | 1.592376 | 3.326196 | 25.05535 |

## Belangrijk resultaat

`Ks(S1)/Ks(S4) ≈ 14,4` bij een dichtheidstoename van 1416 naar 1573 kg/m3 in deze ene proefgrond. Maar bij `|h|=100 cm` geeft de volledige curve van casus 0 **K(S1) ≈ 0,0665 cm/d, K(S2) ≈ 0,0793, K(S3) ≈ 0,0828 en K(S4) ≈ 0,1002 cm/d**. De *onverzadigde* volgorde keert hier dus om, door de gezamenlijk veranderende parameters. Dit is een berekend modelverschijnsel op basis van gefitte curves, geen direct gemeten bewijs van een verdichtingsbaat. Ter controle is het verschil tussen casus 0 en 1 op dezelfde drukhoogten vastgelegd.

## Reproduceerbaarheid

Een zelfstandig diagnostisch pakket is in deze sessie geproduceerd met `parameters.csv`, `vg_curves.csv`, `fit_comparison.csv`, `build.py` en een README. Het pakket kan na bewuste review aan de repository worden toegevoegd. De tabellen in deze tekst komen rechtstreeks uit rapport 3404 en de curvewaarden zijn berekend met de weergegeven formules. Totale dataset: 8 parametersets, 88 curvepunten, 12 geselecteerde casusvergelijkingen.

## Wetenschappelijke begrenzing

- Bevat geen gekwalificeerde minder verdichte **current/reference**-paar voor een echt Nederlands perceel; S0 mag niet als automatisch toepasbare referentie worden gekozen.
- De `lambda`-parameter is potentieel onzeker; appendix 5 van BoVer laat grote gevolgen voor het procesgebaseerde wortelwateropnamemodel zien.
- Geen rekening met oorspronkelijke macroporiën, anisotropie of bodemstructuur; de grond was gehomogeniseerd.
- Geen SWAP-run en geen modeluitvoer van runoff/drainage/percolatie in dit document.
- Geen landelijk schadepercentage, emissiefactor of gewasopbrengstderving afgeleid.

**Vervolg:** expliciete modelconfiguratie, onafhankelijke referentiestaat en vergelijking met oorspronkelijke SWAP-WOFOST-kolomconfiguratie uit BoVer appendix 5. Pas daarna een klein diagnostisch hydraulisch experiment, en de uitkomst toetsen op waterbalans en gevoeligheid voor lambda.
