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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       585    |            40 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/rosaliagasse---charmante-2-zi-altbauwohnung-in-1120-wien-2049720524/)                                                                                                | Feb 04, 11:58      |
|       781.81 |            54 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-altbau-mit-guter-anbindung-1942641153/)                                                                                                                     | Feb 04, 11:58      |
|       584.17 |            48 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristet---entz%C3%BCckende-neu-sanierte-altbauwohnung%21-anfragen-nur-per-mail%21-1410913037/)                                                                  | Feb 04, 11:51      |
|       799    |            44 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-und-kellerabteil-/-hs17-a-16-1693967151/)                                                                    | Feb 04, 10:54      |
|       727    |            64 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/hauptmietwohnung-mit-balkon-2062797517/)                                                                                                                              | Feb 04, 09:57      |
|       708.41 |            59 |          3 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/grabnergasse-8-besichtigung-am-5.2.-von-10.30-bis-11-uhr-1029025859/)                                                                                               | Feb 04, 09:36      |
|       599    |            47 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/maroltingergasse-61-besichtigung-am-05.02.-von-9---9.30-uhr-1187813468/)                                                                                            | Feb 04, 09:36      |
|       708.96 |            51 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-sanierte-2-zimmer-wohnung-im-1.og.-835884494/)                                                                                                                  | Feb 04, 02:55      |
|       746.01 |            48 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/unbefristete-2-zimmer-wohnung-in-1020-wien-n%C3%A4chst-urania-in-unmittelbarer-n%C3%A4he-des-donaukanals-und-ca.-3-gehminuten-vom-1.-bezirk-entfernt-921981730/) | Feb 03, 18:57      |
|       700.7  |            49 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%22charmanter-altbau-traum:-helle-hohe-r%C3%A4ume-mit-stil%22-1646223139/)                                                                                          | Feb 03, 17:08      |
|       431.56 |            39 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-provisionsfrei-%7C-gem%C3%BCtliche-helle-2-zimmer-wohnung-%7C-n%C3%A4he-u3-%7C-m%C3%B6bel-auf-anfrage-1818318006/)                                 | Feb 03, 15:44      |
|       480    |            55 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gemeindewohnung-im-6.-bezirk---millergasse---direktvergabe-1920920882/)                                                                                             | Feb 03, 15:15      |
|       460    |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-zu-vergeben-1100-wien-1435384049/)                                                                                                                 | Feb 03, 13:03      |
|       650    |            57 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-in-1030-wien---57-m%C2%B2-im-1.-liftstock-1385945099/)                                                                                       | Feb 03, 12:22      |
|       799    |            70 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-wohnung-in-u3-n%C3%A4he-zu-mieten-in-1110-wien-1371652053/)                                                                                                | Feb 03, 11:29      |
