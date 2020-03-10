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
