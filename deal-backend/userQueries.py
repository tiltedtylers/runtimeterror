import mysql.connector

connection = mysql.connector.connect(host='localhost', database='mysql', user='root',
                                     password='ppp', auth_plugin='mysql_native_password')
cursor = connection.cursor()

#Average Sell Price
cursor.execute("SELECT instrument_name, AVG(deal_amount) FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='S' AND deal_time BETWEEN '2017-07-28T17:06:29.955' AND '2017-07-28T17:06:30.049' GROUP BY deal_instrument_id;")
for avgSellPrice in cursor:
    print(avgSellPrice)

#Average Buy Price
cursor.execute("SELECT instrument_name, AVG(deal_amount) FROM db_grad_cs_1917.deal INNER JOIN db_grad_cs_1917.instrument ON deal.deal_instrument_id=instrument.instrument_id WHERE deal_type='B' AND deal_time BETWEEN '2017-07-28T17:06:29.955' AND '2017-07-28T17:06:30.049' GROUP BY deal_instrument_id;")
for avgBuyPrice in cursor:
    print(avgBuyPrice)


