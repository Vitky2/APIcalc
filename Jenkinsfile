pipeline {
    agent any

    stages {
        
        stage('build') {

            steps {

                echo 'building'
                sh 'sudo docker build -t test:latest .'
                sh 'sudo docker run -d -p 8001:8001 test'

            }
        }

        
        stage('test') {

            steps {

                echo 'testing'
                sh 'sleep 60'
                sh 'curl "http://localhost:8001/plus?x=4&y=5"'
                sh 'sudo docker stop $(docker ps -q --filter ancestor=test)' 
                
            }
        }
        
    }

    post {
        success {
            echo 'Docker image built and pushed successfully!'
        }
        failure {
            echo 'Something went wrong with the build.'
        }
    }
}
