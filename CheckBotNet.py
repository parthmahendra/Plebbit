import json, praw

def ReadDetails(name):
    return json.load(open('botnet.json', 'r'))[name]

def ReturnUsers():
    Usernames = []
    for RT in ReadDetails('REFRESHTOKENS'):
        plebbit = praw.Reddit(client_id = ClientID,
                              client_secret = ClientSecret,
                              refresh_token = RT,
                              user_agent = 'r/cuck')
        Usernames.append(plebbit.user.me().name)
    return Usernames

def RedditClient():
    reddit = praw.Reddit(client_id = ClientID,
                          client_secret = ClientSecret,
                          user_agent = 'r/cuck')
    return reddit

def CheckUsers(UserArray, Reddit):
    Users = UserArray
    for User in UserArray:
        try:
            redditor = Reddit.redditor(User)
            if hasattr(redditor, 'fullname'):
                print(User + " ===> Alive\n")
            elif hasattr(redditor, 'is_suspended'):
                print(User + " ===> Suspended\n")
        except praw.errors.NotFound:
            print(User + " ===> ShadowBanned\n")
            Users.remove(User)
    return Users

ClientID = ReadDetails('CLIENTID')
ClientSecret = ReadDetails('CLIENTSECRET')
ArmyLeft = CheckUsers(ReturnUsers(), RedditClient())

print(ArmyLeft)
print(len(ArmyLeft))
