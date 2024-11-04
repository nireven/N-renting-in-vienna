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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       777    |            44 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/freundliche-und-moderne-2-zimmer-wohnung-mit-gro%C3%9Fem-hofseitigem-balkon-nahe-u3-simmering-/-ab-1.1.25-verf%C3%BCgbar.-1461778021/)                                   | Nov 04, 12:27      |
|       789    |            41 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnungen-nahe-u1-kagraner-platz---aufstrebendes-wohnviertel-991040077/)                                                                                  | Nov 04, 11:58      |
|       550    |            51 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-2-zimmer-gemeindewohnung-1680972474/)                                                                                                                      | Nov 04, 11:55      |
|       495    |            43 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe:-letztmaliges-angebot:-abl%C3%B6se-%E2%82%AC-1500-f%C3%BCr-m%C3%B6blierte-43m2-wohnung-1163696543/)                                       | Nov 04, 11:50      |
|       730    |            42 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/basler-gasse---neubau-erstbez%C3%BCge-mit-garage-in-1230-wien-1215481577/)                                                                                                 | Nov 04, 11:19      |
|       798.58 |            45 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---sonnige-neubauwohnung-mit-s%C3%BCdbalkon-und-k%C3%BCche---10-minuten-zu-u6-und-s-bahn-floridsdorf-sowie-siemensstra%C3%9Fe-bahnhof.---wohntraum-1042336912/) | Nov 04, 11:19      |
|       649    |            33 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---fernblick---attraktive-kleinwohnung-im-dachgescho%C3%9F-----ab-1.12.2024-1329071562/)                                                                       | Nov 04, 11:05      |
|       695    |            39 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1590133781/)                                                                                                              | Nov 04, 11:03      |
|       674.43 |            34 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-terrassenwohnung-in-n%C3%A4he-des-flughafens%21-814789913/)                                                                                                     | Nov 04, 10:58      |
|       623.65 |            52 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sozialbau-wohnung-hoflage---2.-stock-mit-auzug-964357301/)                                                                                                                | Nov 04, 10:48      |
|       746.09 |            44 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung---nahe-der-alten-donau-953832565/)                                                                                                             | Nov 04, 10:37      |
|       792.89 |            40 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/top-wohnung-in-ruhiger-lage-beim-kirschbl%C3%BCtenpark-1642990666/)                                                                                                     | Nov 04, 10:08      |
|       772.07 |            49 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-49-2128415232/)                                                                                                                   | Nov 04, 09:47      |
|       770    |            55 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/generalsanierte-hofseitige-2-zimmerwohnung-mit-tischlerk%C3%BCche-1139038480/)                                                                                        | Nov 04, 09:47      |
|       656    |            66 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%28reserviert%29-2-zimmer-gemeindewohnung-in-zentraler-lage-n%C3%A4he-u4-1210817078/)                                                                                   | Nov 04, 09:47      |
|       799.05 |            46 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-46-915431798/)                                                                                                                    | Nov 04, 09:34      |
|       757.82 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina-%E2%97%8F-wohnanlage-am-leberberg:-b1-12-1773365340/)                                                                                                                | Nov 04, 09:34      |
|       790    |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohntr%C3%A4ume-erleben:-mietwohnungen-mit-option-auf-zuk%C3%BCnftigen-kauf-739383800/)                                                                 | Nov 04, 08:56      |
|       556.28 |            50 |          2 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/tolles-gesamtpaket-__urangenehme-gegend-__sonnige-wohnung-1103751504/)                                                                                                    | Nov 04, 08:38      |
|       770    |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhaftes-wohnen:-gartenwohnung-mit-kaufoption-in-idyllischer-wohngegend-1541740154/)                                                                                | Nov 04, 07:55      |
