# PYTHON BINARIES

## build binary

```bash
pyinstaller -F --distpath binaries hello_world/hello.py 
```

## test binary

### download binary to local machine

(if you are running this example on your local machine, you can skip this step)

### copy binary to docker container

```bash
sudo chmod +x Downloads/hello
docker run -d -it --name debian debian  /bin/bash
docker cp Downloads/hello debian:/hello
docker exec debian ./hello
```
