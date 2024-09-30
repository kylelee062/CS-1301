def build_dictionary(words):
    word_freq = {}
    for i in words:
        if i in word_freq:
            word_freq[i] += 1
        else:
            word_freq[i] = 1
    return word_freq

def word_bag():
    phrase = input("Enter text: ")
    word_list = phrase.split()
    word_freq_dict = build_dictionary(word_list)
    sorted_dict = dict(sorted(word_freq_dict.items()))

    for i, freq in sorted_dict.items():
        print(f"{i}: {freq}")



word_bag()

