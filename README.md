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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       520.37 |            52 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-per-direktvergabe---abl%C3%B6se---moderne-ausstattung-inkl.-neuer-k%C3%BCche-785367603/)                                                                              | Jul 03, 20:16      |
|       778.71 |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmerwohnung-mit-gartenblick-1347260771/)                                                                                                                                             | Jul 03, 19:46      |
|       798    |            60 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/provisionsfrei-f%C3%BCr-den-mieter%21-oberm%C3%BCllnerstra%C3%9Fe-n%C3%A4chst-u1/u2-zentrumn%C3%A4he-hofruhelage-60m%C2%B2-altbaumiete-wg-eignung%21-studenten-bevorzugt%21-1814397752/) | Jul 03, 19:10      |
|       780    |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/sch%C3%B6ne-ruhige-2-zimmer-wohnung-nahe-wu-und-praterpark-626188180/)                                                                                                                   | Jul 03, 10:43      |
|       899    |            35 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/%2Avollm%C3%B6blierte-2-zimmer-stadtwohnung-in-toplage---sofort-einziehen-&-wohlf%C3%BChlen%2A-1701286778/)                                                                                | Jul 03, 03:40      |
