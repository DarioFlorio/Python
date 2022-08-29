
#Input a website and crawl internal links

############################################################################################
#IMPORT DEPENDENCIES
import requests
############################################################################################
class Crawler:
    def __init__(self, website, domain):
        
        self.website = website
        self.domain = domain

    #set website url 
    def set_website(self):  
        self.website=input("Enter website:")
        #
        
        request = requests.get('http://www.example.com')
        if request.status_code == 200:
            print('Web site exists')
            return self.website
        else:
            print('Web site does not exist')
            self.website=input("Enter website:")
        
    #get website url
    def get_website(self):  
        #self.website=input("Enter website:")
        return self.website
    
    #set domain name
    def set_domain(self):  
        self.domain=input("Enter domain:")
        #return self.website
    #get domain name
    def get_domain(self):  
        #self.website=input("Enter website:")
        return self.domain
    
    
    
    
    
    
    
###########################################################################################


    
#create new object
crawl = Crawler("","")

#set website name
crawl.set_website()

#set domain name
crawl.set_domain()

#set domain name
website = crawl.get_website()





print(website)