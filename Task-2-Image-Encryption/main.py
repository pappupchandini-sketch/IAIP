from PIL import Image

def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_image)
    print("Image Encrypted Successfully!")

def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_image)
    print("Image Decrypted Successfully!")

print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter Choice (1 or 2): ")
key = int(input("Enter Key (0-255): "))

if choice == "1":
    encrypt_image("input.jpg", "encrypted.png", key)
elif choice == "2":
    decrypt_image("encrypted.png", "decrypted.png", key)
else:
    print("Invalid Choice")