![Scraping Pipeline](https://github.com/AthomsG/renting-in-vienna/actions/workflows/run_pipeline.yml/badge.svg)


# Renting in Vienna

This repo fetches every two hours the latest listings from [willhaben](https://www.willhaben.at/).
It then filters the listings down according to my preferences and stores these listings in `check_these.csv`. 

You can change filter in the `filter_dataset.py` script.

## Recent Listings
|   Rent (€) |   Size (m²) |   Rooms | Location                      | Link                                                                                                                                                                                           |
|-----------:|------------:|--------:|:------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     770    |          49 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-später-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                            |
|     720    |          44 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genießen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)               |
|     730    |          37 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhaftes-wohnen:-mietwohnungen-mit-kaufoption-in-stammersdorfer-ruhelage-761411354/)                 |
|     798.99 |          40 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-neubauwohnung-mit-balkon-und-einbauküche!-nahe-straßenbahn-26-lorettowiese-und-scn-1740472691/) |
|     798.99 |          40 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumwohnungen-in-top-lage-zu-vermieten!-1055837955/)                                                   |
|     749    |          38 |       2 | Wien, 10. Bezirk, Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon!-1929020483/)                                                                 |
|     685.08 |          52 |       2 | Wien, 23. Bezirk, Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/zwei-zimmer-wohnung-hofseitig-inzersdorf-1230-wien-742385399/)                                              |
|     586.06 |          42 |       2 | Wien, 10. Bezirk, Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/günstge-dzt.-noch-voll-angerümpelte-neubauwohnung-1536482145/)                                            |
|     752.84 |          44 |       2 | Wien, 12. Bezirk, Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neuwertige-wohlfühloase-mit-gartenanteil---43.5m²-für-nur-75284-eur-miete-in-1120-wien!-1634330371/)       |
|     792    |          50 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnung-ab-oktober-2024-zu-vermieten-1727828166/)                                                       |
|     685.01 |          43 |       2 | Wien, 10. Bezirk, Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleinod--erstbezug-in-hauptbahnhof-nähe-1577186673/)                                                      |
|     695    |          43 |       2 | Wien, 10. Bezirk, Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmer-erstbezug-in-hauptbahnhof-nähe-824306479/)                                                     |
|     787.92 |          41 |       2 | Wien, 22. Bezirk, Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m²-zum-mietpreis-von-78792-eur!-1580236359/)               |
|     782.71 |          51 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/attraktive-wohnung-mit-loggia-nahe-floridsdorfer-wasserpark-1099198210/)                                |
|     730    |          48 |       2 | Wien, 10. Bezirk, Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-zwei-zimmer-wohnung-mit-großer-terrasse-und-garage-2098097818/)                                     |
|     527    |          35 |       2 | Wien, 16. Bezirk, Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wohnung-1160-35kv-1479636601/)                                                                            |
|     650.11 |          44 |       2 | Wien, 05. Bezirk, Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sonnige-15-zimmer-wohnung-nähe-siebenbrunnenplatz-2033714399/)                                           |
|     699    |          41 |       2 | Wien, 14. Bezirk, Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/tolle-2-zimmer-wohnung-im-herzen-von-breitensee!-ab-dem-01.02.2025-verfügbar-2146732696/)                   |
|     749    |          30 |       2 | Wien, 22. Bezirk, Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/möbliertes-studio-apartment-mit-terrasse---hochwertige-ausstattung---nahe-u1-782519959/)                 |
|     798    |          42 |       2 | Wien, 21. Bezirk, Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/schöne-2-zimmerwohnung-mit-loggia-zu-vermieten-1744568207/)                                             |
