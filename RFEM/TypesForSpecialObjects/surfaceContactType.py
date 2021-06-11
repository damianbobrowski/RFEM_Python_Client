from RFEM.initModel import *
from RFEM.enums import SetType

class SurfaceContactType():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Surface Contact Type
        clientObject = clientModel.factory.create('ns0:surfaces_contact_type')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Contact Type No.
        clientObject.no = no

        # Add Surface Contact Type to client model
        clientModel.service.set_surfaces_contact_type(clientObject)