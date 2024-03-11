def main():
    book_path = './books/frankenstein.txt'
    text = get_book_text(book_path)
    # list
    no_words = count_words(text)
    # dictionary
    no_letters = count_letters(text)
    # list of dictionarys
    separated_list = list_dic(no_letters)
    # sorted
    separated_list.sort(reverse=True, key=re_number)
    # print report
    print_report(separated_list, no_words)


# Prints a report of the text letters
def print_report(list, words):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{words} words found in document')
    for i in list:
        if i['letter'].isalpha():
            lett = i['letter']
            number = i['num']
            print(f'The {lett} character was found {number} times')
    print('--- End report ---')

# Takes a dictionary and returns a list separated by each key and value as their own dic
def list_dic(dic):
    list = []
    for key, value in dic.items():
        list.append({"letter": key, "num": value})
    return list

# Takes a dictionary and returns the value of the Key == "num" 
def re_number(dic):
    return dic["num"]

# Returns a list of all the characters of a string numbered by each letter on the string
def count_letters(str):
    low = str.lower()
    output = {}
    for i in low:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1

    return output

# Counts words on a string
def count_words(str):
    list = str.split()
    return len(list)

# Path of the text
def get_book_text(book_path):
    with open(book_path) as f :
        return f.read()



if __name__ == '__main__':
    main()