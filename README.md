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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799.26 |            37 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-nahe-der-seestadt-aspern-1964223642/)                                                                         | May 22, 08:21      |
|       799.99 |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-nahe-der-seestadt-aspern-1230842268/)                                                                         | May 22, 08:19      |
|       739.64 |            34 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-gartenwohnung-im-neubau-957095458/)                                                                                  | May 22, 08:18      |
|       418.88 |            31 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sanierungsbed%C3%BCrftige-bastlerwohnung-mit-potenzial-1062571834/)                                                             | May 22, 06:51      |
|       886.77 |            49 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/charmante-2-zimmer-wohnung-899332174/)                                                                                      | May 22, 06:51      |
|       763.35 |            42 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                                    | May 22, 06:48      |
|       860.12 |            60 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/leo-am-teich---wohnen-am-badeteich-hirschstetten-873710450/)                                                                  | May 21, 21:33      |
|       857.32 |            61 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/leo-am-teich---wohnen-am-badeteich-hirschstetten-1681435685/)                                                                 | May 21, 21:33      |
|       849    |            36 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderner-2-zimmer-wohntraum-der-keine-w%C3%BCnsche-offen-l%C3%A4sst-%21-1412614922/)                                          | May 21, 20:59      |
|       849    |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/kagraner-laberl---wohnen-zum-fairen-preis%21---neubaugebiet-n%C3%A4he-u1-kagraner-platz-1610687445/)                          | May 21, 20:35      |
|       899    |            46 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-ruhige-balkonwohnung-mit-top-anbindung-im-4.-liftstock-1362490098/)                                                      | May 21, 19:12      |
|       800.2  |            48 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/modern-m%C3%B6bliertes-mietapartment---kurz-oder-langfristig-1906152750/)                                                     | May 21, 18:36      |
|       857.2  |            60 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/mietkauf---leo-am-teich%21-willkommensbonus---2-monate-mietfrei%21-2026392354/)                                               | May 21, 18:27      |
|       854.4  |            61 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/mietkauf---leo-am-teich%21-willkommensbonus---2-monate-mietfrei%21-1831402204/)                                               | May 21, 18:27      |
|       873.11 |            53 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/mietkauf---leo-am-teich%21-willkommensbonus---2-monate-mietfrei%21-1057448629/)                                               | May 21, 18:27      |
|       868.69 |            51 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/mietkauf---leo-am-teich%21-willkommensbonus---2-monate-mietfrei%21-1888486411/)                                               | May 21, 18:27      |
|       884.02 |            55 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/mietkauf---leo-am-teich%21-willkommensbonus---2-monate-mietfrei%21-2116155360/)                                               | May 21, 18:27      |
|       884.4  |            64 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/ruhige-wohnung-%28innenhof%29-auf-der-pragerstra%C3%9Fe-76-mit-loggia-%7C-kaufoption-nach-5-jahren-m%C3%B6glich-2015108638/) | May 21, 17:25      |
|       896.96 |            54 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/provisionsfreier-mietkauf-in-gretl%27s-garten%21-1323578673/)                                                                 | May 21, 17:17      |
|       895    |            47 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnige-ruhige-wohnung-1584655273/)                                                                                              | May 21, 17:09      |
