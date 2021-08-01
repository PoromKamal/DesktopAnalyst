import yfinance as yf
from datetime import datetime
from yfinance import ticker
from ratios import *

def basicInfo(info: dict):
    """
    Write out the basic info for the stock
    1. Ticker Symbol
    2. Company Name
    3. Current Share Price
    4. Time of Upload
    """
    now = datetime.now()
    currentDatetime = now.strftime("%d/%m/%Y %H:%M:%S")
    return f"Ticker: {info['symbol']}\
        \nCompany: {info['shortName']}\
        \nCurrent Market Price: ${info['currentPrice']}\
        \nSector: {info['sector']}\
        \nCurrent Time: {currentDatetime}"
def ratioInfo(information: dict):
    """
    Output the raw ratio info.
    """
    ratios ="Earnings Ratios-\n"
    #Key error safeguard
    if 'trailingPE' in information and information['trailingPE'] != None:
        ratios += f"Price to earnings: {round(information['trailingPE'], 2)}\n"
    else:
        ratios += f"Price to earnings: N/A\n"

    if 'priceToBook' in information and information['priceToBook'] != None:
        ratios += f"Price to book: {round(information['priceToBook'], 2)}\n"
    else:
        ratios += f"Price to book: N/A\n"
    
    if 'earningsGrowth' in information and information['earningsGrowth'] != None:
        ratios += f"EPS growth: {round(information['earningsGrowth'], 3)}\n"
    else:
        ratios += f"EPS growth: N/A\n"

    ratios += 'Liquidity Ratios- \n'
    if 'currentRatio' in information and information['currentRatio'] != None:
        ratios += f"Current Ratio: {round(information['currentRatio'], 2)}\n"
    else:
        ratios += f"Current Ratio: N/A\n"

    if 'quickRatio' in information and information['quickRatio'] != None:
        ratios += f"Quick Ratio: {round(information['quickRatio'], 2)}\n"
    else:
        ratios += f"Quick Ratio: N/A\n"

    ratios += 'Profitability Ratios- \n'
    if 'operatingMargins' in information and information['operatingMargins'] != None:
        ratios += f"Operating Margins: {round(information['operatingMargins'], 2)}\n"
    else:
        ratios += f"Operating Margins: N/A\n"

    if 'returnOnEquity' in information and information['returnOnEquity'] != None:
        ratios += f"Return on equity: {round(information['returnOnEquity'], 2)}\n"
    else:
        ratios += f"Return on equity: N/A\n"

    ratios += 'Solvency Ratios- \n'    
    if 'debtToEquity' in information and information['debtToEquity'] != None:
        ratios += f"Debt to equity: {round(information['debtToEquity'], 2)}%\n"
    else:
        ratios += f"Debt to equity: N/A\n"

    return ratios

def analyzeEarnings(company: dict):
    """
    Analyze the pe, pb, and EPS growth ratio,
    and return a list, with the output message in the first index,
    and the scoring for the second index.
    Scoring goes as follows: 
    -   return 1, if the stock is within 10% of the industry average (normal)
    -   return 0, if the stock is worse than the industry average (worse)
    -   return 2, if the stock is better than the industry average (better)
    """
    score = 0
    score += (pe(company) + pb(company) + eps_growth(company))
    message = "After analyzing the PE, PB, and EPS growth ratios, Desktop Analyst\ncan report that: "
    if score == 3:
        message += f"{company['shortName']} has normal earnings in the {company['sector']} sector.\n"
    elif score < 3:
        message += f"{company['shortName']} has below average earnings in the {company['sector']} sector.\n"
    else:
        message += f"{company['shortName']} has above average earnings in the {company['sector']} sector.\n"
    return [message, score]
def analyzeLiquidity(company: dict):
    """
    Analyze the current, and quick ratio,
    and return a list, with the output message in the first index,
    and the scoring for the second index.
    Scoring goes as follows: 
    -   return 1, if the stock is within 10% of the industry average (normal)
    -   return 0, if the stock is worse than the industry average (worse)
    -   return 2, if the stock is better than the industry average (better)
    """
    score = 0
    score += (current_ratio(company) + quick_ratio(company))
    message = f"After analyzing the liquidity of {company['shortName']}, through the current,\nand quick ratio, we can report that: "
    if score == 3:
        message += f"{company['shortName']} has normal liquidity in comparison to companies in the {company['sector']} sector.\n"
    elif score < 3:
        message += f"{company['shortName']} has low liquidity in comparison to companies in the {company['sector']} sector.\n"
    else:
        message += f"{company['shortName']} is highly liquid in comparison to companies in the {company['sector']} sector.\n"
    return [message, score]
def analyzeProfitability(company: dict):
    """
    Analyze the operating margin, and return on equity ratio,
    and return a list, with the output message in the first index,
    and the scoring for the second index.
    Scoring goes as follows: 
    -   return 1, if the stock is within 10% of the industry average (normal)
    -   return 0, if the stock is worse than the industry average (worse)
    -   return 2, if the stock is better than the industry average (better)
    """
    score = 0
    score += (operating_margin(company) + return_on_equity(company))
    message = f"Using the operating margin, and return on equity, Desktop Analyst has analyzed\n{company['shortName']}'s profitability and found that:\n"
    if score == 3:
        message += f"{company['shortName']} has average profitability in comparison to its competitors.\n"
    elif score < 3:
        message += f"{company['shortName']} is not as profitable as its competitors.\n"
    else:
        message += f"{company['shortName']} is much more profitable than its competitors.\n"
    return [message, score]
def analyzeSolvency(company: dict):
    """
    Analyze the debt to equity growth ratio,
    and return a list, with the output message in the first index,
    and the scoring for the second index.
    Scoring goes as follows: 
    -   return 1, if the stock is within 10% of the industry average (normal)
    -   return 0, if the stock is worse than the industry average (worse)
    -   return 2, if the stock is better than the industry average (better)
    """
    score = 0
    score += (de(company))
    message = f"Finally, Desktop Analyst has checked {company['shortName']}'s solvency, and found that:\n"
    if score == 3:
        message += f"{company['shortName']} has average solvency in its sector.\n"
    elif score < 3:
        message += f"{company['shortName']} has below average solvency in its sector.\n"
    else:
        message += f"{company['shortName']} has high solvency in comparison to companies in its sector.\n"
    return [message, score]

def summary(company: dict):
    """
    Construct a output paragraph which talks about the companies,
    liquidity, profitability, solvency, earnings based on the scoring,
    of the previous functions.
    Output a list, with the output message in the first index, and the overall,
    score (sum of analyzeEarnings, analyzeLiquidity, ...) in the second index.
    """
    #Returned arrays:
    earning_eval = analyzeEarnings(company)
    liquidity_eval = analyzeLiquidity(company)
    profitability_eval = analyzeProfitability(company)
    solvency_eval = analyzeSolvency(company)
    
    #Return values
    paragraph_summary = ""
    overall_score = 0
    
    #Build return values
    #Append Earnings report
    paragraph_summary+= earning_eval[0]
    overall_score += earning_eval[1]

    #Append Liquidity report
    paragraph_summary+= liquidity_eval[0]
    overall_score += liquidity_eval[1]

    #Append profitability report
    paragraph_summary+= profitability_eval[0]
    overall_score += profitability_eval[1]

    #Append solvency report
    paragraph_summary+= solvency_eval[0]
    overall_score += solvency_eval[1]

    return [paragraph_summary, overall_score]