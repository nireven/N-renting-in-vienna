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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       663.05 |            42 |          2 | 07. Neubau      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/wohnen-im-kloster%21-moderne-2-zimmer-1649182290/)                                                                                                             | Oct 29, 09:26      |
|       670    |            57 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-1210-wien-%28ruthnergasse%29-2-zimmer---vormerkschein-stichtag-31.10.2024-1805903422/)                                                    | Oct 29, 09:24      |
|       725    |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-im-10.bezirk---renovierter-altbau---gute-anbindung-und-infrastruktur-1894245947/)                                                          | Oct 29, 09:17      |
|       680    |            44 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/privat%21-2-zimmerwohnung-zu-vermieten-1865971676/)                                                                                                         | Oct 29, 09:16      |
|       750    |            56 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ruhige-mietwohnung-schloss-neugeb%C3%A4ude-barrierefrei-unm%C3%B6bliert-1769667348/)                                                                        | Oct 29, 08:39      |
|       457    |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-vormerkschein-vor-30.09.2024-1195305098/)                                                                                     | Oct 29, 07:38      |
|       699    |            47 |          2 | 06. Mariahilf   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/1060-wien-hornbostelgasse-2-zimmer-k%C3%BCche-duschbad-ruhelage-1.-stock-ohne-lift-864706857/)                                                              | Oct 29, 07:35      |
|       798.91 |            60 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/ger%C3%A4umige-2-zimmer--wohnung-1530891048/)                                                                                                                 | Oct 29, 06:52      |
|       782    |            43 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/tolle-2-zimmer-wohnung-in-absoluter-ruhelage-mit-sch%C3%B6nem-balkon-1191538653/)                                                                             | Oct 29, 03:21      |
|       420.46 |            42 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeinde-wohnung-vmd-31102024-1423456187/)                                                                                                                    | Oct 28, 21:52      |
|       769.7  |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/nette-2-zimmerwohnung-mit-freifl%C3%A4che-%7C-unbefristet%7C-gro%C3%9Fenzersdorfer-stra%C3%9Fe-%7C-top-1/2/35-1157402518/)                                 | Oct 28, 19:41      |
|       725    |            40 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neubau-ab-01.02.-beziehbar:-sch%C3%B6ne-2-zimmerwohnung-mit-loggia-im-3.-og-2055199338/)                                                                     | Oct 28, 19:32      |
|       749    |            47 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/nachmieter-f%C3%BCr-eine-2-zimmer-wohnung-ab-sofort-gesucht%21%21%21-2020879630/)                                                                          | Oct 28, 19:24      |
|       610    |            55 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/%28reserviert%29-gemeindewohnung-1200-wien-direktvergabe-1959296997/)                                                                                     | Oct 28, 19:07      |
|       732.65 |            62 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/zu-vermieten-in-wien-19-%28wohnung-miete-haus%29-1943265672/)                                                                                            | Oct 28, 19:01      |
|       714.88 |            53 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfreie-2-zimmer-wohnung-im-10.-bezirk-1381815814/)                                                                                                 | Oct 28, 18:43      |
|       799    |            41 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-blick-auf-den-stephansdom---ab-15.12.2024-beziehbar%21-1125235828/)                                                                    | Oct 28, 18:35      |
|       789    |            48 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/toll-aufgeteilte-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1174359063/)                                                                                     | Oct 28, 17:38      |
|       799    |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnen-zum-fairen-preis---wohnen-im-gr%C3%BCnen-und-doch-urban-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche%21-1647352448/) | Oct 28, 17:36      |
|       780    |            40 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/preis-inkl.-heizung-von-privat:-tolle-studio-wohnung-in-ruhiger-lage-1243001313/)                                                                           | Oct 28, 17:28      |
