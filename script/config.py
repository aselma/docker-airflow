import os
from cryptography.fernet import Fernet

fernet_key= Fernet.generate_key().decode()

os.system("echo 'AIRFLOW__CORE__FERNET_KEY={}' >> /root/.bashrc".format(fernet_key))
os.system("export AIRFLOW__CORE__FERNET_KEY")