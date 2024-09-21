pipeline {
    agent any
    
    environment {
        DOCKER_CREDENTIALS_ID = 'DOCKER_HUB' 
        VERSION = "${env.BUILD_NUMBER}" // Используем номер сборки как версию
    }
    
    stages {
        
        stage('build') {

            steps {

                echo 'building'
                sh 'docker build -t vitky2/calcapi:latest .'
		sh 'export x=$(cat version.txt)'
		sh 'echo $((x+1)) |tee version.txt'            
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
