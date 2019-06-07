###PART 2 - The Northwind Databases

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

#- What are the ten most expensive items (per unit price) in the database?
#- What is the average age of an employee at the time of their hiring? (Hint: a
#  lot of arithmetic works with dates.)
#- (*Stretch*) How does the average age of employee at hire vary by city?

query = """SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;"""
result = curs.execute(query)
print('Ten most expensive items (per Unite Price):', result.fetchall())

#Result:Côte de Blaye
#Thüringer Rostbratwurst
#Mishi Kobe Niku
#Sir Rodney's Marmalade
#Carnarvon Tigers
#Raclette Courdavault
#Manjimup Dried Apples
#Tarte au sucre
##Ipoh Coffee
#Rössle Sauerkraut '''

# hiredate is in datetime format
# we need to subtract the hire date from birthdate and get taht number in years.
query2 = """SELECT Id, FirstName, LastName, AVG(HireDate - BirthDate) AS 'age at hiring'
            FROM Employee"""
result2 = curs.execute(query2)
print(result2.fetchall())

# this is only returning one result in DB browser, can't think of any other way to get average of subtraction...?
# maybe avg function is causing a ruckus where it is only returning one value in DB browser.

# Stretch:
# SAME THING, just group by City
query3 = """SELECT City, AVG(HireDate - BirthDate) AS 'age at hiring'
            FROM Employee
            GROUP BY City;"""
result3 = curs.execute(query3)
print('Hire Age of employee per city:', result3.fetchall())


# Part3
# Sailing the Northwind sqlite_master
#- What are the ten most expensive items (per unit price) in the database *and*
#  their suppliers?
# We get the product name from product where we ordered the unit price in descending order and limiting it to 10
# then we used that to get the company name from supplier column

query4 = """SELECT ProductName, Supplier.CompanyName FROM Product
            JOIN Supplier ON  Product.SupplierId = Supplier.ID ORDER BY UnitPrice DESC
            LIMIT 10"""

result4 = curs.execute(query4)
print('Ten most expensive items (per unit price) in the database *and* their suppliers:')
for products in result4.fetchall():
    print(products[0] + ', ' + products[1])


# Apparently top 10 products are supplied by 290 suppliers. some supplier might show up twice
# but the same product is supplied by many supplier

#- What is the largest category (by number of unique products in it)?
query5 = """SELECT category.CategoryName
            FROM Product JOIN Category ON product.CategoryId = Category.Id
            GROUP BY CategoryId
            ORDER BY Count(CategoryId) DESC LIMIT 1;"""

#result5 = curs.execute(query5)
#print('Largest category(by number of products in it)', result5.fetchall())
#for suppliers in result5.fetchall():
#    print(suppliers[0] + ', ' + suppliers[1])
# Confections! no wonder the obesity rate is so high
#not running in atom for some reason. Runs fine in DB.
