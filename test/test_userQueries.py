from unittest import TestCase

from deal_backend.userQueries import *

class Test(TestCase):

    def test_effective_profit(self):
        trader = "Selvyn"
        expected = 145720181.6751198
        result = effective_profit()
        if expected != result.get(trader):
            self.fail()

    def test_realised_profit(self):
        trader = "John"
        expected = 104108599.633728
        result = realised_profit()
        if expected != result.get(trader):
            self.fail()

    def test_calculate_avg_buy_sell_price(self):
        testInstrument = "Astronomica"
        expected = {"avgSellPrice": 3377.000000, "avgBuyPrice": 3407.785000}
        result = calculate_avg_buy_sell_price(start_date='2017-07-28T17:06:29.955', end_date='2017-07-28T17:06:30.049')
        if expected != result.get(testInstrument):
            self.fail()

    def test_calculate_ending_position(self):
        trader = "Lina"
        expected = "{'quantityBought': 106767, 'quantitySold': 97546, 'endingPosition': 9221}"
        result = calculate_ending_position()
        if expected != result.get(trader).get("Koronis"):
            self.fail()

    def test_calculate_aggregate_ending_positions(self):
        obj = "Deuteronic"
        expected = "{'quantityBought': 620256, 'quantitySold': 572202, 'endingPosition': 48054}"
        result = calculate_aggregate_ending_positions()
        if expected != result.get(obj):
            self.fail()

