### python-hello-app

## Overview
`python-hello-app` is a simple application deployed on Kubernetes using Minikube.

## Features
- Provides a basic "Hello World" web application.
- Utilizes Flask as the web framework.
- Deployed within a Minikube Kubernetes cluster.
- Exposed externally using a NodePort service.

## Prerequisites
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) installed and running on your local machine.
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) installed to interact with the Kubernetes cluster.

## Getting Started
1. Clone this repository:

    ```bash
    git clone git@github.com:pharesd/python-hello-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd python-hello-app
    ```

3. Apply the Kubernetes manifest files to deploy the application:

    ```bash
    kubectl apply -f deployment.yaml
    ```

4. Access the application:

    ```bash
    minikube service hello-python-app
    ```

## Directory Structure
- `app.py`: Main Python file containing the Flask application.
- `Dockerfile`: Dockerfile for building the Docker image.
- `deployment.yaml`: Kubernetes Deployment manifest file.
