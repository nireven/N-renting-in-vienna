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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       695    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmer-erstbezug-in-hauptbahnhof-n%C3%A4he-824306479/)                                                                                                            | Nov 05, 19:35      |
|       790.44 |            53 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer/53-m%C2%B2-wohnung---inkl.-kellerabteil-1665132600/)                                                                                                       | Nov 05, 18:41      |
|       787.92 |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m%C2%B2-zum-mietpreis-von-78792-eur%21-1580236359/)                                                                    | Nov 05, 18:35      |
|       699.75 |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/tolle-2-zimmerwohnung-an-der-u4%21-1880079982/)                                                                                                       | Nov 05, 18:33      |
|       652.84 |            50 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/gut-geschnittene-2-zimmerwohnung-in-beliebter-gr%C3%BCnruhelage%21-1823539964/)                                                                                        | Nov 05, 18:33      |
|       750    |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-dachgeschosswohnung-%2A%2Aohne-provision%2A%2Abusstation-vor-der-haust%C3%BCre%2A%2A-2030561384/)                                                          | Nov 05, 17:44      |
|       608.59 |            41 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/herzige-singlewohnung-f%C3%BCr-naturliebhaber%2Ainnen-mit-gartennutzung-1303942806/)                                                                                    | Nov 05, 17:36      |
|       781.3  |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gro%C3%9Fe-2-zimmer-wohnung-zum-guten-preis-bei-u1-1132481725/)                                                                                                       | Nov 05, 15:47      |
|       731    |            43 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/niederhofstra%C3%9Fe-39-43m-wohnung-1763245094/)                                                                                                                       | Nov 05, 15:32      |
|       799.35 |            47 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/bezugsfertige-25-zimmer-in-ottakring-1219433957/)                                                                                                                     | Nov 05, 15:28      |
|       464.02 |            55 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ruhige-2-zimmer-gemeindewohnung-mit-loggia-1295704242/)                                                                                                                | Nov 05, 14:24      |
|       765.37 |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/tolle-2-zimmer-wohnung-mit-idealer-raumaufteilung-in-guter-und-infrastrukturell-ansprechender-lage%21-1791769254/)                                                  | Nov 05, 14:18      |
|       690    |            50 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/ruhige-wohnung-im-17.-bezirk-akh-und-ubahn-n%C3%A4he-privat-zu-vermieten-1960960709/)                                                                                   | Nov 05, 14:05      |
|       700    |            44 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/orea-%7C-traumhafte-2-zimmer-neubauwohnung-in-bester-lage-%7C-smart-besichtigen-%C2%B7-online-anmieten-1261856577/)                                                 | Nov 05, 13:58      |
|       716.37 |            40 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/orea-%7C-gem%C3%BCtliche-neubauwohnung-mit-gro%C3%9Fem-garten-und-top-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-957197651/)                            | Nov 05, 13:52      |
|       795    |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wundersch%C3%B6ne-2-zimmer-wohnung-mit-terrasse-1939918169/)                                                                                          | Nov 05, 13:51      |
|       798.88 |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend-living%21-inklusive-k%C3%BCche%21-erstbezug%21-elektrische-raffstores%21-klima-vorb.%21-n%C3%A4he-u1.---wohntraum-774645004/)                                | Nov 05, 13:49      |
|       779.01 |            43 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2-zimmer-neubauwohnung-mit-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil/-bg17-2-08-1513550130/)                                                     | Nov 05, 13:31      |
|       795    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/baujahr-2020-van-der-n%C3%BCll-gasse---hofseitige-2-zimmer-mit-957m2-gro%C3%9Fem-balkon-1877544970/)                                                                  | Nov 05, 12:35      |
|       473.09 |            64 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug%21-/-vormerkschein-bis-30.09.2024-/-n%C3%A4chste-sammelbesichtigung-am-10.11.24-von-14-bis-17h-%21%21-1551815967/) | Nov 05, 12:33      |
