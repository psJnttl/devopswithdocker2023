# Stable distro.
FROM ubuntu:22.04

WORKDIR /tmp

# Copy Golang sources
COPY ./go1.20.2.linux-amd64.tar.gz .

# Setup path for building go
ENV PATH="${PATH}:/usr/local/go/bin"

RUN apt-get update && \
    apt-get -y install git && \
    git clone https://github.com/docker-hy/material-applications.git && \
    tar -C /usr/local -xzf ./go1.20.2.linux-amd64.tar.gz && \
    cd ./material-applications/example-backend && go build && \
    useradd -m appuser && \
    chown appuser /tmp/material-applications/example-backend/server && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove git && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/go1.20.2.linux-amd64.tar.gz

USER appuser

EXPOSE 8080
ENTRYPOINT [ "/tmp/material-applications/example-backend/server" ]
