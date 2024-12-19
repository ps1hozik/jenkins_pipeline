pipeline {
    agent {
        docker {
            image 'python:3.12'
        }
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/ps1hozik/jenkins_pipeline.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t task-app .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy stage...'
            }
        }
    }
}
