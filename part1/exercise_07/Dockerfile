# Based on Ubuntu Linux distro.
FROM ubuntu:20.04

# Install curl
RUN apt-get update
RUN apt-get -y install curl

# It's Ubuntu let's use /tmp
WORKDIR /tmp

# Add the shell script and execution permission
COPY the_app.sh .
RUN chmod +x the_app.sh

# Run the app
CMD ./the_app.sh