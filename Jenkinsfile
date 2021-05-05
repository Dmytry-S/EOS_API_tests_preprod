node {
    stage("Checkout Repo"){
        git branch: 'main',
        url: 'https://github.com/Dmytry-S/EOS_API_tests_preprod.git'
    }

    stage("Create venv"){
        sh 'virtualenv venv'
    }

    stage("Add deps"){
        sh 'pip install -r requirements.txt'
    }

    stage("Run tests"){
        sh 'pytest test_api_tests.py'
    }
}
