node {
    stage("Checkout Repo"){
        git branch: 'main',
        url: 'https://github.com/Dmytry-S/EOS_API_tests_preprod.git'
    }

    stage("Create venv & run test"){
        sh 'virtualenv venv && sh ./venv/bin/activate && pip3 install -r requirements.txt && cd ./tests && pytest test_api_tests.py'
    }
}
