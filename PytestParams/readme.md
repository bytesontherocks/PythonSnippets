`poetry install`
`poetry add pytest-cov` # for example to add a new dependency or it can be manually added in the *.toml

`poetry run pytest main.py --cov`

```
---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name      Stmts   Miss  Cover
-----------------------------
main.py      14      4    71%
-----------------------------
TOTAL        14      4    71%

```

`poetry run ruff check`   # Lint all files in the current directory (and any subdirectories) using ruff a light way linter
`poetry run mypy .`   # Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. 