from operator import itemgetter # itemgetter helps you sort lists of dictionaries by a specific key.

import requests # requests lets you make web requests (HTTP calls).

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json" # Makes an API Call Hacker News to get a list for the top stories
r = requests.get(url) 
print(f"Status code: {r.status_code}") # The status code tells you if the rquest was successfull(200 means successfull)

# Process information about each submission.
submission_ids = r.json() # r.json() converts the JSON response into a Python list of story IDs

submission_dicts = []
for submission_id in submission_ids[:5]: # loops through the first 5 story ID's
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url) # For each one, it fetches detailed info (title, URL, number of comments, etc) using another API call.
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json() # Converts the Json response into a Python Dictionary called response_dict
    
    # Build a dictionary for each article.
    submission_dict = {'title': response_dict['title'], 'hn_link': f"https://news.ycombinator.com/item?id={submission_id}", 'comments': response_dict['descendants'],} # Extracts only the title, discussion link and comment count from each article.
    submission_dicts.append(submission_dict) # Adds this smaller dictionary to the submission_dicts list.
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True) # Sorts the list of stories so that the one with the most comments appears first.

for submission_dict in submission_dicts: # Displays each story’s title, Hacker News link, and number of comments.
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
    
# Chat GPT Summary 
# It imports the necessary modules — one for making web requests and another for sorting data easily.
# It connects to the Hacker News API to get a list of the current top story IDs.
# It loops through the first five stories, and for each one, it makes another request to get detailed information like the title and number of comments.
# It extracts only the useful information (title, discussion link, and comment count) and stores these in a list of dictionaries.
# It sorts the stories so that the ones with the most comments appear first.
# It prints out the results, showing each story’s title, the link to its discussion page on Hacker News, and the number of comments it has.
# In short: the script fetches the top five Hacker News stories, sorts them by popularity, and displays their key details neatly.