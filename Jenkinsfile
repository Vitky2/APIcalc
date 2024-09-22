pipeline {
    agent any
    
    stages {        

	stage('test') {

            steps {

                echo 'testing'
                sh 'docker stop $(docker ps -q --filter ancestor=apicalc)' 
                
            }
        }

	stage('build') {
            steps {

                echo 'building'
                sh 'docker build -t apicalc:latest .'
                sh 'docker run --rm -d -p 8001:8001 apicalc'

            }
        }
        
    }

    post {
        success {
            echo 'Docker image built and pushed successfully!!'
        }
        failure {
            echo 'Something went wrong with the build.'
        }
    }
}
