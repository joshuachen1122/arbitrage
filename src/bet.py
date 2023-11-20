# PAYOUT = BET AMOUNT / (-1  x MONEYLINE ODDS / 100) [negative]
# PAYOUT = BET AMOUNT x ODDS / 100 [positive]
def payout(bet_amount, moneyline_odds):
    if moneyline_odds < 0:
        return round(bet_amount / (-1 * moneyline_odds / 100), 2)
    else:
        return round(bet_amount * moneyline_odds / 100)