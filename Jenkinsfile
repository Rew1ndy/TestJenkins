pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Rew1ndy/TestJenkins.git'
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
