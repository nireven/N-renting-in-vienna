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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       690    |            82 |          3 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnung-mit-direkt-vergabe-vms-08.03.2024-1559971839/)                                                                                                                     | Jan 28, 19:31      |
|       787.92 |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m%C2%B2-zum-mietpreis-von-78792-eur%21-1580236359/)                                                                           | Jan 28, 18:35      |
|       745.36 |            64 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/stilvolle-altbauwohnung-in-zentraler-lage---h%C3%BCtteldorfer-stra%C3%9Fe-113a-1140-wien-1388329135/)                                                                          | Jan 28, 17:22      |
|       759.5  |            63 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charmante-altbauwohnung-in-zentraler-lage---goldschlagstra%C3%9Fe-110-1150-wien-1807809785/)                                                                 | Jan 28, 16:52      |
|       745.38 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gem%C3%BCtliche-2-zimmer-wohnung-1978898807/)                                                                                                                                | Jan 28, 16:36      |
|       730    |            71 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-direktvergabe-967536679/)                                                                                                                                   | Jan 28, 16:30      |
|       749    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/perfekt-angelegte-2-zimmer-wohnung-hell-und-freundlich-150m-zur-u3-sackgasse-1269416129/)                                                                                    | Jan 28, 15:27      |
|       761    |            38 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/2-zimmerwohnung-mit-balkon-provisionsfrei-2113576897/)                                                                                                                    | Jan 28, 14:17      |
|       799    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-und-kellerabteil-bei-u1-neulaa-/hs17-a-14-825042242/)                                                                 | Jan 28, 14:00      |
|       739    |            42 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---attraktive-neubauwohnung-mit-sch%C3%B6nem-nordseitigen-balkon---bezug-ab-m%C3%A4rz-2025-1633481574/)                                                           | Jan 28, 13:57      |
|       461.59 |            47 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/2-zimmer-gemeindewohnung-wohnticket-vorm-31.01.2025-1647826322/)                                                                                                           | Jan 28, 12:59      |
|       760    |            57 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-und-helle-2-zimmer-wohnung-1407609179/)                                                                                                                           | Jan 28, 12:57      |
|       790    |            46 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/wundersch%C3%B6ne-gepflegte-2-zimmer-mit-grossem-balkon%21-789859620/)                                                                                                         | Jan 28, 11:23      |
|       799    |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertiger-neubau-zu-fairen-preisen---gut-angebunden-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche-&-freifl%C3%A4che-1255186415/) | Jan 28, 09:27      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-981921692/)                                                          | Jan 28, 09:00      |
|       729.21 |            33 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/exklusives-wohnen-in-stadlau---erzherzog-karl-stra%C3%9Fe-bahnhof-und-u2-stadlau-in-wenigen-gehminuten.---wohntraum-2131488813/)                                            | Jan 28, 06:55      |
|       582.16 |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-sanierte-2-zimmer-wohnung-im-dg%21-978184730/)                                                                                                                           | Jan 28, 02:45      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/neu-am-markt:-2-zimmer-wohnung-im-niedrigenergiehaus-%7C-balkon-fu%C3%9Fbodenheizung-kellerabteil-u2-1749536592/)                                                           | Jan 28, 02:19      |
|       791.03 |            85 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung-im-sanierten-altbau-mit-balkon-zu-vermieten---unbefristet-1167305728/)                                                                          | Jan 27, 21:26      |
|       570    |            43 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/2-zimmer-wohnung---43-m%C2%B2---unbefristet---direkt-vom-eigent%C3%BCmer-1544132850/)                                                                                      | Jan 27, 21:04      |
