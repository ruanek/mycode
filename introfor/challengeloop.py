#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for x in farms:
    print(x.get("name") + "'s agriculture is", end=":\n")
    
    for y in x.get("agriculture"):     
            print("  -", y) 

print("\nEnd of loop.") 