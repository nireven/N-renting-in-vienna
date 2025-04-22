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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            50 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/altbauwohnung-im-3.-liftstock-nahe-prater/praterstern/messe-wien-1895554376/)                                 | Apr 22, 15:08      |
|       770    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ihr-neuer-lieblingsort:-viola-park---2-zimmer-wohnung-mit-gem%C3%BCtlichem-balkon-%7C-am-laaer-berg-1333439140/) | Apr 22, 13:56      |
|       730.57 |            65 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gro%C3%9Fz%C3%BCgig-geschnittene-2-zimmerwohnung-n%C3%A4he-sch%C3%B6nbrunn-819426561/)           | Apr 22, 13:54      |
|       799.86 |            41 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/modernes-wohnen-im-erstbezug---frisch-sanierte-wohnung-mit-hochwertiger-ausstattung---jetzt-anfragen-1366664417/)  | Apr 22, 13:48      |
|       785.01 |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---2-zimmer-balkonwohnung---ihr-zuhause-mit-direkter-u1-anbindung-%7Cam-laaer-berg-1139947170/)        | Apr 22, 11:59      |
|       790    |            64 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/attraktive-2-zimmer-wohnung-n%C3%A4he-thaliastr.-unbefristet%21-790409516/)                                      | Apr 22, 11:52      |
|       690    |            60 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-wohnung-in-ottakring-788620535/)                                                                  | Apr 22, 10:46      |
|       748    |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmerwohnung-im-2.og-mit-loggia-1221595165/)                                                                  | Apr 22, 07:38      |
|       750    |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmerwohnung-im-10.-bezirk%21%21-360%C2%B0--3d-grad-besichtigung-1045577323/)               | Apr 22, 07:34      |
|       790    |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei---2-zimmer-apartment-mit-toller-anbindung-976837166/)                                             | Apr 21, 17:13      |
|       680    |            45 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/charmante-helle-2-zimmer-wohnung-mit-wohlf%C3%BChlbad-und-einbauk%C3%BCche-1644504246/)                       | Apr 21, 14:25      |
|       792.32 |            66 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-hauptmiete-unbefristet-2031684765/)                                                       | Apr 21, 14:01      |
