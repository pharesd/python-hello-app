### python-hello-app

## Overview
`python-hello-app` is a simple application deployed on Kubernetes using Minikube.

## Features
- Provides a basic "Hello World" web application.
- Utilizes Flask as the web framework.
- Deployed within a Minikube Kubernetes cluster.

## Prerequisites
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) installed on your local machine.
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) installed to interact with the Kubernetes cluster.

## Getting Started
1. Clone this repository:

    ```bash
    git clone https://github.com/pharesd/python-hello-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd python-hello-app
    ```

3. Start Minikube:
    ```bash
    minikube start
    ```

4. Apply the Kubernetes manifest files to deploy the application:

    ```bash
    kubectl apply -f deployment.yaml
    ```

4. Access the application:

    ```bash
    minikube service hello-python-app
    ```
