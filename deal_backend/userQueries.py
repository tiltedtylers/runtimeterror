import mysql.connector
import pandas as pd

connection = mysql.connector.connect(host='localhost', database='mysql', user='root',
                                     password='ppp', auth_plugin='mysql_native_password')
cursor = connection.cursor()


def realised_profit():
    sell_df = pd.read_sql(
        "SELECT counterparty_name, instrument_name, deal_quantity, deal_amount FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id  INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='S';",
        con=connection)
    buy_df = pd.read_sql(
        "SELECT counterparty_name, instrument_name, deal_amount, deal_quantity FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='B';",
        con=connection)
    counterparties = sell_df.counterparty_name.unique()
    instruments = sell_df.instrument_name.unique()
    pnldict = {}
    for counterparty in counterparties:
        pnldict[str(counterparty)] = 0
        for instrument in instruments:
            temp = sell_df[sell_df['counterparty_name'] == counterparty]
            newSelldf = temp[temp['instrument_name'] == instrument]
            newSelldf['total'] = newSelldf['deal_amount'] * newSelldf['deal_quantity']
            avg_sell = newSelldf['total'].sum() / newSelldf['deal_quantity'].sum()

            temp = buy_df[buy_df['counterparty_name'] == counterparty]
            newBuydf = temp[temp['instrument_name'] == instrument]
            newBuydf['total'] = newBuydf['deal_amount'] * newBuydf['deal_quantity']
            avg_buy = newBuydf['total'].sum() / newBuydf['deal_quantity'].sum()

            PnL = (avg_sell - avg_buy) * newSelldf['deal_quantity'].sum()
            pnldict[str(counterparty)] += PnL

    return pnldict


def effective_profit():
    sell_df = pd.read_sql(
        "SELECT counterparty_name, instrument_name, deal_quantity, deal_amount FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id  INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='S';",
        con=connection)
    buy_df = pd.read_sql(
        "SELECT counterparty_name, instrument_name, deal_amount, deal_quantity FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='B';",
        con=connection)
    counterparties = sell_df.counterparty_name.unique()
    instruments = sell_df.instrument_name.unique()
    pnldict = {}
    for counterparty in counterparties:
        pnldict[str(counterparty)] = 0
        effective_PnL = 0
        for instrument in instruments:
            temp = sell_df[sell_df['counterparty_name'] == counterparty]
            newSelldf = temp[temp['instrument_name'] == instrument]
            newSelldf['total'] = newSelldf['deal_amount'] * newSelldf['deal_quantity']
            avg_sell = newSelldf['total'].sum() / newSelldf['deal_quantity'].sum()

            temp = buy_df[buy_df['counterparty_name'] == counterparty]
            newBuydf = temp[temp['instrument_name'] == instrument]
            newBuydf['total'] = newBuydf['deal_amount'] * newBuydf['deal_quantity']
            avg_buy = newBuydf['total'].sum() / newBuydf['deal_quantity'].sum()

            realized_PnL = (avg_sell - avg_buy) * newSelldf['deal_quantity'].sum()
            pnldict[str(counterparty)] += realized_PnL + (
                        newBuydf['deal_quantity'].sum() - newSelldf['deal_quantity'].sum()) * (
                                                      newSelldf['deal_amount'].iloc[-1] - newBuydf[
                                                  'deal_amount'].mean())
    return pnldict


def calculate_avg_buy_sell_price(start_date='2017-07-28T17:06:29.955', end_date='2017-07-28T17:06:30.049'):
    avg_sell_buy_dict = {}  # Dictionary where instrument name is the key, each instrument is a dictionary with buy & sell prices
    # Calculate Avg Sell Price
    query = "SELECT instrument_name, AVG(deal_amount) FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='S' AND deal_time BETWEEN \'" + start_date + "\' AND \'" + end_date + "\' GROUP BY deal_instrument_id"
    cursor.execute(query)
    for avgSellPrice in cursor:
        instrument = avgSellPrice[0]
        avgSell = float(avgSellPrice[1])
        avg_sell_buy_dict[instrument] = {"avgSellPrice": avgSell}
    # Calculate Average Buy Price
    query = "SELECT instrument_name, AVG(deal_amount) FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='B' AND deal_time BETWEEN \'" + start_date + "\' AND \'" + end_date + "\' GROUP BY deal_instrument_id"
    cursor.execute(query)
    for avgBuyPrice in cursor:
        instrument = avgBuyPrice[0]
        avgBuy = float(avgBuyPrice[1])
        avg_sell_buy_dict.get(instrument)["avgBuyPrice"] = avgBuy
    return avg_sell_buy_dict


def calculate_ending_position():
    ending_position_dict = {}  # Dictionary with dictionaries for each trader with dictionaries for each instrument
    cursor.execute("SELECT counterparty_name, instrument_name, deal_quantity FROM db_grad_cs_1917.deal "
                   "INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id "
                   "INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id "
                   "WHERE deal_type='B'")
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
    cursor.execute("SELECT counterparty_name, instrument_name, deal_quantity FROM db_grad_cs_1917.deal "
                   "INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id "
                   "INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id "
                   "WHERE deal_type='S'")
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
    return ending_position_dict


def calculate_aggregate_ending_positions():
    aggregate_ending_position_dict = {}  # Dictionary with dictionaries for each trader with dictionaries for each instrument
    cursor.execute("SELECT instrument_name, deal_quantity FROM db_grad_cs_1917.deal "
                   "INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id "
                   "WHERE deal_type='B'")
    for purchase in cursor:
        instrument = purchase[0]
        quantity = purchase[1]
        if instrument in aggregate_ending_position_dict:
            q_bought = aggregate_ending_position_dict.get(instrument).get("quantityBought")
            aggregate_ending_position_dict.get(instrument)["quantityBought"] = q_bought + quantity
        else:
            aggregate_ending_position_dict[instrument] = {"quantityBought": quantity}
    cursor.execute("SELECT instrument_name, deal_quantity FROM db_grad_cs_1917.deal "
                   "INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id "
                   "WHERE deal_type='S'")
    for sale in cursor:
        instrument = sale[0]
        quantity = sale[1]
        q_bought = aggregate_ending_position_dict.get(instrument).get("quantityBought")
        if "quantitySold" in aggregate_ending_position_dict.get(instrument):
            q_sold = aggregate_ending_position_dict.get(instrument).get("quantitySold")
            aggregate_ending_position_dict.get(instrument)["quantitySold"] = q_sold + quantity
            aggregate_ending_position_dict.get(instrument)["endingPosition"] = q_bought - (q_sold + quantity)
        else:
            aggregate_ending_position_dict.get(instrument)["quantitySold"] = quantity
            aggregate_ending_position_dict.get(instrument)["endingPosition"] = q_bought - quantity
    return aggregate_ending_position_dict


print(calculate_avg_buy_sell_price())
