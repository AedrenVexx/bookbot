import sys
def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path) as f:
        text = f.read()
    count = word_count(text)
    chars = count_chars(text)
    sorted_chars = sorted_list(chars)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")
    print ("----------- Word Count ----------")
    print (f"Found {count} total words")
    print ("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print ("============= END ===============")

def word_count(text):
    words = text.split()
    final_count = len(words)
    return final_count

def count_chars(text):
    letters = {}
    for  i in text.lower():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters
def sorted_list(char_counts):
    items = []
    for ch, n in char_counts.items():
        items.append({"char": ch, "num": n})
    def sort_on(d):
        return d["num"]
    items.sort(reverse=True, key=sort_on)
    return items

