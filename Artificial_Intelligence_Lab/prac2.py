def suggest_career(interests):
    interests = [interest.strip().lower() for interest in interests]

    # Convert to lowercase to make matching case-insensitive
    has_maths = 'maths' in interests
    has_physics = 'physics' in interests
    has_chemistry = 'chemistry' in interests
    has_programming = 'programming' in interests
    has_graphics = 'graphics' in interests

    # Check combinations
    if has_maths and has_physics and has_chemistry:
        print("Suggested Career Path: Engineering Sciences")
    elif has_programming and has_maths:
        print("Suggested Career Path: Computer Engineering")
    elif has_maths and has_graphics:
        print("Suggested Career Path: Mechanical Engineering")
    else:
        print("No matching career path found based on provided interests.")

def main():
    print("Welcome to the Career Path Expert System (if-else version)!")
    interests_input = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ")
    interests = interests_input.split(',')
    suggest_career(interests)

if __name__ == "__main__":
    main()

