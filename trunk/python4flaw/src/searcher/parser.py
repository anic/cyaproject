from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.markData = False
 
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        self.markData = False
        if tag == "span":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "class" and value == "f34_":
                        self.markData = True
#                        self.links.append(tag.data)
    
    def handle_data(self, data):
        if self.markData == True:
            self.links.append(data)

    def handle_endtag(self, tag):
        self.markData = False