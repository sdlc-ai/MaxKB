docker rm -f sdlc-kb
docker rmi -f sdlc-kb
docker build -f ./installer/Dockerfile-sdlc -t sdlc-kb .
docker run -d --restart always --name sdlc-kb -p 9092:8080 -p 9093:9091 -v /root/sdlc-code/kb/data/.maxkb:/var/lib/postgresql/data sdlc-kb