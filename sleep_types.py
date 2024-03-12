

NOTE = """
        Note: This should not be interpreted as a diagnosis of your sleep type. These results should only be interpreted as a general idea of how you compare against the rest of the audience.
       """

COPYRIGHT = """
Copyright
Copyright © 1989 by the American Psychological Association. Reproduced with permission.

"""
SOURCE = '''
Source:
Smith, C. S., Reilly, C., & Midkiff, K. (1989). Evaluation of three circadian rhythm questionnaires with suggestions for an improved measure of morningness. Journal of Applied Psychology, 74(5), 728–738. https://doi.org/10.1037/0021-9010.74.5.728
'''



# Function to ask a question and get a valid answer
def ask_question(question, options):
    print(question)
    print()
    for option in options:
        print(f"{option}: {options[option]}")
    print()
    answer = input("Enter the number of your choice: ")
    while not answer.isdigit() or int(answer) not in options.keys():
        print("Invalid input. Please enter a valid number.")
        answer = input("Enter the number of your choice: ")
    return int(answer)

# List of questions and scoring options
questions_and_options = [
    ("Considering only your own \"feeling best\" rhythm, at what time would you get up if you were entirely free to plan your day?", 
     {1: "5:00-6:30 a.m", 2: "6:30-7:45 a.m.", 3: "7:45-9:45 a.m.", 4: "9:45-11:00 a.m.", 5: "11:00 a.m. - 12:00 (noon)"},
     {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}),
    ("Considering your only \"feeling best\" rhythm, at what time would you go to bed if you were entirely free to plan your evening?",
     {1: "8:00-9:00 p.m.", 2: "9:00-10:15 p.m.", 3: "10:15 p.m. - 12:30 a.m.", 4: "12:30-1:45 a.m.", 5: "1:45-3:00 a.m."},
     {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}),
    ("Assuming normal circumstance, how easy do you find getting up in the morning?", 
     {1: "Not at all easy", 2: "Slightly easy", 3: "Fairly easy", 4: "Very easy"},
     {1: 1, 2: 2, 3: 3, 4: 4}),
    ("How alert do you feel during the first half hour after having awakened in the morning?", 
     {1: "Not at all alert", 2: "Slightly alert", 3: "Fairly alert", 4: "Very alert"},
     {1: 1, 2: 2, 3: 3, 4: 4}),
    ("During the first half hour after having awakened in the morning, how tired do you feel?", 
     {1: "Very tired", 2: "Fairly tired", 3: "Fairly refreshed", 4: "Very refreshed"},
     {1: 1, 2: 2, 3: 3, 4: 4}),
    ("You have decided to engage in some physical exercise. A friend suggests that you do this one hour twice a week and the best time for him is 7:00-8:00 a.m. Bearing in mind nothing else but your own \"feeling best\" rhythm, how do you think you would perform?",
     {1: "Would be in good form", 2: "Would be in reasonable form", 3: "Would find it difficult", 4: "Would find it very difficult"},
     {1: 4, 2: 3, 3: 2, 4: 1}),
    ("At what time in the evening do you feel tired and, as a result, in need of sleep?",
     {1: "8:00-9:00 p.m.", 2: "9:00-10:15 p.m.", 3: "10:15 p.m. - 12:30 a.m.", 4: "12:30-1:45 a.m.", 5: "1:45-3:00 a.m"},
     {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}),
    ("You wish to be at your peak performance for a test which you know is going to be mentally exhausting and lasting for two hours. You are entirely free to plan your day, and considering only your own \"feeling best\" rhythm, which ONE of the four testing times would you choose?",
     {1: "8:00-10:00 a.m.", 2: "11:00 a.m. - 1:00 p.m.", 3: "3:00-5:00 p.m.", 4: "7:00-9:00 p.m."},
     {1: 4, 2: 3, 3: 2, 4: 1}),
    ("One hears about \"morning\" and \"evening\" types of people. Which ONE of these types do you consider yourself to be?",
     {1: "Definitely a morning type", 2: "More a morning than an evening type", 3: "More an evening than a morning type", 4: "Definitely an evening type"},
     {1: 4, 2: 3, 3: 2, 4: 1}),
    ("When would you prefer to rise (provided you have a full day's work-8 hours) if you were totally free to arrange your time?",
     {1: "Before 6:30 a.m.", 2: "6:30-7:30 a.m.", 3: "7:30-8:30 a.m.", 4: "8:30 a.m. or later"},
     {1: 4, 2: 3, 3: 2, 4: 1}),
    ("If you always had to rise at 6:00 a.m., what do you think it would be like?",
     {1: "Very difficult and unpleasant", 2: "Rather difficult and unpleasant", 3: "A little unpleasant but no great problem", 4: "Easy and not unpleasant"},
     {1: 1, 2: 2, 3: 3, 4: 4}),
    ("How long a time does it usually take before you \"recover your senses\" in the morning after rising from a night's sleep?",
     {1: "0-10 minutes", 2: "11-20 minutes", 3: "21-40 minutes", 4: "More than 40 minutes"},
     {1: 4, 2: 3, 3: 2, 4: 1}),
    ("Please indicate to what extent you are a morning or evening active individual.",
     {1: "Pronounced morning active (morning alert and evening tired)", 2: "To some extent, morning active", 3: "To some extent, evening active", 4: "Pronounced evening active (morning tired and evening alert)"},
     {1: 4, 2: 3, 3: 2, 4: 1}),
]

def main():
    
    print(NOTE.strip())
    print()
    total_score = 0
    
    for question, options, scores in questions_and_options:
        answer = ask_question(question, options)
        total_score += scores[answer]
    
    # Determine sleep type based on total score
    if total_score <= 22:
        sleep_type = "Evening Type (Night Owl)"
    elif 23 <= total_score <= 44:
        sleep_type = "Neither Type"
    else:
        sleep_type = "Morning Type (Early Bird)"
    
    print(f"\nYour total score is: {total_score}")
    print(f"Your sleep type is: {sleep_type}")
    
    
    print(COPYRIGHT.strip())
    
    print()
    
    print(SOURCE)
    

if __name__ == "__main__":
    main()
