import itertools

class Allergies:
    allergy_dictionary = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, score):
        allergens = []
        for i in range(len(self.allergy_dictionary)):
            for j in itertools.combinations(self.allergy_dictionary.values(), i):
                if sum(j) == self.score:
                    for item in j:
                        for allergen, a_score in self.allergy_dictionary.items():
                            if a_score == item:
                                allergens.append(allergen)
        return allergens


# allergy = Allergies(129)
#
# allergy.is_allergic_to(129)

