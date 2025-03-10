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
                bat 'C:\\Users\\Rezi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install pytest'
            }
        }

        stage('Install RenPy') {
            steps {
                bat 'choco install renpy -y'  // Встановлення Ren'Py
            }
        }

        stage('Run Syntax Check') {
            steps {
                bat '"C:\\ProgramData\\chocolatey\\lib\\renpy\\tools\\renpy.exe" check game/'
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
            echo 'Build failed. Check logs for details.'  // Тимчасово відключіть email
        }
    }
}
