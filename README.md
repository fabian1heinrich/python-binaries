# PYTHON BINARIES

## build binary

```bash
uv run pyinstaller \
-F \
-p  /home/vscode/.cache/.venv/lib/python3.12/site-packages \
--distpath . \
--workpath /tmp/pyinstaller \
hello_world/hello.py 
```

## test binary

```bash
docker run -v ./hello:/hello debian:latest ./hello fabian
```
