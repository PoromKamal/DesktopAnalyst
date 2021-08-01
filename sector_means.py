"""
Industry average ratios per sector from 2020, this data was taken from:
https://csimarket.com/, https://www.gurufocus.com/ and https://www.readyratios.com/sec/industry/48/
There are 11 sectors:
    1.Information Technology
    2.Health Care
    3.Financials
    4.Consumer Discretionary
    5.Communication Services
    6.Industrials
    7.Consumer defensive
    8.Energy
    9.Utilities
    10.Real Estate
    11.Materials.
"""

industry_median_master_list = {'Technology': {'PE':35, 'PB':4.8, 'EPS_gwth': 0.52, 'currRat': 2.49, 'qckRat':2.05, 'opMar': 0.03, 'ROE': 0.016, 'debtoEq%': 28},
                    'Consumer Cyclical': {'PE':23, 'PB':10.94, 'EPS_gwth': 1.12, 'currRat': 1.2, 'qckRat':0.74, 'opMar': 0.126, 'ROE': 0.25, 'debtoEq%': 59},
                    'Communication Services': {'PE':19.2, 'PB':10.27, 'EPS_gwth': 0.67, 'currRat': 1.25, 'qckRat':1.01, 'opMar': 0.084, 'ROE': 0.26, 'debtoEq%': 128},
                    'Industrials': {'PE':42.54, 'PB':2.97, 'EPS_gwth': -0.58, 'currRat': 1.89, 'qckRat':1.4, 'opMar': 0.047, 'ROE': 0.0537, 'debtoEq%': 59},
                    'Consumer Defensive': {'PE':27.75, 'PB':5.02, 'EPS_gwth': 0.504, 'currRat': 1.53, 'qckRat':1.04, 'opMar': 0.057, 'ROE': 0.056, 'debtoEq%': 52},
                    'Energy': {'PE':18.8, 'PB':1.24, 'EPS_gwth': -0.49, 'currRat': 1.35, 'qckRat':1.10, 'opMar': 0.024, 'ROE': -0.084, 'debtoEq%': 67},
                    'Utilities': {'PE':36.08, 'PB':2.47, 'EPS_gwth': 2.31, 'currRat': 1.32, 'qckRat':1.25, 'opMar': 0.126, 'ROE': 0.044, 'debtoEq%': 12},
                    'Real Estate': {'PE':31.84, 'PB':1.82, 'EPS_gwth': 0.06, 'currRat': 1.78, 'qckRat':1.67, 'opMar': 0.11, 'ROE': 0.025, 'debtoEq%': 89},
                    'Basic Materials': {'PE':18.54, 'PB':2.45, 'EPS_gwth': 7.88, 'currRat': 2.43, 'qckRat':1.7, 'opMar': 0.067, 'ROE': 0.05, 'debtoEq%': 43},
                    'Healthcare': {'PE':27, 'PB':3.73, 'EPS_gwth': -0.39, 'currRat': 3.21, 'qckRat':2.79, 'opMar': -0.63, 'ROE': -0.14, 'debtoEq%': 41},
                    'Financial Services': {'PE':22.29, 'PB':1.68, 'EPS_gwth': 1.68, 'currRat': 1.71, 'qckRat':1.68, 'opMar': -0.037, 'ROE': 0.105, 'debtoEq%': 33}}
#Generic median list for overall stock market average ratios in case a stock doesnt fit a sector.
generic_median_master_list = {'PE':15, 'PB':4, 'EPS_gwth': 0.12, 'currRat': 1.2, 'qckRat':1, 'opMar': 0.10, 'ROE': 0.15, 'debtoEq%': 70}
