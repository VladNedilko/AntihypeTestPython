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
                    bat 'python unit_tests.py'
                    bat 'python integration_tests.py'
                    bat 'python performance_tests.py'
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