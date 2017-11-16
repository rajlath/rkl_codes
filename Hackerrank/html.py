from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : " + tag)
    def handle_endtag(self, tag):
        print("End : "+ tag)
    def handle_startendtag(self, tag, attrs):
        print("Found an empty tag :", tag)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body><h1>HackerRank</h1><br /></body></html>")
