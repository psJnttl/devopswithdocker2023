#!/bin/ash
echo "----- Pull from github: $1"
git clone https://github.com/psJnttl/$1

echo "----- Change folder to: $1"
cd $1

echo "----- Build image"
docker build . -t tempname

echo "----- Login to Docker"
docker login -u $DOCKER_USER -p $DOCKER_PASSWORD

echo "----- Set tag to: $2"
docker tag tempname $2

echo "----- Push to hub.docker"
docker push $2
