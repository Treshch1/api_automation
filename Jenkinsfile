node {
    stage("Checkout repo"){
        git branch: 'main',
        url: 'https://github.com/Treshch1/api_automation.git'
    }
    stage("Install dependencies"){
        sh 'pyenv activate api_automation'
    }
}
