pipeline {
    agent any
    stages {
        
        stage("build") {
            steps {
                echo 'building application ...'
            }
        }
        
        stage("test") {
            steps {
                echo 'testing application ...'
                script {
                    // def test = 2 + 2 > 3 ? 'cool' : 'not cool'
                    // echo test
                    sh 'python api-cat-image.py'
                }
            }
        }
        
        stage("deploy") {
            steps {
                echo 'deploying application ...'
            }
        }
    }
}

/*
node {
    groovy script
}
*/
