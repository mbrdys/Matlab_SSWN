import numpy as np


class Portfolio:

    def __init__(self, params, assets):
        self.params = params
        self.assets = assets.assets_list
        self.data = PortfolioData()
        self.constraints = params.portfolio_constraints
        self.short_data = None
        self.weights = None  # self.init_portfolio_weights()
        self.weighted_data = None  # self.get_weighted_data()
        self.model = None  # ModelForMPC(self.weighted_data, self.params)

    def init_portfolio_weights(self):
        inp = self.params.portfolio_number_of_assets
        weights = np.ndarray(shape=inp)
        return weights

    def get_weighted_data(self):
        return self.weights * self.data

    def prepare_portfolio_data(self):
        for asset in self.assets:
            self.data.append(asset)
        self.data.to_numpy()

    def get_sample_length(self):
        return len(self.data.quarter_date)

    def solve_the_portfolio(self, step, horizon):
        # prepare the data for limited samples:
        self.short_data = PortfolioShortData(self.data, [step, step + horizon])
        assets_respective_volatility = self.do_statistics()
        average_return_vector = self.short_data.relative.mean(1)*4  # TODO: why multiplied by 4 ??

        # TODO: initialize first portfolio weights
        self.weights = np.array([0.05, 0.05, 0.05, 0.35, 0.35, 0.15])

        # TODO: until optimum:
        j_value = self.calculate_current_j_function_value(assets_respective_volatility, average_return_vector)
        # TODO:     update portfolio weights if needed

        # TODO: as a return from above we get weighted portfolio VOLATILITY and optimal portfolio weights {pw}

        # TODO: convert short portfolio data into mpc_data.input & mpc_data.target
        # TODO: portfolio.model = ModelForMPC(self.weighted_data, self.params)
        # TODO: predict the next step expected return using Response(mpc_data.input, sswn_weights_matrix, structure)

        # TODO: compute the Monte Carlo prediction

    def do_statistics(self):
        correlation_matrix = np.corrcoef(self.short_data.relative)  # why not origin?
        vv = np.empty(0)
        for row in self.short_data.relative:
            vv = np.append(vv, np.std(row, ddof=1)*2)

        assets_respective_volatility = (vv * correlation_matrix).transpose() * vv
        return assets_respective_volatility

    def calculate_current_j_function_value(self, respective_volatility, average_return_vector):
        # calculate weighted portfolio VOLATILITY
        weighted_volatility = np.sqrt(np.sum((self.weights * respective_volatility).transpose() * self.weights))
        # calculate weighted expected return
        weighted_return = sum(average_return_vector * self.weights)
        # calculate J-function
        current_j_function_value = weighted_return/weighted_volatility
        print('-------------------')
        print(weighted_volatility)
        print(weighted_return)
        print(current_j_function_value)

        return current_j_function_value


class PortfolioData:

    def __init__(self):
        self.quarter_date = []
        self.origin = []
        self.relative = []
        self.sswn_data = []

    def append(self, asset):
        if len(self.quarter_date) == 0:
            self.quarter_date = asset.data.time_line

        self.origin.append(asset.data.origin_data)
        self.relative.append(asset.data.relative_data)
        self.sswn_data.append(asset.data.sswn_data)

    def to_numpy(self):
        self.origin = np.array(self.origin)
        self.relative = np.array(self.relative)
        self.sswn_data = np.array(self.sswn_data)


class PortfolioShortData:

    def __init__(self, data, time_range):
        self.quarter_date = data.quarter_date[time_range[0]:time_range[1]]
        self.origin = data.origin[:, time_range[0]:time_range[1]]
        self.relative = data.relative[:, time_range[0]:time_range[1]]
        self.sswn_data = data.sswn_data[:, time_range[0]:time_range[1]]
