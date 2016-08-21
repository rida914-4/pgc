__author__ = 'lap-0079'


import cx_Oracle

con = cx_Oracle.connect('pgc_am/pass@42.201.238.170/orcl')

# con = cx_Oracle.connect('django/django@server/orcl')
print con.version
con.close()