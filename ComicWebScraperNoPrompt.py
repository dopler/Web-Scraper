import requests, webbrowser, bs4, time, datetime, smtplib

#print(type(smtpObj))

'''chosenTime = datetime.datetime(2016,8,23,8,51,0)

while datetime.datetime.now() < chosenTime:
	time.sleep(3)
	
print('hello world')

'''

comicList = 'Subject: This Weeks List: \n\n'

#make request and open page
res = requests.get('http://www.comiclist.com/index.php')
res.raise_for_status()
#parse html contents into 'soup'
soup = bs4.BeautifulSoup(res.text, "html.parser")
#find all the <a> tags (html links within the page)
linkElms = soup.find_all('a')

#read pull list from file
comicsFile = open('ComicSeries.txt')
comicsCompare = comicsFile.read().split('\n')

#comicsCompare = comicsCompare[:-1]

for linkElm in linkElms:
	for titles in comicsCompare:
		if(titles.strip('\n') in linkElm.getText()):
			#print('hit')
			##baconFile.write(linkElm.getText() + '\n')
			comicList += linkElm.getText() + '\n'

#file contains email to send to and email to send from
credentialsFile = open('Credentials.txt')
credentials = credentialsFile.read().split('\n')

#establish port
#establish port
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
##print(smtpObj.ehlo())
#start encryption
smtpObj.starttls()
#login succesful?
print(smtpObj.login(credentials[0], credentials[1]))
#send email
smtpObj.sendmail(credentials[0], credentials[2], comicList)
#close connection
smtpObj.quit()
print("This Weeks Comics:\n")
print(comicList)
