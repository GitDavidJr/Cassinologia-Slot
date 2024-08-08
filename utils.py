import random


slot_types = ["A", "B", "C", "D", "F", "G"]

def random_slot():
    return random.choices(slot_types)