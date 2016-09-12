import httplib, time, datetime

while (True):
    conn = httplib.HTTPConnection("localhost", 8000)
    conn.request("GET", "/tenis/refresh/")
    r1 = conn.getresponse()
    print "[" + str(datetime.datetime.now()) + "] - ", r1.status, r1.reason
    time.sleep(2)
