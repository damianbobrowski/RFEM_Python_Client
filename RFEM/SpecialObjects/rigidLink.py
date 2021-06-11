from RFEM.initModel import *
from RFEM.enums import SetType

class RigidLink():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Rigid Link
        clientObject = clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Add rigid link to client model
        clientModel.service.set_rigid_link(clientObject)

    def LineToLine(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Line To Line Rigid Link
        clientObject = clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Add rigid link to client model
        clientModel.service.set_rigid_link(clientObject)

    def LineToSurface(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Line To Surface Rigid Link
        clientObject = clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Add rigid link to client model
        clientModel.service.set_rigid_link(clientObject)

    def Diapragm(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Diapragm Rigid Link
        clientObject = clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Add rigid link to client model
        clientModel.service.set_rigid_link(clientObject)