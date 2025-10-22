import pymysql  

miConexion = pymysql.connect(host='localhost', user='root', password='12345', db='empresa')

print(miConexion)