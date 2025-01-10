import cherrypy
import random
import string
#service that is able to read the uri we send as GET request and return the string reversed

#exmaple : URL: http://127.0.0.1:8081/generate/cacca?first=1&second=2
# uri[0] = generate
# uri[1] = cacca
# params['first'] = 1
# params['second']=2

class ReversedUri(object):
    exposed = True
    
    def GET(self, *uri , **params):
        output = ""
        self.params = params
        #uri is an array , params a dictionary
        if len(uri) != 0:
            reversed_uri = ' '.join(uri)[::-1]
            output += reversed_uri
            return output + " " + self.generate()
        else:
            raise cherrypy.HTTPError(500)
        
    def generate(self):
        return "".join(random.sample(string.hexdigits , int(self.params['first']) ))
    
    def POST(self, *uri , **params):
        mystring = 'POST RESPONSE'
        mystring += cherrypy.request.body.read().decode('utf-8')
        return mystring
        
    def PUT(self, *uri , **params):
        mystring = 'PUT RESPONSE'
        mystring += cherrypy.request.body.read().decode('utf-8')
        return mystring
    
if __name__ == '__main__':
    conf = {
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tool.sessions.on':True
        }
    }
    webService = ReversedUri()
    cherrypy.tree.mount(webService , '/' , conf)
    cherrypy.config.update({'server.socket_port':8081})
    cherrypy.engine.start()
    cherrypy.engine.block()