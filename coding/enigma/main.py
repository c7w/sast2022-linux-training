import random

if __name__ == "__main__":
    with open("Enigma.txt", 'w+') as file:
        for _ in range(5000):
            file.write("".join([random.choice("QWERTYUIOPASDFGHJKLZXCVBNM1234567890{}[]") for _ in range(100)]))
            file.write("\n")
