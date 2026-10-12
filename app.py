import os

import psycopg2
from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello DevOps</title>
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-family: system-ui, sans-serif;
      background: #0d1117;
      color: #e6edf3;
    }
    h1 { font-size: 3rem; margin: 0 0 0.5rem; }
    p { font-size: 1.25rem; color: #8b949e; margin: 0; }
  </style>
</head>
<body>
  <h1>Hello DevOps</h1>
  <p>Visits: {{ count }}</p>
</body>
</html>
"""


def get_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        dbname=os.environ.get("DB_NAME", "appdb"),
        user=os.environ.get("DB_USER", "appuser"),
        password=os.environ.get("DB_PASSWORD", "apppass"),
    )


@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS visits (id INT PRIMARY KEY, count INT NOT NULL)"
    )
    cur.execute(
        "INSERT INTO visits (id, count) VALUES (1, 1) "
        "ON CONFLICT (id) DO UPDATE SET count = visits.count + 1 "
        "RETURNING count"
    )
    count = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return render_template_string(PAGE, count=count)


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)