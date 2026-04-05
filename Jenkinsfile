pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t tasktrack-app .'
            }
        }
        stage('Run') {
            steps {
                echo 'Running container...'
                sh 'docker rm -f jenkins-test || true'
                sh 'docker run -d -p 5000:5000 --name jenkins-test tasktrack-app'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing application...'
                sh '''
                    CONTAINER_IP=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' jenkins-test)
                    echo "Container IP: $CONTAINER_IP"
                    for i in $(seq 1 10); do
                        echo "Attempt $i..."
                        curl -sf http://$CONTAINER_IP:5000 && echo "App is up!" && exit 0
                        sleep 3
                    done
                    echo "App failed to respond after 30 seconds"
                    docker logs jenkins-test
                    exit 1
                '''
            }
        }
        stage('Cleanup Test Container') {
            steps {
                echo 'Cleaning up test container...'
                sh 'docker stop jenkins-test || true'
                sh 'docker rm jenkins-test || true'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
            sh 'docker stop jenkins-test || true'
            sh 'docker rm jenkins-test || true'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
