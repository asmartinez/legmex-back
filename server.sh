#!/bin/bash
# Scrip para iniciar el server necesario 
mkdir dataElasticSearch
cd dataElasticSearch
mkdir es01
mkdir es02
mkdir es03
cd ..
mkdir dataPostgresql
cd dataPostgresql
mkdir datadir
cd ..
sudo sysctl -w vm.max_map_count=262144
docker-compose up 