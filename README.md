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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       433.18 |            39 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/direktvergabe-gemeindewohnung--nur-mit-wiener-wohn-ticket-1205437738/)                                                                                               | Oct 29, 18:44      |
|       680    |            34 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/smarte-zwei-zimmerwohnung-in-penzing-mit-balkon-1560025533/)                                                                                                            | Oct 29, 18:25      |
|       540    |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-mit-direktvergabe-2115627502/)                                                                                                                                | Oct 29, 18:07      |
|       779    |            44 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/moderne-2-zimmer-wohnung-in-donaun%C3%A4he-831020847/)                                                                                                              | Oct 29, 14:57      |
|       570    |            55 |          3 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/helle-&-renovierte-3-zimmer-gemeinde-wohnung-weiterzugeben-1159566384/)                                                                                            | Oct 29, 14:26      |
|       765.37 |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/tolle-2-zimmer-wohnung-mit-idealer-raumaufteilung-in-guter-und-infrastrukturell-ansprechender-lage%21-1791769254/)                                                  | Oct 29, 14:18      |
|       795    |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wundersch%C3%B6ne-2-zimmer-wohnung-mit-terrasse-1939918169/)                                                                                          | Oct 29, 13:51      |
|       798.88 |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend-living%21-inklusive-k%C3%BCche%21-erstbezug%21-elektrische-raffstores%21-klima-vorb.%21-n%C3%A4he-u1.---wohntraum-774645004/)                                | Oct 29, 13:49      |
|       461    |            51 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/u-6-n%C3%A4he-topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-1957819797/)                                                              | Oct 29, 12:40      |
|       473.09 |            64 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug%21-/-vormerkschein-bis-30.09.2024-/-n%C3%A4chste-sammelbesichtigung-am-10.11.24-von-14-bis-17h-%21%21-1551815967/) | Oct 29, 12:33      |
|       749.93 |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/orea-%7C-sch%C3%B6ne-2-zimmer-wohnung-nahe-u1-keplerplatz-%7C-smart-besichtigen-%C2%B7-online-anmieten-1898525995/)                                                   | Oct 29, 12:26      |
|       799.84 |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/orea-%7C-helle-2-zimmer-wohnung-mit-guter-%C3%B6ffentlicher-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-1282757982/)                                       | Oct 29, 12:26      |
|       740    |            75 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/hauptmiethit-n%C3%A4he-enkplatz-1236225938/)                                                                                                                          | Oct 29, 11:57      |
|       730    |            78 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gartenseitige-eg-wohnung-mit-1-schlafzimmer.-teilm%C3%B6bliert-mit-k%C3%BCchenutensilien-auch-f%C3%BCr-%C3%BCbergangsl%C3%B6sung-geeignet.-1553418773/)                 | Oct 29, 11:40      |
|       749    |            46 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ruhige-25-zimmerwohnung-in-guter-lage-%7C-zellmann-immobilien-1178243261/)                                                                                              | Oct 29, 11:37      |
|       477.4  |            32 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/top-pendlerwohnung-in-biedermeierhaus-bei-mariahilferstra%C3%9Fe-2050175027/)                                                                                         | Oct 29, 10:16      |
|       726.94 |            38 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/living-in-%E2%80%9823---mietkauf-1687798252/)                                                                                                                           | Oct 29, 10:06      |
|       779.3  |            52 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/renovierte-2-zimmer-wohnung-im-dachgescho%C3%9F-1780082573/)                                                                                                        | Oct 29, 09:49      |
|       790    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohntraum-mit-balkon-im-viola-park-896639808/)                                                                                                               | Oct 29, 09:47      |
|       590    |            57 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-1210-wien-%28ruthnergasse%29-2-zimmer---vormerkschein-stichtag-31.10.2024-1805903422/)                                                              | Oct 29, 09:24      |
