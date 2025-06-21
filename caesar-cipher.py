import art
print(art.logo)

alphabet = [chr(i) for i in range(97, 123)]  # نفس ['a' to 'z']

restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(original_text, shift_amount, dir):
        cipher_text = ""
        if dir == "decode":
            shift_amount *= -1
        for letter in original_text:
            if letter in alphabet:
                shift_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
                cipher_text += alphabet[shift_position]
            else:
                cipher_text += letter
        print(f"Here is the {dir}d result: {cipher_text}")

    caesar(text, shift, direction)

    state = input("Type 'yes' to go again. Otherwise type 'exit':\n").lower()
    if state == 'exit':
        restart = False
        print("Goodbye!")
