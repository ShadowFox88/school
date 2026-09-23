word = input()

def encrypt(word):
    odd_letters = [i for idx, i in enumerate(word) if idx % 2 == 0]
    even_letters = [i for idx, i in enumerate(word) if idx % 2 == 1]

    return "".join(odd_letters) + ("".join(even_letters))[::-1]

def encryptions_until_original(word):
    encrypted = encrypt(word)
    count = 1

    while encrypted != word:
        encrypted = encrypt(encrypted)
        count += 1

    return count

print(encryptions_until_original(word))