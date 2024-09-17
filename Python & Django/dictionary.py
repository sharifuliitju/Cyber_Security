carsIwishIwoned = {
    "ford" : "gt",
    "ford" : "focus", #don't allow duplicate
    "ferrari" : "laferrari",
    "bugatti" : {      ## another dictionary
        "name":"chiron",
        "price": "2.6 million"

    }
}
print(carsIwishIwoned)
print(carsIwishIwoned["ferrari"])
print(carsIwishIwoned.keys()) # for access key
print(carsIwishIwoned.values()) # for access values

print("\n ---------------")
carsIwishIwoned["ferrari"] = "sf90"
carsIwishIwoned.update({"bugatti": "iron"}) #update one item
carsIwishIwoned.update({"toyota" : "supra"}) #add new item
carsIwishIwoned.pop("ford")

carsIwishIwoned=carsIwishIwoned.copy()

print(carsIwishIwoned)