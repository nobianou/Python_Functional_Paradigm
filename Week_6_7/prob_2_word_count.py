def intro():
    print("This program counts the number of words in a sentence")
    print()
def user_Input():
    sentence = input("Enter the Sentence for counting number of words: ")
    return sentence
def solution(sentence):
    words = sentence.split()
    len_word = len(words)
    return len_word

def main():
    intro()
    sentence = user_Input()
    len_word = solution(sentence)
    print()
    print("The number of words in the given sentence is: ", len_word)
main()
"""
This program counts the number of words in a sentence

Enter the Sentence for counting number of words: Hi there. Whats up

The number of words in the given sentence is:  4
"""
    
