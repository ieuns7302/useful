def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char

    return decrypted_text



ciphertext = "{Encode Text}"
shift = 

decrypted_text = caesar_decrypt(ciphertext, shift)
print("복호화된 텍스트:", decrypted_text)
