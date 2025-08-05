def word_count(file_contents):
    num_words = len(file_contents.split())
    return num_words


def character_count(file_contents):
    characters = {}
    for letter in file_contents:
        letters = letter.lower()
        if letters in characters:
            characters[letters] += 1
        
        else:
            characters[letters] = 1

    return characters


def sort_on(characters):
    sorted_list = []
    for char, num in characters.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list