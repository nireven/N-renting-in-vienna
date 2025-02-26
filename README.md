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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       479    |            45 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-wohnung-1637086890/)                                                                                             | Feb 26, 08:13      |
|       716.8  |            52 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ger%C3%A4umige-2-zimmer-wohnung-im-eg-1214111912/)                                                                       | Feb 26, 02:47      |
|       680    |            53 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei:-toprenovierter-53m%C2%B2-altbau-mit-2-zimmern-und-einbauk%C3%BCche---1050-wien-1258352506/)            | Feb 25, 19:35      |
|       742    |            37 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/suche-nachmieter%21-1951247027/)                                                                                        | Feb 25, 18:58      |
|       735.91 |            35 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neubau--sch%C3%B6ne-dachgescho%C3%9Fwohnung-zu-vermieten-1975974582/)                                                   | Feb 25, 18:51      |
|       758.72 |            53 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-altbauwohnung-mit-viel-potential-i-1.-stock-ohne-lift-i-n%C3%A4he-thaliastra%C3%9Fe-bezirksamt-840947172/)     | Feb 25, 16:55      |
|       529.83 |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-altbauwohnung-in-top-lage-i-3.-stock-ohne-lift-i-n%C3%A4he-thaliastra%C3%9Fe-bezirksamt-1057111022/)           | Feb 25, 16:55      |
|       588.65 |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gut-geschnittene-2-zimmer-altbauwohnung-i-1.-stock-ohne-lift-i-n%C3%A4he-thaliastra%C3%9Fe-bezirksamt-1925017129/)      | Feb 25, 16:55      |
|       740    |            48 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wohnung-1150-mit-10m%C2%B2-balkon-%28innenhof%29-1244249433/)                                           | Feb 25, 14:43      |
|       699    |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---s%C3%BCd-westblick---neuwertige-2-zimmer-terrassenwohnung---ab-01.03.2025-945593308/)                       | Feb 25, 13:50      |
|       790    |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-mietwohnung-bei-u4-station-unter-st.-veit-1922612354/)                                                           | Feb 25, 13:48      |
|       785    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/)   | Feb 25, 13:28      |
|       590    |            47 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/1090-wien-r%C3%B6gergasse-47m%C2%B2-2-zimmer-duschbad-mit-wc-einbauk%C3%BCche-4.-stock-ohne-lift-ruhelage-820548198/)  | Feb 25, 12:20      |
|       733.92 |            56 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sanierte-2-zimmer-wohnung-im-15.-n%C3%A4he-westbahnhof-1239337781/)                                     | Feb 25, 11:47      |
|       729.01 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-mit-dachschr%C3%A4ge-inkl.-k%C3%BCche-dachterrasse-und-kellerabteil-/hs28-top-2-261-1162587651/) | Feb 25, 11:26      |
|       768    |            51 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-ger%C3%A4umige-neue-51m%C2%B2-3-zimmer-mietwohnung-f%C3%BCr-768%E2%82%AC-in-wien-1160-928466323/)           | Feb 25, 10:44      |
