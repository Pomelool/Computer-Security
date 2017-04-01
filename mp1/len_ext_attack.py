from pymd5 import md5, padding
import urllib
#token=94d5acaecc0d6d45f6bdabe2948722d2&user=admin&command1=ListFiles&command2=NoOp
m = "&command3=DeleteAllFiles"
x = md5()
h = md5(state = "94d5acaecc0d6d45f6bdabe2948722d2".decode("hex"), count = 512)
h.update(m)
h =  h.hexdigest()
url = "token="+h+"&user=admin&command1=ListFiles&command2=NoOp"+urllib.quote(padding(52*8))+m
f = open("./sol_2.1.2.txt","wb")
f.write(url)
