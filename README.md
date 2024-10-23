![Scraping Pipeline](https://github.com/AthomsG/renting-in-vienna/actions/workflows/run_pipeline.yml/badge.svg)


# Renting in Vienna

This repo fetches every **5 minutes** the latest apartments from [willhaben](https://www.willhaben.at/).
It then filters the listings according to my preferences and stores them in `check_these.csv`. 

You can change filter settings in the `filter_dataset.py` script.

## Recent Listings
|   Rent (€) |   Size (m²) |   Rooms | Location                      | Link                                                                                                                                                                                           |
|-----------:|------------:|--------:|:------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     650    |          58 |       2 | Wien, 14. Bezirk, Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-ruhige-2-zimmer-wohnung-mit-blick-ins-grüne-1691838531/)                                              |
|     650    |          36 |       2 | Wien, 22. Bezirk, Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/helle-2-zimmer-mietwohnung-mit-loggia-nähe-u1-kagraner-platz-2044095270/)                                |
|     478.7  |          45 |       2 | Wien, 12. Bezirk, Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe-1900649810/)                                                                 |
|     695.12 |          55 |       2 | Wien, 14. Bezirk, Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/erstbezug-nach-generalsanierung-helle-2-zimmer-altbau-wohnung-unbefristet-1328035751/)                      |
|     630.4  |          42 |       2 | Wien, 23. Bezirk, Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/unbefristete-ruhige-wohnung-mit-südostloggia-1375678827/)                                                   |
|     505    |          53 |       2 | Wien, 19. Bezirk, Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-döbling/gemeindewohung-direktvergabe-mit-ablöse-1374904983/)                                                        |
|     530    |          50 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-direktvergabe-wohnticket:-31.8.2024!!-1285229637/)                                      |
|     789.9  |          39 |       2 | Wien, 10. Bezirk, Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zi.-whg.-mit-terrasse-1490322788/)                                                                |
|     799    |          40 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung-mit-balkon!-1693093114/)                                                        |
|     640    |          58 |       2 | Wien, 12. Bezirk, Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeinde-wohnung-1120-wien-mit-vormekschein-bis-01.07.2024-842069402/)                                     |
|     770    |          49 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-später-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                            |
|     720    |          44 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genießen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)               |
|     730    |          37 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhaftes-wohnen:-mietwohnungen-mit-kaufoption-in-stammersdorfer-ruhelage-761411354/)                 |
|     798.99 |          40 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-neubauwohnung-mit-balkon-und-einbauküche!-nahe-straßenbahn-26-lorettowiese-und-scn-1740472691/) |
|     798.99 |          40 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumwohnungen-in-top-lage-zu-vermieten!-1055837955/)                                                   |
|     749    |          38 |       2 | Wien, 10. Bezirk, Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon!-1929020483/)                                                                 |
|     685.08 |          52 |       2 | Wien, 23. Bezirk, Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/zwei-zimmer-wohnung-hofseitig-inzersdorf-1230-wien-742385399/)                                              |
|     752.84 |          44 |       2 | Wien, 12. Bezirk, Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neuwertige-wohlfühloase-mit-gartenanteil---43.5m²-für-nur-75284-eur-miete-in-1120-wien!-1634330371/)       |
|     792    |          50 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnung-ab-oktober-2024-zu-vermieten-1727828166/)                                                       |
|     685.01 |          43 |       2 | Wien, 10. Bezirk, Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleinod--erstbezug-in-hauptbahnhof-nähe-1577186673/)                                                      |
