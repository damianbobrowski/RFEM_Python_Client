from RFEM.initModel import *
from RFEM.enums import SetType

class MemberSupport():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Member Support
        clientObject = clientModel.factory.create('ns0:member_support')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Support No.
        clientObject.no = no

        # Add Member Support to client model
        clientModel.service.set_member_support(clientObject)