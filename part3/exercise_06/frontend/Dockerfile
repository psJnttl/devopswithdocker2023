# This should be stable distro.
FROM ubuntu:22.04

# It's Ubuntu let's use /tmp
WORKDIR /tmp

# Install curl
RUN apt-get update && \
    apt-get -y install curl && \
    curl -sL https://deb.nodesource.com/setup_16.x | bash && \
    apt install -y nodejs && \
    apt-get -y install git && \
    git clone https://github.com/docker-hy/material-applications.git && \
    cd /tmp/material-applications/example-frontend/ && npm install && \
    cd /tmp/material-applications/example-frontend/ && npm run build && \
    npm install -g serve && \
    useradd -m appuser && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove curl && \
    apt-get purge -y --auto-remove git && \
    rm -rf /var/lib/apt/lists/*

# Serve the app from port 5000
EXPOSE 5000

# User with lower privileges
USER appuser

ENTRYPOINT [ "serve", "-s", "-l", "5000", "./material-applications/example-frontend/build" ]
