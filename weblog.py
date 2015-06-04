# Import required modules
try:
    import sys
    import re
except ImportError:
    print "Could not import required modules"
    sys.exit()

# Global Variables (Dictionaries) to store count
IPs = {}    # <ip>:<hits>
Hosts = {}  # <hostname>:<other info>
UAs = {"Firefox":{},"Safari":{},"MSIE":{},"Googlebot":{},"Yahoo":{},"Chrome":{},"Opera":{},"BrowseX":{},"Exabot":{}}

# Classes
class Host(dict):
    def __init__(self, **kwargs):
        super(Host, self).__init__(**kwargs)
        self.__dict__ = self
        
class UserAgent():
    def __init__(self, name):
        self.count = 0
        self.name = name
        self.details = ""

# Open Weblog file
try:
    logfile = open("weblog.txt")
except:
    print "Cannot open log file."
    sys.exit()

pattern = r'([\d\.]+) - - \[(.*?)\] "(\w+) (.*?) (HTTP/1.[01])" (\d+) (\d+|-) "(.*?)" "(.*?)"'

# Each line in log is divided into groups by above RE pattern
#group 1 - IP Address
#group 2 - day and date
#group 3 - Request method
#group 4 - Requested URL
#group 5 - HTTP Version
#group 6 - HTTP status
#group 7 - Response size
#group 8 - Referer
#group 9 - User-agent

user_agents = {"Firefox":0,"Safari":0,"MSIE":0,"Googlebot":0,"Yahoo":0,"Chrome":0,"Opera":0,"BrowseX":0,"Exabot":0}

for line in logfile:
    match = re.search(pattern,line)

    # IP Address
    ip = match.group(1)
    if ip not in IPs:
        IPs[ip] = 1
    else:
        IPs[ip] += 1
    

    # Request URL
    request = match.group(4)
    req_url = re.search(r'^\w\w\w\.(.*?)\.\w\w\w(.*)', request)
    if req_url == None:
        req_url = re.search(r'^(.*?)\.\w\w\w(.*)', request)
    hostname = req_url.group(1)
    page = req_url.group(2)
    
    if hostname not in Hosts:
        host_obj = Host(hostname = hostname, pages={},response = {},day_count = {},referers={})
        Hosts[hostname] = host_obj
        Hosts[hostname].pages[page] = 1
    elif page not in Hosts[hostname].pages:
        Hosts[hostname].pages[page] = 1
    else:
        Hosts[hostname].pages[page] += 1
    
    
    # Response code
    response_code = int(match.group(6))
    response_key = str(int(response_code/100))+"xx"
    if response_key not in Hosts[hostname].responses:
        Hosts[hostname].responses[response_key] = 1
    else:
        Hosts[hostname].response[response_key] += 1
    
    
    # Date
    date_string = re.search(r'(.*?):',match.group(2))
    req_date = date_string.group(1)

    if req_date not in Hosts[hostname].day_count:
        Hosts[hostname].day_count[req_date] = 1
    else:
        Hosts[hostname].day_count[req_date] += 1
    

    # Referer
    referer = match.group(8)
    if referer != "-":
        if referer not in Hosts[hostname].referers:
            Hosts[hostname].referers[referer] = 1
        else:
            Hosts[hostname].referers[referer] += 1

    # User agent
    user_agent = match.group(9)
    
    for ua in UAs:
        if ua in user_agent:
            if UAs[ua].keys()==[]:
                UAs[ua]['count'] = 1
            else:
                UAs[ua]['count'] += 1
            UAs[ua]['details'] = user_agent
            
for host in Hosts:
    print Hosts[host]
for ua in UAs:
    print UAs[ua]
