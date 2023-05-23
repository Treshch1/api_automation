node {
    stage("Checkout repo"){
        git branch: 'main',
        url: 'https://github.com/Treshch1/api_automation.git'
    }
    stage("Install dependencies"){
            withPythonEnv('api_automation') {
                sh 'pip install ipdb'
        }
    }
}
