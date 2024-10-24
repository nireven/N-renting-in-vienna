![Scraping Pipeline](https://github.com/AthomsG/renting-in-vienna/actions/workflows/run_pipeline.yml/badge.svg)


# Renting in Vienna

This repo fetches every **5 minutes** (Actually it's less than 30 minutes because github is a bit unreliable with the cron functionality) the latest apartments from [willhaben](https://www.willhaben.at/).
It then filters the listings according to my preferences and stores them in `check_these.csv` - You can change filter settings in the `filter_dataset.py` script.

The 20 latest listings according to my preferences are printed in this README for you conviniece! Press the link to see the listing post.
The table is sorted by publish times in ascending order, with the closest publish time to the current time listed first.

## Recent Listings
|   Rent (€) |   Size (m²) |   Rooms | District        | Link                                                                                                                                                                                              |
|-----------:|------------:|--------:|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     740.01 |          73 |       2 | 05. Margareten  | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/großzügige-2-zimmer-wohnung-in-gepflegtem-haus-beim-hauptbahnhof-1025067408/)                            |
|     790    |          56 |       3 | 16. Ottakring   | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/erstbezug-in-heller-sanierter-altbauwohnung-782617572/)                                                   |
|     749    |          41 |       2 | 22. Donaustadt  | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---helle-gepfegte-neubauwohnung-im-4ten-liftstock---sofortbezug-1857182406/)      |
|     760    |          55 |       2 | 05. Margareten  | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zimmerwohnung*-privat-1366897509/)                                                                     |
|     650    |          36 |       2 | 22. Donaustadt  | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/helle-2-zimmer-mietwohnung-mit-loggia-nähe-u1-kagraner-platz-2044095270/)                                |
|     478.7  |          45 |       2 | 12. Meidling    | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe-1900649810/)                                                                 |
|     505    |          53 |       2 | 19. Döbling     | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-döbling/gemeindewohung-direktvergabe-mit-ablöse-1374904983/)                                                        |
|     530    |          50 |       2 | 21. Floridsdorf | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-direktvergabe-wohnticket:-31.8.2024!!-1285229637/)                                      |
|     789.9  |          39 |       2 | 10. Favoriten   | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zi.-whg.-mit-terrasse-1490322788/)                                                                |
|     799    |          40 |       2 | 21. Floridsdorf | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung-mit-balkon!-1693093114/)                                                        |
|     640    |          58 |       2 | 12. Meidling    | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeinde-wohnung-1120-wien-mit-vormekschein-bis-01.07.2024-842069402/)                                     |
|     770    |          49 |       2 | 21. Floridsdorf | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-später-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                            |
|     720    |          44 |       2 | 21. Floridsdorf | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genießen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)               |
|     730    |          37 |       2 | 21. Floridsdorf | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhaftes-wohnen:-mietwohnungen-mit-kaufoption-in-stammersdorfer-ruhelage-761411354/)                 |
|     798.99 |          40 |       2 | 21. Floridsdorf | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-neubauwohnung-mit-balkon-und-einbauküche!-nahe-straßenbahn-26-lorettowiese-und-scn-1740472691/) |
|     798.99 |          40 |       2 | 21. Floridsdorf | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumwohnungen-in-top-lage-zu-vermieten!-1055837955/)                                                   |
|     749    |          38 |       2 | 10. Favoriten   | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon!-1929020483/)                                                                 |
|     685.08 |          52 |       2 | 23. Liesing     | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/zwei-zimmer-wohnung-hofseitig-inzersdorf-1230-wien-742385399/)                                              |
|     752.84 |          44 |       2 | 12. Meidling    | [Link](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neuwertige-wohlfühloase-mit-gartenanteil---43.5m²-für-nur-75284-eur-miete-in-1120-wien!-1634330371/)       |
