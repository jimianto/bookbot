def word_count(book):
    words = book.split()
    count =len(words)
    return count

def char_appear(book):
    text = book.lower()
    huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    char_count ={}

    for char in text:
        if char in huruf:
            if char in char_count:
                char_count[char] += 1
            else: 
                char_count[char] = 1
        else:
            pass
        
    return char_count
    
def report(book):
    words = word_count(book)
    char_count= char_appear(book)

    sorted_char = sorted(char_count.items(), key= lambda x: x[1], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the documentary\n")

    for word, count in sorted_char:
        print(f'the {word} character was found {count} times')
    

    print("--- End report ---")
    


def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()


    report(file_content)





main()
