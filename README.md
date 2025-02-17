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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       645.18 |            41 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/balkonwohnung-unbefristet-und-ruhig-gelegen-1748078208/)                                                                                                  | Feb 17, 16:52      |
|       748.91 |            37 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/the-arrow---willkommen-im-gr%C3%BCnen-teil-simmerings-974631888/)                                                                                        | Feb 17, 16:49      |
|       763.4  |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ausschlie%C3%9Flich-schriftliche-anfragen-bitte-keine-anrufe%21-unbefristet.-tolle--helle-2-zimmer-terrassen--wohnung-in-der-karmarschgasse-1236515767/) | Feb 17, 16:27      |
|       728    |            61 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gut-geschnittene-wohnung-in-guter-lage-932927905/)                                                                                                       | Feb 17, 13:49      |
|       799.79 |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-886056076/)                                                                        | Feb 17, 13:28      |
|       740    |            46 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/bitte-ausschlie%C3%9Flich-schriftliche-anfragen%21%21-gem%C3%BCtliche-hofseitig-gelegene-2-zimmer-wohnung-in-der-strohmayergasse-994244171/)             | Feb 17, 13:14      |
|       725    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gr%C3%BCnruhelage---unbefristete-altbaumiete-in-sch%C3%B6nem-eckzinshaus-%21-1203845465/)                                                                 | Feb 17, 13:08      |
|       636    |            56 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-mit-vormerkschein-bis-30.06.2024-1432576054/)                                                                                            | Feb 17, 07:46      |
|       579    |            54 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-direktvergabe-1219733109/)                                                                                                                | Feb 16, 22:37      |
|       790.65 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-huma-eleven---wohnung-perfekt-f%C3%BCr-p%C3%A4rchen-geeignet-mit-balkon-1309031000/)                                                           | Feb 16, 21:37      |
|       647.9  |            62 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/helle-charmante-62m%C2%B2-2-zimmerwohnung-direktvergabe-u1-vorgartenstra%C3%9Fe-ab-sofort%21-1067291073/)                                             | Feb 16, 19:37      |
|       790    |            30 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/huglgasse:-sanierte-3-zimmer-wohnung-in-u-bahn-n%C3%A4he-937057262/)                                                                     | Feb 16, 17:25      |
