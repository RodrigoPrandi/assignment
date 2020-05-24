# FuelSave - Assignmen


## How to run

* Start the stack with Docker Compose:

```bash
docker-compose up
```

* JSON based web API based on OpenAPI: http://localhost/

## Test running stack

If your stack is already up and you just want to run the tests, you can use:

```bash
docker-compose exec app /app/tests-start.sh
```

That `/app/tests-start.sh` script just calls `pytest` after making sure that the rest of the stack is running.



## Features

* Full **Docker** integration (Docker based).
* **Docker Compose** integration and optimization for local development.
* Python <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">**FastAPI**</a>.
* **Secure password** hashing by default.
* **JWT token** authentication.
* **PostgreSQL**
* **SQLAlchemy** 
* **Alembic** migrations.
* Tests based on **Pytest**, integrated with Docker, so you can test the full API interaction, independent on the database.
