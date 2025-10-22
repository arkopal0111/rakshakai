# Deployment Instructions for Rakshak.ai

## Overview
This document provides detailed instructions for deploying the Rakshak.ai application. The application is designed to be modern, secure, and AI-driven, focusing on women's safety and navigation.

## Prerequisites
Before deploying the application, ensure you have the following installed:
- Python 3.8 or higher
- Docker and Docker Compose (if using containerization)
- Access to a cloud service provider (e.g., Heroku, AWS, GCP) for deployment

## Deployment Steps

### 1. Clone the Repository
Clone the Rakshak.ai repository to your local machine:
```bash
git clone https://github.com/yourusername/rakshak-streamlit.git
cd rakshak-streamlit
```

### 2. Set Up Environment
Create a virtual environment and install the required dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Set up the necessary environment variables for your application. You can create a `.env` file in the root directory with the following variables:
```
FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
FIREBASE_DATABASE_URL=your_firebase_database_url
FIREBASE_PROJECT_ID=your_firebase_project_id
```

### 4. Running Locally
To run the application locally, use the following command:
```bash
streamlit run app.py
```
Visit `http://localhost:8501` in your web browser to view the application.

### 5. Docker Deployment
If you prefer to deploy using Docker, build the Docker image:
```bash
docker build -t rakshak-ai .
```
Run the Docker container:
```bash
docker run -p 8501:8501 rakshak-ai
```

### 6. Deploying to Heroku
If deploying to Heroku, ensure you have the Heroku CLI installed and logged in. Create a new Heroku app:
```bash
heroku create rakshak-ai
```
Deploy the application:
```bash
git push heroku main
```

### 7. Kubernetes Deployment
For Kubernetes deployment, ensure you have a Kubernetes cluster set up. Apply the deployment and service configurations:
```bash
kubectl apply -f infra/k8s/deployment.yaml
kubectl apply -f infra/k8s/service.yaml
```

### 8. Monitoring and Maintenance
After deployment, monitor the application for performance and errors. Use logging and monitoring tools to ensure the application runs smoothly.

## Conclusion
Following these steps will help you successfully deploy the Rakshak.ai application. For any issues or further assistance, please refer to the documentation or contact support.