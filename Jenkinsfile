pipeline {
  agent { docker 'python'}
  stages {
    stage('Test') {
      steps {
        sh 'python ./main.py < potato add 6'
      }
    }
  }
}
