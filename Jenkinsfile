pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh 'mvn -f java-tomcat-sample/pom.xml clean package'
            }
        }
           Stage('Build'){
            steps {
                sh "docker build . -t tomcatsamplewebapp:${env.BUILD_ID}"
            }
        }
    }
}