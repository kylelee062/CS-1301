def text_filter(filter):
    banned_words = ["Turkey", "Dog", "Fox", "Cat", "Chicken",]
    for word in banned_words:
        filter = filter.replace(word,"")
    return filter

message = input("Input Message: ")
filtered_message = text_filter(message)
print("Output Message:", filtered_message)