#!/bin/sh
set -x

read -p "Enter the hostname  " hostname
read -p "how many host to create " NUM
read -p "Enter the contact email " email
read -p "Enter the server role " role
read -p "Enter the environment " senv
echo "HOST, contact, role, senv"

for item in $(seq -w 0$NUM)
 do

salt 'houvlxsalt01*' etcd.set /store/${hostname}"${item}".eogresources.com/contact "${email}"
salt 'houvlxsalt01*' etcd.set /store/${hostname}"${item}".eogresources.com/senv "${senv}"
salt 'houvlxsalt01*' etcd.set /store/${hostname}"${item}".eogresources.com/role "${role}"

done
