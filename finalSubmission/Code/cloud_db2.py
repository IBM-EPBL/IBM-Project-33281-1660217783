import ibm_db
hostname="19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"

uid="yrx08873"
pwd="3q2cVkfmwZwvH8UU"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="30699"
protocol="TCP/IP"
cert="Certificate.crt"

dsn=(
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5};"
    ).format(db,hostname,port,uid,cert,pwd)
print(dsn)


try:
    db2=ibm_db.connect(dsn,"","")
    print("connected to data base")
except:
    print("unable to connect",ibm_db.conn_errormsg())