pipeline {
    agent any
    stages {
        stage('Stage 1--> Checkout - checkout the repository.') {
            steps {
                git branch: 'main',
                credentialsId: 'omerkenig',
                url: 'https://github.com/omerkenig/WorldOfGame.git'
                }
        }
           Stage('Stage 2--> Build - Build docker image.'){
            steps {
				script{
					if (isUnix()==true) {
						sh "docker-compose build"
						echo "Docker build complete"
					}
					else {
						bat "docker-compose build"
						echo "Docker build complete"
					}
				}
            }
        }
        Stage('Stage 3--> Run - run dockerized application.'){
            steps {
				script{
					if (isUnix()==true) {
						sh "docker-compose build"
						echo "Docker build complete"
					}
					else {
						bat "docker-compose build"
						echo "Docker build complete"
					}
				}
            }
        }
        stage('Stage 3--> Docker UP') {
            steps {
				script{
					if (isUnix()==true) {
						sh "docker-compose up -d"
						echo "Docker Container is running! Flask online."
						docker_run_check = 1
					}
					else {
						bat "docker-compose up -d"
						echo "Docker Container is running! Flask online."
						docker_run_check = 1
					}
				}
            }
		}
		 stage('Stage 4--> Testing - Run test by selenium') {
            steps {
				script {
					if (isUnix()==true) {
						sh "pip install selenium"
						sh "python3 tests//e2e.py"

					}
					else {
						bat "pip install selenium"
						bat "cd tests"
						bat "python tests//e2e.py"
					}
				}
            }
		}
		stage('Stage 4--> Docker push') {
            steps {
				script{
					if (isUnix()==true) {
						sh 'docker push omerkenig/wog_omer'

					}
					else {
								bat 'docker push omerkenig/wog_omer'
					}
				}
            }
		}
		stage('Stage 5--> Finalize') {
            steps {
				script{
					if (isUnix()==true) {
					sh "docker stop omerkenig/wog_omer:1.1.1 "
					sh "docker rm omerkenig/wog_omer:1.1.1 "
					sh "docker rmi omerkenig/wog_omer"
					echo "Docker Container has been terminated & removed."
					sh 'docker logout'
					echo "Logged out of Dockerhub"
					}
					else {
                    bat "docker stop omerkenig/wog_omer:1.1.1 "
					bat "docker rm omerkenig/wog_omer:1.1.1 "
					bat "docker rmi omerkenig/wog_omer"
					echo "Docker Container has been terminated & removed."
					bat 'docker logout'
					echo "Logged out of Dockerhub"					}
				}
            }
		}
		}
		}