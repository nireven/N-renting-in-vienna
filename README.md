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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       544.08 |            65 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/6517-qm---54408--eur-sehr-angenehme-lage-l%C3%A4ssig-lebenswert-eingeteilt-1882991663/)                                                         | Feb 27, 09:30      |
|       574.68 |            43 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/erstbezug%21-traumhafte-2-zimmer-altbauwohnung---unbefristet-1629284658/)                                                                       | Feb 27, 09:25      |
|       570    |            52 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%21%21%21%21%21-bitte-nur-mit-g%C3%BCltigen-vormerkschein-od-wienerwohnticket-melden%21%21%21%21%21%21-datum-31.12.24%21%21%21%21%21-1199028751/) | Feb 27, 08:15      |
|       671.51 |            44 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-%7C-wundersch%C3%B6ne-unbefristete-2-zimmer-wohnung-in-ruhiger-lage-n%C3%A4he-meidlinger-hauptstra%C3%9Fe-1520958715/)                  | Feb 27, 03:28      |
|       770    |            76 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-gemeindewohnung-76m%C2%B2-in-direktvergabe-mit-vormerkschein-und-abl%C3%B6se-zu-vergeben-1198270634/)                                   | Feb 26, 21:56      |
|       716.44 |            52 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmerwohnung-n%C3%A4he-schloss-sch%C3%B6nbrunn-1747742351/)                                                                                    | Feb 26, 18:16      |
|       686.95 |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-lichtdurchflutete-2-zimmer-wohnung-in-1020-wien-mit-ca.-50-m%C2%B2%21-1377195855/)                                           | Feb 26, 16:04      |
|       795    |            40 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/glaskristall:-ger%C3%A4umige-2-zimmerwohnung-mit-balkon-1898153917/)                                                                               | Feb 26, 15:28      |
|       598    |            56 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%2Asonniger-altbau-nahe-elterleinplatz%2A-1737237926/)                                                                                             | Feb 26, 13:28      |
|       670    |            42 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmerwohnung-in-ottakring-1117903803/)                                                                                        | Feb 26, 13:24      |
|       545    |            53 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-2-zimmer-wohnung-im-2.-bezirk---hell-ruhig-&-zentral-1388051434/)                                                            | Feb 26, 10:59      |
|       795    |            63 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/12.-bezirk-p%C3%A4rchenhit-922278769/)                                                                                                            | Feb 26, 10:34      |
|       623.58 |            63 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-mit-direktvergabr-1927370518/)                                                                                                | Feb 26, 10:00      |
|       627    |            54 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-direkt-vergabe-vormerkschein-bis-31.12.2024-2037114955/)                                                                        | Feb 26, 09:14      |
