FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000 
CMD ["python", "serve_model.py"] 

#docker build -t my_model_server .
#docker run -p 5000:5000 my_model_server
# To build the Docker image, run:
# docker build -t my_model_server .
# To run the Docker container, use:
# docker run -p 5000:5000 my_model_server
# To test the model server, you can use curl or any HTTP client to send a POST request:
# curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"data": [1, 2, 3]}'
# To stop the Docker container, you can use:
# docker stop <container_id>
# To remove the Docker container, you can use:
# docker rm <container_id>
# To remove the Docker image, you can use:
# docker rmi my_model_server
# To run the Docker container in detached mode, you can use:
# docker run -d -p 5000:5000 my_model_server
# To view the logs of the running container, you can use:
# docker logs <container_id>
# To remove all stopped containers, you can use:
# docker container prune
# To remove all unused images, you can use:
# docker image prune