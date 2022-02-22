Provision a new site
====================

## Required packages:

* nignx
* Python 3.6 (for this example...)
* virtualenv + pip (but consider Poetry)
* Git

eg, on Ubuntu

    sudo add-apt-repository ppa:deadsnakes/ppa && apt update
    sudo apt install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.config
* replace DOMAIN with site staging url (e.g. staging.my-domain.com)
* replace USERNAME with non-admin user account name

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with site staging url (e.g. staging.my-domain.com)
* replace USERNAME with non-admin user account name

## Folder structure:

Assuming a user account at /home/username
```
/home/username
+--sites
   +-- DOMAIN1
   |   +-- .env
   |   +-- db.sqlite3
   |   +-- manage.py etc
   |   +-- static
   |   +-- virtualenv
   |   +-- 
   |
   +-- DOMAIN2
       +-- .env etc
```



