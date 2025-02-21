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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       740.51 |            71 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-altbauwohnung-im-16.-wiener-bezirk-1494292241/)                                                                                                                               | Feb 21, 14:27      |
|       619    |            57 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe-vmd-bis-30.11.2024-1146780432/)                                                                                                                          | Feb 21, 12:35      |
|       758.42 |            57 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug-sch%C3%B6ne-3-zimmerwohnung-quellenstrasse-1713097205/)                                                                                                                       | Feb 21, 12:17      |
|       780    |            71 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hofseitige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen%2A%2A%2Aunbefristet%2A%2A%2A-1781169223/)                                                                                         | Feb 21, 11:58      |
|       774.93 |            41 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neubau-wohnung-inkl.-praktischer-k%C3%BCche-mit-dem-vorteil-ausgew%C3%A4hlter-nachbarschaft%21-einzigartige-wohnatmosph%C3%A4re-dank-balkon-und-1a-infrastruktur%21-1590344910/)         | Feb 21, 11:29      |
|       799.79 |            44 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-und-sch%C3%B6ne-2-zimmer-wohnung-in-der-r%C3%B6mergasse%21-1971283728/)                                                                                                      | Feb 21, 11:29      |
|       699.94 |            45 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-2-zimmer-wohnung-in-hernals-1771799327/)                                                                                                                                      | Feb 21, 08:44      |
|       727.27 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/11.hugogasse---unbefristete-provisionsfreie-2-zimmer-neubaumiete-in-u3-n%C3%A4he-1327292696/)                                                                                           | Feb 21, 07:52      |
|       432    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen-ticket-31.12.2024-1147334553/)                                                                                                                              | Feb 21, 07:38      |
|       748.38 |            65 |          3 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristete-ger%C3%A4umige-3-zimmer-wohnung-in-hetzendorf---gr%C3%BCn-und-ruhig-1147594750/)                                                                                            | Feb 21, 02:44      |
|       500    |            45 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%21%21-bitte-beschreibungstext-vor-anfrage-vollst%C3%A4ndig-lesen%21%21-unbefristete-renovierte-teilm%C3%B6blierte-altbau--mietwohnung-mit-freifl%C3%A4che---vorschlagerecht-2017798161/) | Feb 20, 19:33      |
|       705    |            60 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-wohnung-nordbahnviertel-2089712964/)                                                                                                                                        | Feb 20, 18:27      |
|       513    |            47 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/direktvergabe-gemeindewohnung-1850071438/)                                                                                                                                                 | Feb 20, 18:02      |
|       754.5  |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Am%C3%B6blierte%2A-2-zimmer-mietwohnung-mit-terrasse-im-1.-dachgeschoss-%28=-5.-stock%29-806312230/)                                                                                  | Feb 20, 16:26      |
|       799    |            40 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wundersch%C3%B6ne-2-zimmer-neubauwohnung-mit-terrasse-n%C3%A4he-hernalser-hauptstra%C3%9Fe-1902613117/)                                                                                   | Feb 20, 16:26      |
|       595    |            41 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aprovisionsfrei%2A-gepflegte-2-zimmer-wohnung-ideal-f%C3%BCr-singles-oder-studenten-1412179388/)                                                                                       | Feb 20, 15:21      |
