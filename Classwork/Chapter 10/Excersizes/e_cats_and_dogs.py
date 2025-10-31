# 10-8 Cats and Dogs & 10-9
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"- Sorry, I can't find the file '{filename}'.")
        pass
    else:
        print(f"Contents of {filename}: ")
        print(contents)
        print("--------------------------------------")