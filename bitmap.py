
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

def bitmap_input(bitmap):
    while True:
        try:
            valid_input = input("Enter a message to display on the bitmap: ").lower()
            assert (len(valid_input) > 0)
        
        except AssertionError:
            print('Please enter minimum 1 character')
        
        except ValueError:
            print("Sorry I didn't understand your input")
        
        else:
            print('valid_input')
            return bitmap_message(valid_input, bitmap)


def bitmap_message(message, bitmap):
    message = message * len(bitmap)
    for line in bitmap.splitlines():
        for i, char in enumerate(line):
            if char == ' ':
                print(' ', end='')
            elif char == '.':
                print('.', end='')
            else:
                print(message[i], end='')
                
                
        print()       
        
bitmap_input(bitmap)