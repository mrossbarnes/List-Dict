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


groceries["apples"] = 1.20
groceries["grapes"] = 2.00
groceries["rice"] = 3.00


football_players ["shaquon barkley"] = 26
football_players ["joe burrow"] = 9
football_players ["dak prescott"] =4


shoe_inv["nike"] = 7
shoe_inv["puma"] = 12
shoe_inv["polo boots"] = 25


del shoe_inv["puma"] 
del shoe_inv["nike"] 


del football_players["mac jones"]
del football_players["joe burrow"]


del groceries["beef"]
del groceries["rice"]

def total_price(food_item, food_item2):
    total = groceries[food_item] + groceries[food_item2]
    return total

print (total_price("turkey", "pie"))

def price_diff(food_item, food_item2):
    diff = groceries[food_item] - groceries[food_item2]
    return abs(diff)

print (price_diff("turkey", "pie"))



def shoe_restock(shoe, num):
    shoe_inv[shoe] *=num
    return shoe_inv
print(shoe_restock("yeezy", 3))

def clearence_sale(shoe, num):
    shoe_inv[shoe] /=num
    return shoe_inv
print(clearence_sale("sb dunk", 2))

def football_jersey(dict):
    largest = 0
    supply =''
    for key in dict.keys():
        if dict [key] > largest:
            largest = dict[key]
            supply = key
    
    return(supply,largest)
print(football_jersey(football_players))