Prueba de API de manera local

source gdu-env/bin/activate
uvicorn app:app --reload

En caso de ejecutarlo de manera local
y de tener postgres en su SO ejecutandose en el mismo
puerto que el de docker en linux ejecutar en consola;

/etc/init.d/postgresql stop


Para correr los 3 contenedores ejecutar

sudo docker compose up


necesita un .env con las siguientes variables



DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=