#!/bin/bash
country=Russia
mkdir -p out
wget https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv --output-document=global.csv
python3 filter_country.py global.csv $country local.csv
python3 draw_graph.py local.csv $country out/local.png