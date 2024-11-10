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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       645    |            49 |          2 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/kleine-wohnung-in-1130-wien-1492229474/)                                                                                     | Nov 10, 08:04      |
|       680    |            64 |          3 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/gemeinde-wohnung-direktvergabe-vormerkschein-31.10.2024-1866807470/)                                                         | Nov 09, 22:37      |
|       780    |            48 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/neuwertige-2-zimmerwohnung/-klimatisiert/-gute-lage-im-22.-bezirk-1451008645/)                                             | Nov 09, 20:39      |
|       799.24 |            58 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-58m%C2%B2-altbau-mit-lift-beim-humboldtplatz---1100-wien-2060419785/)                         | Nov 09, 16:34      |
|       530    |            50 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-12.-bezirk-%28vmd-31.10.2024%29-1731146026/)                                                                 | Nov 09, 13:55      |
|       779    |            38 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/singelhit-/-p%C3%A4rchenhit-in-neubau-provsionsfrei-1676811835/)                                                            | Nov 09, 12:24      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---2-zimmer-und-balkon---wohnen-mit-komfort-und-ausblick---ihre-wohlf%C3%BChloase-am-laaer-berg-1233725437/)      | Nov 09, 11:28      |
|       760    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---zwei-zimmer-ein-balkon---wohnen-in-perfekter-balance---ihre-wohlf%C3%BChloase-am-laaer-berg-1019099001/)       | Nov 09, 11:28      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hochwertige-2-zimmer-wohnung-mit-balkon-und-wohlf%C3%BChlatmosph%C3%A4re---viola-park---am-laaer-berg-1094558488/)          | Nov 09, 11:28      |
|       790    |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg--gem%C3%BCtliche-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1488914495/) | Nov 09, 11:28      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg---leben-mit-aussicht:-2-zimmer-wohnung-mit-balkon-1168697587/)            | Nov 09, 11:28      |
|       759.04 |            62 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/nur-sozialbau-mieter---2-zimmer-wohnung-im-aufstrebenden-nordbahnviertel-1238777386/)                                    | Nov 09, 10:49      |
|       685    |            42 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%28reserviert%29-helle-2-zimmer-wohnung-in-der-seestadt---5-minuten-zur-u2-1255093104/)                                    | Nov 09, 10:02      |
|       460    |            45 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%21%21-gemeindewohnung-2-zimmer-direktvergabe-%21%21-972301523/)                                                            | Nov 09, 09:18      |
