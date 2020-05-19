# docker_cluster_demo

## Used technologies:
- apache 2.4 for proxy server
- python + flask for app server
- mysql for database

## Prerequisites
Make sure you have already installed both Docker Engine and Docker Compose.
Make sure you have port 80 free and available otherwise apache will not start up.

## Usage:
From the command line go to the project root and start the docker cluster:
cd <project_root>
docker-compose up

Application is listening on http://localhost:80

Application will show total number of accesses and list all content of access_journal table (note as user authentication was not implemented the user name and surname data is static value)

