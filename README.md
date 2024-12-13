![Scraping Pipeline](https://github.com/AthomsG/renting-in-vienna/actions/workflows/run_pipeline.yml/badge.svg)


# Renting in Vienna

This repo fetches every **5 minutes** (Actually it's less than 30 minutes because github is a bit unreliable with the cron functionality) the latest apartments from [willhaben](https://www.willhaben.at/).
It then filters the listings according to my preferences and stores them in `check_these.csv` - You can change filter settings in the `filter_dataset.py` script.

```python
filtered_df = df[(df.State == 'Wien') & 
                 (df.Price < 800) &
                 (df.Price > 400) &
                 (df.Rooms > 1) &
                 (df['Property Type'] == 'Wohnung') &
                 (df['Published Date'] >= one_day_ago)]
```

The 20 latest listings according to my preferences are printed in this README for you conviniece! Press the link to see the listing post.
The table is sorted by publish times in ascending order, with the closest publish time to the current time listed first.

If you want to get notifications in real time for when new apartments pop up, you can join the telegram channel synced to this repo [here](https://t.me/+1HPAYOf5BSsyNTlk).

## Recent Active Listings

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       757.82 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina-%E2%97%8F-wohnanlage-am-leberberg:-b1-12-776673186/)                                                                                                   | Dec 13, 06:10      |
|       755.72 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-05-1727649923/)                                                                                                     | Dec 13, 06:10      |
|       748.62 |            40 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-18-1243081816/)                                                                                                     | Dec 13, 06:10      |
|       798.34 |            47 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a2-29-1201479630/)                                                                                                     | Dec 13, 06:10      |
|       762.56 |            40 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---sonnige-wohnung-mit-loggia/balkon-:-top-a3-39-1456380993/)                                                                                           | Dec 13, 06:10      |
|       754.86 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-13-1254657699/)                                                                                                     | Dec 13, 06:10      |
|       678.83 |            49 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-im-3.-og-2009648704/)                                                                                                     | Dec 13, 02:49      |
|       691.56 |            58 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/taborstrasse-68%21-bastlerhit%21-1252170560/)                                                                                                           | Dec 12, 20:38      |
|       653    |            68 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%21%212-zimmer-gemeindewohnung-ab-m%C3%A4rz-verf%C3%BCgbar-ist%21-852578685/)                                                                             | Dec 12, 19:33      |
|       693.94 |            56 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gelegenheit-%7C-unbefristete-%7C-helle-3-zimmer-wohnung-%7C-erstbezug-nach-sanierung-%7C-neue-einbauk%C3%BCche-%7C-wg-eignung-2128237317/)                   | Dec 12, 19:32      |
|       686.98 |            33 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmerwohnung-mit-balkon-1394736292/)                                                                                                                      | Dec 12, 18:16      |
|       778.65 |            74 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-ca.-74-m%C2%B2-wohnung-mit-westseitiger-loggia-%21-992127259/)                                                                                       | Dec 12, 15:37      |
|       690    |            53 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/befristete-hochparterre-loggia-wohnung-ohne-k%C3%BCche-1523045931/)                                                                                     | Dec 12, 15:07      |
|       783.78 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderner-komfort-mit-aussicht:-balkonwohnung-in-top-lage-zu-einem-tollen-preis-880566402/)                                                                 | Dec 12, 14:18      |
|       660    |            66 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/g%C3%BCnstige-wohnung-mit-balkon-im-10.-bezirk-1081257437/)                                                                                                | Dec 12, 14:15      |
|       649    |            33 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/ab-1.1.2025---s%C3%BCssenbrunnerstra%C3%9Fe-11-1220-wien---hofseitige-singlewohnung-mit-balkon-1409258859/)                                               | Dec 12, 14:02      |
|       690.04 |            61 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-2-zimmer-wohnung-n%C3%A4he-westbahnhof-und-sch%C3%B6nbrunn-mit-guter-%C3%B6ffentlicher-anbindung-1959729729/)                        | Dec 12, 13:44      |
|       537.9  |            50 |          3 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/3-zimmer-gemeindewohnung-in-1060-wien-mit-balkon-%28gemeinde-wohnung%29-1879538742/)                                                                       | Dec 12, 13:37      |
|       749.99 |            40 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-k%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-sp64-top-6-26-2111497728/)                                        | Dec 12, 12:28      |
|       799    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ca.-55-m2-%282-zimmer%29-erstbezug-nach-sanierung-atelier-im-souterrain-f%C3%BCr-firma-oder-privat---all-inclusive-miete-warm-1832119767/) | Dec 12, 11:55      |
