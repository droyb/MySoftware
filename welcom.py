properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
pipeline {
    agent any

    stages {
        stage('new screen') {
            steps {
                echo 'new screen'
            }
        }
    }
}
