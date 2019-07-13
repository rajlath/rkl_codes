class Allergies(object):

    allergie_list = ['eggs',        # 1
                    'peanuts',     # 2
                    'shellfish',   # 4
                    'strawberries',# 8
                    'tomatoes',    # 16
                    'chocolate',   # 32
                    'pollen',      # 64
                    'cats',        # 128
                    ]

    def __init__(self, score):
        self.lst = [allergie for i, allergie in enumerate(Allergies.allergie_list)
                    if 0 < (score & 1 << i )]

    def is_allergic_to(self, item):
        return allergie in self.lst

    @property
    def lst(self):
        pass
