# AI CI Fix Agent Demo

This tiny FastAPI app starts with one intentional arithmetic bug to demonstrate CI failure investigation. It is not a production service.

- `GET /health` should return `{"status":"ok"}`.
- `GET /add?a=7&b=3` should return `{"result":10}`. The initial version fails this regression test.

Run the tests with Python 3.11 in an isolated environment:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

The CI workflow runs pytest on GitHub-hosted runners for pushes to `main` and `repair/**`, and can also be run manually. The initial run is expected to fail one test. Repairs belong on a separate branch for review, not directly on `main`.
