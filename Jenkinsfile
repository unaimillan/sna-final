pipeline {
  agent any
  stages{
    stage("build"){
      steps {
        echo "test build"
        sh 'sudo apt update'
        sh 'sudo apt install python3-pip'
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
