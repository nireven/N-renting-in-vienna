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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       798.5  |            46 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-dachgeschoss-wohnung-in-top-lage---10.bezirk%21---jetzt-zuschlagen-1845688255/)                                                   | Dec 14, 18:56      |
|       750    |            47 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/vollmoblierte-sanierte-und-gepflegte-wohnung-in-einem-ruhigen-geb%C3%A4ude-im-2.-stock-mit-lift-im-2.-wiener-gemeindebezirk-964895860/) | Dec 14, 17:48      |
|       795.74 |            64 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/zwei-zimmer-gartenseitige-loggia-nahe-liesingbach-&-stadtpark-atzgersdorf-1123269196/)                                                       | Dec 14, 15:39      |
|       755    |            30 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/urgem%C3%BCtliche-30m%C2%B2-designerwohnung-mit-riesiger-terrasse%21-1889468448/)                                                        | Dec 14, 13:05      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---2-zimmer-und-balkon---wohnen-mit-komfort-und-ausblick---ihre-wohlf%C3%BChloase-am-laaer-berg-1233725437/)                     | Dec 14, 11:28      |
|       790    |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg--gem%C3%BCtliche-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1488914495/)                | Dec 14, 11:28      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hochwertige-2-zimmer-wohnung-mit-balkon-und-wohlf%C3%BChlatmosph%C3%A4re---viola-park---am-laaer-berg-1094558488/)                         | Dec 14, 11:28      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg---leben-mit-aussicht:-2-zimmer-wohnung-mit-balkon-1168697587/)                           | Dec 14, 11:28      |
|       790    |            49 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/erstbezug%21-moderne-2-zimmer-wohnung-mit-balkon-1230948998/)                                                                            | Dec 14, 11:00      |
|       780    |            47 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/erstbezug%21-moderne-2-zimmer-wohnung-mit-balkon-und-fu%C3%9Fbodenheizung-1797292448/)                                                   | Dec 14, 09:36      |
|       550    |            53 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2zimmer-gemeindewohnung-2131728834/)                                                                                                        | Dec 13, 23:10      |
