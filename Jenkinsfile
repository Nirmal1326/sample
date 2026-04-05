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
                sh 'docker run -d --network host --name jenkins-test tasktrack-app'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing application...'
                retry(5) {
                    sh 'sleep 3'
                    sh 'curl -f http://localhost:5000'
                }
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
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
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
