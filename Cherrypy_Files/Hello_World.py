import cherrypy

class HelloWorld (object) :
    @cherrypy.expose
    def index (self):
        return "HELLO WORLD"

if __name__ == "__main__" :
    cherrypy.quickstart(HelloWorld())