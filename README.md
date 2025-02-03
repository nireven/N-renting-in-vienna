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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       480    |            55 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gemeindewohnung-im-6.-bezirk---millergasse---direktvergabe-1920920882/)                         | Feb 03, 15:15      |
|       780    |            54 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/erstbezug-nach-sanierung-tolle-altbauwohnung-an-der-u4-785548802/)                             | Feb 03, 13:55      |
|       460    |            43 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-zu-vergeben-1100-wien-1435384049/)                                             | Feb 03, 13:03      |
|       650    |            57 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-in-1030-wien---57-m%C2%B2-im-1.-liftstock-1385945099/)                   | Feb 03, 12:22      |
|       799    |            70 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-wohnung-in-u3-n%C3%A4he-zu-mieten-in-1110-wien-1371652053/)                            | Feb 03, 11:29      |
|       608.3  |            56 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/studentenwohnung-1735437151/)                                                                     | Feb 03, 10:36      |
|       660    |            61 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/nachmieter-f%C3%BCr-neue-richtwertmietzins-wohnung-2091110674/)                                    | Feb 03, 10:09      |
|       790.65 |            43 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-huma-eleven---wohnung-perfekt-f%C3%BCr-p%C3%A4rchen-geeignet-mit-balkon-1309031000/)  | Feb 02, 21:37      |
|       799.96 |            47 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1810981329/) | Feb 02, 21:35      |
|       677    |            50 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/apartment-mit-b%C3%BCroeignung-1908796667/)                                                       | Feb 02, 16:05      |
