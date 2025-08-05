import sys
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
def main(filepath):
        file_contents = get_book_text(filepath)
        words = word_count(file_contents)
        characters_count = character_count(file_contents)
        sorted_list = sort_on(characters_count)
        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {filepath}")
        print ("----------- Word Count ----------")
        print (f"Found {words} total words")
        print ("--------- Character Count -------")
        for item in sorted_list:
            print (f"{item['char']}: {item['num']}")
        print ("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count

from stats import character_count

from stats import sort_on
main(sys.argv[1])
