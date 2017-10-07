import praw
import time
from config import my_user_agent, my_client_id, my_client_secret, my_username, my_password, blacklist


class DeveloperNotDevloper(object):
    def __init__(self):
        self.is_running = True
        self.user_agent = my_user_agent
        self.client_id = my_client_id
        self.client_secret = my_client_secret
        self.username = my_username
        self.password = my_password

        self.reddit = praw.Reddit(user_agent=self.user_agent,
                                  client_id=self.client_id,
                                  client_secret=self.client_secret,
                                  username=self.username,
                                  password=self.password)
        self.sw_subreddits = self.reddit.subreddit("Programming+Python+ProgrammingHumor+learnpython+learnprogramming+dailyprogrammer")
        self.comment_stream = self.sw_subreddits.stream.comments()

    def run(self):
        for comment in self.comment_stream:
            clock = time.strftime("%H:%M:%S")
            day = time.strftime("%Y/%m/%d")
            print("{} - {} New comment by: {}".format(day, clock, comment.author))
            print(comment.body)
            print()

            comment_lower = comment.body.lower()

            if "devloper" in comment_lower and "developer" not in comment_lower:
                already_replied = False
                comment.refresh()
                for reply in comment.replies:
                    print("Reply author:", reply.author)
                    if reply.author == self.username:
                        already_replied = True

                if not already_replied and str(comment.author) != self.username and str(comment.author) not in blacklist:
                    print("---Misspelling Detected---")
                    self.correct_spelling(comment)

    def correct_spelling(self, comment):
        author = "/u/" + comment.author.name
        message = ('###\*sad beep\*\n\n' +
                   '---\n\n' +
                   'Hi, ', author, ', I noticed you typed "devloper". The correct spelling is "developer".\n\n' +
                   'Please don\'t do that!\n\n' +
                   '---\n\n' +
                   '^I\'m ^just ^a ^hard ^working ^droid ^created ^by ^/u/BlckJesus ^and ^forked ^by ^/u/OverOverOverlord ^| ' +
                   '[^Github ^Link](https://github.com/billpapadimas/DeveloperNotDevloper)')
        message = "".join(message)

        print()
        self.write_to_log(author, comment.body)
        self.reply_to_comment(comment, message)

    def reply_to_comment(self, comment, message):
        comment.reply(message)

    def write_to_log(self, author, comment_body):
        with open("log.txt", "a") as file:
            clock = time.strftime("%H:%M:%S")
            day = time.strftime("%m/%d/%Y")
            file.write("Misspelling detected from {} at {} - {}\n".format(author, clock, day))
            file.write('"' + comment_body + '"\n\n')
