"""
This file generates the advanced analysis data output
"""
from yfinance.ticker import Ticker
from sector_means import industry_median_master_list as medians
from sector_means import generic_median_master_list as generic


def report(t: Ticker):

    f = open("Detailed Analysis", 'w')
    file_output = ""
    file_output += deep_earnings(t)
    file_output += deep_liquidity(t)
    file_output += deep_profitability(t)
    file_output += deep_solvency(t)
    f.write(file_output)
    f.close()    

def deep_earnings(tick: Ticker):
    rep = "Earnings Analysis Report: \n"
    info = tick.info
    #Append P/E analysis
    if 'trailingPE' in info and info['trailingPE'] != None:
        rep += f"{tick.info['shortName']} has a: {round(info['trailingPE'], 2)} P/E Ratio.\n\
        {tick.info['sector']} has an average P/E of: {medians[tick.info['sector']]['PE']}.\n"
    else:
        rep += f"{tick.info['shortName']} has no published P/E Ratio.\n"
    
    #Append P/B analysis
    if 'priceToBook' in info and info['priceToBook'] != None:
        rep += f"{tick.info['shortName']} has a: {round(info['priceToBook'], 2)} PB Ratio.\n\
        {tick.info['sector']} has an average PB of: {medians[tick.info['sector']]['PB']}.\n"
    else:
        rep += f"{tick.info['shortName']} has no published PB Ratio.\n"

    #Append EPS analysis
    if 'earningsGrowth' in info and info['earningsGrowth'] != None:
        rep += f"{tick.info['shortName']} has a: {round(info['earningsGrowth'], 2)} EPS Growth.\n\
        {tick.info['sector']} has an average EPS Growth of: {medians[tick.info['sector']]['EPS_gwth']}.\n"
    else:
        rep += f"{tick.info['shortName']} has no published EPS Growth.\n"
    rep += "\n ---------------------------------------------- \n"
    return rep

def deep_liquidity(tick: Ticker):
    rep = "Liquidity Analysis Report: \n"
    info = tick.info
    #Append current ratio analysis
    if 'currentRatio' in info and info['currentRatio'] != None:
        rep += f"{tick.info['shortName']} has a: {round(info['currentRatio'], 2)} current Ratio.\n\
        {tick.info['sector']} has an average current ratio of: {medians[tick.info['sector']]['currRat']}.\n"
    else:
        rep += f"{tick.info['shortName']} has no published current Ratio.\n"

    #Append quick ratio analysis
    if 'quickRatio' in info and info['quickRatio'] != None:
        rep += f"{tick.info['shortName']} has a: {round(info['quickRatio'], 2)} Quick Ratio.\n\
        {tick.info['sector']} has an average quick ratio of: {medians[tick.info['sector']]['qckRat']}.\n"
    else:
        rep += f"{tick.info['shortName']} has no published quick Ratio.\n"
    rep += "\n ---------------------------------------------- \n"
    return rep

def deep_profitability(tick: Ticker):
    rep = "Profitability Analysis Report: \n"
    info = tick.info

    #Append operating margin Analysis
    if 'operatingMargins' in info and info['operatingMargins'] != None:
        rep += f"{tick.info['shortName']} has a: {round(info['operatingMargins'], 2)} operating margin.\n\
        {tick.info['sector']} has an average operating margin of: {medians[tick.info['sector']]['opMar']}.\n"
    else:
        rep += f"{tick.info['shortName']} has no published operating margin.\n"
    
    #Append return on equity Analysis
    if 'returnOnEquity' in info and info['returnOnEquity'] != None:
        rep += f"{tick.info['shortName']} has a: {round(info['returnOnEquity'], 2)} return on equity.\n\
        {tick.info['sector']} has a return on equity of: {medians[tick.info['sector']]['ROE']}.\n"
    else:
        rep += f"{tick.info['shortName']} has no published return on equity.\n"
    rep += "\n ---------------------------------------------- \n"
    return rep
def deep_solvency(tick: Ticker):
    rep = "Solvency Analysis Report: \n"
    info = tick.info

    #Append operating margin Analysis
    if 'debtToEquity' in info and info['debtToEquity'] != None:
        rep += f"{tick.info['shortName']} has a {round(info['debtToEquity'], 2)}% debt to equity.\n\
        {tick.info['sector']} has an average debt to equity of {medians[tick.info['sector']]['debtoEq%']}%.\n"
    else:
        rep += f"{tick.info['shortName']} has no published debt to equity ratio\n."
    rep += "\n ---------------------------------------------- \n"
    return rep
