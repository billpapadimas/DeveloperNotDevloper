import praw
from config import my_user_agent, my_client_id, my_client_secret, my_username, my_password


class RogueOneBot(object):
    def __init__(self):
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
        self.sw_subreddit = self.reddit.subreddit("StarWars")
        self.comment_stream = self.sw_subreddit.stream.comments()
        self.hot_submissions = []

    def run(self):
        for comment in self.comment_stream:
            print("New comment by:", comment.author.name)

            if "rouge one" in comment.body.lower():
                print("---Misspelling Detected---")
                self.correct_spelling(comment)

            print(comment.body)
            print()

    def correct_spelling(self, comment):
        author = "/u/" + comment.author.name
        message = ('*sad beep*\n\n'
                   'Hi,', author, 'I noticed you typed "Rouge One". The correct spelling is "Rogue One".\n\n'
                   'May the force be with you!\n\n'
                   'I\'m just a hard working bot created by /u/BlckJesus.\n\n')

        self.write_to_file(message)

    def reply_to_comment(self):
        pass

    @staticmethod
    def write_to_file(message):
        with open("log.txt", "a") as file:
            file.write(message + "\n")
