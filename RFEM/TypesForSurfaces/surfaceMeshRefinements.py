from RFEM.initModel import *
from RFEM.enums import SetType

class SurfaceMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Surface Mesh Refinement
        clientObject = clientModel.factory.create('ns0:surface_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Mesh Refinement No.
        clientObject.no = no

        # Add Surface Mesh Refinement to client model
        clientModel.service.set_surface_mesh_refinement(clientObject)