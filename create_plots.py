from matplotlib import pyplot as plt
import pandas as pd
'''
SETUP FOR DATA
'''
data = pd.read_csv('raw_groupme_data.csv')
names = data['Name']
msgs = data['Messages']
char_count = data['Char Count']
likes_g = data['Likes Given']
likes_r = data['Likes Received']
friends = dict()
count = 0
for person in names:
    friends[person] = dict()
    for friend in names: 
        friends[person].update({friend : data[friend][count]})
    count += 1

'''
SETUP FOR MOST MESSAGES SENT GRAPH (PEOPLE, MSG_COUNT)
'''
grp_msgs = dict()
for i in range(len(names)):
    grp_msgs[names[i]] = msgs[i]
people_msg = []
msg_count = []
for i in sorted(grp_msgs.items(), key=lambda x:x[1]):
    msg_count.append(i[1])
    people_msg.append(i[0])

'''
SETUP FOR CHAR/MESSAGE (PEOPLE, CHAR/MESSAGE)
'''
chars = dict()
for i in range(len(names)):
    if msgs[i] == 0:
        chars[names[i]] = 0      
    else:
        chars[names[i]] = round((char_count[i]/msgs[i]), 2)
people_char = []
verbose = []
for i in sorted(chars.items(), key=lambda x:x[1]):
    verbose.append(i[1])
    people_char.append(i[0])

'''
SETUP FOR LIKES GIVEN (PEOPLE, LIKES GIVEN)
'''
lg = dict()
for i in range(len(names)):
    lg[names[i]] = likes_g[i]
people_lg = []
charit = []
for i in sorted(lg.items(), key=lambda x:x[1]):
    charit.append(i[1])
    people_lg.append(i[0])

'''
SETUP FOR LIKES RECEIVED (PEOPLE, LIKES RECEIVED)
'''
lr = dict()
for i in range(len(names)):
    lr[names[i]] = (likes_r[i])
people_lr = []
popular = []
for i in sorted(lr.items(), key=lambda x:x[1]):
    popular.append(i[1])
    people_lr.append(i[0])
    
'''
SETUP FOR CHAR/MESSAGE (PEOPLE, CHAR/MESSAGE)
'''
lpm = dict()
for i in range(len(names)):
    if msgs[i] == 0:
        lpm[names[i]] = 0       
    else:
        lpm[names[i]] = round((likes_r[i]/msgs[i]), 2)
people_qual = []
quality = []
for i in sorted(lpm.items(), key=lambda x:x[1]):
    quality.append(i[1])
    people_qual.append(i[0])
'''
SETUP FOR SELF LIKES
'''
selfl = dict()
for i in range(len(names)):
    selfl[names[i]] = data[names[i]][i]
people_l = []
self_l = []
for i in sorted(selfl.items(), key=lambda x:x[1]):
    self_l.append(i[1])
    people_l.append(i[0])
'''
SETUP FOR FRIENDS GRAPH (PEOPLE, LIKES)
'''
for i in range(len(names)):
    a = dict()
    fans = []
    likes = []    
    for fan in names:
        if names[i] == fan:
            continue
        else:
            a[fan] = data[fan][i]
    for j in sorted(a.items(), key=lambda x:x[1]):
        fans.append(j[0])
        likes.append(j[1])    
    fig, ax = plt.subplots()
    ax.barh(fans, likes, color='#42C1EE')
    ax.set_title(f"{names[i]}'s Fan List")
    ax.set_xlabel('Number of likes')
    for i, v in enumerate(likes):
        ax.text(v, i, str(v))    
    fig.savefig(f'{names[i]}_fans.png')
    

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
fig6, ax6 = plt.subplots()

plt.style.use('fivethirtyeight')

##ax1b.pie(msg_count, labels=people_msg, wedgeprops={'edgecolor': 'black'}, startangle=90)
ax1.barh(people_msg, msg_count, color='#42C1EE')
ax1.set_title('Most Messages Sent')
ax1.set_xlabel('# of Messages')

ax2.barh(people_char, verbose, color='#42C1EE')
ax2.set_title('Most Characters/Message')
ax2.set_xlabel('# of Characters/Message')

ax3.barh(people_lg, charit, color='#42C1EE')
ax3.set_title('Most Likes Given')
ax3.set_xlabel('Likes given')

ax4.barh(people_lr, popular, color='#42C1EE')
ax4.set_title('Most Likes Received')
ax4.set_xlabel('Likes received')

ax5.barh(people_qual, quality, color='#42C1EE')
ax5.set_title('Average Likes per Message')
ax5.set_xlabel('Likes/Message')

ax6.barh(people_l, self_l, color='#42C1EE')
ax6.set_title('Self Promotion')
ax6.set_xlabel('Self likes')

for i, v in enumerate(msg_count):
    ax1.text(v, i, str(v))
for i, v in enumerate(verbose):
    ax2.text(v, i, str(v))
for i,v in enumerate(charit):
    ax3.text(v, i, str(v))
for i,v in enumerate(popular):
    ax4.text(v, i, str(v))
for i,v in enumerate(quality):
    ax5.text(v, i, str(v))
for i,v in enumerate(self_l):
    ax6.text(v, i, str(v))
    
plt.tight_layout()
plt.grid(False)
plt.show()
fig1.savefig('most_msgs.png')
fig2.savefig('char_per_msg.png')
fig3.savefig('likes_given.png')
fig4.savefig('likes_received.png')
fig5.savefig('like_per_msg.png')
fig6.savefig('self_like.png')
