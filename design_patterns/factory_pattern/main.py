from .factory import CritterFactory

critter = CritterFactory().get_critter(length=9000, width=10, height=10)
print(critter.get_name())
