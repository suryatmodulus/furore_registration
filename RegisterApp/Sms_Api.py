import urllib.request
import urllib.parse
 
def Send_Sms(number,message):
    data =  urllib.parse.urlencode({'mobiles':number,'message' : message})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://control.msg91.com/api/sendhttp.php?authkey=144888A5cM4rfEm5d58c7d224&sender=FURORE&route=4&country=91")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    print(fr)
 
