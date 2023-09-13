
pipeline {
    agent any
    stages {
        stage('Run Tests and Sleep') {
            parallel {
                stage('Test') {
                    steps {
                        sh 'python3 -m pytest test.py'
                    }
                }
                stage('Sleep') {
                    steps {
                        sleep(time: 2, unit: 'SECONDS')
                    }
                }
            }
        }
    }
}
