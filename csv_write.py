import csv
import person

headers = ['Name', 'Messages', 'Char Count', 'Likes Given', 'Likes Received', 'Image URL']

'''
#tester code
people = ['bob', 'joe', 'gmo']
bob = person.Person(111, 'bob', 'www.bob.com', members=people)
joe = person.Person(222, 'joe', 'www.joe.com', members=people)
gmo = person.Person(333, 'gmo', 'www.gmo.com', members=people)
members = [bob, joe, gmo]
'''

# loop through the list of members and add their names to the headers
for member in members:
    headers.append(member.name)

with open('raw_groupme_data.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    for member in members:
        row = [member.name, member.msgs, member.chars, member.likes_given, 
               member.likes_received, member.image_url]
        print(member.friends)
        for friend in member.friends:
            row.append(member.friends[friend])
            print(member.friends[friend])
        csv_writer.writerow(row)