# Example of docker microservice architecture composed of three flask applications

There are two branches, "main" for Linux hosts and "windows" for Windows hosts.
The difference is that on Windows systems one more step needs to take place in order to build the flask2 Dockerfile.

### Main functionalities

- flask1 acts as a "coordinator", it calls the other two services to trigger several actions
- flask1 publishes port 80 -> 5000 (5000:80) (code commented in docker-compose.yml)
- flask2 can save a file into disk (with no persistence)
- flask3 can save a file into disk with persistence

For further information, check all the endpoints provided in each of the flask services and watch the video provided in the description.
