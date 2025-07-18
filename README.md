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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                                                      |   📅 Published Date |
|-------------:|--------------:|-----------:|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------:|
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/mitten-am-rochusmarkt---erstklassig-ausgestattete-altbauwohnung-mit-air-condition-1906628014/)                                                                 |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2er-wg-taugliche-studentenwohnung-%28optimale-lage%29-2083697480/)                                                                                                  |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/balkontraum-in-hietzing:-moderne-2-zimmer-mietwohnung-mit-gro%C3%9Fem-balkon-1330831294/)                                                                             |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/helle-2-zimmer-wohnung-%28w%C3%A4hringer-stra%C3%9Fe-12%29---ab-01.09.2025-1096657959/)                                                                             |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/kaasgraben-moderne-4-zimmer-wohnung-mit-2-balkonen-perfekte-raumaufteilung%21-925625102/)                                                                         |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/erstbezug-nach-sanierung---stilvolles-wohnung-direkt-bei-der-u1-870812227/)                                                                                             |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1010-innere-stadt/penthouse-mit-blick-auf-den-stephansdom-801923353/)                                                                                                               |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/%2Avollm%C3%B6blierte-2-zimmer-stadtwohnung-in-toplage---sofort-einziehen-&-wohlf%C3%BChlen%2A-1701286778/)                                                         |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/sonnendurchflutete-dachgeschoss-wohnung-nahe-kutschkermarkt-%7C%C2%A05-min-fu%C3%9Fweg-zur-u6-station-michelbeuern-akh-2087619990/)                               |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/provisionsfreier-mietkauf-in-gretl%27s-garten%21-1989858755/)                                                                                                       |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/provisionsfreier-mietkauf-in-gretl%27s-garten%21-1765680738/)                                                                                                       |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-wg-geeignet:-ruhige-hochwertig-ausgestattete-3-zimmerwohnung-mit-mini-balkon-klimavorbereitung-1.dg-bei-meidlinger-hauptstra%C3%9Fe--u6-und-u4-1820310889/) |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/wohnen-am-prater---2-4-zimmer-mit-balkon-und-top-ausstattung-1319555816/)                                                                                         |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zentrale-2-zimmer-wohnung-n%C3%A4he-hauptbahnhof%21-1239998640/)                                                                                                     |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/tolle-helle-2-zimmer-wohnung-mit-21-m%C2%B2-balkon---neuwertig---krottenbachstrasse-835140999/)                                                                   |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/exklusive-altbau-etagenwohnung-mit-5-zimmern-im-herzen-des-7.-bezirks-1108185473/)                                                                                      |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/top-09---gro%C3%9Fz%C3%BCgige-4-zimmer-wohnung-mit-loggia-1356056160/)                                                                                              |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/exklusives-penthouse-b%C3%BCro-mit-traumhaftem-panoramaausblick---top-lage---uno-city---alte-donau-1650508929/)                                                     |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-wohnung-im-19.-bezirk-1748281441/)                                                                                                                |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug---mietwohnungen-mit-style---modernste-ausstattung-1626408182/)                                                                                             |                nan |
