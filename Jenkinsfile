pipeline {
   agent any

   stages {
       stage('Build') {
           steps {
               sh 'docker build -t tasktrack-app .'
           }
       }

       stage('Run') {
           steps {
               sh '''
               docker stop jenkins-test || true
               docker rm jenkins-test || true
               docker run -d -p 5000:5000 --name jenkins-test tasktrack-app
               '''
           }
       }

       stage('Test') {
           steps {
               sh '''
               docker logs jenkins-test
               for i in {1..10}; do
                 curl -f http://localhost:5000 && exit 0
                 sleep 3
               done
               exit 1
               '''
           }
       }

       stage('Cleanup') {
           steps {
               sh 'docker rm -f jenkins-test || true'
           }
       }
   }
}
