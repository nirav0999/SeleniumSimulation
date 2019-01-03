"""
Author-Nirav :D  
This is a Selenium Simulation to extract Author links from The Hindu Website and store them in all_authors_link[]
Through this ,we can access each individual author page 
"""
from selenium import webdriver 
# Install selenium by ------> python3 -m pip install --user selenium
import time
# to time each task 




chrome_path="chrome_driver/chromedriver"
#Download the chrome driver from Website and pate the path of the zip file here
driver=webdriver.Chrome(chrome_path)
driver.get("http://www.thehindu.com/profile/")
my_link="http://www.thehindu.com/profile/"


all_authors_link=[]



for j in range(1,27):#Scanning through all the Alphabets 
	print("============================================Starting a new Alphabet===================================="+str(j))
	alphabet_extract="//*[@id=\"correspondent\"]/div/div/div/div/div[1]/div[1]/ul/li["+str(j)+"]/a"
	driver.find_element_by_xpath(alphabet_extract).click()
	time.sleep(10)#Delay TO allow the page to load#Increase Delay on Slow Internet
	#Searching the Required Links on the page
	for i in range(4,13):
		print("--------------------------------This is a new XPath--------------------------------",str(i))
		links=driver.find_elements_by_class_name("auth-nm")
		for link in links:
			author_link=link.get_attribute('href')
			if author_link!=None:
				print(link.get_attribute('href'))
				all_authors_link.append(author_link)
		try:
			driver.find_element_by_xpath("//*[@id=\"correspondent\"]/div/div/div/div/div[3]/ul/li["+str(i)+"]/a/span").click()
			time.sleep(10)
		except:
			time.sleep(5)
			break
	
	
	






	


	