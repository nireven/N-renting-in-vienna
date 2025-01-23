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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       790    |            36 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/top-aussicht-city-appartement-1757399551/)                                                                                        | Jan 23, 08:39      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1881694930/)            | Jan 23, 07:45      |
|       733.77 |            42 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                                     | Jan 23, 06:48      |
|       560    |            53 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-in-direktvergabe-971791515/)                                                                                  | Jan 23, 06:34      |
|       445    |            42 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/perfekte-single--oder-p%C3%A4rchenwohnung---42-m%C2%B2-f%C3%BCr-nur-445-%E2%82%AC-inkl.-betriebskosten%21-821077138/)         | Jan 22, 21:45      |
|       550.17 |            37 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei:-ruhiger-37m%C2%B2-altbau-mit-2-zimmern-n%C3%A4he-vogelweidpark---1150-wien-1017620748/)         | Jan 22, 21:35      |
|       650    |            47 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-2-zimmerwohnung-in-fu%C3%9Fg%C3%A4ngerzone-2085540447/)                                                     | Jan 22, 21:20      |
|       725    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-im-10.bezirk---renovierter-altbau---gute-anbindung-und-infrastruktur-2030148768/)                              | Jan 22, 20:41      |
|       780    |            81 |          3 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeinde-wohnung-1144614472/)                                                                                                     | Jan 22, 19:51      |
|       798.79 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/komfortabler-erstbezug:-2-zimmer-wohnungen-im-21.-bezirk-mit-balkon-und-moderner-k%C3%BCche.---wohntraum-1104579405/)         | Jan 22, 18:57      |
|       765    |            44 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1649059268/)                                                      | Jan 22, 18:07      |
|       799.03 |            37 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/provisionsfrei---2-zimmer-wohnung-mit-tiefgargenplatz-1287857440/)                                                             | Jan 22, 16:55      |
|       790    |            44 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/sanierte-ruhige-altbauwohnung-mit-erker-und-kompletter-k%C3%BCche-in-sackgasse-direkt-im-zentrum-gersthof-831788780/)        | Jan 22, 16:43      |
|       475    |            48 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/direktvergabe-gemeindewohnung-1709341730/)                                                                      | Jan 22, 16:18      |
|       737.01 |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/orea-%7C-sch%C3%B6ne-2-zimmer-wohnung-nahe-u1-keplerplatz-%7C-smart-besichtigen-%C2%B7-online-anmieten-2139772733/)             | Jan 22, 15:18      |
|       799.99 |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-%7C-u3-ottakring-%7C-garagenplatz-verf%C3%BCgbar-1041913329/)                                                          | Jan 22, 14:48      |
|       780    |            50 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sch%C3%B6ne-und-ruhige-neubauwohnung-973746485/)                                                                               | Jan 22, 14:29      |
|       717.61 |            48 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-balkonwohnung-mit-neuer-k%C3%BCche-1792040415/)                                                                        | Jan 22, 14:27      |
|       788.56 |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertige-neubauwohnungen-mit-anbindung-zu-u6-s-bahn-und-u1-in-leopoldau-mit-inkludierter-k%C3%BCche-1058670682/) | Jan 22, 14:17      |
|       595    |            32 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei---sch%C3%B6ne-2-zimmer-wohnung-ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-2109286336/)                             | Jan 22, 14:03      |
