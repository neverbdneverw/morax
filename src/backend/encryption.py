import random

def encrypt(text: str):
    text = text[::-1]
    shift = random.randint(1, 2 ** 16)
    encrypted_text = f"{shift}Γ"
    for char in text:
        if char == " ":
            encrypted_text += 'Ñ'
        elif char == ",":
            encrypted_text += "Σ"
        elif char == ".":
            encrypted_text += "β"
        elif char == "!":
            encrypted_text += "Δ"
        elif char == "@":
            encrypted_text += "ε"
        elif char.isalpha():
            shifted = ''
            if char.isupper():
                encrypted_text += "Φ"
                shifted = (ord(char.upper()) - ord('A') + shift) % 26 + ord('A')
            else:
                encrypted_text += "ρ"
                shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            encrypted_text += chr(shifted).upper()
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext: str):
    capitalize = False
    decrypted_text = ""
    split = ciphertext.split("Γ")
    shift = int(split[0])
    ciphertext = split[1]
    for char in ciphertext:
        if char == "Ñ":
            decrypted_text += " "
        elif char == "Σ":
            decrypted_text += ","
        elif char == "β":
            decrypted_text += "."
        elif char == "Δ":
            decrypted_text += "!"
        elif char == "ε":
            decrypted_text += "@"
        elif char == "Φ":
            capitalize = True
            continue
        elif char == "ρ":
            capitalize = False
            continue
        elif char.isalpha():
            shifted = ''
            if capitalize:
                shifted = (ord(char.upper()) - ord('A') - shift) % 26 + ord('A')
            else:
                shifted = (ord(char.lower()) - ord('a') - shift) % 26 + ord('a')
            decrypted_text += chr(shifted)
            capitalize = False
        else:
            decrypted_text += char
    return decrypted_text[::-1]
