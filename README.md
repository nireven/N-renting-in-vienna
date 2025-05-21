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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       569.59 |            53 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/vollsanierte-2-zimmer-wohnung-in-1210-wien---ihr-neues-zuhause-f%C3%BCr-nur-56959-eur%21-1713210880/)                                                  | May 21, 10:50      |
|       569    |            52 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/%2Atop-altbau-mit-wintergarten-u6-um%60s-eck%2A-1983177099/)                                                                                           | May 21, 10:28      |
|       799.99 |            50 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-neubauwohnung-inkl.-loggia-komplettk%C3%BCche-und-kellerabteil-nahe-bahnhof-floridsdorf/-ls84-top-35-1479984052/)                             | May 21, 08:46      |
|       798.28 |            45 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sanierte-2-zimmer-wohnung-%7C-tolle-ausstattung-%7C-bahnhof-penzing-1529095853/)                                                                           | May 21, 08:46      |
|       795    |            64 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gem%C3%BCtliche-2-zimmer-mietwohnung-nahe-der-scn-1495470356/)                                                                                         | May 21, 07:14      |
|       660    |            44 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/1190-wien-heiligenst%C3%A4dter-str.-zwei-zimmer-top-14-44m%C2%B2-k%C3%BCche-im-wohnzimmer-duschbad-1.-liftstock-ruhelage-miete-eur-660---1709631176/) | May 21, 06:48      |
|       800    |            45 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/erstbezug%21-stilvolle-2-zimmer-neubauwohnung_balkon_top-ausstattung_1210-wien%21-1165832201/)                                                         | May 21, 06:48      |
|       699    |            38 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/superkompakt-%7C-saniert-%7C-zentral-1290304278/)                                                                                                       | May 21, 00:38      |
|       540    |            48 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%21-dringend%21-gemeindewohnung%21-direktvergabe-nur-mit-g%C3%BCltigem-wiener-wohnticket-vms-30.04.25%21-1068837510/)                                     | May 20, 22:11      |
|       850    |            45 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/m%C3%B6blierte-2-zimmer-wohnung-auf-der-hellwagstra%C3%9Fe-zu-vermieten-1036281423/)                                                                   | May 20, 21:28      |
|       848    |            43 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%7C-2-zimmer-%7C-ab-september-%7C-nachvermietung-%7C-nordwestlich-%7C-balkon-%7C-an-der-alten-donau-%7C-donaustadtbr%C3%BCcke-916358290/)               | May 20, 20:39      |
|       830    |            68 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/u4/u6-l%C3%A4ngenfeldgasse---2-zimmer-wohnung-zur-vermietung-1633237659/)                                                                                 | May 20, 20:34      |
|       673    |            52 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/mietwohnung-52m%C2%B2---zwei-zimmer---naherholung-liesingbach-1709293417/)                                                                                 | May 20, 20:26      |
|       412    |            52 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/direktvergabe-gemeindebauwohnung-2045526229/)                                                                                                              | May 20, 19:56      |
|       889.15 |            42 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-wohnung-in-1220-wien---stadlau-%7C-balkon-&-top-anbindung%21-1157852095/)                                                              | May 20, 18:20      |
|       886    |            51 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-im-16.-bezirk-in-ruhiger-lage-sowie-zentrumnah-1174305286/)                                                                             | May 20, 17:33      |
|       865    |            46 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-neubauwohnung-mit-innenhof-balkon-und-abstellraum-nahe-s-bahn-jedlersdorf-stra%C3%9Fenbahn-26-und-scn%21-1694025998/)                          | May 20, 17:26      |
|       790    |            44 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/charmante-2-zimmer-wohnung-mit-freifl%C3%A4che-in-ruhiger-lage---ab-01.08.2025%21-1100301109/)                                                          | May 20, 17:25      |
|       789.93 |            44 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pog-81---hochwertige-ausstattung-ruhelage-nahe-kagraner-platz-und-top-grundriss%21-ab-august-2025---jetzt-anfragen-1424305801/)                         | May 20, 16:47      |
|       750    |            57 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/erstbezug---sanierte-2-zimmer-wohnung-mit-separater-k%C3%BCche-und-kellerabteil-im-1.-stock-ohne-lift---n%C3%A4he-lidlpark---unbefristet-947146560/)       | May 20, 15:56      |
