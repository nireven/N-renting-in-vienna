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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       660    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-privat-zu-vergeben-1953364286/)                                                                               | Oct 30, 10:40      |
|       730    |            37 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhaftes-wohnen:-mietwohnungen-mit-kaufoption-in-stammersdorfer-ruhelage-761411354/)                             | Oct 30, 10:07      |
|       720    |            44 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genie%C3%9Fen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)                      | Oct 30, 10:07      |
|       770    |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-sp%C3%A4ter-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                                   | Oct 30, 10:07      |
|       798.99 |            40 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-neubauwohnung-mit-balkon-und-einbauk%C3%BCche%21-nahe-stra%C3%9Fenbahn-26-lorettowiese-und-scn-1740472691/) | Oct 30, 09:59      |
|       750.03 |            45 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nahe-sch%C3%B6nbrunn-%7C-2--zimmer-neubauwohnung-%7C-befristet-%7C-ab-sofort-1809715429/)                               | Oct 30, 09:56      |
|       798.99 |            40 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumwohnungen-in-top-lage-zu-vermieten%21-1055837955/)                                                             | Oct 30, 09:48      |
|       560    |            54 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/direktvergabe-gemeindewohnung-2-zimmer-%28generalsaniert%29-2080958038/)                                            | Oct 30, 08:01      |
|       676.17 |            45 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/n%C3%A4he-einsiedlerpark-hell-&-freundlich-neue-k%C3%BCche-schlafzimmer-in-den-innenhofunbefristet-1108902255/)      | Oct 30, 04:47      |
|       561.11 |            41 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristete-altbauwohnung-mit-terrasse-in-der-wolfganggasse-1054729284/)                                              | Oct 30, 03:20      |
|       781.45 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/praktisch-gelegene-2-zimmer-wohnung-1723277411/)                                                                      | Oct 30, 00:38      |
|       723    |            74 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wiener-wohnen-direktvergabe-1456899497/)                                                              | Oct 29, 22:19      |
|       516.02 |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtliche-2-zimmer-wohnung-2090680683/)                                                                         | Oct 29, 21:31      |
|       430    |            45 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-/-wiener-wohnen-1140-wien--nur-mit-vormerkschein-1773891561/)                                           | Oct 29, 20:59      |
|       685.01 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleinod--erstbezug-in-hauptbahnhof-n%C3%A4he-1577186673/)                                                             | Oct 29, 20:33      |
|       695    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmer-erstbezug-in-hauptbahnhof-n%C3%A4he-824306479/)                                                            | Oct 29, 19:35      |
|       433.18 |            39 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/direktvergabe-gemeindewohnung--nur-mit-wiener-wohn-ticket-1205437738/)                                               | Oct 29, 18:44      |
|       540    |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-mit-direktvergabe-2115627502/)                                                                                | Oct 29, 18:07      |
|       570    |            55 |          3 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/helle-&-renovierte-3-zimmer-gemeinde-wohnung-weiterzugeben-1159566384/)                                            | Oct 29, 14:26      |
|       765.37 |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/tolle-2-zimmer-wohnung-mit-idealer-raumaufteilung-in-guter-und-infrastrukturell-ansprechender-lage%21-1791769254/)  | Oct 29, 14:18      |
