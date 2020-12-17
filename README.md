# CGO-interview-Session

# How to run docker container
1. pull docker image from docker registry
```
docker pull firstspk1/test:latest
docker run -it -p 9999:9999 firstspk1/test:latest
```

2. git clone this repository
```
# After clone this repository
docker build -t testcgo .
docker run -it -p 9999:9999 testcgo
```


If the container can work normally, It will show results as follows
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 17, 2020 - 04:05:01
Django version 2.2.6, using settings 'cgoInterviewSession.settings'
Starting development server at http://0.0.0.0:9999/
Quit the server with CONTROL-C.
```
