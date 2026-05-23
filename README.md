# jinkensLab
# Todo App — Flask

A minimal task manager with a REST API and dark UI.

## Run locally

```bash
pip install -r requirements.txt
python app.py
# → http://localhost:5000
```

## Run tests

```bash
python -m pytest test_app.py -v
```

## Run with Docker

```bash
docker build -t todo-app .
docker run -d -p 5000:5000 --name todo-app todo-app
# → http://localhost:5000
```

## API

| Method | URL | Body | Description |
|--------|-----|------|-------------|
| GET | /api/todos | — | List all todos |
| POST | /api/todos | `{"text": "..."}` | Add a todo |
| PATCH | /api/todos/:id | — | Toggle done |
| DELETE | /api/todos/:id | — | Delete a todo |

## Project structure

```
todo-app/
├── app.py           # Flask app + REST API
├── test_app.py      # pytest tests (6 tests)
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── templates/
    └── index.html   # Frontend UI
```