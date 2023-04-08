pipeline {
    agent any
    stages {
        stage('Code') {
            steps{
                git url: 'https://github.com/rohan-somkuwar/Doc-Compose-Project.git', branch: 'main'
            }
        }
        stage('Build') {
            steps{
                sh 'docker build . -t 9145503154/my-app-test:latest'
            }
        }
        stage('Push'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]){
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                    sh 'docker push 9145503154/my-app-test:latest'
                }
            }
        }
        stage('Test'){
            steps{
                echo "Testing this master pipline"
            }
        }
        stage('Deploy'){
            steps{
                echo "docker-compose down && docker-compose up -d"
            }
        }
    }
}
