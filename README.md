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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       535    |            55 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-vormerkschein-nr:-31.03.2025-776001728/)                                                                                                                                                                            | Mar 21, 20:34      |
|       462    |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeidewohnug-direktvergabe-1429603546/)                                                                                                                                                                                             | Mar 21, 20:32      |
|       680    |            46 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/provisionsfreie-m%C3%B6blierte-46-m%C2%B2-single-altbauwohnung-befristet-auf-3-jahre-1201476125/)                                                                                                                                   | Mar 21, 19:43      |
|       603    |            55 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/1090:-55m%C2%B2-altbau-befr.-603---%3B-hwb-1552-489782661/)                                                                                                                                                                         | Mar 21, 17:22      |
|       799    |            38 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---wohnen-am-erlachpark---6ter-liftstock---garagenplatz-inklusive-1331806037/)                                                                                                                                              | Mar 21, 16:46      |
|       458.26 |            46 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1160-wien-wiener-wohnticket-erforderlich%21-2021986358/)                                                                                                                                                             | Mar 21, 16:17      |
|       450    |           140 |          5 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ein-helles-zimmer-mit-direktem-terrassenzugang-in-7-zimmer-studenten-wohngemeinschaft-mit-5-schlafzimmern-22-m%C2%B2-terrasse-f%C3%BCr-studentinnen-wg-geeignet-%281-k%C3%BCche-2-badezimmer-und-2-wcs%29-ab-1.-april-2-1746791727/) | Mar 21, 12:58      |
|       700    |            65 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/65m%C2%B2-gr%C3%BCnruhelage-in-neuwaldegg-1245061073/)                                                                                                                                                                                 | Mar 21, 12:45      |
|       790    |            47 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnquartier-wildgarten---familienfreundliches-wohnen-auf-der-sonnenseite-wiens-direkt-am-rosenh%C3%BCgel-1126709749/)                                                                                                                | Mar 21, 11:48      |
|       570    |            39 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-in-top-lage-mit-garten%21-1622656867/)                                                                                                                                                                                        | Mar 21, 10:31      |
|       757    |            73 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/bitte-keine-anfragen-mehr%21%21%21-suche-nachmieter%2Ain-f%C3%BCr-3zimmer-im-15.-bezirk-1955537941/)                                                                                                                 | Mar 21, 09:33      |
|       616    |           nan |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sensationelle-garconniere-in-wien-altmannsdorf-1860133618/)                                                                                                                                                                           | Mar 21, 09:26      |
|       738.21 |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wunderbare-2-zimmer-wohnung-mit-balkon-in-gr%C3%BCnruhelage-u-1-kurpark-oberlaa-n%C3%A4he-1393330499/)                                                                                                                               | Mar 21, 02:30      |
