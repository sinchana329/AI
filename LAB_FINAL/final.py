
sentences = [
    "Darjeeling is a holiday spot",
    "Munnar and Darjeeling are highly visited places",
    "At holiday spots, ice cream is available",
    "It is a highly visited place",
    "It is not a Munnar"
]

goal = "ice_cream_available"



logical_forms = [
    "HolidaySpot(Darjeeling)",                            
    "HighlyVisited(Munnar) ∧ HighlyVisited(Darjeeling)",      
    "∀x (HolidaySpot(x) → IceCreamAvailable(x))",               
    "HighlyVisited(It)",                                        
    "¬(It = Munnar)"                                           
]

cnf_forms = [
    "HolidaySpot(Darjeeling)",                               
    "HighlyVisited(Munnar)",                                 
    "HighlyVisited(Darjeeling)",                                
    "¬HolidaySpot(x) ∨ IceCreamAvailable(x)",                
    "HighlyVisited(It)",                                       
    "¬Equal(It, Munnar)"                                        
]

print("=== CNF CONVERSION OF KNOWLEDGE BASE ===")
for i, s in enumerate(cnf_forms, start=1):
    print(f"Clause {i}: {s}")
print("\n")



KB = {
    "holiday_spot": {"darjeeling"},
    "highly_visited": {"munnar", "darjeeling"},
    "rule": [("ice_cream_available(X)", "holiday_spot(X)")],
    "not": {"munnar"}
}

entity = "darjeeling"  

def backward_chaining(goal, entity, level=0):
    indent = "  " * level
    print(f"{indent}🔹 Step {level+1}: Try to prove {goal}({entity})")


    if goal == "ice_cream_available":
        print(f"{indent}   Apply Rule (from CNF: ¬HolidaySpot(x) ∨ IceCreamAvailable(x))")
        print(f"{indent}   To prove IceCreamAvailable({entity}), need to prove HolidaySpot({entity}).")

        subgoal = "holiday_spot"
        if backward_chaining(subgoal, entity, level + 1):
            print(f"{indent}✅ Subgoal satisfied: HolidaySpot({entity}) is TRUE.")
            print(f"{indent}✅ Therefore, IceCreamAvailable({entity}) is TRUE.")
            return True
        else:
            print(f"{indent}❌ Could not prove HolidaySpot({entity}) → goal fails.")
            return False

    elif goal == "holiday_spot":
        print(f"{indent}   Checking KB facts for HolidaySpot({entity})...")
        if entity in KB["holiday_spot"]:
            print(f"{indent}   ✔ Found in KB: HolidaySpot({entity})")
            return True
        else:
            print(f"{indent}   ❌ Not found: HolidaySpot({entity})")
            return False

    elif goal == "highly_visited":
        print(f"{indent}   Checking KB facts for HighlyVisited({entity})...")
        if entity in KB["highly_visited"]:
            print(f"{indent}   ✔ Found in KB: HighlyVisited({entity})")
            return True
        else:
            print(f"{indent}   ❌ Not found: HighlyVisited({entity})")
            return False

    else:
        print(f"{indent}❌ Unknown goal type: {goal}")
        return False


print("=== BACKWARD REASONING TRACE ===\n")
print(f"Entity determined from facts: IT → DARJEELING (since it's not Munnar)\n")

result = backward_chaining(goal, entity)

print("\n=== TRACE SUMMARY ===")
trace = [
    "1️⃣ CNF Rule Used: ¬HolidaySpot(x) ∨ IceCreamAvailable(x)",
    "2️⃣ Fact Used: HolidaySpot(Darjeeling)",
    "3️⃣ Derived: IceCreamAvailable(Darjeeling)",
]
for t in trace:
    print(t)

print("\n=== FINAL CONCLUSION ===")
if result:
    print(f"✅ Therefore, IceCreamAvailable(Darjeeling) → Ice cream is available at Darjeeling.")
else:
    print(f"❌ Could not prove that IceCreamAvailable(Darjeeling).")
