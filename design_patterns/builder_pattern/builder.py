from .critters import Critter


class CritterBuilder:
    @staticmethod
    def build_critter(age, height, weight):
        critter = Critter()
        critter.set_age(age)
        critter.set_height(height)
        critter.set_weight(weight)
        return critter
