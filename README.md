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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       899    |            61 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/perfekte-stadtwohnung:-direkt-bei-der-urania-mit-donaublick%21-1335060887/)                                                                  | Jun 12, 08:05      |
|       825    |            80 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeinde-wohnung-80m2-3-zimmer-vm-31.05.2024-1136669019/)                                                                                       | Jun 11, 19:51      |
|       895    |            55 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/laendyard:-erstklassige-zwei-zimmer-gartenwohnung-zwischen-prater-und-city---miete-1030-wien-1613667954/)                                    | Jun 11, 18:19      |
|       795    |            54 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3.erdbergstrasse---provisionsfreie-charmante-2-zimmer-neubaumiete-direkt-beim-kardinal-naglplatz-2105617351/)                                | Jun 11, 15:32      |
|       698    |            46 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/g%C3%BCnstige-altbauwohnung-in-ruhiger-lage-direkt-an-der-mariahilfer-stra%C3%9Fe-vollm%C3%B6bliert-und-einzugsfertig-keine-provision-1535227526/) | Jun 11, 14:41      |
|       845.51 |            38 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/nette-2-zimmerwohnung-in-mariahilf-1127052797/)                                                                                                    | Jun 11, 14:26      |
|       899    |            38 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/tolle-neubauwohnung-in-bestlage%21-907866199/)                                                                                                    | Jun 11, 13:34      |
