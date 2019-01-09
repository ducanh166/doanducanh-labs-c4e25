import datetime

x = 0

from gmail import GMail, Message

while x == 0:
    now = datetime.datetime.now()
    if now.hour == 7 :
       gmail = GMail('Duck And <highfivemid@gmail.com>','Htda181699')
       msg = Message('nghi om',to='xyz <tamha99hg@gmail.com>',text='<p>anh y&ecirc;u em</p>
<p>&nbsp;</p>')
       gmail.send(msg)
       x += 1