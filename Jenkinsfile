pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('docker-hub-cred') // Jenkins credentials ID
    }

    stages {

        stage("Check Docker") {
            steps {
                echo "Checking Docker installation..."
                bat "where docker"
                bat "docker --version"
            }
        }

        stage("Build Docker Image") {
            steps {
                echo "Building Docker image..."
                bat "docker build -t medicinereminder:v1 ."
            }
        }

        stage("Docker Login") {
            steps {
                echo "Logging in to Docker Hub..."
                bat "docker login -u %DOCKER_CREDENTIALS_USR% -p %DOCKER_CREDENTIALS_PSW%"
            }
        }

        stage("Push Docker Image") {
            steps {
                echo "Tagging and pushing Docker image..."
                bat "docker tag medicinereminder:v1 sahithi2108/medicinereminder:latest"
                bat "docker push sahithi2108/medicinereminder:latest"
            }
        }

        stage("Deploy to Kubernetes") {
            steps {
                echo "Deploying application to Kubernetes..."
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo "Pipeline failed. Please check the logs."
        }
    }
}
