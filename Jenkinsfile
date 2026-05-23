pipeline {
    agent any
    environment {
        IMAGE = "todo-app"
    }
    	stage('Checkout') {
    	steps {
        	git branch: 'main',
            	url: 'https://github.com/Abdelrahman094/jinkensLab.git'
    		}
	}
        stage('Build') {
            steps {
                script {
                    docker.build("${IMAGE}:${BUILD_NUMBER}")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image("${IMAGE}:${BUILD_NUMBER}").inside {
                        sh 'python -m pytest test_app.py -v'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop todo-app || true'
                sh 'docker rm todo-app || true'
                sh "docker run -d --name todo-app -p 5000:5000 ${IMAGE}:${BUILD_NUMBER}"
            }
        }
    }
    post {
        success {
            echo "App deployed → http://localhost:5000"
        }
        failure {
            echo "Pipeline failed. Check console output above."
        }
    }
}
