from faker import Faker

fake = Faker(['ru_RU'])  

class DataCreatedUser:

    @staticmethod
    def generate_body():
        return {
            "email": fake.unique.email(),      
            "password": fake.password(length=8),  
            "name": fake.first_name() + str(fake.random_int(min=100, max=999))  
        }
