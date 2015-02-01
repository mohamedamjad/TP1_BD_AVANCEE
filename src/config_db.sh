#! /bin/bash
echo This program will install the following packages:
echo pip3 for python3
echo psycopg2 plugin for python3
echo pymongo plugin for python3
sudo apt-get install python3-pip
sudo pip3 install psycopg2
sudo pip3 install pymongo
sudo -u postgres createuser --superuser mit15
sudo -u postgres createdb mit15
sudo apt-get install mongodb
sudo apt-get install mongodb-server
sudo apt-get install mongodb-clients
