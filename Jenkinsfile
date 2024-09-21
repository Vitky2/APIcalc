pipeline {
    agent any
    
    environment {
        DOCKER_CREDENTIALS_ID = 'DOCKER_HUB' 
        VERSION = "${env.BUILD_NUMBER}" // Используем номер сборки как версию
    }
    
    stages {
        
	stage('Login to Docker Hub') {
            steps {
                script {
                    // Входим в Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        // Здесь можно добавить другие команды, если нужно
                    }
                }
            }
        }
	
        stage('build') {

            steps {

                echo 'building'
                sh 'docker build -t vitky2/calcapi:latest .'
		sh 'docker tag vitky2/calcapi:latest vitky2/calcapi:{$((VERSION+1))}'
		sh 'sudo docker push vitky2/calcapi:{$((VERSION+1))}'
		sh 'echo "export BUILD_NUMBER="{$((VERSION+1))} >> /home/kali/.zshrc'
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
