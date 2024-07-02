import psycopg2

def lire_requetes_sql(fichier_sql):
    with open(fichier_sql, 'r') as file:
        requetes = file.read()
    return requetes

try:

connection = psycopg2.connect(database= exam_MADOUGOU,
                        host=3.253.139.171,
                        user= daniel,
                        password= datascientest,
                        port= 5432)


cursor = connection.cursor()
requetes = lire_requetes_sql('SQL_Partie2_exam_MADOUGOU.txt')
for requete in requetes.split(';'):
    if requete.strip():  
        cursor.execute(requete)
        connection.commit()  

if requete.strip().upper().startswith('SELECT'):
    rows = cursor.fetchall()
    for row in rows:
        print(row)



cursor.close()
connection.close()