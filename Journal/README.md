I managed to get my hands on this article from Dirk Rijmenants' website on Cipher Machines and Cryptology.
Under technical details of the Enigma Machine, I understood the basic principles of how the electrical current flowed when a letter is pressed on the keyboard.

However, one problem I encountered was the accounting for the Ring Settings (Ringstellung), I had no idea how it worked. I tried referring to 'The Code Book' by Simon Singh but apparently it was too insignificant such that Ringstellung was left out.
Hence I had to derive a way to ensure a correct path of the electrical current when passing through the rotor.

After a few night shifts, I managed to derive the index to which it flowed from input to output:
Let A=0; B=1; C=2; ....... ; Y=24; Z=25 where the number is the index of the corresponding alphabet      
               index[OUTPUT] = [index(WINDOW_LETTER)-index(RINGSTELLUNG)+index(INPUT)] (mod 26)

Apparently it worked! Following the same principle, It can be implemented 5 more times for each rotor it flows through and fro.

Next, the reflectors:
A simple dictionary would suffice.

Now I have another problem, the transition of the electrical current from subsequent rotors. For example, if electrical current leaves rotor 1 at 'W', at what contact would it enter at rotor 2?

