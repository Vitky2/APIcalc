pipeline {
    agent any
    
    environment {
        DOCKER_CREDENTIALS_ID = 'DOCKER_HUB' 
    }
    
    stages {
        
        stage('build') {

            steps {

                echo 'building'
		sh 'whoami'
                sh 'docker build -t vitky2/calcapi:latest .'
		sh 'ls -la'
		sh './udpate.sh'	
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
