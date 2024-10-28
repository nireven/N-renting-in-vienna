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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       710    |            61 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ruhige-wohnung-in-guter-lage-1343079052/)                                                                                                                                | Oct 28, 12:10      |
|       789    |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnungen-nahe-u1-kagraner-platz---aufstrebendes-wohnviertel-991040077/)                                                                                  | Oct 28, 11:58      |
|       795    |            59 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/best-living-oberlaa---moderne-wohnung%21-1185221694/)                                                                                                                    | Oct 28, 11:56      |
|       495    |            43 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe:-letztmaliges-angebot:-abl%C3%B6se-%E2%82%AC-1500-f%C3%BCr-m%C3%B6blierte-43m2-wohnung-1163696543/)                                       | Oct 28, 11:50      |
|       798.58 |            45 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---sonnige-neubauwohnung-mit-s%C3%BCdbalkon-und-k%C3%BCche---10-minuten-zu-u6-und-s-bahn-floridsdorf-sowie-siemensstra%C3%9Fe-bahnhof.---wohntraum-1042336912/) | Oct 28, 11:19      |
|       730    |            42 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/basler-gasse---neubau-erstbez%C3%BCge-mit-garage-in-1230-wien-1215481577/)                                                                                                 | Oct 28, 11:19      |
|       695    |            39 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1590133781/)                                                                                                              | Oct 28, 11:03      |
|       779.99 |            46 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2-zimmerwohnung---dachterrasse---einbauk%C3%BCche-1847041513/)                                                                                                             | Oct 28, 11:01      |
|       746.09 |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung---nahe-der-alten-donau-953832565/)                                                                                                             | Oct 28, 10:37      |
|       790    |            55 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gut-geschnittene-2-zimmer-wohnung-direkt-bei-der-ubahn---ab-sofort%21-1495581085/)                                                                                       | Oct 28, 10:08      |
|       595.66 |            42 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-sanierte-dachgeschosswohnung-im-10ten%21-1623442092/)                                                                                                  | Oct 28, 09:40      |
|       790    |            46 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohntr%C3%A4ume-erleben:-mietwohnungen-mit-option-auf-zuk%C3%BCnftigen-kauf-739383800/)                                                                 | Oct 28, 08:56      |
|       770    |            46 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhaftes-wohnen:-gartenwohnung-mit-kaufoption-in-idyllischer-wohngegend-1541740154/)                                                                                | Oct 28, 07:55      |
|       676.17 |            45 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/n%C3%A4he-einsiedlerpark-hell-&-freundlich-neue-k%C3%BCche-schlafzimmer-in-den-innenhofunbefristet-1778395783/)                                                         | Oct 28, 07:25      |
|       788.76 |            76 |          3 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/direktvergabe-3-zimmer-gemeindewohnung-1951126353/)                                                                                                                    | Oct 28, 05:49      |
|       552    |            54 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gemeindewohnung-direktvergabe-vms-31.07.2024-971207788/)                                                                                                              | Oct 27, 20:38      |
|       502    |            55 |          3 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeinde-wohnung-zu-vermieten-1772184612/)                                                                                                                                 | Oct 27, 20:02      |
|       780    |            77 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/2--zimmerwohnung-nur-mit-wohnticket-1490228131/)                                                                                                                       | Oct 27, 19:24      |
|       530.37 |            50 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-direcktvergabe-vormerkschein-30.09.2024-1998155311/)                                                                                                    | Oct 27, 18:14      |
|       773.7  |            75 |          3 | 18. Währing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/sanierte-wohnung-f%C3%BCr-zwei-medizinstudentinnen-in-perfekter-lage-%28erstbezug%29---beschreibung-lesen-978750611/)                                                 | Oct 27, 16:13      |
