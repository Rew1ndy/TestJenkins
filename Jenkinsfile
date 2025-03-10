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
                bat 'C:\\Users\\Rezi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install pytest renpy'
            }
        }

        stage('Run Syntax Check') {
            steps {
                bat 'C:\\Users\\Rezi\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\renpy.exe check game/'
                bat 'git status'  // Проверка состояния репозитория
                bat 'type game/script.rpy'  // Проверка содержимого файла
            }
        }

        stage('Run Tests') {
            steps {
                bat 'C:\\Users\\Rezi\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest.exe --junitxml=reports/unit.xml tests/test_jumps.py'
                bat 'C:\\Users\\Rezi\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest.exe --junitxml=reports/ui.xml tests/test_ui.py'
                // bat 'pytest --junitxml=reports/unit.xml tests/test_jumps.py'
                // bat 'pytest --junitxml=reports/ui.xml tests/test_ui.py'
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
