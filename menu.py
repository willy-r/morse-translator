from morse import to_morse, from_morse,morse_code_sound,main
from cli import get_args
from time import sleep

def launch():
    prompt = input('Do you want to use the command based program(1) or the text based(2): ')
    if prompt == '1':
        main()

    elif prompt == '2':
        lambda:run()
    else:
        print('Error')
    
                   

def run():

    print('What do you want do do? \n1.Transalte from morse to text\n2.Translate from text to morse')
    print('Or enter Q to quit.')
    choice = input('Enter your choice(1/2): ')

    if choice == '1':
        args = input('Your sentence:')
        sound_choice = input('Want to play the sound?(y/n): ')
        result = to_morse(args)
        #print(result)
        if sound_choice == 'y' and args is not None:
            print(args)
            print(result)
            morse_code_sound(result)
            run()
        else:
            print(result)
            run()

    elif choice == '2':
        args = input('The Morse code:')
        sound_choice = input('Want to play the sound?(y/n): ')
        result = from_morse(args)
        if sound_choice == 'y' and result is not None:
            print(result)
            morse_code_sound(args)
            run()
        else:
            print(result)
            run()

    elif choice.lower == 'q':
        print('See you soon!')
        sleep(1.5)
        exit()

    else:
        print('Invalide choice')
launch()
