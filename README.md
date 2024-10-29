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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       461    |            51 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/u-6-n%C3%A4he-topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-1957819797/)                                                              | Oct 29, 12:40      |
|       473.09 |            64 |          3 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug%21-/-vormerkschein-bis-30.09.2024-/-n%C3%A4chste-sammelbesichtigung-am-10.11.24-von-14-bis-17h-%21%21-1551815967/) | Oct 29, 12:33      |
|       749.93 |            45 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/orea-%7C-sch%C3%B6ne-2-zimmer-wohnung-nahe-u1-keplerplatz-%7C-smart-besichtigen-%C2%B7-online-anmieten-1898525995/)                                                   | Oct 29, 12:26      |
|       799.84 |            46 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/orea-%7C-helle-2-zimmer-wohnung-mit-guter-%C3%B6ffentlicher-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-1282757982/)                                       | Oct 29, 12:26      |
|       740    |            75 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/hauptmiethit-n%C3%A4he-enkplatz-1236225938/)                                                                                                                          | Oct 29, 11:57      |
|       730    |            78 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gartenseitige-eg-wohnung-mit-1-schlafzimmer.-teilm%C3%B6bliert-mit-k%C3%BCchenutensilien-auch-f%C3%BCr-%C3%BCbergangsl%C3%B6sung-geeignet.-1553418773/)                 | Oct 29, 11:40      |
|       749    |            46 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ruhige-25-zimmerwohnung-in-guter-lage-%7C-zellmann-immobilien-1178243261/)                                                                                              | Oct 29, 11:37      |
|       477.4  |            32 |          2 | 06. Mariahilf   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/top-pendlerwohnung-in-biedermeierhaus-bei-mariahilferstra%C3%9Fe-2050175027/)                                                                                         | Oct 29, 10:16      |
|       726.94 |            38 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/living-in-%E2%80%9823---mietkauf-1687798252/)                                                                                                                           | Oct 29, 10:06      |
|       779.3  |            52 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/renovierte-2-zimmer-wohnung-im-dachgescho%C3%9F-1780082573/)                                                                                                        | Oct 29, 09:49      |
|       790    |            44 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohntraum-mit-balkon-im-viola-park-896639808/)                                                                                                               | Oct 29, 09:47      |
|       590    |            57 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-1210-wien-%28ruthnergasse%29-2-zimmer---vormerkschein-stichtag-31.10.2024-1805903422/)                                                              | Oct 29, 09:24      |
|       725    |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-im-10.bezirk---renovierter-altbau---gute-anbindung-und-infrastruktur-1894245947/)                                                                    | Oct 29, 09:17      |
|       680    |            44 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/privat%21-2-zimmerwohnung-zu-vermieten-1865971676/)                                                                                                                   | Oct 29, 09:16      |
|       750    |            56 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ruhige-mietwohnung-schloss-neugeb%C3%A4ude-barrierefrei-unm%C3%B6bliert-1769667348/)                                                                                  | Oct 29, 08:39      |
|       457    |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-vormerkschein-vor-30.09.2024-1195305098/)                                                                                               | Oct 29, 07:38      |
|       699    |            47 |          2 | 06. Mariahilf   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/1060-wien-hornbostelgasse-2-zimmer-k%C3%BCche-duschbad-ruhelage-1.-stock-ohne-lift-864706857/)                                                                        | Oct 29, 07:35      |
|       798.91 |            60 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/ger%C3%A4umige-2-zimmer--wohnung-1530891048/)                                                                                                                           | Oct 29, 06:52      |
|       782    |            43 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/tolle-2-zimmer-wohnung-in-absoluter-ruhelage-mit-sch%C3%B6nem-balkon-1191538653/)                                                                                       | Oct 29, 03:21      |
|       420.46 |            42 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeinde-wohnung-vmd-31102024-1423456187/)                                                                                                                              | Oct 28, 21:52      |
