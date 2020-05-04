out_folder=${PWD}/out
/usr/bin/docker build -t covid-19 .
/usr/bin/docker run -v $out_folder:/out covid-19
