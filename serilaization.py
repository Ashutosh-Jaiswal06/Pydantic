from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip_code: int
    state : str

class Patient(BaseModel):
    name: str
    age: int
    address: Address

address = {'street': 'jaypee Wishtown', 'city': 'Noida', 'zip_code':201304, 'state' : 'Uttar Pradesh'}
address_obj = Address(**address)

patient_info = {'name': 'John Doe', 'age': 30, 'address': address}
patient1 = Patient(**patient_info)
print(patient1)

print(patient1.address.city)
print(patient1.address.zip_code)
print(patient1.address.state)
print(patient1.address.street)
print(patient1.name)
print(patient1.age)
temp1 = patient1.model_dump()
temp2 = patient1.model_dump_json()
print(temp1)
print(type(temp1))
print(temp2)
print(type(temp2))
temp3 = patient1.model_dump(include= {'name','age','bmi'})
print(temp3)
temp4 = patient1.model_dump(exclude= ['contact_detail','allergy'])
print(temp4)

temp5 = patient1.model_dump(exclude = {'address' : ['state','city']})
print('this is temp5', temp5)
    