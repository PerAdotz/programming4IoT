import requests

print('Available commands:')
print('all:      Return all the json')
print('devices:  Return all the devices')
print('houses:   Return all the houses')
print('users:    Return all the users')
print('quit:     Exit')

API = 'https://catalog-p4iot.onrender.com'
cmd_list = ['all','devices', 'houses','users']
cmd = input("Choose the command: ")
if cmd.strip().lower() != 'quit' :
    if  cmd.strip().lower() in cmd_list :
        URL = API + f"/{cmd}"
        r = requests.get(URL)
        if r.status_code == 200:
            json_cnt = r.json()
            print(json_cnt)
            #oppure
            """
            cnt = r.content.decode('utf-8')
            json_cnt = json.loads(cnt)
            print(json_cnt)
            """
        else:
            print(f'Error {r.status_code} fetching data')
    else:
        print('Command not available')
else:
    print('End')