FROM mysql:latest

ENV MYSQL_DATABASE swat

RUN mkdir -p /etc/certs
COPY certs/*.pem /etc/certs/
RUN chown -R mysql:mysql /etc/certs