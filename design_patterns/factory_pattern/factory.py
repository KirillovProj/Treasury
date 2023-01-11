from .critters import SmallCritter, MediumCritter, BigCritter


class CritterFactory:
    """
    The critter factory class
    """
    @staticmethod
    def get_critter(length: int, width: int, height: int):
        params_sum = length + width + height
        if params_sum < 100:
            return SmallCritter()
        if params_sum < 500:
            return MediumCritter()
        else:
            return BigCritter()
