def caesar_encrypt_russian(text, shift):
    encrypted_text = ""
    for char in text:
        if 'А' <= char <= 'Я' or 'а' <= char <= 'я':
            shift_base = ord('А') if char.isupper() else ord('а')
            encrypted_text += chr((ord(char) - shift_base + shift) % 32 + shift_base)
        else:
            encrypted_text += char  # не изменяем пробелы и знаки препинания
    return encrypted_text

def caesar_decrypt_russian(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if 'А' <= char <= 'Я' or 'а' <= char <= 'я':
            shift_base = ord('А') if char.isupper() else ord('а')
            decrypted_text += chr((ord(char) - shift_base - shift) % 32 + shift_base)
        else:
            decrypted_text += char  # не изменяем пробелы и знаки препинания
    return decrypted_text

# Тестируем шифрование и дешифрование
text = "Технологии защиты компьютерный информации"
shift = 3  # Указываем ключ (например, 3)
encrypted = caesar_encrypt_russian(text, shift)
decrypted = caesar_decrypt_russian(encrypted, shift)

print("Зашифрованный текст:", encrypted)
print("Расшифрованный текст:", decrypted)
