from RFEM.initModel import *
from RFEM.enums import SetType

class SurfaceResultsAdjustment():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Surface Result Adjustment
        clientObject = clientModel.factory.create('ns0:surface_results_adjustment')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Result Adjustment No.
        clientObject.no = no

        # Add Surface Result Adjustmentto client model
        clientModel.service.set_surface_results_adjustment(clientObject)