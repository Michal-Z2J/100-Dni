# This Python file uses the following encoding: Windows-1250
import os, sys

WEIGHT_UNITS = ["mg", "g", "dg", "kg", "t"]
LENGTH_UNITS = ["mm", "cm", "dm", "m", "km"]

def weight_conv_ratio(unitInitial):
    mg = [("mg", 1), ("g", 0.001), ("dg", 0.0001), ("kg", 0.000001), ("t", 0.000000001),]
    g = [("mg", 1000), ("g", 1), ("dg", 0.1), ("kg", 0.001), ("t", 0.000001),]
    dg = [("mg", 10000), ("g", 10), ("dg", 1), ("kg", 0.01), ("t", 0.00001),]
    kg = [("mg", 1000000), ("g", 1000), ("dg", 100), ("kg", 1), ("t", 0.001),]
    t = [("mg", 1000000000), ("g", 1000000), ("dg", 100000), ("kg", 1000), ("t", 1),]

    if unitInitial == "mg":
        return mg
    elif unitInitial == "g":
        return g
    elif unitInitial == "dg":
        return dg
    elif unitInitial == "mg":
        return kg
    elif unitInitial == "t":
        return t

def length_conv_ratio(unitInitial):
    mm = [("mm", 1), ("cm", 0.1), ("dm", 0.01), ("m", 0.001), ("km", 0.000001),]
    cm = [("mm", 10), ("cm", 1), ("dm", 0.1), ("m", 0.01), ("km", 0.00001),]
    dm = [("mm", 100), ("cm", 10), ("dm", 1), ("m", 0.1), ("km", 0.0001),]
    m = [("mm", 1000), ("cm", 100), ("dm", 10), ("m", 1), ("km", 0.001),]
    km = [("mm", 1000000), ("cm", 100000), ("dm", 10000), ("m", 1000), ("km", 1),]

    if unitInitial == "mm":
        return mm
    elif unitInitial == "cm":
        return cm
    elif unitInitial == "dm":
        return dm
    elif unitInitial == "m":
        return m
    elif unitInitial == "km":
        return km

def convert_weight(value, unitConverted, weightRatio):
    for index in range(len(weightRatio)):
        if unitConverted == weightRatio[index][0]:
            return value * weightRatio[index][1]

def convert_length(value, unitConverted, lengthRatio):
    for index in range(len(lengthRatio)):
        if unitConverted == lengthRatio[index][0]:
            return value * lengthRatio[index][1]

def get_value(prompt):
    while True:
        val_str = input(prompt)
        if val_str == "exit":
            return val_str
        if val_str.isdigit() or val_str[1:].isdigit():
            return float(val_str)
        print("Invalid input. Please enter a number.")

def get_unit_initial():
    while True:
        unit = input("Enter length unit (mm, cm, dm, m, km) or weight unit (mg, g, dg, kg, t) you want to convert from: ")
        unit = unit.lower()
        if unit in WEIGHT_UNITS or LENGTH_UNITS:
            return unit
        elif unit == "exit":
            return unit
        print("Invalid operator. Please enter mm, cm, dm, m, km, mg, g, dg, kg, t)")

def get_unit_converted(unitInitial):
    if unitInitial in WEIGHT_UNITS:
        while True:
            unit = input("Enter weight unit (mg, g, dg, kg, t) you want to convert to: ")
            unit = unit.lower()
            if unit in WEIGHT_UNITS:
                return unit
            elif unit == "exit":
                return unit
            print("Invalid unit. You can convert weight to length. Please enter mg, g, dg, kg, t.)")
    if unitInitial in LENGTH_UNITS:
        while True:
            unit = input("Enter length unit (mm, cm, dm, m, km) you want to convert to: ")
            unit = unit.lower()
            if unit in LENGTH_UNITS:
                return unit
            elif unit == "exit":
                return unit
            print("Invalid unit. You can convert length to weight. Please enter mm, cm, dm, m, km.)")

def print_result(result):
    print("Result:", result)
    input("Press Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")

def run_converter():
    unitInitial = get_unit_initial()
    if unitInitial == "exit":
        return False
    unitConverted = get_unit_converted(unitInitial)
    if unitConverted == "exit":
        return False
    value = get_value("Enter value you want to convert: ")
    if value == "exit":
        return False
    if unitInitial in WEIGHT_UNITS:
        weightRatio = weight_conv_ratio(unitInitial)
        result = convert_weight(value, unitConverted, weightRatio)
    elif unitInitial in LENGTH_UNITS:
        lengthRatio = length_conv_ratio(unitInitial)
        result = convert_length(value, unitConverted, lengthRatio)
    print_result(result)
    return True

def desc():
    print("Welcome to the converter.")
    print("Converter allows for converting length units: mm, cm, dm, m, km.")
    print("Converter allows for converting weight units: mg, g, dg, kg, t.")
    print("To exit, type 'exit'.")
    print()

ok = True
while ok:
    desc()
    ok = run_converter()
