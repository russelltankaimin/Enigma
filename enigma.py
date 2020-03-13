def settings():
    reflector=input("Pick a reflector: UKW-B or UKW-C\n")
    if reflector=="UKW-B":
        reflector={"A":"Y","Y":"A","B":"R","R":"B","C":"U","U":"C","D":"H","H":"D","E":"Q","Q":"E","F":"S","S":"F","G":"L","L":"G","I":"P","P":"I","J":"X","X":"J","K":"N","N":"K","M":"O","O":"M","T":"Z","Z":"T","V":"W","W":"V"}
    else:
        reflector={"A":"F","F":"A","B":"V","V":"B","C":"P","P":"C","D":"J","J":"D","E":"I","I":"E","G":"O","O":"G","H":"Y","Y":"H","K":"R","R":"K","L":"Z","Z":"L","M":"X","X":"M","N":"W","W":"N","Q":"T","T":"Q","S":"U","U":"S"}
    rotor_choice=input("Input the rotor choice from Left to Right in the format: 124 for rotors I, II, IV")
    rotors=[]
    for i in range(0,3):
        rotors.append(int(rotor_choice[i]))
    pb=[]
    for j in range(0,10):
        first=input("Input_pair for plugboard settings: e.g : AB\n ")
        pb.append(first)
    plugboard_settings={pb[0][0]:pb[0][1],pb[0][1]:pb[0][0],pb[1][0]:pb[1][1],pb[1][1]:pb[1][0],pb[2][0]:pb[2][1],pb[2][1]:pb[2][0],pb[3][0]:pb[3][1],pb[3][1]:pb[3][0],pb[4][0]:pb[4][1],pb[4][1]:pb[4][0],pb[5][0]:pb[5][1],pb[5][1]:pb[5][0],pb[6][0]:pb[6][1],pb[6][1]:pb[6][0],pb[7][0]:pb[7][1],pb[7][1]:pb[7][0],pb[8][0]:pb[8][1],pb[8][1]:pb[8][0],pb[9][0]:pb[9][1],pb[9][1]:pb[9][0]}
    rotors_positions=[]
    for i in range(0,3):
        start=input("Enter the rotor_positions from right to left\n")
        rotors_positions.append(start)
    ringstellung=[]
    for i in range(0,3):
        ringsettings=input("Enter ring settings from right to left\n")
        ringstellung.append(ringsettings)
    return [reflector,rotors,plugboard_settings,rotors_positions,ringstellung]
    
def rotor_shift(rotor):
    return rotor[1:]+rotor[0]
    
def encode(settings):
  [reflector,rotors,plugboard_settings,rotor_positions,ringstellung]=[settings[0],settings[1],settings[2],settings[3],settings[4]]
  #[reflector,rotors,plugboard_settings,rotor_positions,ringstellung]= [{'A': 'Y', 'Y': 'A', 'B': 'R', 'R': 'B', 'C': 'U', 'U': 'C', 'D': 'H', 'H': 'D', 'E': 'Q', 'Q': 'E', 'F': 'S', 'S': 'F', 'G': 'L', 'L': 'G', 'I': 'P', 'P': 'I', 'J': 'X', 'X': 'J', 'K': 'N', 'N': 'K', 'M': 'O', 'O': 'M', 'T': 'Z', 'Z': 'T', 'V': 'W', 'W': 'V'}, [3, 2, 1], {'A': 'B', 'B': 'A', 'L': 'H', 'H': 'L', 'V': 'J', 'J': 'V', 'P': 'E', 'E': 'P', 'C': 'M', 'M': 'C', 'R': 'I', 'I': 'R', 'D': 'T', 'T': 'D', 'K': 'F', 'F': 'K', 'X': 'O', 'O': 'X', 'N': 'Q', 'Q': 'N'}, ['O', 'D', 'K'], ['F', 'B', 'A']]
  rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  rotor1Notch = "Q"
  rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  rotor2Notch = "E"
  rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  rotor3Notch = "V"
  rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  rotor4Notch = "J"
  rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
  rotor5Notch = "Z" 
  rotorDict = {1:rotor1,2:rotor2,3:rotor3,4:rotor4,5:rotor5}
  rotorNotchDict = {1:rotor1Notch,2:rotor2Notch,3:rotor3Notch,4:rotor4Notch,5:rotor5Notch}  
  alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  plaintext=input("Input a message to encode or decode: \n")
  plaintext=plaintext.upper()
  #---------Initialise Rotors-------------------
  left_rotor_permutation=rotorDict[rotors[0]]
  middle_rotor_permutation=rotorDict[rotors[1]]
  right_rotor_permutation=rotorDict[rotors[2]]
  #--------Initialise Notch----------------
  left_rotor_notch=rotorNotchDict[rotors[0]]
  middle_rotor_notch=rotorNotchDict[rotors[1]]
  right_rotor_notch=rotorNotchDict[rotors[2]]
  #--------Initialise Window Settings---------
  left_window=alphabet[alphabet.index(rotor_positions[2]):]+alphabet[:alphabet.index(rotor_positions[2])]
  middle_window=alphabet[alphabet.index(rotor_positions[1]):]+alphabet[:alphabet.index(rotor_positions[1])]
  right_window=alphabet[alphabet.index(rotor_positions[0]):]+alphabet[:alphabet.index(rotor_positions[0])]
  ciphertext=''
  for letter in plaintext:
        if letter in alphabet:
            trigger=False
            if right_window[0]==right_rotor_notch:
                trigger=True
            right_window=rotor_shift(right_window)
            if trigger:
                trigger=False
                if middle_window[0]==middle_rotor_notch:
                    trigger=True
                middle_window=rotor_shift(middle_window)
                if trigger:
                    trigger=False
                    left_window=rotor_shift(left_window)
            else:
                if middle_window[0]==middle_rotor_notch:
                    middle_window=rotor_shift(middle_window)
                    left_window=rotor_shift(left_window)
            #---Check if letter passes through the Plugboard
            #print("Rotors from left to right shows:"+str(left_window[0])+str(middle_window[0])+str(right_window[0]))
            if letter in plugboard_settings:
                letter=plugboard_settings[letter]
            else:
                pass
            #---Right rotor--------------
            letter=alphabet[(alphabet.index(right_window[0])-alphabet.index(ringstellung[0])+alphabet.index(letter))%26]
            letter=right_rotor_permutation[alphabet.index(letter)]
            letter=alphabet[(alphabet.index(letter)+alphabet.index(ringstellung[0])-alphabet.index(right_window[0]))%26]
            #---Middle rotor-------------
            letter=alphabet[(alphabet.index(middle_window[0])-alphabet.index(ringstellung[1])+alphabet.index(letter))%26]
            letter=middle_rotor_permutation[alphabet.index(letter)]
            letter=alphabet[(alphabet.index(letter)+alphabet.index(ringstellung[1])-alphabet.index(middle_window[0]))%26]
            #---Left rotor---------------
            letter=alphabet[(alphabet.index(left_window[0])-alphabet.index(ringstellung[2])+alphabet.index(letter))%26]
            letter=left_rotor_permutation[alphabet.index(letter)]
            letter=alphabet[(alphabet.index(letter)+alphabet.index(ringstellung[2])-alphabet.index(left_window[0]))%26]
            #---Reflector----------------
            letter=reflector[letter]
            #---Left Rotor---------------
            letter=alphabet[(alphabet.index(left_window[0])-alphabet.index(ringstellung[2])+alphabet.index(letter))%26]
            letter=alphabet[left_rotor_permutation.index(letter)]
            letter=alphabet[(alphabet.index(letter)+alphabet.index(ringstellung[2])-alphabet.index(left_window[0]))%26]
            #---Middle rotor-------------
            letter=alphabet[(alphabet.index(middle_window[0])-alphabet.index(ringstellung[1])+alphabet.index(letter))%26]
            letter=alphabet[middle_rotor_permutation.index(letter)]
            letter=alphabet[(alphabet.index(letter)+alphabet.index(ringstellung[1])-alphabet.index(middle_window[0]))%26]
            #---Right rotor--------------
            letter=alphabet[(alphabet.index(right_window[0])-alphabet.index(ringstellung[0])+alphabet.index(letter))%26]
            letter=alphabet[right_rotor_permutation.index(letter)]
            letter=alphabet[(alphabet.index(letter)+alphabet.index(ringstellung[0])-alphabet.index(right_window[0]))%26]
            #---Plugboard----------------
            if letter in plugboard_settings:
                letter=plugboard_settings[letter]
            else:
                pass
            ciphertext+=letter
        else:
            ciphertext+=' '
  print(ciphertext)
  
if __name__== __"main"__ :
  encode(settings())

 
