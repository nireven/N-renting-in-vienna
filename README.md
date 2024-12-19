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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       540    |            40 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-ca.-40-m%C2%B2-mit-wohnk%C3%BCche-schlafzimmer-bad-wc-1681868389/)                                                                                     | Dec 19, 12:58      |
|       650    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/befristete-miete-1960545360/)                                                                                                                                           | Dec 19, 12:05      |
|       768.97 |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charmante-2-zimmer-wohnung-am-sechshauser-g%C3%BCrtel%21-1142683402/)                                                                                  | Dec 19, 11:58      |
|       799    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ca.-55-m2-%282-zimmer%29-erstbezug-nach-sanierung-atelier-im-souterrain-f%C3%BCr-firma-oder-privat---all-inclusive-miete-warm-1832119767/)             | Dec 19, 11:55      |
|       790    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1566207186/)                                                                                                                 | Dec 19, 11:51      |
|       790    |            43 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/m%C3%B6blierte-wohnung-f%C3%BCr-eine-person-in-wien-9.-bezirk-1849488992/)                                                                                            | Dec 19, 11:43      |
|       749.97 |            43 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemuetliche-2-zimmerwohnung-an-der-h%C3%BCtteldorferstra%C3%9Fe-1508438578/)                                                                                             | Dec 19, 10:47      |
|       598    |            58 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-2-zimmer-1110-wien-1124888707/)                                                                                                                        | Dec 19, 10:35      |
|       749    |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gut-geschnittene-2-zimmer-wohnung-mit-knapp-40m2---leo-131---ab-01.02-1026345968/)                                                                                   | Dec 19, 08:57      |
|       798    |            63 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-f%C3%BCr-den-mieter%21-dadlergasse-altbaumiete-63m%C2%B2-komplettk%C3%BCche-halbstock-wg-eignung%21-studenten-bevorzugt%21-1331749446/) | Dec 19, 07:50      |
|       705.19 |            41 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/sch%C3%B6ne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                                                                             | Dec 19, 06:48      |
|       733.77 |            42 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                                                                            | Dec 19, 06:48      |
|       795    |            47 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnquartier-wildgarten---familienfreundliches-wohnen-auf-der-sonnenseite-wiens-direkt-am-rosenh%C3%BCgel-1596135640/)                                                  | Dec 18, 20:38      |
|       799.63 |            42 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-in-floridsdorf:-nachhaltigkeit-trifft-wohnkomfort.---wohntraum-1891395928/)                                                                 | Dec 18, 18:57      |
|       795.06 |            63 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2-zimmer-wohnung-in-absoluter-ruhelage-%7C-zellmann-immobilien-971518084/)                                                                                               | Dec 18, 18:57      |
|       769.94 |            65 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gepflegte-2-zimmer-wohnung-in-1230-wien-1973771947/)                                                                                                                     | Dec 18, 16:56      |
|       769.36 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/ideale-2-zimmer-dachgeschosswohnung-mit-gr%C3%BCnblick-in-stammersdorfer-heurigengegend-880459439/)                                                                  | Dec 18, 16:17      |
|       439    |            37 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/teilm%C3%B6blierter-altbau-nahe-u1-keplerplatz-1413881651/)                                                                                                            | Dec 18, 16:16      |
|       750    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/brunnenmarkt:-stylische-2-zimmer-wohnung-mit-gutem-grundriss-in-hofruhelage-1860136196/)                                                                               | Dec 18, 15:29      |
|       788.56 |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnen-zum-fairen-preis---wohnen-im-gr%C3%BCnen-und-doch-urban-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche%21-2073689009/)            | Dec 18, 14:46      |
