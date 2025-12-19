def solve(s):
    words = s.split(' ')
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return ' '.join(capitalized_words)
    
print(solve("hello world"))    
