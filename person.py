'''
Class Person()
A class to contain relevant data for a single member of a group on Groupme
'''
class Person(object):
    def __init__(self, id, name, image_url='', nickname='', members=[]):
        self.id = id
        self.name = name
        self.nickname = ''
        self.likes_given = 0
        self.likes_received = 0
        self.msgs = 0
        self.chars = 0
        self.image_url = image_url
        self.friends = dict()
        for member in members:
            self.friends.update({ member : 0 })

    # Basic print
    def __repr__(self):
        return self.name

    # Just to print out people/debugging repr(Person)
    def __str__(self):
        return ("id: {}\n"
                "name: {}\n"
                "nickname: {}\n"
                "likes_given: {}\n"
                "likes_received: {}\n"
                "msgs: {}\n"
                "chars: {}\n"
                "image_url:{}\n").format(self.id, self.name, self.nickname,
                                         self.likes_given, self.likes_received,
                                         self.msgs, self.chars, self.image_url)