import random

def random_shift_encrypt(text):
    shifts = [random.randint(1, 25) for _ in text]  # случайные смещения от 1 до 25
    encrypted_text = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shifts[i]) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text, shifts

def random_shift_decrypt(encrypted_text, shifts):
    decrypted_text = ""
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shifts[i]) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

# Пример использования:
text = "HELLO"
encrypted, shifts = random_shift_encrypt(text)
decrypted = random_shift_decrypt(encrypted, shifts)
print("Зашифрованный текст:", encrypted)
print("Расшифрованный текст:", decrypted)
