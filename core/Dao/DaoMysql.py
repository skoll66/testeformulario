import os
if os.name == 'nt':
    import pymysql as MySQLdb
else:
    import pymysql as MySQLdb

def conect_mysql():
    try:
        connect = MySQLdb.connect(host='192.168.0.192',port=3306, user='glpisot',password="glpisot%401234",db="glpisot")
        cursor = connect.cursor()
        return connect, cursor
    except Exception as ex:
        print(ex)

def insertUsuario(cpf,sobrenome,nome,email):
    try:
       connect, cursor = conect_mysql()
       #sql= """UPDATE crapp_hml.u9t1i_fields_values SET value = \'{}\' WHERE item_id = {} and field_id ={};""".format(valor,condicao1,condicao2 )
       sql= """INSERT INTO glpisot.glpi_users(name,realname,firstname)VALUES(\'{}\',\'{}\',\'{}\');""".format(cpf,sobrenome,nome)
       cursor.execute(sql)
       connect.commit()
       sql2 = """INSERT INTO  glpisot.glpi_useremails(users_id, email)VALUES((SELECT id FROM glpisot.glpi_users where name =\'{}\'),\'{}\');""".format(cpf, email)
       cursor.execute(sql2)
       connect.commit()
       connect.close()
    except Exception as ex:
        print(ex)

def inserticket(cpf,texto,email,data):
    try:
       connect, cursor = conect_mysql()
       sql3= """INSERT INTO glpisot.glpi_tickets (name,content,date,date_creation,urgency,impact,priority,itilcategories_id)VALUES(\'{}\',\'{}\',\'{}\',\'{}\',3,3,3,4);""".format(cpf,texto,data,data)
       cursor.execute(sql3)
       connect.commit()
       sql4 = """INSERT INTO glpisot.glpi_tickets_users(tickets_id,users_id,alternative_email)VALUES((select id from glpisot.glpi_tickets where name = \'{}\' and date_creation =\'{}\'),(SELECT id FROM glpisot.glpi_users where name = \'{}\'),\'{}\');""".format(cpf, data,cpf, email)
       cursor.execute(sql4)
       connect.commit()
       connect.close()
    except Exception as ex:
        print(ex)

