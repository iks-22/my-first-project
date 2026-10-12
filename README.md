# My First Project

![CI](https://github.com/iks-22/my-first-project/actions/workflows/ci.yml/badge.svg)

A small Flask app with a PostgreSQL database, containerized with Docker Compose and tested automatically with GitHub Actions.

## What it does

- `/` returns "Hello DevOps" and a visit counter stored in PostgreSQL
- `/health` returns "ok"

## Run it

```
docker compose up --build
```

Then open http://localhost:5000. Each visit is counted and stored in PostgreSQL, and the count survives restarts thanks to a Docker volume.

## CI

On every push to `main`, GitHub Actions builds the image, runs the container, and checks `/health`.

## Tech

Python, Flask, PostgreSQL, Docker, Docker Compose, GitHub Actions, Git