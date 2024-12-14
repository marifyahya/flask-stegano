def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
            key_index = (key_index + 1) % key_length
        else:
            encrypted_text += char

    return encrypted_text


def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_text += decrypted_char
            key_index = (key_index + 1) % key_length
        else:
            decrypted_text += char

    return decrypted_text
