# --------------------------- updated version using functions -----------------------------------

def display_question(question):
    print('Question: ', question['Question'])
    for i, opition in enumerate(question['Options']):
        print(f'{i}) {opition}')
        

def get_user_choice(options_gty):
    while True: 
        choice = input ('Choose an option (enter the corresponding number): ')
        if choice.isdigit():
            choice_int = int(choice)
            if 0 <= choice_int < options_gty:
                return choice_int
            print('Invalid choice. Please choose a valid option.')
        else:
            print('Invalid input. Please enter a valid number.')
            
def quiz(): 
    questions = [
        {
            'Question': 'How much is 2+2?',
            'Options': ['1', '3', '4', '5'],
            'Answer': '4',
        },
        {
            'Question': 'How much is 5*5?',
            'Options': ['25', '55', '10', '51'],
            'Answer': '25',
        },
        {
            'Question': 'How much is 10/2?',
            'Options': ['4', '5', '2', '1'],
            'Answer': '5',
        },
    ]
    
    right_answers_qty = 0
    for question in questions:
        display_question(question)
        opttions_qty = len(question['Options'])
        user_choice = get_user_choice(opttions_qty)
        
        if question['Options'][user_choice] == question['Answer']:
            right_answers_qty += 1
            print('You got it right 👍')
        else:
            print('You got it wrong ❌')
            
        print()
        
    
    print(f'You got {right_answers_qty} answers right')
    print('of', len(questions), 'questions.')
    

if __name__ == "__main__":
    quiz()
    
# --------------------------- updated version using functions -----------------------------------

# --------------------------- original version from the course -------------------------------------

# questions = [
#     {
#         'Question': 'How much is 2+2?',
#         'Options': ['1', '3', '4', '5'],
#         'Answer': '4',
#     },
#     {
#         'Question': 'How much is 5*5?',
#         'Options': ['25', '55', '10', '51'],
#         'Answer': '25',
#     },
#     {
#         'Question': 'How much is 10/2?',
#         'Options': ['4', '5', '2', '1'],
#         'Answer': '5',
#     },
# ]

# right_answers_qty = 0
# for question in questions:
#     print('Question:', question['Question'])
    
#     options = question['Options']
#     for i, option in enumerate(options):
#         print(f'{i}) {option}')
    
#     while True:
#         choice = input('Choose an option (enter the corresponding number): ')
        
#         if choice.isdigit():
#             choice_int = int(choice)
#             if 0 <= choice_int < len(options):
#                 if options[choice_int] == question['Answer']:
#                     right_answers_qty += 1
#                     print('You got it right 👍')
#                 else:
#                     print('You got it wrong ❌')
#                 break
#             else:
#                 print('Invalid choice. Please choose a valid option.')
#         else:
#             print('Invalid input. Please enter a valid number.')
            
#     print()

# print(f'You got {right_answers_qty} answers right')
# print('of', len(questions), 'questions.')

# --------------------------- original file from the course -----------------------------------