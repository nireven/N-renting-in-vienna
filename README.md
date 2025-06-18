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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       830    |            77 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/3-zimmer-gemeindewohnung-%2877-m%C2%B2%29-n%C3%A4he-nordbahnviertel-%7C-direktvergabe-nur-mit-vormerkschein-vor-30.04.2024-1067744152/) | Jun 17, 23:13      |
|       895    |            40 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/charmante-wohnung-mit-landstrasse-hauptstrasse-n%C3%A4he-2115758901/)                                                                | Jun 17, 21:09      |
|       875.94 |            62 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/tolles-zuhause-n%C3%A4he-hauptbahnhof%21-1615573530/)                                                                                         | Jun 17, 17:16      |
|       845.16 |            82 |          3 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/nette-drei-zimmer-n%C3%A4he-u6-1441198222/)                                                                                               | Jun 17, 14:53      |
|       845.51 |            38 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/nette-2-zimmerwohnung-in-mariahilf-1615877353/)                                                                                            | Jun 17, 13:26      |
|       506    |            43 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-im-3.-bezirk-mit-vormerkschein-1067587977/)                                                                          | Jun 17, 13:04      |
|       820    |            71 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/herrliche-aussicht-1588435316/)                                                                                                         | Jun 17, 10:46      |
|       449.36 |            30 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lager/atelier-zur-miete-in-1050-wien---ehemalige-wohnung-nahe-pilgramgasse-1798271816/)                                                   | Jun 17, 09:57      |
|       770    |            46 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/mietwohnung-von-privat--provisionsfrei-1133204176/)                                                                                       | Jun 17, 08:58      |
