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
|       579    |            42 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/abl%C3%B6sefreie-hauptmietwohnung-in-erdberg-1217041890/)                                 | Feb 08, 09:57      |
|       420    |            60 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeinde-wohnung-3zimmer-1718112961/)                                                            | Feb 08, 07:48      |
|       774    |            73 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeinde-wohnung-mit-vormerkschein-30.9.2024-1977412157/)                                       | Feb 08, 05:26      |
|       750    |            50 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/single-apartement-in-ruhiger-innenstadtlage-%7C-m%C3%B6bliert-1525495016/)                     | Feb 08, 04:38      |
|       742.01 |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2A%2A-u1-troststrasse-neuwertige-2-zimmer-whg-%2A%2A%2A-894413408/)                            | Feb 08, 01:11      |
|       781.58 |            49 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmerwohnung-lambertgasse-4-ecke-schuhmeierplatz-16-1080351829/)                             | Feb 07, 17:45      |
|       729.16 |            55 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/n%C3%A4he-allianz-stadion:-praktische-2-zimmer-altbau-wohnung-ca.-55qm-unbefristet-1758716052/)   | Feb 07, 16:36      |
|       739.18 |            53 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/n%C3%A4he-hanuschkrankenhaus:-gem%C3%BCtliche-2-zimmer--altbauwohnung-befristet-854143881/)       | Feb 07, 16:36      |
|       780    |            71 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hofseitige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen%2A%2A%2Aunbefristet%2A%2A%2A-1781169223/) | Feb 07, 11:58      |
|       460    |            45 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wohnung-weitergabe-%28nur-mit-vormerkschein-von-wiener-wohnen%29-1894237741/)             | Feb 07, 09:29      |
|       752.6  |            67 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/provisionsfrei%21-helle-mietwohnung-n%C3%A4he-grillgasse-1605227571/)                           | Feb 07, 09:26      |
