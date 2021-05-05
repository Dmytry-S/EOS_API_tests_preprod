node {
    stage("Checkout Repo"){
        git branch: 'main',
        url: 'https://github.com/Dmytry-S/EOS_API_tests_preprod.git'
    }

    stage("Create venv & run test"){
        sh 'pip install virtualenv && virtualenv venv && pip install -r requirements.txt && pytest test_api_tests.py'
    }
}
