from sklearn.metrics import mean_squared_error
from response import Response
from sswn_weights import Weights


class Population:

    def __init__(self, structure, size):
        self.size = size
        self.genotyp = self.genotyp_init(structure)

    def genotyp_init(self, structure):
        genotyp = []
        for i in range(self.size):
            genotyp.append(Gen(structure))
        return genotyp

    def compute(self, structure, u_input, y_target):
        for i in range(self.size):
            resp = Response(u_input, self.genotyp[i].weight, structure)
            self.genotyp[i].mse = mean_squared_error(resp.output, y_target)

    def sort(self):
        self.genotyp = sorted(self.genotyp, key=lambda genotyp: genotyp.mse)

    def get_best_mse(self):
        self.sort()
        return self.genotyp[0].mse

    def get_best_genotyp(self):
        self.sort()
        return self.genotyp[0]

    def get_best_gens(self, best_size, structure):
        if best_size > self.size:
            return self
        else:
            new_pop = Population(structure, best_size)
            for i in range(best_size):
                new_pop.genotyp[i] = self.genotyp[i]
            return new_pop

    def update(self, best_size, random_size, anneal_size, anneal_temperature, structure):
        self.sort()

        if self.size > best_size:
            for i in range(random_size):
                self.genotyp[best_size+i] = Gen(structure)

        if self.size > (best_size+anneal_size):
            for i in range(anneal_size):
                self.genotyp[best_size + random_size + i].g_anneal(anneal_temperature)

    def concatenate(self, second_population):
        self.size = self.size + second_population.size
        for i in range(second_population.size):
            self.genotyp.append(second_population.genotyp[i])


class Gen:

    def __init__(self, structure):
        self.weight = Weights(structure)
        self.mse = None

    def g_anneal(self, temperature):
        self.weight.anneal(temperature)
        self.mse = None
