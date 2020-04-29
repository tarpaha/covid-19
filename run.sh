out_folder=${PWD}/out
docker build -t covid-19 .
docker run -v $out_folder:/out covid-19
