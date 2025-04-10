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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       775    |            75 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/1150-wien-fenzlgasse-n%C3%A4he-u-3-johnstra%C3%9Fe:-3-zimmer-altbauwohnung-ca.-75-m2-unbefristet-zu-vermieten-1025318157/) | Apr 10, 00:32      |
|       595    |            78 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeindewohnung---direktvergabe-f%C3%BCr-3-zimmer-und-vormerkscheindatum-bis-30.11.2024-1215790850/)                       | Apr 09, 21:20      |
|       530    |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/singlewohnung-39-m2-nahe-altes-landgut-1177851985/)                                                                                        | Apr 09, 20:04      |
|       474.63 |            46 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-gemeindewohnung-mit-balkon-in-absoluter-ruhelage---direktvergabe%21-1012930591/)                                            | Apr 09, 17:24      |
|       577.94 |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/altbauwohnung-in-der-johnstrasse-n%C3%A4he-u-3-1063019568/)                                                                | Apr 09, 16:27      |
|       750    |            60 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/komplett-eingerichtete-2-zimmer-wohnung-1469097368/)                                                                                       | Apr 09, 15:08      |
|       700    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmer-neubauwohnung-mit-balkon-im-10.-bezirk---himberger-stra%C3%9Fe-2012205612/)                                               | Apr 09, 14:19      |
|       789    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/orea-%7C-charmante-2-zimmer-wohnung-nahe-u6-%7C-smart-besichtigen-%C2%B7-online-anmieten-1765217068/)                                      | Apr 09, 13:26      |
|       791    |            55 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/g%C3%BCnstige-lage-n%C3%A4he-u3-h%C3%BCtteldorfer-stra%C3%9Fe-1019597990/)                                                                   | Apr 09, 12:42      |
|       723.39 |            53 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/zu-vermieten:-53-m%C2%B2-wohnung-in-der-ruckergasse-49-1120-wien%28offene-besichtigung-am-07.04.2025-um-15:00%29-1088571213/)               | Apr 09, 12:42      |
|       745    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Aprovisionsfrei%2A-sch%C3%B6negeflegte-2-zimmer-wohnung---ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-871791214/)                           | Apr 09, 12:34      |
|       785    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.08.2025-verf%C3%BCgbar%21-1879327887/)                     | Apr 09, 11:48      |
|       780    |            33 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/privat-:-wundersch%C3%B6ne-ruhige-neubau-wohnung-mit-balkon-2-zimmer-1162038703/)                                                           | Apr 09, 10:36      |
