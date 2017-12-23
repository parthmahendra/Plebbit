# Plebbit
A Botnet for Reddit using automated proxies

### BotCreation/accountCreation.py
+ Script that creates accounts using randomized proxies
+ Stores the data into ../botnet.json
+ Uses Adblocker to speed up loading times
+ Unfortunately Captcha needs to be done manually

### Automation.py
+ Script to use the botnet
+ Uses randomized proxies so no rate limitation
+ Can be slow if botnet gets big
+ Don't spam post or else you *will* get everyone banned

### Obfuscation.py
+ Script that cloaks the actions of the botnet through random actions
+ Only Upvotes and Downvotes submissions so far

### CheckBotNet.py
+ Checks how much of the botnet is alive
+ Uses a read-only instance of reddit
+ Slow as all hell as it gathers usernames again (for a good reason)

### botnet.json
+ Used to store the botnet
+ Unfortunately Python automatically minifies it
