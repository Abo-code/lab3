# Казахский алфавит (42 буквы)
kazakh_alphabet = "АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯабвгғдеёжзийкқлмнңоөпрустуұүфхһцчшщъыіьэюя"

def caesar_encrypt_kazakh(text, shift):
    encrypted_text = ""
    for char in text:
        if char in kazakh_alphabet:
            # Получаем индекс символа в алфавите и сдвигаем его
            idx = kazakh_alphabet.index(char)
            new_idx = (idx + shift) % len(kazakh_alphabet)
            encrypted_text += kazakh_alphabet[new_idx]
        else:
            encrypted_text += char  # оставляем символы, не входящие в алфавит, без изменений
    return encrypted_text

def caesar_decrypt_kazakh(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char in kazakh_alphabet:
            # Получаем индекс символа в алфавите и сдвигаем его в обратную сторону
            idx = kazakh_alphabet.index(char)
            new_idx = (idx - shift) % len(kazakh_alphabet)
            decrypted_text += kazakh_alphabet[new_idx]
        else:
            decrypted_text += char  # оставляем символы, не входящие в алфавит, без изменений
    return decrypted_text

# Тестируем шифрование и дешифрование
text = "Компьютерлік ақпаратты қорғау технологиялары"
shift = 3  # Указываем ключ (например, 3)
encrypted = caesar_encrypt_kazakh(text, shift)
decrypted = caesar_decrypt_kazakh(encrypted, shift)

print("Зашифрованный текст:", encrypted)
print("Расшифрованный текст:", decrypted)
