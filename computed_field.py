from pydantic import BaseModel, Field,  EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    age : int
    weight : float # kg
    height : float # meter
    email : EmailStr
    allergy : List[str]
    marriage : bool
    contact_detail : Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2) ,2)
        return bmi

    
        

def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.allergy)
    print(patient.marriage)
    print(patient.contact_detail)
    print("BMI:", patient.bmi)
    print("Patient inserted successfully.")

    


patient_info = {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'email': 'abc@hdfc.com',
                'marriage': True, 'allergy' : ['dust','pollen'], 'contact_detail' : {'phone':'9721478489'},'height' : 1.75 }

patient1 = Patient(**patient_info)

insert_patient(patient1)


    