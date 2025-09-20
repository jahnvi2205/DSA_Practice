# Input: "abc"
# Output: '', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc'

def print_all(input,output):
    if len(input)==0:
        print(f"'{output}'", end=", ")
        return

    print_all(input[1:],output)
    print_all(input[1:],output+input[0])