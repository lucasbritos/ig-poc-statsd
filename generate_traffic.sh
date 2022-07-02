#!/bin/bash
echo Generating traffic....
while :
do
	curl -i -X GET -A "browser_1" http://localhost:8000/helloworld/ > /dev/null 2>&1 
    curl -i -X POST -A "browser_2" http://localhost:8000/helloworld/ > /dev/null 2>&1
    sleep 0.3s
    curl -i -X DELETE -A "browser_1" http://localhost:8000/helloworld/ > /dev/null 2>&1
    curl -i -X PATCH -A "browser_2" http://localhost:8000/helloworld/ > /dev/null 2>&1
    sleep 0.4s
done