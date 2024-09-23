
# <p align="center"> FastAPI Kubernetes Project - HPA</p>

## Project Overview
This project demonstrates how to deploy a FastAPI application to a local Kubernetes cluster using Docker.

Prerequisites:
- Docker
- Kubernetes (Minikube)
- FastAPI

<hr>
Set up your docker image, then we can get started:
For this example I've used a simple docker image with a basic fastapi app.

Starting:
```bash
minikube start
```
Apply the deployment:
```bash
 kubectl apply -f crud-deployment.yaml
```
Apply the service:
```bash
 kubectl apply -f crud-service.yaml
```
Apply the HPA:
```bash
 kubectl apply -f crud-hpa.yaml
```
Access the service:
```bash
kubectl port-forward svc/fastapi-crud-service 8080:80
```
Now you can test it : 
http://localhost:8080/docs
