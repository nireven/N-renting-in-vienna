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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       726    |            74 |          3 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/3-zimmer-gemeindewohnung-mit-balkon-1357910245/)                                                                                                                          | Jan 13, 10:38      |
|       742.01 |            43 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/basler-gasse-17-1230-wien-1827146858/)                                                                                                                                        | Jan 13, 10:00      |
|       546.66 |            53 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-53m%C2%B2-2-zimmer-direktvergabe-wohnticket-11/2024-2140207590/)                                                                                             | Jan 13, 09:50      |
|       799    |            43 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-wohnung-erstbezug-inkl-markenk%C3%BCche-12m%C2%B2-balkon-und-loggia-und-kellerabteil-/alf41-31-1275531367/)                                               | Jan 13, 09:49      |
|       599.44 |            55 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/erstbezug---betreutes-wohnen-%28ab-dem-60.-lebensjahr%29-in-1220-wien-1578195373/)                                                                                         | Jan 13, 09:49      |
|       780    |            47 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/erstbezug%21-moderne-2-zimmer-wohnung-mit-balkon-und-fu%C3%9Fbodenheizung-1797292448/)                                                                                    | Jan 13, 09:36      |
|       770    |            43 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-wohnung-mit-hochwertiger-k%C3%BCche-balkon-und-kellerabteil-%28i3-46%29-864784617/)                                                                       | Jan 13, 09:27      |
|       799    |            44 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-wohnung-mit-hochwertiger-k%C3%BCche-und-kellerabteil-%28i3-31%29-1430668443/)                                                                             | Jan 13, 09:27      |
|       779    |            43 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-wohnung-inkl-hochwertiger-k%C3%BCche-mit-sonderausstattung-balkon-und-kellerabteil-/-i3-14-1996398254/)                                                   | Jan 13, 09:27      |
|       690.54 |            48 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/nette-zwei-zimmer-wohnung-mit-aussenbereich%21%21%21-1452583767/)                                                                                           | Jan 13, 09:21      |
|       790    |            46 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohntr%C3%A4ume-erleben:-mietwohnungen-mit-option-auf-zuk%C3%BCnftigen-kauf-739383800/)                                                                    | Jan 13, 08:56      |
|       730    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-in-favoriten-n%C3%A4he-u1-troststra%C3%9Fe-1073311402/)                                                                                                    | Jan 13, 08:00      |
|       558.47 |            56 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-direktvergabe-883223660/)                                                                                                                                   | Jan 12, 23:16      |
|       750    |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sonnige-2-zimmer-neubau-wohnung-1488758239/)                                                                                                                                | Jan 12, 19:42      |
|       495    |            50 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/mietwohnung-gemeinde-wohnticket-31.12.2024-1368188222/)                                                                                                                      | Jan 12, 19:04      |
|       545.19 |            53 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/%28bitte-derzeit-keine-anfragen-mehr%29-sch%C3%B6ne-2-zimmer-gemeindewohnung-in-zentraler-lage---mit-balkon-in-begr%C3%BCnten-innenhof-1944989193/)                         | Jan 12, 19:04      |
|       798.53 |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristete-neubauwohnung-in-gehweite-des-bahnhof-penzing---ruhige-seitengasse-der-linzer-stra%C3%9Fe%21-ab-m%C3%A4rz-2025%21---jetzt-zuschlagen-2060975917/)                | Jan 12, 18:56      |
|       557.34 |            51 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/direktvergabe-ohne-ger%C3%A4te-wundersch%C3%B6ne-helle-gemeindewohnung-1-wohnraum-1-k%C3%BCchezeile-ohne-elektroger%C3%A4te-vmd-31.12.2024-oder-fr%C3%BCher-1906357566/) | Jan 12, 18:42      |
|       517    |            50 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gemeindewohnung-2-zimmer-1060-vmd-10/2024-1226960909/)                                                                                                                      | Jan 12, 16:12      |
|       687.19 |            58 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/nachmieter-gesucht-1408471351/)                                                                                                                                               | Jan 12, 15:24      |
