groceries = {"beef": 1.59,
"turkey": 1.99,
"pie": 1.00,
"juice": 2.50}

football_players = {"tom brady":12,
"mac jones" :10,
"chase young": 99,
"lamar jackson": 8}

beef_price = groceries ["beef"]
turkey_price = groceries ["turkey"]
pie_price = groceries ["pie"]
juice_price = groceries ["juice"]

football = football_players ["tom brady"]
football= football_players ["mac jones"]
football =  football_players ["chase young"]
football = football_players ["lamar jackson"]

shoe_inv = {"jordan 13":1,
"yeezy":8,
"foamposite":10,
"air max":5,
"sb dunk":20
}
print(shoe_inv)

shoe_inv ["sb dunk"] -= 2
shoe_inv ["yeezy"] += 1
shoe_inv ["sb dunk"] += 7
shoe_inv ["yeezy"] += 7
shoe_inv ["air max"] += 7
shoe_inv ["foamposite"] += 7
shoe_inv ["jordan 13"] += 7
shoe_inv ["sb dunk"] -= 3
shoe_inv ["yeezy"] -= 3
shoe_inv ["air max"] -= 3
shoe_inv ["foamposite"] -= 3
shoe_inv ["jordan 13"] -= 3
print(shoe_inv)

groceries["apples"] = 1.20
groceries["grapes"] = 2.00
groceries["rice"] = 3.00
print(groceries)

football_players ["shaquon barkley"] = 26
football_players ["joe burrow"] = 9
football_players ["dak prescott"] =4
print(football_players)

shoe_inv["nike"] = 7
shoe_inv["puma"] = 12
shoe_inv["polo boots"] = 25
print(shoe_inv)

del shoe_inv["puma"] 
del shoe_inv["nike"] 
print(shoe_inv)

del football_players["mac jones"]
del football_players["joe burrow"]
print(football_players)

del groceries["beef"]
del groceries["rice"]
print(groceries)




