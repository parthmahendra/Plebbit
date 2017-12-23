from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random, string, time, praw, json
from stem import Signal
from stem.control import Controller

UBLOCK = 'extension_1_14_20.crx'
HOST = '127.0.0.1'
PORT = #Your Tor Port
CONTROL_PORT = #Your Control Port

def AddExtensions(options , ExtensionLocation):
    options.add_extension(ExtensionLocation)
    return options

def BlockImages(options):
    prefs = {"profile.managed_default_content_settings.images":2}
    options.add_experimental_option("prefs",prefs)
    return options

def GetWindowDimensions(attribute):
    return driver.get_window_rect()[attribute]

def ResizeWindow(height, width):
    driver.set_window_size(width, height)

def GenerateRandom(initialNumber, range):
    return random.randint(initialNumber - range, initialNumber + range)

def SetSocks(host, port, options):
    options.add_argument("--proxy-server=socks5://" + host + ':' + port)
    return options

def Authorise(token):
    reddit = praw.Reddit(client_id= ReadDetails('CLIENTID'),
                         client_secret= ReadDetails('CLIENTSECRET'),
                         redirect_uri='http://localhost:8080',
                         user_agent='jkawdh')
    return reddit.auth.authorize(token)

def ChooseCountry():
    Choice = random.choice(Countries)
    print("Country ===> " + Choice)
    return Choice

def ClearTorCircuit(Port):
    with Controller.from_port(port = Port) as controller:
        controller.authenticate(password = "")
        controller.set_options({
            'ExitNodes' : '{}'.format(ChooseCountry())
        })
        controller.signal(Signal.NEWNYM)

def Click(xpath):
    Button = None
    while Button == None:
        try: Button = driver.find_element_by_xpath(xpath)
        except: pass
    driver.execute_script("arguments[0].click();", Button)

def Type(xpath, text):
    Field = None
    while Field == None:
        try: Field = driver.find_element_by_xpath(xpath)
        except: pass
    Field.send_keys(text)

def RandomText(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def StoreDetails(data, name):
    destination = json.load(open('../botnet.json', 'r'))
    destination[name].append(data)
    json.dump(destination, open('../botnet.json', 'w'))

def ReadDetails(name):
    return json.load(open('../botnet.json', 'r'))[name]

def Register():
    #Sign Up Button
    Click('//*[@id="header-bottom-right"]/span[1]/a[2]')
    #First Next Button
    Click('//*[@id="desktop-onboarding-sign-up-form"]/button')
    #Second Next Button
    Click('//*[@id="desktop-onboarding-browse"]/div[2]/footer/div[2]/button[2]')
    #Username
    Username = RandomText(7)
    Type('//*[@id="user_reg"]', Username)
    #Password
    Password = RandomText(9)
    Type('//*[@id="passwd_reg"]', Password)

    while driver.current_url != "https://www.reddit.com/r/popular/":
        pass

    StoreDetails(Password, 'PASSWORDS')
    StoreDetails(Username, 'USERNAMES')

def ReturnCode(url):
    return url.split("code=")[1]

def GetToken():
    driver.get(ReadDetails('URL'))
    Click('/html/body/div[3]/div/div[2]/form/div/input[1]')
    RefreshToken = Authorise(ReturnCode(driver.current_url))
    driver.quit()
    StoreDetails(RefreshToken, 'REFRESHTOKENS')

def Resize(Range):
    OldHeight = GetWindowDimensions('height')
    OldWidth  = GetWindowDimensions('width')
    NewHeight = GenerateRandom(OldHeight, Range)
    NewWidth  = GenerateRandom(OldWidth, Range)
    ResizeWindow(NewWidth, NewHeight)

def ChromeOptions():
    chrome_options = Options()
    chrome_options = AddExtensions(chrome_options ,UBLOCK)
    chrome_options = SetSocks(HOST, PORT, chrome_options)
    #chrome_options = BlockImages(chrome_options)
    return chrome_options

def Initialize():
    ClearTorCircuit(CONTROL_PORT)
    Resize(100)
    driver.get('https://www.reddit.com/')

Countries = ReadDetails("COUNTRIES")
driver = webdriver.Chrome("./chromedriver", chrome_options = ChromeOptions())
Initialize()
Register()
GetToken()
