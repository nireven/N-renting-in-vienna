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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       650    |            62 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-altbauwohnung-2140700600/)                                                                                                                                             | Feb 22, 11:29      |
|       556    |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-gemeinde-wohnung-%21-1461420898/)                                                                                                                                 | Feb 22, 10:07      |
|       680.43 |            75 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/befristete-m%C3%B6blierte-2-zimmerwohnung-in-der-hauffgasse-1524360684/)                                                                                                        | Feb 22, 09:45      |
|       749.27 |            40 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zimmerwohnung---zu-mieten%21-besichtigung-21.2.25-1528837476/)                                                                                                               | Feb 21, 20:32      |
|       601.85 |            74 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-direktvergabe-mit-wohnticket---3-zimmerwohnung-mit-k%C3%BCche-%2874-m%C2%B2-wohnfl%C3%A4che-%2B-8-m%C2%B2-balkon%29-845589635/)                              | Feb 21, 20:15      |
|       704.69 |            62 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%2A%2A%2A-unbefristete-2-zimmer-altbauwohnung-/-n%C3%A4he-bezirksvorstehung-penzing-776282708/)                                                                                   | Feb 21, 19:05      |
|       729.98 |            53 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-sch%C3%B6ne-2-zimmer-wohnung-mit-balkon%21-2011185545/)                                                                                                                    | Feb 21, 18:49      |
|       603    |            55 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/1090:-55m%C2%B2-altbau-befr.-603---%3B-hwb-1552-489782661/)                                                                                                                    | Feb 21, 17:22      |
|       799    |            38 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---wohnen-am-erlachpark---6ter-liftstock---garagenplatz-inklusive-1331806037/)                                                                                         | Feb 21, 16:46      |
|       739.18 |            53 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/n%C3%A4he-hanuschkrankenhaus:-gem%C3%BCtliche-2-zimmer--altbauwohnung-befristet-854143881/)                                                                                       | Feb 21, 16:36      |
|       740.51 |            71 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-charmante-altbauwohnung-im-16.-wiener-bezirk-1494292241/)                                                                                                      | Feb 21, 14:27      |
|       619    |            57 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe-vmd-bis-30.11.2024-1146780432/)                                                                                                                  | Feb 21, 12:35      |
|       780    |            71 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hofseitige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen%2A%2A%2Aunbefristet%2A%2A%2A-1781169223/)                                                                                 | Feb 21, 11:58      |
|       774.93 |            41 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neubau-wohnung-inkl.-praktischer-k%C3%BCche-mit-dem-vorteil-ausgew%C3%A4hlter-nachbarschaft%21-einzigartige-wohnatmosph%C3%A4re-dank-balkon-und-1a-infrastruktur%21-1590344910/) | Feb 21, 11:29      |
