# Keep size low
FROM alpine:latest

# Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash
ADD ./app/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD ./app /opt/webapp/
WORKDIR /opt/webapp

# Heroku: Run the image as a non-root user
RUN adduser -D myuser
USER myuser

# Remove this for Heroku. Local development.
#EXPOSE 8080
#ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8080", "wsgi" ]

# Heroku, run the App.  CMD is required to run on Heroku. $PORT comes from Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
