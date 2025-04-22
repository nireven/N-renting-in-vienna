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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       715    |            67 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/komfortable-2--zimmer--altbauwohnung-%7C-befristet-%7C-ab-sofort-1967881003/)                                    | Apr 22, 16:56      |
|       799    |            67 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/360-tour-/-gro%C3%9Fz%C3%BCgige-2-zimmer-altbauwohnung-in-guter-lage-des-10.-bezirks-804705394/)                 | Apr 22, 16:47      |
|       795    |            39 |          2 | 07. Neubau    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/ruhige-2-zimmer-wohnung-mit-eigengarten-2119393669/)                                                                | Apr 22, 15:57      |
|       770    |            46 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ihr-neuer-lieblingsort:-viola-park---2-zimmer-wohnung-mit-gem%C3%BCtlichem-balkon-%7C-am-laaer-berg-1333439140/) | Apr 22, 13:56      |
|       799.86 |            41 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/modernes-wohnen-im-erstbezug---frisch-sanierte-wohnung-mit-hochwertiger-ausstattung---jetzt-anfragen-1366664417/)  | Apr 22, 13:48      |
|       785.01 |            48 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---2-zimmer-balkonwohnung---ihr-zuhause-mit-direkter-u1-anbindung-%7Cam-laaer-berg-1139947170/)        | Apr 22, 11:59      |
|       790    |            64 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-2-zimmer-wohnung-n%C3%A4he-thaliastr.-unbefristet%21-790409516/)                                      | Apr 22, 11:52      |
|       690    |            60 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-wohnung-in-ottakring-788620535/)                                                                  | Apr 22, 10:46      |
|       750    |            53 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmerwohnung-im-10.-bezirk%21%21-360%C2%B0--3d-grad-besichtigung-1045577323/)               | Apr 22, 07:34      |
|       790    |            40 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei---2-zimmer-apartment-mit-toller-anbindung-976837166/)                                             | Apr 21, 17:13      |
