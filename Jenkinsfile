pipeline {
    agent any
    stages {
        stage("Build Docker Image") {
            steps {
                bat "docker build -t medicinereminder:v1 ."
            }
        }
        stage("Docker Login") {
            steps {
                bat "docker login -u <your_dockerhub_username> -p <your_password>"
            }
        }
        stage("Push Docker Image") {
            steps {
                bat "docker tag medicinereminder:v1 <your_dockerhub_username>/medicinereminder:latest"
                bat "docker push <your_dockerhub_username>/medicinereminder:latest"
            }
        }
        stage("Deploy to Kubernetes") {
            steps {
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
    }
}
