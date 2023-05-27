#!/bin/bash
cd /home/jordan_esc/Proyectos/SAE_gestionDeUsuarios_ms
source gdu-env/bin/activate
sudo docker compose down
sudo docker rmi sae_gestion_de_usuarios_ms:latest
#sudo docker volume rm sae_gestiondeusuarios_ms_postgres-data 
sudo docker compose up