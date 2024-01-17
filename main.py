DATABASE="prontocoffeeshop"

def additem(mycon,itemValues):
    if mycon.is_connected():
        print("Successfully connected to mysql")
        cursor = mycon.cursor()
        query = "INSERT INTO "+DATABASE+".`menu` (`ItemName`, `ItemSize`,`Cost`) VALUES"+str(itemValues)+";"
        cursor.execute(query)
        mycon.commit()


def readitem(mycon):
    if mycon.is_connected():
        print("Successfully connected to mysql")
        cursor = mycon.cursor()
        display = "Describe " + DATABASE + ".`menu`;"
        cursor.execute(display)
        val = cursor.fetchall()
        for col in val:
            print(col[0] + "|", end=" ")
        print("\n-------------------------------")
        showdata = "Select * from " + DATABASE + ".`menu`;"
        cursor.execute(showdata)
        data = cursor.fetchall()
        for value in data:
            print(value)


def deleteitem(mycon):
    if mycon.is_connected():
        cursor = mycon.cursor()
        readitem(mycon)
        itemid = input("Enter Item id of record to be deleted")
        query = "Delete from "+DATABASE+".`menu` where ItemId="+(itemid)+";"
        cursor.execute(query)
        mycon.commit()


def updateitem(mycon):
    if mycon.is_connected():
        cursor=mycon.cursor()
        readitem(mycon)
        itemid = input("Enter Item id of record to be updated")
        colname = input("Enter Item Colname of record to be updated")
        newvalue = input("Enter New Value to be updated")
        query = "Update "+DATABASE+".`menu` SET "+colname+"='"+newvalue+"' where ItemId="+(itemid)+";"
        cursor.execute(query)
        mycon.commit()


def addorder(mycon,orderchain):
    if mycon.is_connected():
        print("Successfully connected to mysql")
        cursor = mycon.cursor()
        for orderid,itemid,quant in orderchain:
            query = "INSERT INTO "+DATABASE+".`orderinfo` (`OrderId`,`ItemId`,`Quantity`) VALUES"+str((orderid,itemid,quant))+";"
            cursor.execute(query)
            mycon.commit()
        return orderid


def readorder(mycon):
    if mycon.is_connected():
        print("Successfully connected to mysql")
        cursor = mycon.cursor()
        display = "Describe " + DATABASE + ".`orderinfo`;"
        cursor.execute(display)
        val = cursor.fetchall()
        for col in val:
            print(col[0] + "|", end=" ")
        print("\n-------------------------------")
        showdata = "Select * from " + DATABASE + ".`orderinfo`;"
        cursor.execute(showdata)
        data = cursor.fetchall()
        for value in data:
            print(value)


def deleteorder(mycon):
    if mycon.is_connected():
        cursor = mycon.cursor()
        readitem(mycon)
        readorder(mycon)
        orderid = input("Enter order id to be deleted ")
        query = "Delete from "+DATABASE+".`orderinfo` where OrderId="+(orderid)+";"
        cursor.execute(query)
        mycon.commit()


def updateorder(mycon):
    if mycon.is_connected():
        cursor=mycon.cursor()
        readitem(mycon)
        readorder(mycon)
        orderid = input("Enter order id of record to be updated ")
        itemid=input("Enter item id of record to be updated ")
        colname = input("Enter Item Colname of record to be updated ")
        newvalue = input("Enter New Value to be updated ")
        query = "Update "+DATABASE+".`orderinfo` SET "+colname+"='"+newvalue+"' where OrderId="+(orderid)+" and ItemId="+(itemid)+";"
        cursor.execute(query)
        mycon.commit()


def billgenerate(mycon,orderid):
    if mycon.is_connected():
        cursor=mycon.cursor()
        query = "Select * from "+DATABASE+".`orderinfo` left join "+DATABASE+".`menu` on "+DATABASE+".`orderinfo`.`ItemId`="+DATABASE+".`menu`.`ItemId`;"
        cursor.execute(query)
        itemcost = cursor.fetchall()
        totalcost=0
        for val in itemcost:
            if val[0]==orderid:
                totalcost += val[2]*val[6]

        mycon.commit()
        return totalcost