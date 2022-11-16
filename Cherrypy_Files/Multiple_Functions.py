import cherrypy

class WebClass(object) :
    @cherrypy.expose
    def index (self):
        return "This is the First Page"
    
    @cherrypy.expose
    def secondPage(self):
        return "This is the second page"

if __name__ == '__main__' :
    cherrypy.quickstart(WebClass())

''' 
The first page i.e index page will open when we run our program    
To open the second page we will run http://127.0.0.1:8080/secondPage
'''
