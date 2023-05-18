# Stable distro.
FROM ubuntu:22.04

WORKDIR /tmp

# Install git
RUN apt-get update
RUN apt-get -y install git

# Clone project
RUN git clone https://github.com/docker-hy/material-applications.git

# install go
COPY ./go1.20.2.linux-amd64.tar.gz .
RUN tar -C /usr/local -xzf ./go1.20.2.linux-amd64.tar.gz
ENV PATH="${PATH}:/usr/local/go/bin"

# Build project
RUN cd ./material-applications/example-backend && go build

ENV REQUEST_ORIGIN=http://localhost:5000

EXPOSE 8080
ENTRYPOINT [ "/tmp/material-applications/example-backend/server" ]
