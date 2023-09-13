
pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh 'python3 -m pytest test.py'
            }
        }
        stage('sleep') {
            steps {
                sleep(time:3, unit: 'MINUTES')
            }
        }
    }
}

