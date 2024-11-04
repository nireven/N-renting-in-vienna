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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       623.65 |            52 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sozialbau-wohnung-hoflage---2.-stock-mit-auzug-964357301/)                                                | Nov 04, 10:48      |
|       746.09 |            44 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung---nahe-der-alten-donau-953832565/)                                             | Nov 04, 10:37      |
|       782.08 |            56 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sehr-sch%C3%B6ne-2-zimmer-wohnung---n%C3%A4he-lugner-city%21-1419282449/)                                | Nov 04, 10:17      |
|       792.89 |            40 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/top-wohnung-in-ruhiger-lage-beim-kirschbl%C3%BCtenpark-1642990666/)                                     | Nov 04, 10:08      |
|       770    |            55 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/generalsanierte-hofseitige-2-zimmerwohnung-mit-tischlerk%C3%BCche-1139038480/)                        | Nov 04, 09:47      |
|       772.07 |            49 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-49-2128415232/)                                                   | Nov 04, 09:47      |
|       656    |            66 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zimmer-gemeindewohnung-in-zentraler-lage-n%C3%A4he-u4-1210817078/)                                    | Nov 04, 09:47      |
|       799.05 |            46 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-46-915431798/)                                                    | Nov 04, 09:34      |
|       757.82 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina-%E2%97%8F-wohnanlage-am-leberberg:-b1-12-1773365340/)                                                | Nov 04, 09:34      |
|       790    |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohntr%C3%A4ume-erleben:-mietwohnungen-mit-option-auf-zuk%C3%BCnftigen-kauf-739383800/) | Nov 04, 08:56      |
|       556.28 |            50 |          2 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/tolles-gesamtpaket-__urangenehme-gegend-__sonnige-wohnung-1103751504/)                                    | Nov 04, 08:38      |
|       770    |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhaftes-wohnen:-gartenwohnung-mit-kaufoption-in-idyllischer-wohngegend-1541740154/)                | Nov 04, 07:55      |
|       788.76 |            76 |          3 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/direktvergabe-3-zimmer-gemeindewohnung-1951126353/)                                                    | Nov 04, 05:49      |
|       799.9  |            47 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/ruhige-zweizimmerwohnung-mit-morgensonne-%2B%2B%2B-neubau-1270240134/)                                  | Nov 04, 03:35      |
|       780    |            40 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/preis-inkl.-heizung-von-privat:-tolle-studio-wohnung-in-ruhiger-lage-1243001313/)                        | Nov 03, 22:55      |
|       797    |            77 |          3 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinde-wohnung-im-22.-bezirk-zu-vergeben-897939444/)                                                  | Nov 03, 22:13      |
|       687.19 |            44 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%28reserviert%29-charmante-2-zimmer-wohnung-in-toplage-des-9.-bezirks%21-1375125146/)                   | Nov 03, 22:12      |
|       750    |            52 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-25-zimmer-im-1160-1872133360/)                                                                       | Nov 03, 19:12      |
|       540    |            54 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-direktvergabe-helle-2-zimmerwohnung-vms-bis-30.09.2024-1944879853/)                      | Nov 03, 16:13      |
|       663    |            62 |          3 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinede-wohnung-dirktvergabe-833386502/)                                                              | Nov 03, 15:50      |
