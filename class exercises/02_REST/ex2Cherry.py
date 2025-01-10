import cherrypy
import json
#service that is able to read the body of a POST request and return a json response with the values reversed, use thunderclient
# input : {"param1" : "Hey" , "param2" : "Friday"}
#output : {"param1": "yeH","param2": "yadirF"}
class doingPOST(object):
    exposed = True
    
    def POST(self, *path , **query):
        res = dict()
        req = cherrypy.request.body.read().decode('utf-8')
        dict_req = json.loads(req)
        for key, value in dict_req.items():
            res[key] = value[::-1]
        return json.dumps(res)
    
    #prof solution
    # def PUT(self,*uri,**params):
    # body_read=cherrypy.request.body.read()
    # if len(body_read)>0:
    #     try:
    #         json_body=json.loads(body_read)
    #         output={}
    #         for key in json_body.keys():
    #             output[key]=string_reverse(json_body[key])
    #         return json.dumps(output)
    #     except json.decoder.JSONDecodeError:
    #         raise cherrypy.HTTPError(400,"Bad Request. Body must be a valid JSON")
    #     except:
    #         raise cherrypy.HTTPError(500,"Internal Server Error")
    # else:
    #     return "Empty body"

    
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