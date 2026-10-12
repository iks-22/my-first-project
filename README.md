\# My First Project



!\[CI](https://github.com/iks-22/my-first-project/actions/workflows/ci.yml/badge.svg)



A small Flask app, containerized with Docker and tested automatically with GitHub Actions.



\## What it does



\- `/` returns "Hello DevOps"

\- `/health` returns "ok"



\## Run it



```

docker build -t my-first-project .

docker run -p 5000:5000 my-first-project

```



Then open http://localhost:5000



\## CI



On every push to `main`, GitHub Actions builds the image, runs the container, and checks `/health`.



\## Tech



Python, Flask, Docker, GitHub Actions, Git

