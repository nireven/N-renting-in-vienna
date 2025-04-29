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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       619    |            57 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe-f%C3%BCr-3-zimmer-mit-vmd-bis-31.03.2025-1942525057/)                                                                 | Apr 29, 06:42      |
|       675.98 |            47 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristet---2-zimmer-altbauwohnung-in-ruhiger-lage%21-2131839672/)                                                                                  | Apr 29, 06:35      |
|       654.62 |            50 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/erstbezug%21-stilvoll-hell-und-modern:-2-zimmer-wohnung-in-1030-wien---oberzellergasse-2030710220/)                                            | Apr 29, 03:04      |
|       718.44 |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/supermiete--ruhige-2-zimmerwohnung--n%C3%A4he-augarten-823336343/)                                                                                | Apr 28, 20:31      |
|       588.86 |            56 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-11.-bezirk-mit-balkon-5662m2-1820479435/)                                                                                            | Apr 28, 15:44      |
|       750    |            45 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-45-m2-wohnung-privat-zu-vermieten-1835727011/)                                                                                                  | Apr 28, 12:30      |
|       735    |            37 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-komplettk%C3%BCche-loggia-und-kellerabteil-/-hs28-top-216-840338411/)                                                    | Apr 28, 11:16      |
|       640.4  |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neu-sanierte-445-m%C2%B2-wohnung-in-der-erlachgasse-3---ihr-neues-zuhause-wartet-auf-sie%21%28offene-besichtigung-29.04.2025-um-15:00%29-848766450/) | Apr 28, 10:17      |
|       530    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-zu-vergeben-%28nur-mit-wiener-wohn-ticket-vor-dem-28.2.2025%29-1877800390/)                                                 | Apr 28, 08:01      |
