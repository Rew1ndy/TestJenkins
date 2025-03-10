pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://ваш-репозиторій.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install pytest renpy'
            }
        }

        stage('Run Syntax Check') {
            steps {
                bat 'renpy check game/'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --junitxml=reports/unit.xml tests/test_jumps.py'
                bat 'pytest --junitxml=reports/ui.xml tests/test_ui.py'
            }
        }

        stage('Publish Results') {
            steps {
                junit 'reports/*.xml'
            }
        }
    }

    post {
        failure {
            mail to: 'ваш-email@example.com',
                 subject: 'Помилка тестування',
                 body: "Деталі: ${env.BUILD_URL}"
        }
    }
}
