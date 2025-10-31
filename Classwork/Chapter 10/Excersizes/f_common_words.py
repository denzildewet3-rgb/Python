# 10-10 Common words
filenames = ['text_files/macbeth.txt', 'text_files/true_stories_of_wonderfull_deeds.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    
    except FileNotFoundError:
        print(f"Sorry, I can't find the '{filename}'.")
        
    else:
        word = 'the'
        count = contents.lower().count(word)
        count_with_space = contents.lower().count('the ')
        
        print(f"\nIn '{filename}': ")
        print(f"- Approximate count of '{word}': {count}")
        print(f"- Count of '{word}' with space: {count_with_space}")
        print(f"- the total number is: {len(contents)}")        