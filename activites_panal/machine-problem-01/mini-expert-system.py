import csv
import os
from datetime import datetime

# --- Logic Functions ---
def impl(P, Q):
    return (not P) or Q  # Implication (P → Q)

def tf(b: bool) -> str:
    return "T" if b else "F"

# Create data directory if it doesn't exist
def ensure_data_directory():
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Created 'data' folder for storing results.")

# ---------- Logger ----------
def log_result(student_name, rule_name, result):
    with open("logic_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        student_name, rule_name, result])

# --- Rule 1: Attendance ---
def attendance_rule(student_name):
    print("\n--- Attendance Rule Checker ---")
    late = input("Was the student late? (T/F): ").strip().upper() == "T"
    excuse = input("Did the student provide an excuse letter? (T/F): ").strip().upper() == "T"
    
    # Rule: If student is late, they must have an excuse letter
    P = late
    Q = excuse
    result = impl(P, Q)
    
    outcome = "Satisfied ✓" if result else "Violated ✗"
    print(f"p = {tf(P)} (Late), q = {tf(Q)} (Excuse Letter)")
    print("Result:", outcome)
    log_result(student_name, "Attendance Rule", outcome)

# --- Rule 2: Grading ---
def grading_rule(student_name):
    print("\n--- Grading Rule Checker ---")
    try:
        grade = float(input("Enter student grade: "))
    except ValueError:
        print("Invalid grade input.")
        return
    
    P = grade >= 75
    Q = grade >= 75  # pass if ≥75
    result = impl(P, Q)
    
    outcome = "Satisfied ✓" if result else "Violated ✗"
    print(f"p = {tf(P)} (grade ≥ 75), q = {tf(Q)} (student passes)")
    print("Result:", outcome)
    log_result(student_name, "Grading Rule", outcome)

# --- Rule 3: Login System ---
def login_rule(student_name):
    print("\n--- Login Rule Checker ---")
    correct_password = "admin123"
    attempt = input("Enter password: ")
    
    P = (attempt == correct_password)  # Password correct
    Q = (attempt == correct_password)  # Access granted if correct
    result = impl(P, Q)
    
    outcome = "Access granted ✓" if result else "Access denied ✗"
    print(f"p = {tf(P)} (Password Correct), q = {tf(Q)} (Access Granted)")
    print("Result:", outcome)
    log_result(student_name, "Login Rule", outcome)

# --- Rule 4: Bonus Points ---
def bonus_rule(student_name):
    print("\n--- Bonus Points Eligibility Checker ---")
    regular = input("Does the student have regular attendance? (T/F): ").strip().upper() == "T"
    
    P = regular
    Q = regular  # eligible if regular
    result = impl(P, Q)
    
    outcome = "Satisfied ✓" if result else "Violated ✗"
    print(f"p = {tf(regular)} (Regular Attendance), q = {tf(Q)} (Bonus Eligible)")
    print("Result:", outcome)
    log_result(student_name, "Bonus Rule", outcome)

# --- NEW RULE: Library Borrowing ---
def library_rule(student_name):
    print("\n--- Library Borrowing Rule Checker ---")
    valid_id = input("Does the student have a valid ID? (T/F): ").strip().upper() == "T"
    fees_paid = input("Are all library fees paid? (T/F): ").strip().upper() == "T"
    
    # Rule: If ID is valid AND fees are paid → Allowed to borrow books
    P = valid_id and fees_paid
    Q = valid_id and fees_paid  # Allowed to borrow if both conditions are met
    result = impl(P, Q)
    
    outcome = "Allowed to borrow ✓" if result else "Not allowed to borrow ✗"
    print(f"p = {tf(P)} (Valid ID and Fees Paid), q = {tf(Q)} (Allowed to Borrow)")
    print("Result:", outcome)
    log_result(student_name, "Library Rule", outcome)

# --- Main Menu ---
def main():
    print("=== University Logic Rules System ===")
    student_name = input("Enter student name: ").strip()
    
    # Create CSV with headers if not exists
    with open("logic_results.csv", "a+", newline="") as file:
        file.seek(0)
        if file.read(1) == "":  # Check if file is empty
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Student Name", "Rule", "Result"])
    
    while True:
        print("\n=== Main Menu ===")
        print("1) Attendance Rule Checker")
        print("2) Grading Rule Checker")
        print("3) Login System Rule Checker")
        print("4) Bonus Points Checker")
        print("5) Library Borrowing Rule Checker")  # New option
        print("6) Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            attendance_rule(student_name)
        elif choice == "2":
            grading_rule(student_name)
        elif choice == "3":
            login_rule(student_name)
        elif choice == "4":
            bonus_rule(student_name)
        elif choice == "5":  # New rule option
            library_rule(student_name)
        elif choice == "6":
            # Create data directory and move CSV file with duplication prevention
            ensure_data_directory()
            if os.path.exists("logic_results.csv"):
                import shutil
                destination = "data/logic_results.csv"
                
                # Check if file already exists in destination
                if os.path.exists(destination):
                    # Create timestamped filename to avoid overwriting
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    base_name = "logic_results"
                    destination = f"data/{base_name}_{timestamp}.csv"
                    print(f"File already exists. Saving as: {destination}")
                
                shutil.move("logic_results.csv", destination)
                print(f"Results saved to {destination}")
            else:
                print("No results file found.")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()