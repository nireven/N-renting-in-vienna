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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       727.56 |            66 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/ruhige-2-zimmer-wohnung-provisionsfrei-unbefristet-1057479509/)                                                         | Feb 10, 22:01      |
|       605.9  |            42 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/n%C3%A4he-u3-erdberg-ii-1-zimmer-mit-kabinett-und-separater-k%C3%BCche-ii-an-der-erdbergstra%C3%9Fe-933972413/) | Feb 10, 21:38      |
|       739.96 |            51 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/n%C3%A4he-u3-erdberg-ii-2-zimmer-mit-separater-k%C3%BCche-ii-an-der-erdbergstra%C3%9Fe-1316904187/)             | Feb 10, 21:35      |
|       526.43 |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1500893406/)                                                                                          | Feb 10, 18:33      |
|       739.96 |            51 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/unbefristete-altbauwohnung-in-u3-n%C3%A4he-1755801817/)                                                         | Feb 10, 17:28      |
|       748.91 |            37 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/the-arrow---willkommen-im-gr%C3%BCnen-teil-simmerings-974631888/)                                                     | Feb 10, 16:49      |
|       719    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gr%C3%BCnruhelage---unbefristete-altbaumiete-in-sch%C3%B6nem-eckzinshaus-%21-1293383388/)                              | Feb 10, 16:09      |
|       790    |            65 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/toplage%21-sonnige-2-zimmer-neubauwohnung-1538694809/)                                                                  | Feb 10, 15:57      |
|       799.98 |            52 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/nachmieter-f%C3%BCr-meine-mietwohnung-gesucht-/-rosa-jochmann-ring-16-1345788815/)                                    | Feb 10, 15:44      |
|       738    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/renovierte-wohnung-1556167138/)                                                                                        | Feb 10, 14:20      |
|       479    |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zur-direktvergabe-nur-mit-wohnticket-bis-30.06.2024-2021589746/)                                | Feb 10, 14:15      |
|       733.7  |            50 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/suche-nachmieter-f%C3%BCr-50m%C2%B2-wohnung-/-looking-for-tenant-50m%C2%B2-apartment-1729746100/)                    | Feb 10, 13:18      |
|       690    |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweier-wg-oder-f%C3%BCr-ein-p%C3%A4rchen-1385455763/)                                                                 | Feb 10, 12:51      |
|       779    |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/11.braunhubergasse-unbefristete-provisionsfreie-2-zimmer-altbaumiete-in-u3-n%C3%A4he-801910236/)                      | Feb 10, 12:32      |
|       784.38 |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/hollergasse---2-zimmer-erdgeschosswohnung-1602693186/)                                                | Feb 10, 09:15      |
|       730.09 |            53 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/charmante-altbauwohnung-direkt-beim-augarten-zur-unbefristeten-vermietung.-2123519583/)                            | Feb 10, 07:38      |
