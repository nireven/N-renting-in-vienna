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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       656.7  |            64 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/mitten-im-5.%21-charmante-altbauwohnung-unbefristetes-mietverh%C3%A4ltnis-799047854/)                                                          | Mar 20, 11:44      |
|       690    |            75 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2--zi--studenten-whg-75-qm-ab-sofort-zu-vermieten-1362990511/)                                                                                   | Mar 20, 11:35      |
|       799.98 |            41 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/) | Mar 20, 11:22      |
|       660    |            61 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe-nur-mit-vormerkschein-1289738886/)                                                                                 | Mar 20, 10:49      |
|       790    |            67 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gr%C3%BCnruhelage---befristeter-altbauhit-in-gepflegtem-stilhaus-%21-1966676969/)                                                                | Mar 20, 10:39      |
|       641.99 |            71 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/bitte-nur-schriftlich-anfragen---teilm%C3%B6blierte-3-zimmer-wohnung---beachten-sie-das-video---nicht-zentral-begehbar-1400288072/)             | Mar 20, 10:19      |
|       729.01 |            43 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-mit-dachschr%C3%A4ge-inkl.-k%C3%BCche-dachterrasse-und-kellerabteil---mietbeginn-15.06.2025-/hs28-top-2-261-2045954207/) | Mar 20, 10:19      |
|       676.89 |            56 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/erstbezug-direkt-in-der-mollardgasse%21-824275620/)                                                                                             | Mar 20, 09:58      |
|       579    |            54 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-direktvergabe-1087431177/)                                                                                                       | Mar 20, 06:04      |
|       690    |            43 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gut-aufgeteilte-zwei-zimmer-wohnung-n%C3%A4he-hauptbahnhof-%21-1129992449/)                                                                     | Mar 20, 02:07      |
|       799    |            48 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ne-2-zimmerwohnung-mit-loggia-in-u-bahn-n%C3%A4he-%28u3%29-2020249260/)                                                          | Mar 19, 19:35      |
|       627    |            54 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-direkt-vergabe-vormerkschein-bis-28.02.2025-835804490/)                                                                        | Mar 19, 15:55      |
|       450    |            45 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-45m2-872785537/)                                                                                                                | Mar 19, 15:19      |
|       457.85 |            45 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/gemeindewohnung-in-bestlage-4.-bezirk-1415482231/)                                                                                                 | Mar 19, 13:15      |
|       690    |            60 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-wohnung-in-ottakring-867207134/)                                                                                                 | Mar 19, 13:08      |
|       745    |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Aprovisionsfrei%2A-sch%C3%B6negeflegte-2-zimmer-wohnung---ideal-f%C3%BCr-p%C3%A4rchen-oder-singles-871791214/)                                | Mar 19, 12:34      |
