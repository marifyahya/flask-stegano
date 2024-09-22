def vigenere_encrypt(plaintext, keyword):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    encrypted_text = []

    keyword_repeated = ''
    keyword_index = 0
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            keyword_repeated += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            keyword_repeated += plaintext[i]

    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            text_index = alphabet.index(plaintext[i])
            key_index = alphabet.index(keyword_repeated[i])
            encrypted_index = (text_index + key_index) % len(alphabet)
            encrypted_text.append(alphabet[encrypted_index])
        else:
            encrypted_text.append(plaintext[i])

    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, keyword):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    keyword = keyword.upper()
    ciphertext = ciphertext.upper()
    decrypted_text = []

    keyword_repeated = ''
    keyword_index = 0
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            keyword_repeated += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            keyword_repeated += ciphertext[i]

    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            text_index = alphabet.index(ciphertext[i])
            key_index = alphabet.index(keyword_repeated[i])
            decrypted_index = (text_index - key_index) % len(alphabet)
            decrypted_text.append(alphabet[decrypted_index])
        else:
            decrypted_text.append(ciphertext[i])

    return ''.join(decrypted_text)
