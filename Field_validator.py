from pydantic import BaseModel, Field, field_validator, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    age : int
    weight : float
    email : EmailStr
    allergy : List[str]
    marriage : bool
    contact_detail : Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain = ['hdfc.com','icici.com']
        
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):

        return value.upper()
        

def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.allergy)
    print(patient.marriage)
    print(patient.contact_detail)
    print("Patient inserted successfully.")

    


patient_info = {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'email': 'abc@hdfc.com', 'marriage': True, 'allergy' : ['dust','pollen'], 'contact_detail' : {'phone':'9721478489'} }

patient1 = Patient(**patient_info)

insert_patient(patient1)


    