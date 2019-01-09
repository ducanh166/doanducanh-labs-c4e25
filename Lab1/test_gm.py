from gmail import GMail, Message
import random
sickness_list = ["lậu", "giang mai", "hiv"]
gmail = GMail('Duck And <highfivemid@gmail.com>','Htda181699')
html = '''
<p>Ch&agrave;o sếp,</p>
<p>S&aacute;ng nay ngủ dậy em thấy&nbsp;<strong>đau bụng</strong>, b&aacute;c sỹ bảo em bị&nbsp;<strong>{{sickness}}</strong>. Sếp cho em nghỉ l&agrave;m h&ocirc;m nay nh&eacute;.&nbsp;<img class="CToWUd" src="https://ci4.googleusercontent.com/proxy/-DtFjdxQVsaE4cnKPuxdzqCT5p8BaGpR-WzZlV7EDFqFTGpYxle4zD4CkbMUhJ1QaSFITwRl9QjVNZE1Q1WdfkPWyFHL7gW3ihFyuI38tEbSP-7eae-c8g=s0-d-e1-ft#https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>Em cảm ơn sếp,</p>
<p><strong>Nh&acirc;n vi&ecirc;n</strong></p>
'''
html_content = html.replace("{{sickness}}",random.choice(sickness_list))

msg = Message('Test Message',to='qhuydtvt@gmail.com',html=html_content)
gmail.send(msg)

print(html_content)