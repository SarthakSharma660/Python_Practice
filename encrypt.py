alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text , shift):
  new_text=list()
  for letter in text:
    index=alphabet.index(letter)
    shift_index=index+shift
    if shift_index>25:
      temp=shift_index-25
      shift_index=-1+temp
    new_text.append(alphabet[shift_index])
  print("".join(new_text))
encrypt(text,shift)