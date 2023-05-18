# Must be Java 8
FROM openjdk:8

WORKDIR /usr/src/myapp

# Get the source.
RUN git clone https://github.com/docker-hy/material-applications.git

# Build the Project
RUN cd material-applications/spring-example-project && ./mvnw package

# Expose port 8080
EXPOSE 8080

ENTRYPOINT [ "java", "-jar", "./material-applications/spring-example-project/target/docker-example-1.1.3.jar" ]
