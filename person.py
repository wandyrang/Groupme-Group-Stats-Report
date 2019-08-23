'''
Class Person()
A class to contain relevant data for a single member of a group on Groupme
'''
class Person(object):
    def __init__(self, id, name, image_url='', nickname='', members=[]):
        self.id = id
        self.name = name
        self.nickname = nickname
        self.friends = dict()
        self.members = members
        # Track likes recieved by whom by user_id
        for member in self.members:
            self.friends.update({ member : 0 })
        self.image_url = image_url
        # Parsed Data
        self.likes_given = 0
        self.likes_received = 0
        self.msgs = 0
        self.chars = 0

    # Basic print
    def __repr__(self):
        return self.name

    # Print out for debugging
    def __str__(self):
        return (f"id: {self.id}\n"
                f"name: {self.name}\n"
                f"nickname: {self.nickname}\n"
                f"likes_given: {self.likes_given}\n"
                f"likes_received: {self.likes_received}\n"
                f"msgs: {self.msgs}\n"
                f"chars: {self.chars}\n"
                f"image_url:{self.image_url}\n"
                f"friends:{self.friends}\n")
