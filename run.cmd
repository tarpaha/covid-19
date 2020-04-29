set country=Russia
mkdir out
wget https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv --output-document=out\global.csv
python src\filter_country.py out\global.csv %country% out\local.csv
python src\draw_graph.py out\local.csv %country% out\local.png
del out\*.csv
