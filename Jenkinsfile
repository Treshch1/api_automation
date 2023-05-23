pipeline {
    agent any
    environment {
        BASE_URL = 'https://staging.icans.ai/api/v1'
        USER_EMAIL = credentials('user_email')
        USER_PASSWORD = credentials('user_password')
    }
    stages {
        stage('Setup parameters') {
            steps {
                script {
                    properties([
                        parameters([
                            choice(
                                choices: ['https://staging.icans.ai/api/v1', 'https://www.google.com/search'],
                                name: 'BASE_URL_PARAM'
                            )
                        ])
                    ])
                }
            }
        }
        stage("Override environmental variables"){
            steps {
                sh 'export BASE_URL=${params.BASE_URL_PARAM}'
            }
        }
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
