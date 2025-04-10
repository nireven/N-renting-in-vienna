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
|       799    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1393569049/)                                                | Apr 10, 18:49      |
|       789.57 |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/reserviert---komfortable-2-zimmer-wohnung-2012590885/)                                                                                          | Apr 10, 18:19      |
|       654.09 |            37 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/mitten-im-6.bezirk-unbefristete-kleinwohnung-n%C3%A4he-pilgramgasse-1637708062/)                                                                | Apr 10, 18:15      |
|       799    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/orea-%7C-sch%C3%B6ne-2-zimmer-wohnung-mit-guter-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-935252328/)                              | Apr 10, 17:25      |
|       588.65 |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gut-geschnittene-2-zimmer-altbauwohnung-i-1.-stock-ohne-lift-i-n%C3%A4he-thaliastra%C3%9Fe-bezirksamt-1815190990/)                              | Apr 10, 16:48      |
|       792.61 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sofortbezug-vollm%C3%B6blierte-spitzenneubauwohnung-n%C3%A4chst-u1---keplerplatz-1971622134/)                                                   | Apr 10, 16:09      |
|       566    |            56 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung---wohnticket-vor-28.2.2025-1466530612/)                                                                          | Apr 10, 15:52      |
|       695    |            40 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-nahe-u6-thaliastra%C3%9Fe---perfekt-f%C3%BCr-singles-oder-paare-1813305604/)                                         | Apr 10, 15:48      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/) | Apr 10, 11:22      |
|       775    |            75 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/1150-wien-fenzlgasse-n%C3%A4he-u-3-johnstra%C3%9Fe:-3-zimmer-altbauwohnung-ca.-75-m2-unbefristet-zu-vermieten-1025318157/)      | Apr 10, 00:32      |
|       595    |            78 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeindewohnung---direktvergabe-f%C3%BCr-3-zimmer-und-vormerkscheindatum-bis-30.11.2024-1215790850/)                            | Apr 09, 21:20      |
|       530    |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/singlewohnung-39-m2-nahe-altes-landgut-1177851985/)                                                                                             | Apr 09, 20:04      |
