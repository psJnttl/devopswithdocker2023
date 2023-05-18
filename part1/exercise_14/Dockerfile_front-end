# This should be stable distro.
FROM ubuntu:22.04

# It's Ubuntu let's use /tmp
WORKDIR /tmp

# Install curl
RUN apt-get update
RUN apt-get -y install curl

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash
RUN apt install -y nodejs

# Install git
RUN apt-get -y install git

# Clone project
RUN git clone https://github.com/docker-hy/material-applications.git

# Install npm libraries
RUN cd ./material-applications/example-frontend/ && npm install

# Backend is served from the other container.
ENV REACT_APP_BACKEND_URL=http://localhost:8080/

# Build static files
RUN cd ./material-applications/example-frontend/ && npm run build

# install serve, global
RUN npm install -g serve

# Serve the app from port 5000
EXPOSE 5000

ENTRYPOINT [ "serve", "-s", "-l", "5000", "./material-applications/example-frontend/build" ]
