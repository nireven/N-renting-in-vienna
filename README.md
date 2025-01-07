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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       514.24 |            49 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindebau-wohnung-zu-vermieten-direktvergabe-926979139/)                                                          | Jan 07, 21:28      |
|       777.8  |            40 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/hofseitige-2-zimmer-balkon-nb-wohnung---gleich-bei-u3-simmering%21-1718544028/)                                     | Jan 07, 20:43      |
|       780    |            50 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/helle-2-zimmer-wohnung-parkplatz-optional-1252107760/)                                                             | Jan 07, 20:33      |
|       715    |            45 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/wiedner-hauptstra%C3%9Fe---hofseitiger-2-zimmer-altbau-zu-vermieten-851696952/)                                        | Jan 07, 16:46      |
|       795    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/baujahr-2020-van-der-n%C3%BCll-gasse---hofseitige-2-zimmer-mit-957m2-gro%C3%9Fem-balkon-1770838367/)                | Jan 07, 16:46      |
|       733.7  |            50 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/suche-nachmieter-f%C3%BCr-50m%C2%B2-wohnung-/-looking-for-tenant-50m%C2%B2-apartment-1040628805/)                  | Jan 07, 16:35      |
|       688.27 |            52 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/nette-2-zimmer-wohnung-mit-terrasse-und-balkon%21%21%21-1321953554/)                                                | Jan 07, 16:31      |
|       781    |           nan |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/11-stockwerke-mit-traumhaften-wien-blick-2096675125/)                                                            | Jan 07, 16:29      |
|       737    |           nan |          3 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/wohnkomfort-mitten-in-kagran---u1-kagraner-platz-1494606343/)                                                      | Jan 07, 15:47      |
|       530.87 |            52 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/g%C3%BCnstig-und-charmant-in-wien---studenten-p%C3%A4rchen-single-1826750384/)                                      | Jan 07, 15:41      |
|       750    |            75 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/16.kirchstetterngasse-provisionsfreie-25-zimmer-altbaumiete-in-%C3%A4usserst-gepflegtem-zinshaus-1921519811/)       | Jan 07, 13:33      |
|       549    |            50 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/entz%C3%BCckender-altbau-am-lerchenfelder-g%C3%BCrtel-2056643273/)                                                  | Jan 07, 11:29      |
|       488    |            46 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/renovierte-gemeindewohnung-mit-2-zimmer-in-ruhiger-lage---ab-sofort-verf%C3%BCgbar%21-1243378786/)                 | Jan 07, 11:16      |
|       610    |            60 |          3 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/direkt%C3%BCbergabe-mit-g%C3%BCltigem-wohn-ticket-%28wiener-wohnen-gemeindebau%29-2137261550/)                   | Jan 07, 10:23      |
|       562.31 |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/atelier-:-%29---%3E.-ist-keine-mietwohnung-preiswert-&-aussergew%C3%B6hnlich---56231-eur-bruttomiete-993515347/)    | Jan 07, 09:18      |
|       799    |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-981921692/) | Jan 07, 09:00      |
|       460    |            50 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeinde-wohnung-zu-direkt-vergabe%28-nur-mit-wohnticket-von-wiener-wohnen%29-1598507433/)                        | Jan 07, 08:19      |
|       560    |            64 |          3 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/sehr-sch%C3%B6ne-3-zimmer-gemeinde-wohnung-mit-wohnticket.-unbefristet.-g%C3%BCnstige-abl%C3%B6se%21-897707627/)  | Jan 07, 07:36      |
|       799.32 |            42 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-in-floridsdorf:-nachhaltigkeit-trifft-wohnkomfort%21---jetzt-zuschlagen-1070055439/)     | Jan 07, 06:56      |
|       567.23 |            55 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-gemeindewohnung-1990905572/)                                                                          | Jan 07, 06:07      |
