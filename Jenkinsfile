pipeline{
    agent any
    stages{
        stage ("Build Docker Image"){
            steps{
                echo "Build Docker Image"
                bat "docker build -t kubeapp:v2 ."
            }
        }
        stage ("Docker Login"){
            steps{
                bat "docker login -u sahithi2108 -p Sahithi@08"
            }
        }
        stage("push Docker Iamge to Docker Hub"){
            steps {
                echo "push Docker Image to docker hub"
                bat "docker tag kubeapp:v2 sahithi2108/medicinereminder:latest"
                bat "docker push sahithi2108/medicinereminder:latest"


            }
        }
        stage("Deploy to Kubernetes"){
            steps{
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
        stage('Restart Deployment') {
            steps {
                echo "Restarting Deployment to pick up new image..."
                bat "kubectl rollout restart deployment/kubeapp-deployment"
            }
        }
    }
    post{
        success{
            echo 'Pipeline completed scucessfull!'

        }
        failure{
            echo "Pipeline failed.Please check the logs."
        }
    }
}
