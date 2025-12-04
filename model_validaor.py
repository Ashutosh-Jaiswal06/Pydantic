from pydantic import BaseModel, Field, field_validator, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    age : int
    weight : float
    email : EmailStr
    allergy : List[str]
    marriage : bool
    contact_detail : Dict[str,str]

    @model_validator(mode= 'after')
    def emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_detail:
            raise ValueError('Emergy contact is mandatory for age anove 60')
        return model
    
    
        

def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.allergy)
    print(patient.marriage)
    print(patient.contact_detail)
    print("Patient inserted successfully.")

    


patient_info = {'name': 'John Doe', 'age': 65, 'weight': 70.5, 'email': 'abc@hdfc.com', 'marriage': True, 'allergy' : ['dust','pollen'], 'contact_detail' : {'phone':'9721478489', 'emergency': '8299640182'} }

patient1 = Patient(**patient_info)

insert_patient(patient1)


    