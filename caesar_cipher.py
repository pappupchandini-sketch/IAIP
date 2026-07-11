def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char

    return result


def main():
    print("===== Caesar Cipher Encryption & Decryption =====")

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted = encrypt(message, shift)
    print("\nEncrypted Message:", encrypted)

    decrypted = decrypt(encrypted, shift)
    print("Decrypted Message:", decrypted)


if __name__ == "__main__":
    main()
