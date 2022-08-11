#!/usr/bin/env python3

import uuid


howmany = int(input("How many UUIDs should be generated? "))

print("Generationg UUIDs...")

for rand in range(howmany):
    print(uuid.uuid4())