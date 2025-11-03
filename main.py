from stats import get_word_count
from stats import get_letter_count
from stats import sort_list
import sys

def get_book_text(bookFilePath):
    with open(bookFilePath) as f:
        return f.read()    


def main ():
    if (len(sys.argv) < 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
        return
    txt = get_book_text(sys.argv[1])
    print(f"Found {get_word_count(txt)} total words")
    newList = sort_list(get_letter_count(txt))   
    
    for items in newList:
        print(f"{items['char']}: {items['num']}")


main()
