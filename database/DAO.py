from database.DB_connect import DBConnect
from model.corso import Corso


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getlistCodins():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query ="""select c.codins from corso c"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["codins"])


        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from corso c"""
        cursor.execute(query)

        res = []
        for row in cursor:# row è un dizionario e accedo alla chiave codins
            # res.append(Corso(codins=row["codins"], crediti=row["crediti"],
            #                  nome=row["nome"], pd=row["pd"]))
            res.append(**row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPD():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from corso c where c.pd=%s"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res

if __name__ == '__main__':
    print(DAO.getlistCodins())
    print(DAO.getAllCorsi())