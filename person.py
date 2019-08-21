'''
A class to contain relevant data for a single member of a group on Groupme
'''
class Person(object):
    def __init__(self, id, name, image_url='', members=[]):
        self.id = id
        self.name = name
        self.likes_given = 0
        self.likes_received = 0
        self.msgs = 0
        self.chars = 0
        self.image_url = ''
        self.friends = dict()
        for member in members:
            self.friends.update({ member : 0 })