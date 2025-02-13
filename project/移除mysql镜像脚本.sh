#!/bin/bash

# Stop and remove all containers running based on the 'mysql' image
echo "Stopping and removing MySQL containers..."
docker rm $(docker stop $(docker ps -aq --filter ancestor=mysql))

# Remove the MySQL image
echo "Removing MySQL image..."
docker rmi $(docker images -q mysql)

# Optionally, you can clean up all unused images
read -p "Do you want to remove all unused images? [y/N] " choice
case "$choice" in 
  y|Y ) echo "Cleaning up all unused images..."
        docker image prune -a;;
  * ) echo "No action taken.";;
esac