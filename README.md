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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       695    |            33 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ab-1.2.2025---u6-n%C3%A4he-erlaaer-stra%C3%9Fe---neuwertige-singlewohnung-in-ruhelage---sofortbezug-1461331672/)                               | Jan 27, 10:52      |
|       642.1  |            32 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/zwei-zimmer-balkonwohnung---n%C3%A4he-u6-alser-stra%C3%9Fe%21-1159214903/)                                                                     | Jan 27, 10:14      |
|       729.3  |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/provisionsfreie-traumwohnung:-2-zimmer-%7C-top-lage%7C-ausgezeichnete-anbindung-1587911057/)                                               | Jan 27, 10:03      |
|       678.38 |            57 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen--unbefristet-zu-mieten-1793337601/)                                                       | Jan 27, 10:01      |
|       790    |            46 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohntr%C3%A4ume-erleben:-mietwohnungen-mit-option-auf-zuk%C3%BCnftigen-kauf-739383800/)                                     | Jan 27, 08:56      |
|       780    |            60 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/mietwohnung-935795477/)                                                                                                                      | Jan 26, 22:59      |
|       650    |            40 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%28reserviert%29-privat-vermietung-%28nichtraucher%29-740651970/)                                                                           | Jan 26, 21:50      |
|       790.65 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-huma-eleven---wohnung-perfekt-f%C3%BCr-p%C3%A4rchen-geeignet-mit-balkon-1309031000/)                                               | Jan 26, 21:37      |
|       799.96 |            47 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1810981329/)                                              | Jan 26, 21:35      |
|       710    |            70 |          3 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeinde-wohnung-in-21-.-bezirk-weitergeben-2044563217/)                                                                                   | Jan 26, 21:06      |
|       460    |            46 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-direktvergabe-vm-dez-2024-1254009226/)                                                                                         | Jan 26, 19:47      |
|       774    |            54 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zimmer-single-wohnung-servitenviertel-altbau-1276025198/)                                                                                 | Jan 26, 19:18      |
|       495    |            50 |          2 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/mietwohnung-gemeinde-wohnticket-31.12.2024-1368188222/)                                                                                       | Jan 26, 19:04      |
|       799.42 |            43 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-in-floridsdorf:-nachhaltigkeit-trifft-wohnkomfort---jetzt-anfragen-1794922627/)                                   | Jan 26, 18:55      |
|       699    |            62 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-/-direktvergabe-nur-mit-vormerkschein%21-vsnr:-30.11.2024-1672281334/)                                                       | Jan 26, 18:35      |
|       478    |            49 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/gemeindewohnung-zur-direktvergabe-1220583450/)                                                                                              | Jan 26, 17:26      |
|       525    |            50 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/f%C3%BCr-sportliche:-nette-1-zimmer-%2B-kabinett-wohnung-in-%2A1050-wien%2A-in-sehr-guter-lage-%284.-stock-ohne-aufzug%29-1909653919/)      | Jan 26, 17:21      |
|       490    |            44 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-gemeindewohnung-n%C3%A4he-elterleinplatz-1119455457/)                                                                              | Jan 26, 16:55      |
|       440.72 |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-1020-wien-vms:-31.10.2024-928811082/)                                                                                     | Jan 26, 15:57      |
|       523.08 |            51 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung-1230-/-u-bahn-n%C3%A4he-und-gr%C3%BCnlage-%28nur-mit-vormerkschein-f%C3%BCr-zwei-wohnr%C3%A4ume-bis-30.11.2024%29-1687561871/) | Jan 26, 12:42      |
