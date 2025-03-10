pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://ваш-git-репозиторій.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'sudo apt-get install renpy -y'  // Встановлення Ren'Py
                sh 'pip install pytest pytest-junitxml'
            }
        }

        stage('Run Syntax Check') {
            steps {
                sh 'renpy check game/'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pytest --junitxml=reports/unit.xml tests/test_jumps.py'
                sh 'pytest --junitxml=reports/ui.xml tests/test_ui.py'
            }
        }

        stage('Generate Report') {
            steps {
                junit 'reports/*.xml'
                sh 'echo "Тестування завершено. Перевірте звіт у Jenkins"'
            }
        }
    }

    post {
        failure {
            mail to: 'ваш-email@example.com',
                 subject: "Помилка у тестуванні гри",
                 body: "Деякі тести не пройшли. Деталі: ${env.BUILD_URL}"
        }
    }
}
