# python-mongo-oracle

Intall pymongo by running command:
$ python3 -m pip install pymongo[tls]

Intall cx_Oracle
Download Oracle client libraries — Instant Client Package - Basic
https://www.oracle.com/database/technologies/instant-client.html

Unzip and move all file inside into your project with same level of .py file, such as below screenshot, this could avoid calling cx_Oracle.init_oracle_client(lib_dir=ORACLE_CLIENT_DIR), if Oracle client libraries are in different folder, then need to call cx_Oracle.init_oracle_client(lib_dir=ORACLE_CLIENT_DIR) and specify the folder

refer to https://stackoverflow.com/questions/56119490/cx-oracle-error-dpi-1047-cannot-locate-a-64-bit-oracle-client-library
