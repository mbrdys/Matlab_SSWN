from assets import Assets
from portfolio import Portfolio


class Portfolios:

    def __init__(self, params, assets):
        self.list = []  # list of portfolios
        self.number_of_portfolios = len(self.list)
        self.max_horizon = []
        self.assets = assets.assets_list
        self.params = params

    def get_max_horizon(self):
        self.max_horizon = self.list[0].get_sample_length()
        return self.max_horizon

    def update_data_to_numpy(self):
        for portfolio in self.list:
            portfolio.prepare_portfolio_data()

    def allocate_assets(self):

        for single_portfolio_assets in self.params.portfolios_definition:
            portfolio_assets = Assets()

            for asset in self.assets:
                if asset.name in single_portfolio_assets:
                    portfolio_assets.append_asset(asset)

            single_portfolio = Portfolio(self.params, portfolio_assets)
            self.list.append(single_portfolio)

    def do_all(self, step, horizon):

        for portfolio in self.list:
            portfolio.solve_the_portfolio(step, horizon)

        # TODO: Rate the portfolios
        # TODO: Select optimal portfolio
        # TODO: Change the investment strategy if possible
