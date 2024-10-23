![Scraping Pipeline](https://github.com/AthomsG/renting-in-vienna/actions/workflows/run_pipeline.yml/badge.svg)


# Renting in Vienna

This repo fetches every two hours the latest listings from [willhaben](https://www.willhaben.at/).
It then filters the listings down according to my preferences and stores these listings in `check_these.csv`. 

You can change filter in the `filter_dataset.py` script.

## Recent Listings
|   Rent (€) |   Size (m²) | Published Date            |   Rooms | Location                               | Link                                                         |
|-----------:|------------:|:--------------------------|--------:|:---------------------------------------|:-------------------------------------------------------------|
|     792    |          50 | 2024-10-22 23:02:00+00:00 |       2 | Wien, 21. Bezirk, Floridsdorf          | [link](https://www.willhaben.at/iad/immobilien/d/1727828166) |
|     685.01 |          43 | 2024-10-22 20:33:00+00:00 |       2 | Wien, 10. Bezirk, Favoriten            | [link](https://www.willhaben.at/iad/immobilien/d/1577186673) |
|     695    |          43 | 2024-10-22 19:35:00+00:00 |       2 | Wien, 10. Bezirk, Favoriten            | [link](https://www.willhaben.at/iad/immobilien/d/824306479)  |
|     787.92 |          41 | 2024-10-22 18:35:00+00:00 |       2 | Wien, 22. Bezirk, Donaustadt           | [link](https://www.willhaben.at/iad/immobilien/d/1580236359) |
|     782.71 |          51 | 2024-10-22 18:20:00+00:00 |       2 | Wien, 21. Bezirk, Floridsdorf          | [link](https://www.willhaben.at/iad/immobilien/d/1099198210) |
|     730    |          48 | 2024-10-22 18:16:00+00:00 |       2 | Wien, 10. Bezirk, Favoriten            | [link](https://www.willhaben.at/iad/immobilien/d/2098097818) |
|     527    |          35 | 2024-10-22 17:54:00+00:00 |       2 | Wien, 16. Bezirk, Ottakring            | [link](https://www.willhaben.at/iad/immobilien/d/1479636601) |
|     650.11 |          44 | 2024-10-22 17:05:00+00:00 |       2 | Wien, 05. Bezirk, Margareten           | [link](https://www.willhaben.at/iad/immobilien/d/2033714399) |
|     699    |          41 | 2024-10-22 15:27:00+00:00 |       2 | Wien, 14. Bezirk, Penzing              | [link](https://www.willhaben.at/iad/immobilien/d/2146732696) |
|     749    |          30 | 2024-10-22 15:27:00+00:00 |       2 | Wien, 22. Bezirk, Donaustadt           | [link](https://www.willhaben.at/iad/immobilien/d/782519959)  |
|     798    |          42 | 2024-10-22 14:53:00+00:00 |       2 | Wien, 21. Bezirk, Floridsdorf          | [link](https://www.willhaben.at/iad/immobilien/d/1744568207) |
|     510    |          52 | 2024-10-22 14:33:00+00:00 |       2 | Wien, 13. Bezirk, Hietzing             | [link](https://www.willhaben.at/iad/immobilien/d/1764120561) |
|     741.37 |          57 | 2024-10-22 14:23:00+00:00 |       2 | Wien, 11. Bezirk, Simmering            | [link](https://www.willhaben.at/iad/immobilien/d/1249098665) |
|     699    |          41 | 2024-10-22 14:04:00+00:00 |       2 | Wien, 22. Bezirk, Donaustadt           | [link](https://www.willhaben.at/iad/immobilien/d/1975223161) |
|     795    |          51 | 2024-10-22 13:51:00+00:00 |       2 | Wien, 15. Bezirk, Rudolfsheim-Fünfhaus | [link](https://www.willhaben.at/iad/immobilien/d/1939918169) |
|     798.88 |          41 | 2024-10-22 13:49:00+00:00 |       2 | Wien, 10. Bezirk, Favoriten            | [link](https://www.willhaben.at/iad/immobilien/d/774645004)  |
|     790    |          43 | 2024-10-22 12:57:00+00:00 |       2 | Wien, 23. Bezirk, Liesing              | [link](https://www.willhaben.at/iad/immobilien/d/838423492)  |
|     473.09 |          64 | 2024-10-22 12:33:00+00:00 |       3 | Wien, 10. Bezirk, Favoriten            | [link](https://www.willhaben.at/iad/immobilien/d/1551815967) |
|     799    |          63 | 2024-10-22 10:58:00+00:00 |       2 | Wien, 23. Bezirk, Liesing              | [link](https://www.willhaben.at/iad/immobilien/d/1569994193) |
|     750    |          43 | 2024-10-22 10:53:00+00:00 |       2 | Wien, 07. Bezirk, Neubau               | [link](https://www.willhaben.at/iad/immobilien/d/1123523943) |
