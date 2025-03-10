pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/VladNedilko/AntihypeTestPython.git', branch: 'master'
            }
        }
        stage('Run Tests') {
            steps {
                dir('test') {
                    bat '"C:\\Users\\rregi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" unit_tests.py'
                    bat '"C:\\Users\\rregi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" integration_tests.py'
                    bat '"C:\\Users\\rregi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" performance_tests.py'
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