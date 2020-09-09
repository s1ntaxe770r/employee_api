# employee_api


### A simple API to manage your staff


## Usage

-  using the Dockerfile clone the repo and within the project directory ` docker build -t <image name> .  `

- The image is also  available on [Dockerhub](https://hub.docker.com/r/e770r/micro-manager) 

now `docker run -p 8000:8000 micro-manager`


# Endpoint

` hosturl.com/api/v1/employees `


 |HTTP Method| Description |
| ----------- | ----------- |
| GET         | returns all the employees     |
| POST    |  will create a new employee     |
| DELETE  | removes an employee |
| PUT   | updates employee information |

 
