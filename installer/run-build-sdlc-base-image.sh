#!/bin/bash
cd ../
docker rmi -f sdlc-python-pg:python3.11-pg15.8
docker build -f installer/Dockerfile-python-pg -t sdlc-python-pg:python3.11-pg15.8 .
docker rmi -f sdlc-vector-model:v1.0.1
docker build -f Dockerfile-vector-model -t sdlc-vector-model:v1.0.1 .
