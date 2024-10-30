import cherrypy
#service that is able to read the uri we send as GET request and return the string reversed
class ReversedUri(object):
    exposed = True
    
    def GET(self, *uri , **params):
        output = ""
        if len(uri) != 0:
            # reversed_uri = '/'.join(uri)[::-1]
            reversed_uri = ' '.join(uri)[::-1]
            output += reversed_uri
        if params != {}:
            output += '<br>params: '+ str(params)
        return output
    
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