import praw

reddit1 = praw.Reddit(client_id = "GGj6f657ASp5KYtTU-HxJw",
                     client_secret = "RGFyym8y8tRkfarv3wJpaba2ui7DZA",
                     username = "bigchadtest",
                     password = "v26102002",
                     user_agent="bigchadtest")

subreddit = reddit1.subreddit("memes")

top = subreddit.top(limit = 5)

for submission in top:
    print(submission.title)