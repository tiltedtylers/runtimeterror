from deal_backend.userQueries import *

def test_calculate_avg_buy_sell_price():
    testInstrument = "Astronomica"
    expected = {"avgSellPrice": 3777.000000, "avgBuyPrice": 3407.785000}
    result = calculate_avg_buy_sell_price(start_date = '2017-07-28T17:06:29.955', end_date = '2017-07-28T17:06:30.049')
    print(str(expected) == str(result.get(testInstrument)))
    print(expected)
    print(result['Astronomica'])
    print(result.get(testInstrument))
    print("hey" == "hey")
    "{'avgSellPrice': 3777.0, 'avgBuyPrice': 3407.785}"
    "{'avgSellPrice': 3377.0, 'avgBuyPrice': 3407.785}"
# test_calculate_avg_buy_sell_price()

print("HERE")
# print(calculate_ending_position().get("Lina").get("Koronis"))
# print(calculate_aggregate_ending_positions().get("Deuteronic"))

result = calculate_ending_position()
print(result.get("Lina").get("Koronis"))