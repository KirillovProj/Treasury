from .builder import CritterBuilder

critter = CritterBuilder().build_critter(12, 100, 50)

print(type(critter))  # Critter class instance
print(critter.age)  # 12
print(critter.height)  # 100
print(critter.weight)  # 50
