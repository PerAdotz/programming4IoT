import cherrypy

class HelloWorld(object):
    exposed = True
    def GET(self, *uri , **params):
        output='Hello World'
        if len(uri) != 0:
            output += '<br>uri: '+','.join(uri)
        if params != {}:
            output += '<br>params: '+ str(params)
        return output
    
    #se passo http://localhost:8080/hello/world?name=Simone&age=22 nel browser :
    #questo è l'output
    """
    Hello World
    uri: hello,world
    params: {'name': 'Simone', 'age': '22'}
    """


if __name__ == '__main__':
    conf = {
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tool.sessions.on':True
        }
    }
    webService = HelloWorld()
    cherrypy.tree.mount(webService , '/' , conf)
    cherrypy.engine.start()
    cherrypy.engine.block()