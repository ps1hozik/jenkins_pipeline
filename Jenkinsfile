pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/ps1hozik/jenkins_pipeline.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m pytest
                '''
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
