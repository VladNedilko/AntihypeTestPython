pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/VladNedilko/AntihypeTestPython', branch: 'master'
            }
        }
        stage('Run Tests') {
            steps {
                dir('test') {
                    sh 'python unit_tests.py'
                    sh 'python integration_tests.py'
                    sh 'python performance_tests.py'
                }
            }
        }
    }

    post {
        always {
            echo 'Tests execution completed.'
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}