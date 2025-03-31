from database import DAO


class Model:
    def __init__(self):
        pass

    def getlistCodins(self):
        return DAO.getlistCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self):
        return DAO.getCorsiPD()