import random, json, praw, os
from stem import Signal
from stem.control import Controller
from stem import CircStatus

def ReadDetails(name):
    return json.load(open('botnet.json', 'r'))[name]

possibles = "abcdefghijklmnopqrstuvwxyz0123456789"
def GenerateBase36(length):
    String = ""
    for i in range(length):
        String += RandomCharacter(possibles)
    return String

def RandomCharacter(possibleCharacters):
    characters = list(possibleCharacters)
    return random.choice(characters)

def Upvote(Reddit, ID):
    print("ID ===> " + ID)
    Reddit.submission(ID).upvote()

def Downvote(Reddit, ID):
    print("ID ===> " + ID)
    Reddit.submission(ID).downvote()

def InitRedditInstance(RT):
    plebbit = praw.Reddit(client_id = CLIENTID,
                          client_secret = CLIENTSECRET,
                          refresh_token = RT,
                          user_agent = 'r/cuck')
    print("Username ===> " + plebbit.user.me().name)
    return plebbit

def PickRefreshToken(RTList):
    return random.choice(RTList)

def Choice():
    if random.randint(0, 1) >= 0.5:
        return True
    else:
        return False

def UntilNoError(plebbit, fun):
    Done = False
    while Done != True:
        try:
            fun(plebbit, GenerateBase36(6))
            Done = True
        except Exception as e:
            print(e)

def SetSocks(Host, Port):
    os.environ['https_proxy'] = "socks5://" + Host + ":" + Port

def ChooseCountry():
    return random.choice(COUNTRIES)

def ClearTorCircuit(Port):
    with Controller.from_port(port = Port) as controller:
        controller.authenticate(password = #Your Control Port Password)
        controller.set_options({
            'ExitNodes' : '{}'.format(ChooseCountry())
        })
        controller.signal(Signal.NEWNYM)

CLIENTID = ReadDetails('CLIENTID')
CLIENTSECRET = ReadDetails('CLIENTSECRET')
REFRESHTOKENS = ReadDetails('REFRESHTOKENS')
COUNTRIES = ReadDetails('COUNTRIES')

SetSocks('127.0.0.1', #Your SOCKS Port)
for i in range(50):
    try:
        ClearTorCircuit(#Your Control Port)
        RT = PickRefreshToken(REFRESHTOKENS)
        plebbit = InitRedditInstance(RT)
        ID = GenerateBase36(6)
        if Choice():
            UntilNoError(plebbit, Upvote)
        else:
            UntilNoError(plebbit, Downvote)
        print('done!\n')
    except Exception as e:
        print(e)
        print("Failed!\n")
