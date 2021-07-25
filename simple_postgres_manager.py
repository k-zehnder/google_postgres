from subprocess import PIPE,Popen
import shlex
import gzip
import subprocess
import os

host = "localhost"
port = 5432
username = "zelda"
password = "password"
database = "emptydb" 

# def dump_schema(host, dbname, user, password, **kwargs):
#     command = f'pg_dump -h={host} ' \
#         f'--dbname={dbname} ' \
#         f'--username={user} ' \
#         f'--no-password ' \
#         f'--format=c ' \
#         f'--file=/tmp/schema.dmp '

#     proc = Popen(command, shell=True, env={
#         'PGPASSWORD': password
#     })
#     proc.wait()

# print(dump_schema(host, database, username, password))

import subprocess

DB_NAME = 'emptydb'  # your db name

DB_USER = 'zelda' # you db user
DB_HOST = "localhost"
DB_PASSWORD = 'password'# your db password
dump_success = 1
print('Backing up %s database ' % (DB_NAME))
command_for_dumping = f'pg_dump --host={DB_HOST} ' \
            f'--dbname={DB_NAME} ' \
            f'--username={DB_USER} ' \
            f'--no-password ' \
            f'--file=backup.dmp '
try:
    proc = subprocess.Popen(command_for_dumping, shell=True, env={
                'PGPASSWORD': DB_PASSWORD
                })
    proc.wait()

except Exception as e:
    dump_success = 0
    print('Exception happened during dump %s' %(e))


if dump_success:
    print('db dump successfull')
    print('restoring to a new database database')
