pipeline {
    agent any
    environment {
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
        stage("Set environmental variables"){
            steps {
                script {
                    env.BASE_URL = "${params.BASE_URL_PARAM}"
                }
                sh "echo $BASE_URL"
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
                sh "echo $BASE_URL"
                withPythonEnv('/Users/treshch/.pyenv/versions/api_automation/bin/') {
                    sh 'pytest'
                }
            }
        }
    }
}
