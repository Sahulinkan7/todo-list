pipeline{
    agent any
    stages{
        stage("clone todo application code"){
            steps{
                echo "cloning from github"
                git url:"https://github.com/Sahulinkan7/todo-list.git",branch:"main"
            }
            post{
                success{
                    echo "github clone done"
                }
            }
        }
        stage("Building the code : building docker image"){
            steps{
                echo "building docker image for the application."
                sh "docker build -t todoapp ."
            }
            post{
                success{
                    echo "building image done"
                }
            }
        }
        stage("pushing image to docker hub"){
            steps{
                echo "pushing the image to docker hub"
                withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubpass",usernameVariable:"dockerHubuser")]){
                    sh "docker tag todoapp ${env.dockerHubuser}/todoapp:latest"
                    sh "docker login -u ${env.dockerHubuser} -p ${env.dockerHubpass}"
                    sh "docker push ${env.dockerHubuser}/todoapp:latest"
                }
            }
            post{
                success{
                    echo "Image pushed to dockerhub registry."
                }
            }
        }
        stage (" pull image from dockerhub and run on slave node")
        {
            agent{
                label 'slave'
            }
            steps{
                echo "running todo app container in aws slave node"
                sh "docker-compose up -d"
            }
            post{
                success{
                    echo "======== container running in 8000 port of slave node========"
                }
                failure{
                    echo "======== docker container is not running ========"
                }
            }
        }
    }
    post{
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}