alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def decrypt(text , shift):
  new_text=list()
  for letter in text:
    index=alphabet.index(letter)
    shift_index=index-shift
    new_text.append(alphabet[shift_index])
  print("".join(new_text))
decrypt(text,shift)