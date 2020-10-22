import mysql.connector

connection = mysql.connector.connect(host='localhost', database='mysql', user='root',
                                     password='ppp', auth_plugin='mysql_native_password')
cursor = connection.cursor()
#
# #Average Sell Price
# avgSellBuyDict = {} #Dictionary where instrument name is the key, each instrument is a dictionary with buy and sell prices
# cursor.execute("SELECT instrument_name, AVG(deal_amount) FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='S' AND deal_time BETWEEN '2017-07-28T17:06:29.955' AND '2017-07-28T17:06:30.049' GROUP BY deal_instrument_id;")
# for avgSellPrice in cursor:
#     avgSellBuyDict[avgSellPrice[0]] = {"avgSellPrice": avgSellPrice[1]}
# #Average Buy Price
# cursor.execute("SELECT instrument_name, AVG(deal_amount) FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='B' AND deal_time BETWEEN '2017-07-28T17:06:29.955' AND '2017-07-28T17:06:30.049' GROUP BY deal_instrument_id;")
# for avgBuyPrice in cursor:
#     avgSellBuyDict[avgBuyPrice[0]]["avgBuyPrice"] = avgBuyPrice[1]

#Realised Profit
endingPositionDict = {}
cursor.execute("SELECT counterparty_name, instrument_name, deal_quantity FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='B' AND deal_time LIKE '%2017-07-28%'")
for purchase in cursor:
    counterparty = purchase[0]
    instrument = purchase[1]
    quantity = purchase[2]
    if counterparty in endingPositionDict:
        if instrument in counterparty:
            quantityBought = counterparty.get(instrument)
            instrument["quantityBought"] = quantityBought + quantity
        else:
            endingPositionDict.get(counterparty)[instrument] = {"quantityBought": quantity}
    else:
        endingPositionDict[counterparty] = {instrument: {"quantityBought": quantity}}
cursor.execute("SELECT counterparty_name, instrument_name, deal_quantity FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.counterparty ON deal.deal_counterparty_id=counterparty.counterparty_id INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='S' AND deal_time LIKE '%2017-07-28%'")
for sale in cursor:
    counterparty = sale[0]
    instrument = sale[1]
    quantity = sale[2]
    if "quantitySold" in endingPositionDict.get(counterparty).get(instrument):
        qSold = endingPositionDict.get(counterparty).get(instrument).get("quantitySold")
        endingPositionDict.get(counterparty).get(instrument)["quantitySold"] = qSold + quantity
    else:
        endingPositionDict.get(counterparty).get(instrument)["quantitySold"] = quantity;
print("end")