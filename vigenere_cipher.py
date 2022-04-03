import string

def run_v_cipher():
    c_question = input("Do you want to encrypt or decrypt your message? Enter 'd' (decrypt) or 'e' (encrypt)").lower()
    c_key = input("Enter the key: ")
    c_message = input("Enter the message: ")
    
    return translateMessage(c_key, c_message, c_question)

def get_key(dict, value):
    for k, v in dict.items():
        if v == value:
            return k
 

def translateMessage(key, message, cryption):
    key = key.lower()
    message = message.lower()
    
    #create a dictionary with values A0, B1, C2... using enumerate
    alpha_str = string.ascii_lowercase
    
    cipher_dict = dict((i, j) for j, i in enumerate(alpha_str))
    
    #extend the list to the length of the message to get message key
    long_key = list((key * len(message))[:len(message)])


    #use lambda with a function to map key values across the message while ignoring special characters
    def key_function(char_list):
    
        for char in char_list:
            if char.isalpha():
                return long_key.pop(0)
            else:
                return char
            
    message_key = list(map(key_function, list(message)))
    
    
    #if the cryption is 'e' encrypt
    if cryption == 'e':
        encrypt = ''
        for i in range(len(message)):
            if message[i].isalpha():
                cipher_val = cipher_dict[message[i]] + cipher_dict.get(message_key[i])

                if cipher_val > 25:
                    cipher_val = cipher_val - 26

                v_cipher = get_key(cipher_dict, cipher_val)
                encrypt = encrypt + v_cipher
            else:
                encrypt = encrypt + message[i]
            
        return encrypt
    
    #otherwise decrypt the message    
    else:
        decrypt = ''
        for i in range(len(message)):
            if message[i].isalpha():
                cipher_val = cipher_dict[message[i]] - cipher_dict.get(message_key[i])

                if cipher_val < 0:
                    cipher_val = cipher_val + 26 
                
                val_cipher = get_key(cipher_dict, cipher_val)
                decrypt = decrypt + val_cipher
            
            else:
                decrypt = decrypt + message[i]
            
        return decrypt
        
run_v_cipher()



