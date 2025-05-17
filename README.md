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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            52 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-altbauwohnung-zum-wohlf%C3%BChlen-1859859425/)                                             | May 17, 18:38      |
|       771.81 |            32 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-mit-wohlf%C3%BChlfaktor---topmoderne-mietwohnung-nahe-u6-&-s-bahn-1215454318/)          | May 17, 13:18      |
|       695.01 |            46 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/exklusive-hoflage%21-868058652/)                                                                 | May 17, 12:14      |
|       750    |            60 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-mietwohnung-in-top-lage-n%C3%A4he-bahnhof-meidling-1801432978/)                  | May 17, 11:05      |
|       690    |            66 |          3 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/attraktive-3-zimmer-gemeindewohnung-mit-loggia-in-1040-wien---n%C3%A4he-hauptbahnhof---1531714974/) | May 17, 09:31      |
|       719    |            38 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gellertgasse-20---erstbezug-und-wohnkomfort-beim-gellertplatz-1152954668/)                       | May 17, 04:50      |
|       689    |            40 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gellertgasse-20---erstbezug-und-wohnkomfort-beim-gellertplatz-1928854301/)                       | May 17, 04:50      |
|       759    |            40 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gellertgasse-20---erstbezug-und-wohnkomfort-beim-gellertplatz-1932551211/)                       | May 17, 04:50      |
|       759    |            40 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gellertgasse-20---erstbezug-und-wohnkomfort-beim-gellertplatz-949871284/)                        | May 17, 04:50      |
|       749    |            40 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gellertgasse-20---erstbezug-und-wohnkomfort-beim-gellertplatz-1922224827/)                       | May 17, 04:50      |
|       779    |            40 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gellertgasse-20---erstbezug-und-wohnkomfort-beim-gellertplatz-1647669353/)                       | May 17, 04:50      |
|       659    |            38 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gellertgasse-20---erstbezug-und-wohnkomfort-beim-gellertplatz-1531771612/)                       | May 17, 04:50      |
|       740    |            70 |          3 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeinde-wohnung-direktvergabe-1922505462/)                                                     | May 16, 21:19      |
|       774.8  |            60 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/am-kanal-73a-/-top-a073-1065124034/)                                                             | May 16, 18:43      |
|       728.34 |            56 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/herbortgasse-28-/-top-h085-1330591623/)                                                          | May 16, 18:43      |
