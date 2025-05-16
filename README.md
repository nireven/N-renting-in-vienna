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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       699.99 |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/open-house-am-19.5.-15:50-16:10%21-anfragen-nur-per-mail---keine-anrufe%21-1103624416/)                                                         | May 16, 12:20      |
|       546.39 |            40 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/open-house-21.5.-16:30-16:50-uhr%21-keine-anrufe---anfragen-nur-per-mail%21-1764113241/)                                                          | May 16, 12:03      |
|       652.64 |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/open-house-19.5.-16:30-16:50-uhr%21-anfragen-nur-per-mail---keine-anrufe%21-1366934735/)                                                        | May 16, 11:57      |
|       645.78 |            63 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/generalsanierte-3-zimmer-wohnung---befristet-1497167484/)                                                                                       | May 16, 11:36      |
|       446.88 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/generalsanierte-2-zimmer-wohnung---befristet-1895589718/)                                                                                       | May 16, 11:35      |
|       791.8  |            55 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/klassische-2-zimmer-altbauwohnung%21%21%21-%2Aerstbezug-nach-generalsanierung%2A-1164434850/)                                                     | May 16, 10:58      |
|       678    |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/56-m2-wohnung-wien-16-ruhige-lage-2042061403/)                                                                                                  | May 16, 10:46      |
|       674    |            59 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-sozialbau-625313902/)                                                                                                                    | May 16, 08:18      |
|       638    |            60 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-direkt-vergabe-1035589679/)                                                                                                     | May 15, 21:44      |
|       766    |            73 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-gemeindewohnung-%28direktvergabe%29-1035817556/)                                                                                       | May 15, 20:34      |
|       719.31 |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei:-unbefristete-52m%C2%B2-altbau-hauptmiete-mit-lift---1150-wien-1988626166/)                                      | May 15, 18:57      |
|       748    |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/mit-eigentumsoption%21-helle-neubau-2-zimmergenossenschaftswohnung-nahe-ottakringer-bahnhof-1916797369/)                                        | May 15, 18:07      |
|       669    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neuwertige-2-zimmerwohnung-mit-balkon-inkl.-heizkosten%21-1958767788/)                                                                          | May 15, 16:57      |
|       645    |            40 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-nahe-u6-thaliastra%C3%9Fe---perfekt-f%C3%BCr-singles-oder-paare-1813305604/)                                         | May 15, 15:48      |
|       690    |            64 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-ca.-64m%C2%B2-1205283037/)                                                                                                 | May 15, 15:03      |
|       790    |            35 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/moderne-singlewohnung-in-der-linzer-strasse-1258677953/)                                                                                          | May 15, 13:49      |
|       750    |            54 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%28reserviert%29-charmante-single-oder-p%C3%A4rchen-wohnung-798890361/)                                                                            | May 15, 13:18      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/) | May 15, 11:22      |
