from RFEM.initModel import *
from RFEM.enums import SetType

class SurfaceStiffnessModification():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Surface Stifness Modification
        clientObject = clientModel.factory.create('ns0:surface_stiffness_modification')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Stifness Modification No.
        clientObject.no = no

        # Add Surface Stifness Modification to client model
        clientModel.service.set_surface_stiffness_modification(clientObject)