from lingua import Language, LanguageDetectorBuilder
from langdetect import detect
from langdetect import DetectorFactory
DetectorFactory.seed = 0
from caesar_cipher import c_dict, get_key, access_cipher_letter, access_cipher_message

def build_detector():
    languages = [Language.ENGLISH, Language.JAPANESE]
    detector = LanguageDetectorBuilder.from_languages(*languages).build()
    
    return detector
    

def validate_test(test_message, detector):
    
    result = detector.detect_language_of(test_message)
    valid = False
    
    if str(result) == "Language.ENGLISH":
        valid = True
    
    return valid



def try_cipher_key(message):
    
    encryption = False #value for decryption
    results_list = []
    found = False
    
    detector = build_detector()
    
    
    for i in range(26):
        test_message = access_cipher_message(message, encryption, i)
        
        if validate_test(test_message, detector):
            if detect(test_message) == 'en':
                result = str(test_message)
                found = True
                results_list.append(result)
            
        else:
            continue
    
    return results_list, found



def main():
    
    input_message = input("Enter text for decryption: ")
    
    results, found = try_cipher_key(input_message)
    
    if found:
        if len(results) > 1:
            print("More than one result found.")
            for result in results:
                print(f"Possible Result: {result}")
        else:
            print(f"Result: {''.join(results)}")
    
    else:
        print('Could not detect the language')




if __name__ == "__main__":
    main()

    

