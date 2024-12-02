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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       742.17 |            41 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                                                           | Dec 02, 16:51      |
|       684.72 |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-2-zimmer-wohnung-mit-loggia%21-1810724423/)                                                                                                                     | Dec 02, 16:50      |
|       780.3  |            35 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/singlehit-in-1210-wien-zu-mieten-1946913358/)                                                                                                                              | Dec 02, 16:35      |
|       799    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-nahe-dem-wien-hauptbahnhof---ab-sofort-beziehbar%21-1091639000/)                                                                                            | Dec 02, 16:19      |
|       573.62 |            50 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/helle-2--zimmer-wohnung-1629127734/)                                                                                                                                       | Dec 02, 16:07      |
|       799    |            50 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/perfekt-aufgeteilte-zweiraumwohnung-mit-sonnigem-balkon-ab-01.02.25-in-penzing-1346278094/)                                                                                    | Dec 02, 15:37      |
|       725    |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-zur-miete-1262465119/)                                                                                                                                      | Dec 02, 15:32      |
|       743.33 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertiger-neubau-zu-fairen-preisen---gut-angebunden-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche-&-freifl%C3%A4che-1510992864/) | Dec 02, 14:58      |
|       743.33 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertiger-neubau-zu-fairen-preisen---gut-angebunden-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche-&-freifl%C3%A4che-1127569884/) | Dec 02, 14:58      |
|       470    |            43 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/2-zimmer-wiener-wohnen-gemeindewohnung-%7C-43-m%C2%B2-1228659901/)                                                                                                         | Dec 02, 14:20      |
|       625    |            60 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-gemeindewohnung-1704367494/)                                                                                                                                        | Dec 02, 14:13      |
|       685    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---8ter-liftstock---neuwertige-helle-singlewohnung-in-modernen-wohnhaus-1072719993/)                                                                 | Dec 02, 14:04      |
|       560    |            53 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-gemeindewohnung-1602313884/)                                                                                                                                       | Dec 02, 13:21      |
|       746.09 |            44 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung---nahe-der-alten-donau-1430023592/)                                                                                                                | Dec 02, 13:19      |
|       799.99 |            44 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-und-kellerabteil-in-ruhiger-lage-/-i3-19-1816066750/)                                                                | Dec 02, 13:15      |
|       585.2  |            42 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/kernsanierte-top-wohnung---alles-neu---n%C3%A4he-prater-1359064182/)                                                                                                      | Dec 02, 12:31      |
|       680    |            45 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/charmante-2-zimmer-wohnung-in-1180-wien-1491256598/)                                                                                                                      | Dec 02, 12:28      |
|       699    |            48 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/in-raten-m%C3%B6glich-untermiete-komplett-m%C3%B6beliert-1322674099/)                                                                                        | Dec 02, 12:19      |
|       790    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-%7C-freiraum-genie%C3%9Fen:-2-zimmer-mit-terrasse-2043360015/)                                                             | Dec 02, 11:55      |
|       790    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stilvolles-2-zimmer-apartment-mit-sonniger-terrasse---viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-1518345975/)                                                         | Dec 02, 11:55      |
