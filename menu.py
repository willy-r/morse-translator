from morse import to_morse, from_morse,morse_code_sound
from cli import get_args
from time import sleep

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
run()

print(to_morse('This is a test'))
print(from_morse('.'))
