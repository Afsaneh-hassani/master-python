# import modules and global variables
from abc import ABC, abstractmethod
import string
import random


# definition of class password generation
class PasswordGeneratorAbstract(ABC):
    
    
    @abstractmethod
    
    def generate_password(self,length=8):
        pass
    


# definition of class numeric password
class NumericPasswordGenarator(PasswordGeneratorAbstract):
    letters=string.digits
    
    def generate_password(self,length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))




# definition of class ascii password
class LetterPasswordGenerator(PasswordGeneratorAbstract):
    letters=string.ascii_letters
    
    def generate_password(self,length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))




# definition of class combination password
class MixedPasswordGenerator(PasswordGeneratorAbstract):
    letters=string.ascii_letters + string.digits
    
    def generate_password(self,length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))





# main function
generator=MixedPasswordGenerator()


print(generator.generate_password(20))