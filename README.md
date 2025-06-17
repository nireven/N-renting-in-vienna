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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       845.51 |            38 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/nette-2-zimmerwohnung-in-mariahilf-1615877353/)                                                      | Jun 17, 13:26      |
|       506    |            43 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-im-3.-bezirk-mit-vormerkschein-1067587977/)                                    | Jun 17, 13:04      |
|       820    |            71 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/herrliche-aussicht-1588435316/)                                                                   | Jun 17, 10:46      |
|       449.36 |            30 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lager/atelier-zur-miete-in-1050-wien---ehemalige-wohnung-nahe-pilgramgasse-1798271816/)             | Jun 17, 09:57      |
|       770    |            46 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/mietwohnung-von-privat--provisionsfrei-1133204176/)                                                 | Jun 17, 08:58      |
|       899.06 |            61 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/perfekte-stadtwohnung:-direkt-bei-der-urania-mit-donaublick%21---jetzt-zuschlagen-1092264776/) | Jun 17, 06:54      |
|       861.55 |            55 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/2-zimmerwohnung-n%C3%A4he-mariahilfer-strasse%21-gfrornergasse-13-top-14-2135258371/)                | Jun 17, 06:21      |
|       499    |            38 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/altbau-charme-in-top-lage-direkt-an-der-u4---perfekt-f%C3%BCr-studierende%21-784673921/)            | Jun 16, 17:27      |
|       610    |            55 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%28reserviert%29-gemeindewohnung-direktvergabe-2-zimmer-in-toplage-1907609198/)                     | Jun 16, 14:25      |
