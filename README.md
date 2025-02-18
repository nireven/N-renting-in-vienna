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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       468    |            41 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gut-gepflegte-m%C3%B6blierte-2-zimmer-wohnung-ab-01.05.2025-wiener-wohnen-1402071743/)                | Feb 18, 15:30      |
|       749    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/perfekt-angelegte-2-zimmer-wohnung-hell-und-freundlich-150m-zur-u3-sackgasse-1269416129/)                             | Feb 18, 15:27      |
|       699    |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---s%C3%BCd-westblick---neuwertige-2-zimmer-terrassenwohnung---ab-01.03.2025-945593308/)                     | Feb 18, 13:50      |
|       785.01 |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wundervolle-2-zimmer-wohnung-in-toller-lage---einbauk%C3%BCche-inklusive---ab-01.05.2025-verf%C3%BCgbar%21-878246672/) | Feb 18, 13:28      |
|       627    |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-direkt-vergabe-vormerkschein-bis-31.12.2024-2037114955/)                                             | Feb 18, 12:55      |
|       700    |            62 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeinde-wohnung-1320625034/)                                                                                   | Feb 18, 12:48      |
|       643.9  |            51 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/unbefristete-2-zimmer-altbauwohnung-beim-augarten-1952215550/)                                                     | Feb 18, 09:49      |
|       750    |            35 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/360%C2%B0-tour-//-neubau-balkonwohnung-am-wienerberg-783053018/)                                                       | Feb 18, 07:13      |
|       708.96 |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-sanierte-2-zimmer-wohnung-im-1.og.-835884494/)                                                                    | Feb 18, 02:55      |
|       750    |            55 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-in-top-lage-n%C3%A4he-schloss-belvedere-831349549/)                                            | Feb 17, 20:34      |
|       678.38 |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen--unbefristet-zu-mieten-1290507034/)                                | Feb 17, 20:32      |
|       745.03 |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/renovierte-2-zimmer-wohnung-in-der-n%C3%A4he-u4-und-u6-1185816086/)                                   | Feb 17, 20:19      |
|       526.43 |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1500893406/)                                                                                          | Feb 17, 18:33      |
|       660    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-wr.-wohnen-ticket-n%C3%B6tig-1571300897/)                                                             | Feb 17, 17:46      |
|       748.91 |            37 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/the-arrow---willkommen-im-gr%C3%BCnen-teil-simmerings-974631888/)                                                     | Feb 17, 16:49      |
