coloursDict = {'blue' : 'niebieski',
               'black' : 'czarny',
               'yellow' : 'żółty',
               'red' : 'czerwony',
               'white' : 'biały',
               'green' : 'zielony'}
menu = 'MENU'
menuCenter = menu.center(50)
print(menuCenter)        

text = '''Welcome to english-polish dictionary of colours.

1 - search a translation
2 - add a translation
3 - delete a translation
4 - exit
'''

print(text)

while True:
    try:
        choice = int(input('Please enter your choice: '))
        if choice == 1:
            colourToTranslate = input('Please write a colour to translate: ')
            if colourToTranslate in coloursDict:
                print(coloursDict[colourToTranslate])
            else:
                addColour = input('There is no such colour in dictionary. Do you want to add it? y/n: ')
                if addColour.lower() == 'y':
                    colourTranslation = input('Please write a translation: ')
                    coloursDict[colourToTranslate] = colourTranslation
                    print('The translation was added')
                elif addColour.lower() == 'n':
                    continue
                else:
                    wrongCharacter = input('Incorrect characer.')
                    continue

        elif choice == 2:
            colourToTranslate = input('Please write a colour to translate: ')
            colourTranslation = input('Please write a translation: ')
            coloursDict[colourToTranslate] = colourTranslation
            print('The translation was added.')

        elif choice == 3:
            colourToRemove = input('Please write a colour to remove from dictionary: ')
            if colourToRemove in coloursDict:
                del coloursDict[colourToRemove]
                print('Translation was removed.')
            else:
                print('No such colour in dictionary.')
                continue
        elif choice == 4:
            break
        else:
            print('Incorrect value.')
            continue
    except ValueError:
        print('Incorect value')
        continue      
        