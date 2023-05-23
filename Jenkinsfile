node {
    stage("Checkout repo"){
        git branch: 'main',
        url: 'https://github.com/Treshch1/api_automation.git'
    }
    stage("Install dependencies"){
        withPythonEnv('/Users/treshch/.pyenv/versions/api_automation/bin/') {
            sh 'pip install -r requirements.txt'
        }
    }
    stage("Run tests"){
        withPythonEnv('/Users/treshch/.pyenv/versions/api_automation/bin/') {
            sh 'pytest'
        }
    }
}
