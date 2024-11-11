pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out repository...'
                git 'https://github.com/Vignesh-war-Reddy/GUESS_NUMBER.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '. venv/bin/activate && python -m unittest discover'
            }
        }
    }
}
