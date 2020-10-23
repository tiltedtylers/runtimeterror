from deal_backend.userQueries import calculate_avg_buy_sell_price

def test_calculate_avg_buy_sell_price():
    testInstrument = "Astronomica"
    expected = {"avgSellPrice": 3777.000000, "avgBuyPrice": 3407.785000}
    result = calculate_avg_buy_sell_price(start_date = '2017-07-28T17:06:29.955', end_date = '2017-07-28T17:06:30.049')
    print(expected == result.get(testInstrument))
    print(expected)
    print(result)
test_calculate_avg_buy_sell_price()