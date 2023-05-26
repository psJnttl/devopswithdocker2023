#FROM docker:23-git
FROM docker:23.0.5-cli-alpine3.17
WORKDIR /tmp
RUN apk update
RUN apk add git
COPY ./builder.sh .

ENTRYPOINT [ "/tmp/builder.sh" ]