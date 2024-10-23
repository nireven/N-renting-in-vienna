![Scraping Pipeline](https://github.com/AthomsG/renting-in-vienna/actions/workflows/run_pipeline.yml/badge.svg)


# Renting in Vienna

This repo fetches every two hours the latest listings from [willhaben](https://www.willhaben.at/).
It then filters the listings down according to my preferences and stores these listings in `check_these.csv`. 

You can change filter in the `filter_dataset.py` script.

## Recent Listings
|   Rent (€) |   Size (m²) |   Rooms | Location                               | Link                                                                                                                                                                                               |
|-----------:|------------:|--------:|:---------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     792    |          50 |       2 | Wien, 21. Bezirk, Floridsdorf          | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnung-ab-oktober-2024-zu-vermieten-1727828166/                                                                |
|     685.01 |          43 |       2 | Wien, 10. Bezirk, Favoriten            | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleinod--erstbezug-in-hauptbahnhof-nähe-1577186673/                                                               |
|     695    |          43 |       2 | Wien, 10. Bezirk, Favoriten            | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmer-erstbezug-in-hauptbahnhof-nähe-824306479/                                                              |
|     787.92 |          41 |       2 | Wien, 22. Bezirk, Donaustadt           | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m²-zum-mietpreis-von-78792-eur!-1580236359/                        |
|     782.71 |          51 |       2 | Wien, 21. Bezirk, Floridsdorf          | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/attraktive-wohnung-mit-loggia-nahe-floridsdorfer-wasserpark-1099198210/                                         |
|     730    |          48 |       2 | Wien, 10. Bezirk, Favoriten            | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-zwei-zimmer-wohnung-mit-großer-terrasse-und-garage-2098097818/                                              |
|     527    |          35 |       2 | Wien, 16. Bezirk, Ottakring            | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wohnung-1160-35kv-1479636601/                                                                                     |
|     650.11 |          44 |       2 | Wien, 05. Bezirk, Margareten           | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sonnige-15-zimmer-wohnung-nähe-siebenbrunnenplatz-2033714399/                                                    |
|     699    |          41 |       2 | Wien, 14. Bezirk, Penzing              | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/tolle-2-zimmer-wohnung-im-herzen-von-breitensee!-ab-dem-01.02.2025-verfügbar-2146732696/                            |
|     749    |          30 |       2 | Wien, 22. Bezirk, Donaustadt           | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/möbliertes-studio-apartment-mit-terrasse---hochwertige-ausstattung---nahe-u1-782519959/                          |
|     798    |          42 |       2 | Wien, 21. Bezirk, Floridsdorf          | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/schöne-2-zimmerwohnung-mit-loggia-zu-vermieten-1744568207/                                                      |
|     510    |          52 |       2 | Wien, 13. Bezirk, Hietzing             | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/52m2-gemeindewohnung-direktvergabe-1764120561/                                                                     |
|     741.37 |          57 |       2 | Wien, 11. Bezirk, Simmering            | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/u3-enkplatz---2-zimmer-altbau-unbefristet-1249098665/                                                             |
|     699    |          41 |       2 | Wien, 22. Bezirk, Donaustadt           | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220---wien---u1-nähe-donauzentrum---gepflegte-singlewohnung-mit-kleinen-garten---ab-1.12.2024-1975223161/       |
|     795    |          51 |       2 | Wien, 15. Bezirk, Rudolfsheim-Fünfhaus | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-fünfhaus/wunderschöne-2-zimmer-wohnung-mit-terrasse-1939918169/                                                 |
|     798.88 |          41 |       2 | Wien, 10. Bezirk, Favoriten            | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend-living!-inklusive-küche!-erstbezug!-elektrische-raffstores!-klima-vorb.!-nähe-u1.---wohntraum-774645004/ |
|     790    |          43 |       2 | Wien, 23. Bezirk, Liesing              | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/dg-traum!-klimatisierter-2-zimmer-neubau-mit-freifläche-und-luftwärmepumpe-838423492/                               |
|     473.09 |          64 |       3 | Wien, 10. Bezirk, Favoriten            | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug!-/-vormerkschein-bis-30.09.2024-1551815967/                    |
|     799    |          63 |       2 | Wien, 23. Bezirk, Liesing              | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/mauer---sonnige-balkon-2-zi.-wohnung-1569994193/                                                                    |
|     750    |          43 |       2 | Wien, 07. Bezirk, Neubau               | https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/hell-und-ruhige-43-m²-wohnung-1123523943/                                                                            |
