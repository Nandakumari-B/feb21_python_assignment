
def voting_eligibility():
    age = int(input("Enter your age:"))
    nationality = input("Enter your nationality: ").lower()

    if age < 18:
        print("You are not eligible to vote because you're under 18.")
    elif age >= 18 and age < 21:  
        print("You are eligible to vote, but may not have all the voting rights depending on your region.")
       
        if nationality == 'usa':
            print("In the USA, you can vote in federal elections.")
        elif nationality == 'india':
            print("In India, you can vote in all elections.")
        else:
            print("Voting rights may vary based on your country.")
    elif age >= 21 and age < 60: 
        print("You are eligible to vote and participate in all elections.")
        
        if nationality == 'usa' and age >= 25:
            print("In the USA, you can run for the House of Representatives.")
        elif nationality == 'india' and age >= 25:
            print("In India, you can run for Lok Sabha.")
        else:
            print("You can participate in elections but cannot hold public office yet.")
    else:
        print("You are in the age group where you have full voting and eligibility rights.")
        
        if nationality != 'usa':
            print("You cannot run for President in the USA because you're not a natural-born citizen.")
        else:
            print("You can run for President in the USA if you're a natural-born citizen.")
        
    
    citizen_status = input("Are you a citizen of your country? (yes/no): ").lower()
    if citizen_status == 'yes' and age >= 18:
        print("You are eligible to vote in your country.")
    elif citizen_status == 'no' or age < 18:
        print("You are not eligible to vote.")
    else:
        print("There seems to be an issue with your inputs.")

    
    if not (age < 18 or citizen_status == 'no'):
        print("You're a qualified citizen with voting rights.")
    else:
        print("You do not meet all the necessary criteria for voting.")

    
    country_specific_rules = input("Does your country have specific voting laws for your age group? (yes/no): ").lower()
    if country_specific_rules == 'yes':
        country = input("Enter your country: ").lower()
        if country == 'usa':
            print("In the USA, you must be at least 35 years old to run for President.")
        elif country == 'india':
            print("In India, you must be at least 35 years old to run for President.")
        else:
            print("Specific laws may vary in your country.")
    else:
        print("There are no specific voting laws that apply to your age group.")

    
    if (age >= 18 and citizen_status == 'yes') or (country_specific_rules == 'yes' and nationality == 'usa'):
        print("You can participate in the voting process or may have additional rights depending on your country.")
    else:
        print("You may have restrictions on voting based on age or nationality.")
voting_eligibility()
