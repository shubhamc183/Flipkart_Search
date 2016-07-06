import sys
import requests
from bs4 import BeautifulSoup
import re
def flipkart(q,n):
	if n!='':
		n=int(n)-1
	else:
		n=0									# if no input is given 
	Q=""
	for i in q.split():
		Q+=i+"+"
	Q=Q[:len(Q)-1]
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}			#To spoof Python
	sort=['relevance','popularity','price_asc','price_desc','recency_desc']		#to sort accordingly
	query=requests.get('http://www.flipkart.com/all-categories/pr?p%5B%5D=sort%3D{s}&sid=search.flipkart.com&filterNone=true&q={q}'.format(q=Q, s=sort[n]),headers=headers)
	soup=BeautifulSoup(query.text,"html.parser")	
	l=soup.findAll("div",{"class":"pu-details lastUnit"})				# "pu-details lastUnit" contains all the details of product
	for i in l:
		t=i.find("a").get_text()
		name=re.findall('[a-zA-Z0-9].*',t)					# link is the name of product ..!
		print(name[0],end=" ")
		if i.find("span",{"class":"fk-font-12"})!=None:				# if price is cut down
			price=re.findall('\s([0-9.,]+)',i.find("span",{"class":"fk-font-12"}).text)
			print('Rs.',price[0],sep='',end=" ")	
		else:									# if not..
			price=re.findall('\s([0-9.,]+)',i.find("div",{"class":"pu-final"}).get_text())
			print('Rs.',price[0],sep='',end=" ")
		if i.find("div",{"class":"pu-rating"})!=None:				#  IF ratings are available
			ratings=re.findall('([0-9]+)',i.find("div",{"class":"pu-rating"}).text)
			print(ratings[0],'_Ratings',sep='')
		else:
			print("No ratings found..!")
c=0
while(1):
	q=input("Name the product\n")
	c+=1
	if len(q)==0:
		print("You typed nothing.....!")
	if c>=2:
		print("TYPE e/E to exit or anything else to continue")
		rep=input()
		if rep=='e' or rep=='E':
			print("Thank You...!")
			sys.exit(0)
		else:
			c=0
			continue
	if len(q)>0:
		break
print("How do you want to sort the items..!")
print("1.Relevance (Default) ","2.Popular","3.Low Price","4.High Price","5.New",sep="\n")
n=input()
flipkart(q,n)
