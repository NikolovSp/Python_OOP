def vowel_filter(function):
    vowels = ["a", "e", "o", "i", "y", "u"]

    def wrapper():

        return [l for l in function() if l.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e", "I"]


print(get_letters())
