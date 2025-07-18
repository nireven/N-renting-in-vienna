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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                          |   📅 Published Date |
|-------------:|--------------:|-----------:|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------:|
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/wohnung-in-nussdorf-%28klimatisiert-garage-terrasse-m%C3%B6bel%29-1616138217/)                                        |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/wohnung-22.-bez.-stadlau-1663147219/)                                                                                   |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/rax2:-s%C3%BCdseitige-2-zimmer-wohnung-mit-loggia-nahe-wienerbergpark-in-1100-wien-zu-mieten-1256354834/)                |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-monat-mietzinsfrei:-4-zimmer-dachgescho%C3%9Fwohnung-mit-k%C3%BChlung-&-blick-%C3%BCber-die-felder-1746632347/)       |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/zentrale-ruhige-wohnung-studentenhit-1652698651/)                                                                        |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/%7C-2-zimmer-%7C-balkon-%7C-st.-veit-gasse-25%7C-erstbezug-in-hietzing-%7C-mietbeginn-per-01.-dezember-2025-1191742944/)  |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/%7C-2-zimmer-%7C-balkon-%7C-st.-veit-gasse-25-%7C-erstbezug-in-hietzing-%7C-mietbeginn-per-01.-dezember-2025-1638850327/) |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/wundersch%C3%B6ne-wohnung-neben-donauzentrum-&-3-min-entfernt-von-der-u1-kagran%21-1906669106/)                         |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/charmante-2-zimmer-wohnung-mit-erker-und-gr%C3%BCnblick-in-1190-wien-1609259449/)                                     |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/zieglergasse:-super-schicke-3-zimmer-neubauwohnung-mit-2-badezimmer-1204735687/)                                            |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/gartenwohnung-im-cottage-inkl-2-garagenpl%C3%A4tzen-inkl.-heizung-und-warmwasser-akonto-1377165941/)                  |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/dem-himmel-so-nah:-elegant-m%C3%B6bliertes-studio-im-42.-stock-mit-cityblick-%28pool-gym-spa-lounges%29-1910079622/)    |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1010-innere-stadt/traumhafte-4-zimmer-wohnung-im-herzen-von-wien---top-innenstadtlage-beim-stephansplatz%21-1591345091/)                |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/mitten-am-rochusmarkt---erstklassig-ausgestattete-altbauwohnung-mit-air-condition-1906628014/)                     |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2er-wg-taugliche-studentenwohnung-%28optimale-lage%29-2083697480/)                                                      |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/balkontraum-in-hietzing:-moderne-2-zimmer-mietwohnung-mit-gro%C3%9Fem-balkon-1330831294/)                                 |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/helle-2-zimmer-wohnung-%28w%C3%A4hringer-stra%C3%9Fe-12%29---ab-01.09.2025-1096657959/)                                 |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/kaasgraben-moderne-4-zimmer-wohnung-mit-2-balkonen-perfekte-raumaufteilung%21-925625102/)                             |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/erstbezug-nach-sanierung---stilvolles-wohnung-direkt-bei-der-u1-870812227/)                                                 |                nan |
|          nan |           nan |        nan | Unknown       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1010-innere-stadt/penthouse-mit-blick-auf-den-stephansdom-801923353/)                                                                   |                nan |
