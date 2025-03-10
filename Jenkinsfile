pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Rew1ndy/TestJenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Варіант 1: Вказати повний шлях до Python (якщо не в PATH)
                bat 'C:\Users\Rezi\AppData\Local\Programs\Python\Python313\python.exe -m pip install pytest pytest-junitxml'

                // Варіант 2: Використовувати requirements.txt
                bat 'pip install -r requirements.txt'
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
