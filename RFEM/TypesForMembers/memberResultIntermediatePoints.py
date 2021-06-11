from RFEM.initModel import *
from RFEM.enums import SetType

class MemberResultIntermediatePoint():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Member Result Intermediate Point
        clientObject = clientModel.factory.create('ns0:member_result_intermediate_point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Result Intermediate Point No.
        clientObject.no = no

        # Add Member Result Intermediate Point to client model
        clientModel.service.set_member_result_intermediate_point(clientObject)