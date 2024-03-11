
def collect_chars(word, rooms):
    word_len = len(word)
    chars_per_room = rooms // word_len
    remaining_chars = rooms % word_len

    repeated_word = word * chars_per_room
    partial_word = word[:remaining_chars]

    return repeated_word + partial_word

print(collect_chars("alta", 10)) 
print(collect_chars("sepulsa", 20))
print(collect_chars("sepulsamantap", 20))