from yfinance.ticker import Ticker
from sector_means import industry_median_master_list as medians
from sector_means import generic_median_master_list as generic
"""
How a ratio fn will work is:
    def ratiofn():
        return 2 for great, 1 for normal, 0 for not good.
    Let normal == a deviation of 10% from the average
It will return one of the numbers pertaining to how good the company ratios are.

"""
def evaluateHigher(value:float, sector: str, ratio: str, medians_list):
    """
    Evaluate function will take in a float representing the ratio value,
    and return the int that pertains to to greater, normal, or lower.
    This fn will be used with ratios which favour a higher number,
    such as EPS growth.
    """
    difference = value - medians_list[sector][ratio]
    deviation = abs(medians[sector][ratio] * 0.1)
    #Check for normal
    if abs(difference) <= deviation:
        return 1 
    #Check for worse value
    elif difference < 0:
        return 0
    #Final Case where the value is better.
    else:
        return 2
def evaluateLower(value:float, sector: str, ratio: str, medians_list):
    """
    Evaluate function will take in a float representing the ratio value,
    and return the int that pertains to to greater, normal, or lower.
    This fn will be used with ratios which favour a lower number,
    such as EPS growth.
    """
    difference = value - medians_list[sector][ratio]
    deviation = abs(medians[sector][ratio] * 0.1)
    #Check for normal
    if abs(difference) <= deviation:
        return 1 
    #Check for better value
    elif difference < 0:
        return 2
    #Final Case where the value is worse.
    else:
        return 0


#Earnings Ratios
def pe(info: dict):
    #Key error safeguard
    if 'trailingPE' not in info or info['trailingPE'] == None:
        return 1
    #Check if the stock sector is in the median list
    sect = info['sector']
    val = info['trailingPE']
    if sect in medians:
        return evaluateLower(val, sect, 'PE', medians)
    #If not use to overall/generic medians to evaluate:
    else:
        return evaluateLower(val, sect, 'PE', generic)
    
def pb(info: dict):
    #Key error safeguard
    if 'priceToBook' not in info or info['priceToBook']== None:
        return 1
    #Check if the stock sector is in the median list
    sect = info['sector']
    val = info['priceToBook']
    if sect in medians:
        return evaluateLower(val, sect, 'PB', medians)
    #If not use to overall/generic medians to evaluate:
    else:
        return evaluateLower(val, sect, 'PB', generic)
def eps_growth(info: dict):
    #Key error safeguard
    if 'earningsGrowth' not in info or info['earningsGrowth']== None:
        return 1
    #Check if the stock sector is in the median list
    sect = info['sector']
    val = info['earningsGrowth']
    if sect in medians:
        return evaluateHigher(val, sect, 'EPS_gwth', medians)
    #If not use to overall/generic medians to evaluate:
    else:
        return evaluateHigher(val, sect, 'EPS_gwth', generic)
#Liquidity Ratios
def quick_ratio(info: dict):
    #Key error safeguard
    if 'quickRatio' not in info or info['quickRatio']== None:
        return 1
    #Check if the stock sector is in the median list
    sect = info['sector']
    val = info['quickRatio']
    if sect in medians:
        return evaluateHigher(val, sect, 'qckRat', medians)
    #If not use to overall/generic medians to evaluate:
    else:
        return evaluateHigher(val, sect, 'qckRat', generic)
def current_ratio(info: dict):
    #Key error safeguard
    if 'currentRatio' not in info or info['currentRatio']== None:
        return 1
    #Check if the stock sector is in the median list
    sect = info['sector']
    val = info['currentRatio']
    if sect in medians:
        return evaluateHigher(val, sect, 'currRat', medians)
    #If not use to overall/generic medians to evaluate:
    else:
        return evaluateHigher(val, sect, 'currRat', generic)

#Profitability Ratios
def operating_margin(info: dict):
    #Key error safeguard
    if 'operatingMargins' not in info or info['operatingMargins']== None:
        return 1
    #Check if the stock sector is in the median list
    sect = info['sector']
    val = info['operatingMargins']
    if sect in medians:
        return evaluateHigher(val, sect, 'opMar', medians)
    #If not use to overall/generic medians to evaluate:
    else:
        return evaluateHigher(val, sect, 'opMar', generic)

def return_on_equity(info: dict):
    #Key error safeguard
    if 'returnOnEquity' not in info or info['returnOnEquity']== None:
        return 1
    #Check if the stock sector is in the median list
    sect = info['sector']
    val = info['returnOnEquity']
    if sect in medians:
        return evaluateHigher(val, sect, 'ROE', medians)
    #If not use to overall/generic medians to evaluate:
    else:
        return evaluateHigher(val, sect, 'ROE', generic)

#Solvency Ratios
def de(info: dict):
    #Key error safeguard
    if 'debtToEquity' not in info or info['debtToEquity']== None:
        return 1
    #Check if the stock sector is in the median list
    sect = info['sector']
    val = info['debtToEquity']
    if sect in medians:
        return evaluateLower(val, sect, 'debtoEq%', medians)
    #If not use to overall/generic medians to evaluate:
    else:
        return evaluateLower(val, sect, 'debtoEq%', medians)