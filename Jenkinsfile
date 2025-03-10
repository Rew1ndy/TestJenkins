pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Rew1ndy/TestJenkins.git'
                // Проверяем структуру репозитория
                bat 'dir game'  // Выводим содержимое папки game
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\Rezi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install pytest'
            }
        }

        // stage('Run Syntax Check') {
        //     steps {
        //         bat 'C:\\Users\\Rezi\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\renpy.exe check --no-renaming game/'
        //     }
        // }

        stage('Run Tests') {
            steps {
                bat 'C:\\Users\\Rezi\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest.exe --junitxml=reports/unit.xml tests/test_jumps.py'
                bat 'C:\\Users\\Rezi\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest.exe --junitxml=reports/ui.xml tests/test_ui.py'
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
            echo 'Build failed. Check logs for details.'  // Отключаем email до настройки SMTP
        }
    }
}
