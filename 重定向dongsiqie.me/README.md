---
title: Bing
emoji: 🐨
colorFrom: green
colorTo: blue
sdk: docker
pinned: false
license: mit
app_port: 5000
---


# Flask Redirect App

This simple Flask application redirects any requests to the root URL to https://dongsiqie.me.

## Pre-requisites

Make sure you have Docker installed on your system. You can download it from [Docker's official website](https://docker.com).

## Build Instructions

To build the Docker image for this application, run the following command:

```bash
docker build -t flask-redirect-app .
```

This will use the `Dockerfile` in the current directory to build an image named `flask-redirect-app`.

## Running the Application

Once the image has been built, you can start a container with:

```bash
docker run -dp 5000:5000 flask-redirect-app
```

The application will be accessible at `http://localhost:5000` and will redirect to https://dongsiqie.me.

## Stopping the Application

To stop the running container, first list all running containers with:

```bash
docker ps
```

Find the container running the `flask-redirect-app` and note the CONTAINER ID. Then run:

```bash
docker stop CONTAINER_ID
```

Replace `CONTAINER_ID` with the actual ID of your container.



