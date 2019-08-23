import csv
import person
from random import randrange

headers = ['Name', 'Messages', 'Char Count', 'Likes Given', 'Likes Received', 'Image URL']


#tester code
people = ['bob', 'joe', 'gmo']
bob = person.Person(111, 'bob', 'www.bob.com', people)
joe = person.Person(222, 'joe', 'www.joe.com', people)
gmo = person.Person(333, 'gmo', 'www.gmo.com', people)
members = [bob, joe, gmo]

bob.msgs = randrange(40)
bob.likes_given = randrange(40)
bob.likes_received = randrange(40)
bob.chars = randrange(40)
bob.friends['gmo'] = randrange(40)
bob.friends['joe'] = randrange(40)
bob.friends['bob'] = randrange(40)

joe.msgs = randrange(40)
joe.likes_given = randrange(40)
joe.likes_received = randrange(40)
joe.chars = randrange(40)
joe.friends['gmo'] = randrange(40)
joe.friends['joe'] = randrange(40)
joe.friends['bob'] = randrange(40)

gmo.msgs = randrange(40)
gmo.likes_given = randrange(40)
gmo.likes_received = randrange(40)
gmo.chars = randrange(40)
gmo.friends['gmo'] = randrange(40)
gmo.friends['joe'] = randrange(40)
gmo.friends['bob'] = randrange(40)

# loop through the list of members and add their names to the headers
for member in members:
    headers.append(member.name)

with open('raw_groupme_data.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    for member in members:
        row = [member.name, member.msgs, member.chars, member.likes_given, 
               member.likes_received, member.image_url]
        for friend in member.friends:
            row.append(member.friends[friend])
        csv_writer.writerow(row)