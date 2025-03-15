# DummyPod

A lightweight, no-frills app designed to help test and deploy Terraform code for AWS EKS Kubernetes clusters. With health checks, monitoring, and a sense of humor, DummyPod is your trusty sidekick for blue-green deployments and CI/CD pipelines. It doesn’t do much, but it does it well! 🚀

## Features

- **Simple Web Server**: Built with Flask (Python), serving a basic homepage.
- **Health Checks**: A `/health` endpoint to verify the app is running.
- **Metrics**: A `/metrics` endpoint to simulate monitoring data.
- **Kubernetes Ready**: Includes Kubernetes manifests for easy deployment to EKS.

## Quick Start

### Prerequisites

- Python 3.12+
- Flask (`pip install Flask`)
- Docker (optional, for containerization)
- Kubernetes cluster (e.g., AWS EKS)

### Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dummypod.git
   cd dummypod
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python -m app.main
   ```

4. Test the endpoints:
   - Homepage: `http://localhost:8080/`
   - Health Check: `http://localhost:8080/health`
   - Metrics: `http://localhost:8080/metrics`

### Building and Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t dummypod:latest .
   ```

2. Run the container:
   ```bash
   docker run -p 8080:8080 dummypod:latest
   ```

3. Access the app at `http://localhost:8080/`.

### Deploying to Kubernetes

1. Apply the Kubernetes manifests:
   ```bash
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
   ```

2. Verify the deployment:
   ```bash
   kubectl get pods
   kubectl get svc
   ```

3. Access the app using the external IP from the service.

## Project Structure

```
dummypod/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── health.py
│   └── routes.py
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
├── requirements.txt
├── Dockerfile
└── README.md
```

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

---

Happy deploying! 🚀