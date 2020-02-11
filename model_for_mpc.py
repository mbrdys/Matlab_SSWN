from population import Population
from sswn_structure import Structure


class ModelForMPC:

    def __init__(self, data, params):
        self.structure = Structure(params.input_size, params.output_size,
                                   params.state_size, params.wavelons_number)
        self.data = data
        self.weights = self.compute_weights(params.pop_size, params.best_size, params.random_size,
                                            params.anneal_size, params.sswn_stop_condition,
                                            params.anneal_temperature)

    def compute_weights(self, pop_size, best_size, random_size, anneal_size, stop_cond, anneal_temperature):
        population = Population(self.structure, pop_size)
        population.compute(self.structure, self.data.u_input, self.data.y_target)

        while population.get_best_mse() > stop_cond:
            population.update(best_size, random_size, anneal_size, anneal_temperature, self.structure)
            population.compute(self.structure, self.data.u_input, self.data.y_target)

        return population.get_best_genotyp().weight
