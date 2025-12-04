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