# In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
#  It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 
# The method is named after Julius Caesar, who used it in his private correspondence.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
out="yes"
while out=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift<25:
        shift%=26

    def caesar(text, shift_amount, direction):
        new_text=list()
        if direction=="decode":
            shift_amount*=-1
        for letter in text:
            if letter in alphabet:
                index=alphabet.index(letter)
                shift_index=index+shift_amount
                if shift_index>25:
                    temp=shift_index-25
                    shift_index=temp-1
                new_text.append(alphabet[shift_index])
            else:
                new_text.append(letter)
            caesar_text=''.join(new_text)
        print(f"The {direction}d text is {caesar_text}")
        


    caesar(text=text,shift_amount=shift,direction=direction)
    out=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
