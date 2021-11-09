Cities = ["Oakland","Atlanta", "New york city","Seattle", "Memphis",
 "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(Cities)

nfl_qb = ["T.Brady", "L.Jackson", "J.Hurts", "P.Maholmes", 
"D.Prescott", "J.Allen", "D.Brees", "J.Feilds", "C.Newton", "R.Wilson"]
print(nfl_qb)

print(Cities[1], Cities[-3], Cities[3])
print(nfl_qb[2], nfl_qb[-3], nfl_qb[4])

first_four_cities = Cities[0:4]
print(first_four_cities)

last_four_qb = nfl_qb[-5:-1]
print(last_four_qb)

Cities[0] = "San Francisco"
Cities[2] = "Brooklyn"
Cities[5] = "Dayton"
Cities[-2] = "Cincinatti"
print(Cities)

Cities.append("Oakland")
Cities.extend(["New York","Los Angles"])
Cities.insert(0, "Miami")
print(Cities)

del Cities[0]
Cities.remove("Dayton")
print(Cities)