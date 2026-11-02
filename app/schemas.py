from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr,Field,StringConstraints

borrower_nameStr=Annotated[str,StringConstraints(min_length=2,max_length=60)]
purposeStr=Annotated[str,StringConstraints(min_length=5,max_length=100)]
statusStr=Annotated[str,StringConstraints(min_length=5,max_length=100)]
class UserCreate(BaseModel):
    id: int  None =Field (default=None,gt=0)
    equipment_id: int  None =Field (default=None,gt=0)
    borrower_name:borrower_nameStr
    purposeStr:purposeStr
    loan_days:int = Field(gt=1,lt=14)
    status:statusStr

    class UserRead(BaseModel):
        model_config=ConfigDict(from_attributes=True)
        User_id: int Field(validation_alias="id")
        borrower_name:borrower_nameStr
        purposeStr:purposeStr
        equipment_id:int
        loan_days:int
        
        

