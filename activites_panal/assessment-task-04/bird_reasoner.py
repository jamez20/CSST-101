known_exceptions = {
    "penguin",
    "ostrich",
    "kiwi",
    "emu",
    "cassowary",
    "dodo"
}

def reason_about(animal_name: str, is_bird: bool, extra_info: str | None = None):
    steps = []
    animal = animal_name.strip().lower()
    steps.append(f"1) Input: animal = '{animal_name.strip()}'")
    steps.append(f"2) Rule: If an animal is a bird, assume it can fly.")
    
    if not is_bird:
        steps.append("3) Fact: The animal is NOT a bird.")
        steps.append("4) Conclusion: The rule does not apply → we cannot conclude it can fly by default.")
        return steps
    
    # It's a bird: apply default rule
    steps.append("3) Fact: The animal IS a bird.")
    steps.append("4) Default conclusion (apply rule): assume it can fly.")
    conclusion = "can fly"
    
    # Check known exceptions
    if animal in known_exceptions:
        steps.append(f"5) New information found: '{animal_name.strip()}' is a known exception (cannot fly).")
        steps.append("6) Retract previous default conclusion because new fact contradicts it.")
        conclusion = "cannot fly"
        steps.append(f"7) Revised conclusion: the animal {conclusion}.")
        return steps
    
    # If extra info provided (user-supplied new fact)
    if extra_info:
        extra = extra_info.strip().lower()
        steps.append(f"5) New information provided: {extra_info.strip()}")
        # simple check: if user says "cannot fly" or names an exception, revise
        if "cannot" in extra or "cannot fly" in extra or extra in known_exceptions:
            steps.append("6) This new information contradicts the default conclusion.")
            steps.append("7) Retracting default conclusion.")
            conclusion = "cannot fly"
            steps.append(f"8) Revised conclusion: the animal {conclusion}.")
            return steps
        else:
            steps.append("6) The new information does not contradict the default conclusion.")
            steps.append(f"7) Conclusion stands: the animal {conclusion}.")
            return steps
    
    # No exceptions found and no extra info -> keep default
    steps.append("5) No known exceptions or extra facts found that contradict the default.")
    steps.append(f"6) Final conclusion: the animal {conclusion}.")
    return steps

def interactive():
    print("=== Simple Non-monotonic Reasoner ===")
    name = input("Enter animal name: ").strip()
    bird_ans = input("Is this animal a bird? (y/n): ").strip().lower()
    is_bird = bird_ans.startswith('y')
    
    # optionally check known exceptions automatically
    extra_info = None
    if name.strip().lower() in known_exceptions:
        # We'll still show that we discovered this as new info
        extra_info = None
    else:
        add_info = input("Do you want to add extra info about this animal? (e.g., 'cannot fly', 'juvenile', etc.) (y/n): ").strip().lower()
        if add_info.startswith('y'):
            extra_info = input("Type the extra information (free text): ").strip()
    
    # produce reasoning steps
    steps = reason_about(name, is_bird, extra_info)
    print("\n--- Reasoning trace ---")
    for s in steps:
        print(s)
    print("--- End of trace ---")
    print()

if __name__ == "__main__":
    # run once, allow the user to test multiple animals if they want
    while True:
        interactive()
        again = input("Try another animal? (y/n): ").strip().lower()
        if not again.startswith('y'):
            print("Goodbye.")
            break
