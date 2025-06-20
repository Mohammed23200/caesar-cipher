import art
print(
art.logo
)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restert = True
while restert:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(original_text, shift_amount,dir):
        cipher_text = ""
        for letter in original_text:
            if letter in alphabet:
                if dir == "decode":
                    shift_amount*=-1
            shift_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shift_position]
        print(f"Here is the {dir}: {cipher_text}")
    caesar(text,shift,direction)
    state=input('you want to continue or exit')
    if state == 'exit':
        restert = False