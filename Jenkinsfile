pipeline {
  agent any
  stages{
    stage("build"){
      steps {
        echo "test build"
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage("test"){
      steps {
        echo "test test"
        sh 'python3 test.py'
      }
    }
    stage("deploy"){
      steps {
        echo "test test"
      }
    }
  }
}
