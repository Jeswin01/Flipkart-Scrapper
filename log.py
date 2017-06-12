from selenium import webdriver
import time
import scrapy
from selenium.webdriver.common.keys import Keys

class LoginSpider(scrapy.Spider):
 name = "log"
 start_urls = [
        'https://www.flipkart.com/search?q=electronics&otracker=start&as-show=on&as=off',
        
              ]
 def parse(self, response):
  path_to_chromedriver = '/home/jeswin/jeswin/chromedriver' 
  self.driver = webdriver.Chrome(executable_path = path_to_chromedriver)
  self.driver.get("https://www.flipkart.com/search?q=electronics&otracker=start&as-show=on&as=off")
  i=1
  while i<=10:
   
  	naml=self.driver.find_elements_by_class_name('_2cLu-l')
  	costl=self.driver.find_elements_by_class_name('_1vC4OE')

  
  	
        
  	
  	j=0
  	'_1No1qI'
  	while j<len(naml) and j<len(costl): 
  		yield {
         	'Name':naml[j].text,
         	'Cost':costl[j].text
       		      }
       		j=j+1
       	i=i+1	
       	#strg=str(i)
       	#nlink=self.driver.find_element_by_link_text(strg)
       	nlink=self.driver.find_element_by_link_text("%s"%i)
  	nlink.click()
  	self.driver.navigate().back()
  	naml=self.driver.find_elements_by_class_name('_1No1qI')
  	while(len(naml)<=0):
  		self.driver.navigate().back()
  		i=i+1
  		naml=self.driver.find_elements_by_class_name('_1No1qI')
  		nlink=self.driver.find_element_by_link_text("%s"%i)
  		nlink.click()	
  	assert "No results found." not in self.driver.page_source      
  	time.sleep(2)     
  self.driver.quit()    
       
      	
