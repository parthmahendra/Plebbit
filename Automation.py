import praw, json, os, random, socks, socket, requests
from stem import Signal
from stem.control import Controller
from stem import CircStatus

def ChooseCountry():
    Choice = random.choice(Countries)
    print("Country ===> " + Choice)
    return Choice

def SetSocks(Host, Port):
    os.environ['https_proxy'] = "socks5://" + Host + ":" + Port

def ClearTorCircuit(Port):
    with Controller.from_port(port = Port) as controller:
        controller.authenticate(password = #Your Control port password)
        controller.set_options({
            'ExitNodes' : '{}'.format(ChooseCountry())
        })
        controller.signal(Signal.NEWNYM)

def ReadDetails(name):
    return json.load(open('botnet.json', 'r'))[name]

def SeeIP():
    with Controller.from_port(port = 9051) as controller:
      controller.authenticate(#Your control port password)
      for circ in controller.get_circuits():
        if circ.status != CircStatus.BUILT:
          continue
        exit_fp, exit_nickname = circ.path[-1]
        exit_desc = controller.get_network_status(exit_fp, None)
        exit_address = exit_desc.address if exit_desc else 'unknown'
        return exit_address

def initRedditInstance(RT):
    reddit = praw.Reddit(client_id = ReadDetails('CLIENTID'),
                         client_secret = ReadDetails('CLIENTSECRET'),
                         refresh_token = RT,
                         user_agent='r/cuck')
    return reddit

Countries = ReadDetails("COUNTRIES")
SetSocks('127.0.0.1', '9050')

CLIENTID = ReadDetails('CLIENTID')
CLIENTSECRET = ReadDetails('CLIENTSECRET')

for RT in ReadDetails('REFRESHTOKENS'):
    ClearTorCircuit(#Your control port)
    print("IP ===> " + str(SeeIP()))
    reddit = initRedditInstance(RT)
    try:
        #what the botnet needs to do
        print('done\n')

    except Exception as e:
        print(e)
        print('failed\n')
