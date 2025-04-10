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
|       654.09 |            37 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/mitten-im-6.bezirk-unbefristete-kleinwohnung-n%C3%A4he-pilgramgasse-1109568843/)                                                                | Apr 10, 12:45      |
|       799.98 |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/studentenhit:-2-zimmer-wohnung-mit-kfz-stellplatz-und-perfekter-infrastruktur---n%C3%A4he-spittelau-/-nu%C3%9Fdorferstra%C3%9Fe-u6-988402127/) | Apr 10, 11:22      |
|       796.38 |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/vollm%C3%B6bliert-gegen-abl%C3%B6se%21%21-neubauwohnung-mit-kl.-west-garten-und-gro%C3%9Fer-terrasse-1271563901/)                               | Apr 10, 10:09      |
|       775    |            75 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/1150-wien-fenzlgasse-n%C3%A4he-u-3-johnstra%C3%9Fe:-3-zimmer-altbauwohnung-ca.-75-m2-unbefristet-zu-vermieten-1025318157/)      | Apr 10, 00:32      |
|       595    |            78 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeindewohnung---direktvergabe-f%C3%BCr-3-zimmer-und-vormerkscheindatum-bis-30.11.2024-1215790850/)                            | Apr 09, 21:20      |
|       530    |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/singlewohnung-39-m2-nahe-altes-landgut-1177851985/)                                                                                             | Apr 09, 20:04      |
|       474.63 |            46 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-gemeindewohnung-mit-balkon-in-absoluter-ruhelage---direktvergabe%21-1012930591/)                                                 | Apr 09, 17:24      |
|       577.94 |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/altbauwohnung-in-der-johnstrasse-n%C3%A4he-u-3-1063019568/)                                                                     | Apr 09, 16:27      |
|       750    |            60 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/komplett-eingerichtete-2-zimmer-wohnung-1469097368/)                                                                                            | Apr 09, 15:08      |
|       789    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/orea-%7C-charmante-2-zimmer-wohnung-nahe-u6-%7C-smart-besichtigen-%C2%B7-online-anmieten-1765217068/)                                           | Apr 09, 13:26      |
