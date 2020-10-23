import deal-backend
import userQueries from deal-backend
import calculate_avg_buy_sell_price from userQueries

def test_calculate_avg_buy_sell_price(start_date = '2017-07-28T17:06:29.955', end_date = '2017-07-28T17:06:30.049'):
    testInstrument = "Astronomica"
    expected = {"avgSellPrice": 3777.000000, "avgBuyPrice": 3407.785000}
    result = calculate_avg_buy_sell_price(start_date = '2017-07-28T17:06:29.955', end_date = '2017-07-28T17:06:30.049')
    assert expected == result.get(testInstrument)


