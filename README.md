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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       628    |            54 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/n%C3%A4he-botanischer-garten---mohsgasse-%7C-zentral-gelegene-54m%C2%B2-altbauwohnung-mit-flair-%7C-2-zimmer-%7C-einbauk%C3%BCche-%7C-neu-adaptiert-%7C-gesamtmiete-%E2%82%AC-628----%7C-1349834495/) | Mar 10, 13:57      |
|       728    |            61 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gut-geschnittene-wohnung-in-guter-lage-932927905/)                                                                                                                                                          | Mar 10, 13:49      |
|       723.39 |            53 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/zu-vermieten:-53-m%C2%B2-wohnung-in-der-ruckergasse-49-1120-wien-1088571213/)                                                                                                                                | Mar 10, 12:42      |
|       791    |            55 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/g%C3%BCnstige-lage-n%C3%A4he-u3-h%C3%BCtteldorfer-stra%C3%9Fe-1019597990/)                                                                                                                                    | Mar 10, 12:42      |
|       457.05 |            38 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/h%C3%BCbsche-hofseitige-singlewohnung-n%C3%A4he-prater-1469247203/)                                                                                                                                      | Mar 10, 11:54      |
|       760    |            79 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-3-zimmer-gemeinde-wohnung-im-1020-wien-wwt/-vk-906762386/)                                                                                                                              | Mar 10, 11:49      |
|       750    |            52 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1505229506/)                                                                                                            | Mar 10, 11:27      |
|       699    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1245276351/)                                                                                                            | Mar 10, 11:27      |
|       789.3  |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-schloss-neugeb%C3%A4ude---wohnung-perfekt-f%C3%BCr-singles-oder-p%C3%A4rchen-mit-freifl%C3%A4che-989562853/)                                                                                      | Mar 10, 11:20      |
|       660    |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-2-zimmer-wohnung-mit-balkon-1769489952/)                                                                                                                                                           | Mar 10, 10:28      |
|       475    |            65 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sozialbau-wohnung-1876496351/)                                                                                                                                                                              | Mar 10, 09:34      |
|       680    |            51 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/ruhige-2-zimmer-wohnung-1757812161/)                                                                                                                                                                       | Mar 09, 17:58      |
|       432    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen-ticket-31.12.2024-1969505461/)                                                                                                                                                  | Mar 09, 16:20      |
