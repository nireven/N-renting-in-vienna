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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       733.7  |            50 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/suche-nachmieter-f%C3%BCr-50m%C2%B2-wohnung-/-looking-for-tenant-50m%C2%B2-apartment-1729746100/)                        | Feb 10, 13:18      |
|       690    |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweier-wg-oder-f%C3%BCr-ein-p%C3%A4rchen-1385455763/)                                                                     | Feb 10, 12:51      |
|       779    |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/11.braunhubergasse-unbefristete-provisionsfreie-2-zimmer-altbaumiete-in-u3-n%C3%A4he-801910236/)                          | Feb 10, 12:32      |
|       784.38 |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/hollergasse---2-zimmer-erdgeschosswohnung-1602693186/)                                                    | Feb 10, 09:15      |
|       730.09 |            53 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/charmante-altbauwohnung-direkt-beim-augarten-zur-unbefristeten-vermietung.-2123519583/)                                | Feb 10, 07:38      |
|       558.73 |            53 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/direktvergabe-gemeindebau-2-zimmer-wohnung-im-5.-bezirk-837220260/)                                                      | Feb 09, 22:48      |
|       790.65 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-huma-eleven---wohnung-perfekt-f%C3%BCr-p%C3%A4rchen-geeignet-mit-balkon-1309031000/)                            | Feb 09, 21:37      |
|       799.96 |            47 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1810981329/)                           | Feb 09, 21:35      |
|       489.19 |            74 |          3 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/wohnung---atelier---gro%C3%9F-und-g%C3%BCnstig-2040066412/)                                                              | Feb 09, 17:52      |
|       756.85 |            79 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-renoviert%21-altbauwohnung-mit-2-zentral-begehbaren-zimmern-und-wohnk%C3%BCche-993349002/)                            | Feb 09, 16:55      |
|       700    |            55 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/befristete-vollm%C3%B6blierte-2-zimmer-wohnung-zur-untermiete-%28ab-april-2025-bis-november-2025%29-1160-wien-864064417/) | Feb 09, 15:34      |
|       556    |            58 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/untermiete%21%21-lichtdurchflutete-altbauwohnung/-2-monate-sommer-juli-august-2049636973/)                               | Feb 09, 13:49      |
|       560.24 |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe:-sch%C3%B6ne-2-zimmer-wohnung-in-oberlaa-2118643302/)                                                       | Feb 09, 13:15      |
|       490    |            37 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-single--und-p%C3%A4rchen-hit-in-1020-wien---erstbezug-nach-sanierung-1282536407/)                     | Feb 09, 12:52      |
