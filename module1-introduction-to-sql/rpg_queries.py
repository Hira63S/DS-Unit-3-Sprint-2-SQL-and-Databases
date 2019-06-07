import sqlite3
#import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

#question 1
#How many total character are there?

query = 'SELECT count(*) FROM charactercreator_character;'
result = curs.execute(query)

print('How many total characters are there?', result.fetchall()[0][0])



#question 2
#how many of each specific subclass?
query = """SELECT(
                SELECT COUNT(*)
                FROM charactercreator_cleric
                ) AS clerics,
                (SELECT COUNT(*)
                FROM charactercreator_fighter
                ) AS 'fighters',
                (SELECT COUNT(*)
                FROM charactercreator_thief
                ) AS theives,
                ( SELECT COUNT(*)
                FROM charactercreator_mage
                ) AS mages,
                (SELECT COUNT(*)
                FROM charactercreator_necromancer
                ) AS necromancers;"""

result = curs.execute(query)

print('How many specific subclasses?', result.fetchall()[0])

#THis is easy!! So what the program basically does is gets counts from all the different subclasses.
#it is fun but what to do if you have trouble understanding schema a little bit?

#Question 3: How many Total items?

query = 'SELECT COUNT(*) FROM armory_item;'
result = curs.execute(query)
print('How manny total items?', result.fetchall()[0][0])

#question 4: how many of the items are weapons? how many are not?
query = """SElECT (
            SELECT COUNT(*)
            FROM armory_weapon) AS weapons,
            (
             SELECT COUNT(item_id)
             FROM armory_item
             WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)
             ) AS 'non-weapons';"""

result = curs.execute(query)
print('How many items are weapons? How many are not?', result.fetchall()[0])

#question 5: how many items does each character have? return first 20 rows

query = """SELECT COUNT(item_id) AS 'total_items' FROM charactercreator_character_inventory
            GROUP BY character_id
            LIMIT 20;"""

result = curs.execute(query)

print('How many items does each character have? Return only first 20 rows', result.fetchall())

#make it so that it returns the name of the character along with the number of items?

#query = """SELECT(
#                SELECT name from armory_item
#            INNER JOIN charactercreator_character_inventory
#            ON armory_item.item_id =
#            charactercreator_character_inventory = character_id
#            LIMIT 20;"""

#result = curs.execute(query)

#print('How many items does each character have?', result.fetchall())

#question 6: How many weapons does each character have? first 20 rows

query = """SELECT COUNT(*), character_id
            FROM charactercreator_character_inventory, armory_weapon
            WHERE charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
            GROUP BY character_id
            LIMIT 20"""

result = curs.execute(query)
print('How many weapons does each character have?', result.fetchall())


#question 7: On average, how many Items does each character have?

query = """SELECT ROUND(AVG(items.count),3)
            FROM (SELECT COUNT(*) as count, character_id
            FROM charactercreator_character_inventory
            GROUP BY character_id) AS items;"""

result = curs.execute(query)
print('On average, How many items does each character have?', result.fetchall()[0][0])

#question8: On average, how many weapons does each character have?

#for weapons, we are going to have to do an inner join to get all the characters with weapons from charactercreator_character_inventory
query = """SELECT ROUND(AVG(item_counts),3)
            FROM (SELECT COUNT(inventory.item_id) as item_counts
            from charactercreator_character_inventory as inventory
            INNER JOIN armory_weapon
            ON inventory.item_id = armory_weapon.item_ptr_id
            GROUP BY inventory.character_id)"""

result = curs.execute(query)

print('How many weapons does each character have?', result.fetchall()[0][0])
