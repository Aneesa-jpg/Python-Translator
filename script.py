from translate import Translator

print('''
ko : Korean,
es: Spanish
''')
language = input("Enter the language to translate into:")
translator= Translator(to_lang=language)

try:
    with open('text.txt',mode='r') as myfile:
        translation = translator.translate(myfile.read())
        print(translation)
        with open('translate.txt', mode='w',encoding="utf-8") as myfile1:
            myfile1.write(translation)

except FileNotFoundError as error:
    print('File does not exist error', error)
