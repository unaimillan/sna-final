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
        echo "test deploy"
        sh 'ssh-keyscan -t rsa 10.0.0.12 >> ~/.ssh/known_hosts'
        sshagent(['1703f27e-4edd-453a-8f8a-978db4dfe12a']) {
            sh 'scp deploy.sh ubuntu@10.0.0.12:~'
            sh 'ssh ubuntu@10.0.0.12 "sudo sh deploy.sh"'
        }
        sh 'ssh-keyscan -t rsa 10.0.0.13 >> ~/.ssh/known_hosts'
        sshagent(['1703f27e-4edd-453a-8f8a-978db4dfe12a']) {
            sh 'scp deploy.sh ubuntu@10.0.0.13:~'
            sh 'ssh ubuntu@10.0.0.13 "sudo sh deploy.sh"'
        }
        
      }
    }
  }
}
