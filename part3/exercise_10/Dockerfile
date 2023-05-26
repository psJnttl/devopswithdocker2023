# Based on Ubuntu Linux distro.
FROM alpine:3.17

WORKDIR /home/appuser
COPY the_app.sh .

# Install curl, add user with lower privileges.
# Add the shell script and execution permission
RUN apk add --no-cache curl && \
    adduser -D appuser && \
    chmod +x the_app.sh && \
    chown appuser:appuser ./the_app.sh

USER appuser

# Run the app
CMD ./the_app.sh