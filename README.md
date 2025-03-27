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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       700    |            78 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/3-zimmer-gemeindewohnung-zur-weitervergabe-1467675361/)                                                                         | Mar 27, 14:17      |
|       600    |            42 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/helle-wohnung-n%C3%A4he-rochusmarkt%21-862216072/)                                                                                        | Mar 27, 13:40      |
|       776.52 |            65 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/neu-sanierte-2-zimmerwohnung-direkt-bei-kardinal-nagel-platz-1026970608/)                                                                 | Mar 27, 13:27      |
|       796.38 |            41 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%2Aab-mai%2A-2-zimmer-wohnung-mit-garten-in-the-arrow-1212860882/)                                                                              | Mar 27, 11:26      |
|       740    |            38 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/kompakte-2-zimmer-wohnung-in-ruhiger-lage-n%C3%A4he-hanusch-krankenhaus-1142619273/)                                                              | Mar 27, 11:26      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/) | Mar 27, 11:22      |
|       786.23 |            68 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/n%C3%A4he-h%C3%BCtteldorferstrasse-sch%C3%B6ne-2-zimmer-wohnung-2er-wg-geeignet-1173772547/)                                                      | Mar 27, 08:25      |
|       698.79 |            56 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zwei-zentrale-zi.--ideal-f%C3%BCr-wohngemeinsch.-eb-k%C3%BC/esspl.-duschbad-sep.wc-4.liftstock%21-1799781569/)                            | Mar 27, 07:12      |
|       770    |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stilvolle-neubauwohnung-mit-top-ausstattung---sofort-verf%C3%BCgbar%21-1372283322/)                                                             | Mar 27, 06:24      |
|       570    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-zu-vermieten-10.-bezirk-1909590930/)                                                                                                    | Mar 26, 19:18      |
|       699.72 |            42 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/anfragen-nur-per-mail%21-keine-anrufe%21-unbefristet-in-der-seegasse%21-g%C3%BCnstige-2-zimmer-wohnung%21-1955834656/)                         | Mar 26, 18:49      |
|       570.87 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-vmd-28.2.25-1735732456/)                                                                                                       | Mar 26, 17:07      |
|       627    |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-direkt-vergabe-vormerkschein-bis-28.02.2025-835804490/)                                                                        | Mar 26, 15:55      |
|       489.49 |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-direktvergabe-vmk:-28.02.2025-2-wohnr%C3%A4ume-1030986315/)                                                                    | Mar 26, 15:42      |
|       640    |            54 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/g%C3%BCnsitge-2-zimmer-wohnung-in-simmering-1394383308/)                                                                                        | Mar 26, 14:38      |
