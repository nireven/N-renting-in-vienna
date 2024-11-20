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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       450    |            47 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/direktvergabe-gemeindewohnung-zu-vergeben-858549974/)                                                                 | Nov 20, 12:38      |
|       456.06 |            41 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet-%2B-perfekte-single-wohnung%21-832154980/)                                                                  | Nov 20, 12:36      |
|       777.21 |            48 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1030049299/)                                      | Nov 20, 12:22      |
|       689    |            38 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1936334166/)                                              | Nov 20, 12:18      |
|       730    |            89 |          4 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-gemeindewohnung-4-zimmer-2104361237/)                                                                               | Nov 20, 11:35      |
|       690    |            46 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gr%C3%BCnlage-golfplatz-s%C3%BC%C3%9Fenbrunn-n%C3%A4he-badeteich-1882252758/)                                          | Nov 20, 11:32      |
|       798.11 |            44 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-1143702571/)                                      | Nov 20, 11:28      |
|       699    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---ab-1.02.2025---gepflegte-neubauwohnung-mit-komplettk%C3%BCche-814791521/)                    | Nov 20, 11:03      |
|       799    |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung-mit-balkon%21-1693093114/)                                                                    | Nov 20, 10:55      |
|       770    |            49 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-sp%C3%A4ter-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                                     | Nov 20, 10:07      |
|       720    |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genie%C3%9Fen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)                        | Nov 20, 10:07      |
|       798.99 |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-neubauwohnung-mit-balkon-und-einbauk%C3%BCche%21-nahe-stra%C3%9Fenbahn-26-lorettowiese-und-scn-1740472691/)   | Nov 20, 09:59      |
|       798.99 |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumwohnungen-in-top-lage-zu-vermieten%21-1055837955/)                                                               | Nov 20, 09:48      |
|       640.01 |            33 |          2 | 09. Alsergrund  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/nette-2-zimmer--altbauwohnung-n%C3%A4he-w%C3%A4hringer-stra%C3%9Fe-1467811369/)                                        | Nov 20, 09:38      |
|       750    |            55 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/open-house-termin-buchen:-https://www.remax.at/de/1609-42321-sonnige-und-ruhige-2-zimmer-wohnung-mit-balkon-1328128151/) | Nov 20, 07:17      |
|       691.33 |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%28reserviert%29-neubauwohnung-zu-vermieten%21-1644760517/)                                                           | Nov 19, 23:11      |
|       693    |            65 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe---wiener-wohnticket-bis-30.09.2024-erforderlich%21-865968237/)                                            | Nov 19, 20:56      |
|       730    |            63 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/nachmieter-gesucht-1037959595/)                                                                                       | Nov 19, 20:12      |
|       787.92 |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m%C2%B2-zum-mietpreis-von-78792-eur%21-1580236359/)                      | Nov 19, 18:35      |
|       500    |            63 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-gemeindewohnung---direktvergabe-1210-wien-974408444/)                                                        | Nov 19, 16:01      |
