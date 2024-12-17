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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       749.98 |            44 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmerwohnung-altbau-frisch-saniert-44m%C2%B2-3.og-in-1150-zu-mieten-1492433546/)                 | Dec 17, 17:23      |
|       599    |            57 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/liebe-mietwohnung-in-der-frauengasse---4.-stock-ohne-lift-1645066402/)                                                | Dec 17, 17:23      |
|       680    |            87 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-wien-1685544825/)                                                                                   | Dec 17, 17:18      |
|       655.29 |            47 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zentrale-helle-2-zimmer-altbauwohnung-im-3.-1633115909/)                                                      | Dec 17, 17:09      |
|       799    |            62 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sonnige--bezugsfertige-2-zimmer-balkonmietegr%C3%BCnruhelage-1364548937/)                                           | Dec 17, 16:54      |
|       672.17 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/cityapartment-in-grandioser-lage%21-1766907319/)                                                                   | Dec 17, 16:54      |
|       782.41 |            39 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/modernes-wohnen-mit-freifl%C3%A4che-und-top-infrastruktur-in-1200-wien-1961756432/)                               | Dec 17, 16:27      |
|       746.4  |            57 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-altbauwohnung-mit-separater-k%C3%BCche-in-der-n%C3%A4he-des-hanusch-krankenhaus-2143966328/)                 | Dec 17, 16:27      |
|       749.98 |            44 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/neu%21-erstbezug%21-ideale-2-zimmerwohnung-im-nibelungenviertel-zu-vermieten%21-1595490809/)        | Dec 17, 16:23      |
|       629.69 |            55 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-n%C3%A4he-u1-leopoldau-%28-2-zimmer%29-868751589/)                                                | Dec 17, 16:21      |
|       799    |            44 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-k3-30-1966364826/) | Dec 17, 16:08      |
|       605    |            54 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/h%C3%BCbsche-sonnige-dg-wohnung-1726247545/)                                                                       | Dec 17, 15:54      |
|       459    |            46 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/2-zimmer-gemeindewohnung-vms-bis-30.11.2024-1436769857/)                                                           | Dec 17, 15:54      |
|       490    |            47 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-2-zimmer-1089812142/)                                                                               | Dec 17, 15:43      |
|       540    |            49 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohunung-im-5.-bezirk-1754240012/)                                                                         | Dec 17, 13:30      |
|       570    |            58 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gut-geschnittene-2-zimmer-wohnung-%28direktvergabe%29-928739665/)                                                   | Dec 17, 13:21      |
|       595    |            52 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sonniger-altbau-nahe-u6-dresdnerstra%C3%9Fe-1109947926/)                                                          | Dec 17, 11:59      |
|       795    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---gem%C3%BCtliche-2-zimmer-wohnung-mit-balkon---ihr-neues-zuhause-wartet%21-am-laaer-berg-1843229963/)   | Dec 17, 11:39      |
|       464.02 |            55 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ruhige-2-zimmer-gemeindewohnung-mit-loggia-1014829857/)                                                              | Dec 17, 11:09      |
|       730.01 |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-wohnung-n%C3%A4he-u4%21-1349280013/)                                                                         | Dec 17, 09:53      |
