set country=Russia
wget https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv --output-document=global.csv
python filter_country.py global.csv %country% local.csv
python draw_graph.py local.csv %country% local.png