FROM golang:alpine3.17 as build-stage

WORKDIR /tmp

# Set golang path
ENV PATH="${PATH}:/usr/local/go/bin"

# Install git, get codes and build
RUN apk add --no-cache git && \
    git clone https://github.com/docker-hy/material-applications.git && \
    cd /tmp/material-applications/example-backend && go build
#    adduser -D appuser && \
#    chown appuser /tmp/material-applications/example-backend/server

#USER appuser

FROM scratch
WORKDIR /app
COPY --from=build-stage /tmp/material-applications/example-backend/server /app

EXPOSE 8080
ENTRYPOINT [ "/app/server" ]
