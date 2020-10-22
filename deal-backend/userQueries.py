import mysql.connector

connection = mysql.connector.connect(host='localhost', database='mysql', user='root',
                                     password='ppp', auth_plugin='mysql_native_password')
cursor = connection.cursor()


def calculate_avg_buy_sell_price(start_date = '2017-07-28T17:06:29.955', end_date = '2017-07-28T17:06:30.049'):
    avg_sell_buy_dict = {}  # Dictionary where instrument name is the key, each instrument is a dictionary with buy & sell prices
    # Calculate Avg Sell Price
    cursor.execute("SELECT instrument_name, AVG(deal_amount) FROM db_grad_cs_1917.deal "
                   "INNER JOIN db_grad_cs_1917.instrument "
                   "ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='S' AND deal_time BETWEEN " + start_date + " AND " + end_date +
                   " GROUP BY deal_instrument_id;")
    for avgSellPrice in cursor:
        avg_sell_buy_dict[avgSellPrice[0]] = {"avgSellPrice": avgSellPrice[1]}
    # Calculate Average Buy Price
    cursor.execute("SELECT instrument_name, AVG(deal_amount) FROM db_grad_cs_1917.deal "
                   "INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id "
                   "WHERE deal_type='B' AND deal_time BETWEEN " + start_date + " AND " + end_date + " GROUP BY deal_instrument_id;")
    for avgBuyPrice in cursor:
        avg_sell_buy_dict[avgBuyPrice[0]]["avgBuyPrice"] = avgBuyPrice[1]


def calculate_ending_position():
    ending_position_dict = {}
    # cursor.execute("SELECT counterparty_name, instrument_name, deal_quantity FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='B' AND deal_time LIKE '%2017-07-28%'")
    cursor.execute("SELECT counterparty_name, instrument_name, deal_quantity FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty "
                   "ON deal.deal_counterparty_id=counterparty.counterparty_id INNER JOIN db_grad_cs_1917.instrument "
                   "ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='B'")
    for purchase in cursor:
        counterparty = purchase[0]
        instrument = purchase[1]
        quantity = purchase[2]
        if counterparty in ending_position_dict:
            if instrument in ending_position_dict.get(counterparty):
                q_bought = ending_position_dict.get(counterparty).get(instrument).get("quantityBought")
                ending_position_dict.get(counterparty).get(instrument)["quantityBought"] = q_bought + quantity
            else:
                ending_position_dict.get(counterparty)[instrument] = {"quantityBought": quantity}
        else:
            ending_position_dict[counterparty] = {instrument: {"quantityBought": quantity}}
    # cursor.execute("SELECT counterparty_name, instrument_name, deal_quantity FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='S' AND deal_time LIKE '%2017-07-28%'")
    cursor.execute("SELECT counterparty_name, instrument_name, deal_quantity FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty "
                   "ON deal.deal_counterparty_id=counterparty.counterparty_id INNER JOIN db_grad_cs_1917.instrument "
                   "ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='S'")
    for sale in cursor:
        counterparty = sale[0]
        instrument = sale[1]
        quantity = sale[2]
        q_bought = ending_position_dict.get(counterparty).get(instrument).get("quantityBought")
        if "quantitySold" in ending_position_dict.get(counterparty).get(instrument):
            q_sold = ending_position_dict.get(counterparty).get(instrument).get("quantitySold")
            ending_position_dict.get(counterparty).get(instrument)["quantitySold"] = q_sold + quantity
            ending_position_dict.get(counterparty).get(instrument)["endingPosition"] = q_bought - (q_sold + quantity)
        else:
            ending_position_dict.get(counterparty).get(instrument)["quantitySold"] = quantity
            ending_position_dict.get(counterparty).get(instrument)["endingPosition"] = q_bought - quantity
