FROM ubuntu:18.04

RUN \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y wget python3 python3-pip

RUN pip3 install matplotlib numpy scipy

COPY process.sh .
COPY filter_country.py .
COPY draw_graph.py .

ENTRYPOINT ["./process.sh"]