import cherrypy
import json
#service that is able to read the body of a POST request and return a json response with the values reversed
class doingPOST(object):
    exposed = True
    
    def POST(self, *path , **query):
        res = dict()
        req = cherrypy.request.body.read().decode('utf-8')
        dict_req = json.loads(req)
        for key, value in dict_req.items():
            res[key] = value[::-1]
        return json.dumps(res)
    
if __name__ == '__main__':
    conf = {
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tool.sessions.on':True
        }
    }
    webService = doingPOST()
    cherrypy.tree.mount(webService , '/' , conf)
    cherrypy.config.update({'server.socket_port':8082})
    cherrypy.engine.start()
    cherrypy.engine.block()