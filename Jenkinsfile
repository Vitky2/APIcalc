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
                sh 'docker run -d -p 8001:8001 apicalc'

            }
        }

	stage('bandit') {
		
	    steps {
		
		sh 'sleep 20'
		sh 'docker run --rm apicalc:latest bandit -r . -lll'
	
	    }
	}

	stage('semgrep') {
	    steps {
	    	sh 'docker run --rm apicalc:latest semgrep --config semgrep-config.yaml .'
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
