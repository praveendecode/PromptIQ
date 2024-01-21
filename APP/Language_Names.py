import googletrans
from googletrans import Translator
from googletrans import LANGUAGES

translator = Translator()

languages = []  # Adding all languages and their code

for code, name in LANGUAGES.items():
    languages.append({name: code})

# Collecting Languages and their codes
languages_name = [list(i.keys())[0] for i in languages]  

# Writing the result to a file
file_path = 'languages.txt'

with open(file_path, 'w') as file:
    for language in languages_name:
        file.write(language + '\n')
        


