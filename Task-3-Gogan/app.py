def main():
    print("--- DecodeLabs User Registration System ---\n")
    
    # initialize empty dictionary for user data
    user_data = {}
    
    # get name and clean up whitespace
    user_data["name"] = input("Enter your Name: ").strip()
    
    # loop until a valid integer is provided for age
    while True:
        try:
            user_data["age"] = int(input("Enter your Age: "))
            break  # exit loop if successful
        except ValueError:
            print("Invalid input! Age must be a whole number. Try again.\n")
            
    # get email and clean up whitespace
    user_data["email"] = input("Enter your Email: ").strip()
    
    print("\n==================================")
    print("      USER PROFILE CREATED        ")
    print("==================================")
    
    # print each key-value pair
    for key, value in user_data.items():
        print(f"- {key.capitalize()}: {value}")
        
    print("==================================")
    
    # display the raw dictionary payload
    print(f"Raw data payload: {user_data}")

# program entry point
if __name__ == "__main__":
    main()