from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getlistCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self):
        return DAO.getCorsiPD()