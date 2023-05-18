# Distro that allows installing python, albeit version 2.7.
FROM ubuntu:18.04
WORKDIR /tmp

# Install Python
RUN apt-get update && apt-get install -y python

COPY ./app.py .

ENTRYPOINT [ "python", "app.py" ]