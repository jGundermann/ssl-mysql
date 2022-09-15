# MySQL + SSL setup

This repository contains the necessary files to set up a simple MySQL deployment with SSL enabled (self-signed certs).

# Running

On the first start, generate the required certificates with `./gen_ssl.sh` (this is only required on the first start).

Then, start the mysql service with `docker-compose up -d`.

Once the service is running, you can ensure everything works by `exec`ing into the container and trying to connect to the server:

```bash
$ docker-compose exec mysql bash
# mysql --host 127.0.0.1 --port 3306 --ssl-mode=VERIFY_IDENTITY --ssl-cert=/var/lib/mysql/certs/client-cert.pem --ssl-key=/var/lib/mysql/certs/client-key.pem --ssl-ca=/var/lib/mysql/certs/ca.pem
```

You may also use the provided python script to connect: `./test_pymysql.py`
