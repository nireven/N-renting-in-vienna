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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       670.96 |            39 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/toplage/zentrum%21-unbefristete-extravagante-altbau-kleinwohnung-ca.-40-m2-2-zimmer%21-sofortbezug%21-1541874302/) | Jun 03, 11:21      |
|       449.36 |            30 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lager/atelier-zur-miete-in-1050-wien---ehemalige-wohnung-nahe-pilgramgasse-1798271816/)                            | Jun 03, 09:57      |
|       829.63 |            56 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/wohnen-in-zentrumsn%C3%A4he-mit-balkon---studenten-nahe-wu-1061532200/)                                          | Jun 03, 03:22      |
|       899    |            61 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/stadtwohnung-in-traumlage:-direkt-bei-der-urania-wien-mitte-mit-donaublick%21-1326151163/)                    | Jun 03, 03:21      |
|       863.87 |            51 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/bitte-nur-schriftliche-anfrage-keine-anrufe.-h%C3%BCbsche-2-zi-wohnung-in-der-laudongasse-1406230610/)             | Jun 02, 16:19      |
|       660    |            57 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zimmer-gemeindewohnung-per-direktvergabe---1090-wien-1405612803/)                                                | Jun 02, 16:19      |
|       465.56 |            45 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/wohnvergabe-einer-2-zimmer-wohnung/-vormerkschein-bis-30.04.2025-1536679945/)                                    | Jun 02, 11:38      |
|       819.25 |            49 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/fasanviertel---tolle-zwei-zimmer-wohnung-1783608545/)                                                         | Jun 02, 10:54      |
