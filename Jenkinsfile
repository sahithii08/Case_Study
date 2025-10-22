pipeline {
    agent any
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
            bat "docker build -t medicinereminder:v1 ."
        }
    }

    stage("Docker Login") {
        steps {
            bat "docker login -u sahithi2108 -p Sahithi@08"
        }
    }

    stage("Push Docker Image") {
        steps {
            bat "docker tag medicinereminder:v1 sahithi2108/medicinereminder:latest"
            bat "docker push sahithi2108/medicinereminder:latest"
        }
    }

    stage("Deploy to Kubernetes") {
        steps {
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

