import pyperclip
import string


#Caesar Cipher

#each letter has a value 0 - 25 in a dictionary letter: value
def c_dict():
    c_dict = {}
    alphabet = string.ascii_lowercase
    for i in range(26):
        c_dict[alphabet[i]] = i
    
    return c_dict
    

def get_key(letterValue, cipher_dict):
    letter = [k for k, v in cipher_dict.items() if v == letterValue][0]
    
    return letter


def access_cipher_letter(letterValue, key, cipher_dict):
    
    letterValue += key
    
    if letterValue > 25:
        letterValue -= 26
    elif letterValue < 0:
        letterValue += 26
    
    letter = get_key(letterValue, cipher_dict)
    
    return letter
    

def access_cipher_message(message, encryption, key):
    
    cipher_dict = c_dict()
    cipher_message = ''
    
    if not encryption:
        key = - key

    for char in message:
        if char.isalpha():
            letterValue = cipher_dict.get(char)
            cipher_message += access_cipher_letter(letterValue, key, cipher_dict)

        else:
            cipher_message += char
    
    return cipher_message



def input_message():
    
    while True:
        try:
            message = input("Enter message: ").lower()
        
        except ValueError:
            print('Enter a message using alphanumeric and special characters.')
        
        else:
            break
    
    return message


def input_encryption():
    
    while True:
        try:
            encryption = input("Enter 'e' for encryption, 'd' for decryption").lower()
            assert encryption == 'e' or encryption == 'd'
        
        except AssertionError:
            print("Enter 'e' for encryption, 'd' for decryption")
        
        else:
            if encryption == 'e':
                encryption = True
            else:
                encryption = False
                
            break
  
    return encryption


def input_key():
    
    while True:
        try:
            key = int(input("Enter a key value from 0 - 25"))
            assert key >= 0 and key <= 25
        
        except ValueError:
            print("Enter a number")
            
        except AssertionError:
            print("Enter a number between 0 - 25")
    
        else:
            break
    
    return key



def main():
    message = input_message()
    encryption = input_encryption() #true or false
    key = input_key()
    
    cipher_message = access_cipher_message(message, encryption, key)

    return pyperclip.copy(cipher_message)

if __name__ == "__main__":
    main()









