pipeline {
  agent any
  stages{
    stage("build"){
      steps {
        echo "test build"
      }
    }
    stage("test"){
      steps {
        echo "test test"
        sh 'python test.py'
      }
    }
    stage("deploy"){
      steps {
        echo "test test"
      }
    }
  }
}
