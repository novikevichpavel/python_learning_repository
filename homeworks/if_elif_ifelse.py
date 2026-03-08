def route_info(dict):
    if "distance" in dict and isinstance(dict["distance"], int):
        return f"Distance to your destination is {dict["distance"]}"
    
    if ("speed" in dict and "time" in dict) and (isinstance(dict["speed"], int) and isinstance(dict["time"], int)):
        return f"Distamce to your destination is {dict["speed"] * dict["time"]}"
    
    return "No distance is available"
    
    
print(route_info({"distance": 15}))
print(route_info({"speed": 25, "time": 60}))
print(route_info({"name": "Pavel"}))
