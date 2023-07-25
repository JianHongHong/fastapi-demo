# Install Poetry

curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true
poetry shell
poetry install

## Before commit
poetry lock
poetry export > requirements.txt

# Tutorial based on:
- https://dev.to/ericchapman/python-fastapi-crash-course-533e

- Demo on setup, CRUD

- Fixed PUT and DELETE functions

- Added in tests based on: https://fastapi.tiangolo.com/tutorial/testing/
