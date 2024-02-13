FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install \
    iputils-ping \
    iproute2 \
    net-tools \
    dnsutils \
    mtr-tiny \
    nano \
    && apt-get clean

COPY file /

CMD ["/bin/bash"]
