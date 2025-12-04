from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50, title = 'Enter the name in less than 50 words', description= 'Enter the patient Name', examples=['Ashutosh Jaiswal','Ashu'])]
    age: Annotated[int, Field(gt=0, lt=120)]
    email: EmailStr
    linked_in : Optional[AnyUrl ] = None
    weight : Annotated[float, Field( gt=0, description="Weight must be greater than zero", strict=True)] 
    marriage_status : bool 
    allergies : Optional[List[str]] = None
    contact_detail : Dict[str,str]


def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.marriage_status)
    print(patient.contact_detail)
    print("Patient inserted successfully.")

patient_info = {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'email': 'abc@gmail.com', 'marriage_status': True, 'allergies' : ['dust','pollen'], 'contact_detail' : {'phone':'9721478489'} }

patient1 = Patient(**patient_info)

insert_patient(patient1)

