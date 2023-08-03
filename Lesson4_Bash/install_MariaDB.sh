#!/bin/bash

# Update the list of packages
sudo apt update

#install MariaDB
sudo apt install mariadb-server -y

#pause to raise the base
sleep 10

#check database status
sudo systemctl status mariadb
