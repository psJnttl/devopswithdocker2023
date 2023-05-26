FROM alpine:3.17 as build-stage

WORKDIR /tmp

ENV NODE_OPTIONS=--openssl-legacy-provider

# Build static files
RUN apk add --no-cache curl && \
    apk add --no-cache nodejs npm && \
    apk add --no-cache git && \
    git clone https://github.com/docker-hy/material-applications.git && \
    cd /tmp/material-applications/example-frontend/ && npm install && npm update && \
    cd /tmp/material-applications/example-frontend/ && npm run build

FROM busybox:1.36

RUN adduser -D appuser

WORKDIR /home/appuser
    
COPY --from=build-stage /tmp/material-applications/example-frontend/build /home/appuser

USER appuser

# Serve the app from port 5000
EXPOSE 5000

ENTRYPOINT [ "busybox", "httpd",  "-f", "-v", "-p", "5000", "/home/appuser" ]
