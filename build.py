import rcssmin

with open('awsl.css', 'r') as inf:
    raw = inf.read()
    copyright = raw[0:raw.find('**/') + 3] + '\n'
    copyright = copyright.replace('\r', '')
    out = rcssmin.cssmin(raw)
    with open('awsl.min.css', 'w+') as outf:
        outf.write(copyright + out)
