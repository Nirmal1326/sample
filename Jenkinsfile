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
               sh '''
               docker stop jenkins-test || true
               docker rm jenkins-test || true
               docker run -d -p 5000:5000 --name jenkins-test tasktrack-app
               '''
           }
       }

       stage('Test') {
           steps {
               echo 'Testing application...'
               sh 'sleep 5'
               sh 'curl -f http://localhost:5000'
           }
       }

       stage('Cleanup') {
           steps {
               echo 'Cleaning up...'
               sh 'docker stop jenkins-test || true'
               sh 'docker rm jenkins-test || true'
           }
       }
   }
}
