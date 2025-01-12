def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

noun1 = get_input("Noun")
verb1 = get_input("Verb")
adjective1 = get_input("Adjective")
noun2 = get_input("Noun")
verb2 = get_input("Verb")
adjective2 = get_input("Adjective")

story = f"""
One day, a {adjective1} {noun1} decided to go on an adventure. 
It loved to {verb1} all day long but always felt something was missing. 
Suddenly, it stumbled upon a {adjective2} {noun2} that seemed magical. 
The {noun2} started to {verb2} and surprised the {noun1}. 
From that day forward, the {noun1} and the {noun2} became the best of friends 
and shared countless adventures together.
"""

print(story)