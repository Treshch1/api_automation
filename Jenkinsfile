pipeline {
    agent any
    environment {
        BASE_URL = 'https://staging.icans.ai/api/v1'
        USER_EMAIL = 'vladislavtreshcheyko+owner@gmail.com'
        USER_PASSWORD = 'Qqwe1123'
    }
    stages {
        stage("Checkout repo"){
            steps {
                git branch: 'main',
                url: 'https://github.com/Treshch1/api_automation.git'
            }
        }
        stage("Install dependencies"){
            steps {
                withPythonEnv('/Users/treshch/.pyenv/versions/api_automation/bin/') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage("Run tests"){
            steps {
                withPythonEnv('/Users/treshch/.pyenv/versions/api_automation/bin/') {
                sh 'pytest'
            }
            }
        }
    }
}
