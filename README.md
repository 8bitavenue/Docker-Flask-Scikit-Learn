* # Build docker image
docker build . -t demo

* # Launch container
docker run -p 4444:7777 -d demo

* # Open browser and have fun
http://127.0.0.1:4444/demo/api/v1.0/predict?p1=3.0&p2=2.0&p3=1.0
