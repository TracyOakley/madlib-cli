from textwrap import dedent

def hello_world():
    welcome_intro = dedent("""
    **************************************
    **    Welcome to the Madlib.py!   **
    **    Enter Adjectives, Nouns,    **
    **    etc as Prompted!
    
    **                                **
    **************************************
        """)
    print(welcome_intro)


def read_template(filepath):
    with open(filepath) as f:
        data = f.read()
        return data



def parse_template(input_string):

    stripped = input_string.replace("Adjective", "").replace("A First Name", "").replace("Past Tense Verb", "").replace("Plural Noun", "").replace("Small Animal", "").replace("Large Animal", "").replace("A Girl's Name", "").replace("Number 1-50", "").replace("Number", "").replace("First Name", "").replace("Noun","")

    parts_string = input_string
    parts = []

    while parts_string.find("{") != -1:
        slice_front = parts_string.find("{")
        slice_back = parts_string.find("}")
        parts.append(parts_string[slice_front+1:slice_back])
        parts_string = parts_string[:slice_front] + parts_string[slice_back+1:]


    parts = tuple(parts)

    #print(stripped)
    #print(parts)

    return (stripped, parts)


def merge(stripped_string, input_tuple):

    result = stripped_string.format(*input_tuple)
    return result


if __name__ == "__main__":
    hello_world()
    my_tuple = []
    (stripped, parts) = parse_template(read_template("../assets/example_madlib_template.txt"))

    for x in parts:
        print(x)
        result = input("> ")
        my_tuple.append(result)

    my_tuple = tuple(my_tuple)

    print(merge(stripped, my_tuple))

