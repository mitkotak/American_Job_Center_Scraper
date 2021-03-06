from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('test_states.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k


print("Zipcodes : ",columns['Zipcode'])

	#header = [ 'Zipcode','Center_Name','Google_Maps_Link','Center_Website','Emails','Address','Phone','Telephones','Fax Machines','On-site Childcare','Video Viewing Stations','Rooms where employers can interview job seekers','Career Resource Room','Copy Machine','Personal Computers','Internet Access','Post your resume for employers to see','Get help in preparing for job interviews','Learn about strategies for finding a job','Find out how to get a work permit','Find out about job openings (including work experience, internships and community service)','Get help preparing your resume','Improve your current job skills','Learn about the world of business','Learn new job skills','Improve your English skills (ESL)','Improve your reading, writing and math skills','Get information about schools and training programs','Prepare for a high school equivalency (HSE) exam','Learn about financial aid for training','Get help finding child care','Get help with living expenses while in training','Get information about employers in your local area','Assess your reading and math skills','Learn about jobs and careers suitable for you','Learn about what employers expect of their workers','Assess your career interests and skills','Learn about jobs in demand and rates of pay','Find out about summer learning opportunities','Get help in finding a summer job','File Unemployment Insurance (UI) Claim','Get help in coping with the stress of job loss','Get help coping financially with job loss','Learn about community resources','Share job-search strategies with other job seekers (job club)','Get help preparing your resume','Learn about strategies for finding a job','Find out about job openings','Get help in preparing for job interviews','Post your resume for employers to see','Get information about education and training schools, such as their tuition and success in placing students in jobs','Prepare for a high school equivalency (HSE) exam','Improve your current job skills','Improve your English skills (ESL)','Improve your reading writing and math skills','Learn how to start your own business','Receive training in new job skills','Get help finding childcare','Get help with living expenses while in training','Assess your reading and math skills','Learn about jobs in demand and rates of pay','Learn about what employers expect of their workers','Get information about employers in your local area','Learn about jobs and careers suitable for you','Assess your career interests','Get outplacement services for employees you are laying off','Get information on employment, wage and salary trends','Receive information on the Work Opportunity Tax Credit and other hiring incentives','Learn about legal requirements for hiring and firing workers','Learn about EEO and ADA requirements','Get your employee training needs analyzed','Learn about Unemployment Insurance taxes and eligibility rules','Get training costs reimbursed for qualified job candidates','Develop programs to train new workers for your business','Get help in analyzing and writing job descriptions','Learn how to interview job applicants effectively','Learn about strategies for recruiting workers','Have job applicants` skills tested','Get job applicants pre-screened','Get access to resumes posted by job applicants','Post your job openings','Have background checks conducted on job applicants','Use on-site facilities for recruiting and interviewing job applicants']	
	
	#writer = csv.DictWriter(file, fieldnames = header)
	#writer.writeheader()
#print("Loading Firefox Driver")
#driver = webdriver.Firefox(executable_path=r'./drivers/geckodriver')
#print("Done")

for zipcode in columns['Zipcode']:
	file = open('scrapped_'+zipcode+'.csv', 'w+', newline ='')
	with file:
		#print("Loading Firefox Driver")
		#driver = webdriver.Firefox(executable_path=r'./drivers/geckodriver')
		#print("Done")
		print("Loading Chrome Driver..")
		driver = webdriver.Chrome('./drivers/chromedriver_mac')
		link_main = 'https://www.careeronestop.org/WorkerReEmployment/Toolkit/find-american-job-centers.aspx?location='+zipcode+'&radius=500&ct=0&y=0&w=0&e=0&sortcolumns=Distance&sortdirections=ASC&centerID=1517839&curPage=1&pagesize=500'
		print('opening link')
		driver.get(link_main)
		print("Let's start scraping :)")
		elems  = driver.find_elements_by_xpath('//*[@id="AJCTable"]/table/tbody//child::td')
		print(len(elems))
		if elems == []:
			continue
		links = []
		for i in range(0,len(elems),3):
			print("We are on Center: " + str(int(i/3)))
			link_html = driver.find_elements_by_xpath('//*[@id="AJCTable"]/table/tbody//child::td')[i].get_attribute("innerHTML")
			link = 'https://www.careeronestop.org'+link_html.replace(';','&')[29:link_html.find('true') + 4]
			print("Let's go to " + link)
			driver.get(link)
			print("Let's start scraping")
			center_name_elems = driver.find_elements_by_xpath('//div[@id = "detailsheading" and @name = "details-heading" and @class="notranslate detail-heading"]')
			if center_name_elems == []:
				center_name = ''	
			else:
				center_name = center_name_elems[0].text
			website_elems  =  driver.find_elements_by_xpath('//a[@target = "_blank"]')
			if website_elems == []:
				website = ''
			else:
				website = website_elems[0].text 
			google_maps_link_elems  = driver.find_elements_by_xpath('//a[@target = "_blank" and @class = "directions-link" and text() = "Directions"]')
			if google_maps_link_elems == []:
				google_maps_link = ''
			else:
				google_maps_link = google_maps_link_elems[0].get_attribute('href')
			address_elems = driver.find_elements_by_xpath('//*[@id="ctl27_tbAJCDetail"]/tr[1]/td[2]/span')
			if address_elems == []:
				address = ''
			else:	
				address = address_elems[0].text
			phone_element = driver.find_elements_by_xpath('//*[@id="ctl27_tbAJCDetail"]/tr[2]/td[2]/a')
			if phone_element == []:
				phone = ''
			else:
				phone = phone_element[0].text
			gr_elements = driver.find_elements_by_xpath('//*[@id="GenInfo"]/table/tbody//child::td')
			if gr_elements == []:
				driver.back()
				continue
			print('############################################################################################################################################################################################')
			grs = []
			for i in range(0,len(gr_elements),2):
				gr_col1_elem = gr_elements[i].get_attribute("innerHTML")
				if gr_col1_elem == []:
					gr_col1 = ''
				else:
					gr_col1 = gr_col1_elem[4:-4]

				gr_col2_elem = gr_elements[i+1].get_attribute("innerHTML")
				if gr_col2_elem == []:
					gr_col2 = ''
				else:
					gr_col2 = gr_col2_elem


				if gr_col2[0] == 'N':
					gr_col2 = gr_col2[0:2]
				elif gr_col2[0] == 'Y':
					gr_col2 = gr_col2[0:3]
				else:
					gr_col2 = gr_col2
				print(gr_col1)

				if gr_col2[1] == 'a':
					dels = []
					for i in range(len(gr_col2)):
						if (gr_col2[i] == ':'):
							dels.append(i)
						elif (gr_col2[i] == '>' and len(dels) != 0):
							pos = dels[-1]
							dels.pop()
						
							length = (i-1) - 1 - pos
				
							gr_col2 = gr_col2[pos + 1 : pos + 1 + length]
							break
			
				if gr_col2[0:25] == '<span class="notranslate"':
					gr_col2 = gr_col2[26:-11]
					print(gr_col2)
				if (gr_col1[0] == 'O') or (gr_col1[0:7]  == 'Parking') or (gr_col1[0:6] == 'Public') or (gr_col1[0:4] == 'Type') or (gr_col1[0:8] == 'Language'):
					gr_col2 = gr_col2[:-4]

				grs.append(gr_col1)
				print(gr_col2)
				grs.append(gr_col2)

			#srs = ['Telephones','Fax Machines','On-site Childcare','Video Viewing Stations','Rooms where employers can interview job seekers','Career Resource Room','Copy Machine','Personal Computers','Internet Access']	
			srs = []
			for i in range(1,10):
				sr_col1_link = '//*[@id="SR"]/table/tbody/tr['+str(i)+']/td[1]'
				sr_col1_elem = driver.find_elements_by_xpath(sr_col1_link)[0].get_attribute("innerHTML")
				if sr_col1_elem == []:
					sr_col1      = ''
				else:
					sr_col1      = sr_col1_elem[4:-4]
				print(sr_col1)
				srs.append(sr_col1)


				sr_col2_link = '//*[@id="SR"]/table/tbody/tr['+str(i)+']/td[2]'
				sr_col2_elem = driver.find_elements_by_xpath(sr_col2_link)[0].get_attribute("innerHTML")
				if sr_col2_elem == []:
					sr_col2 = ''
				else:
					sr_col2 = sr_col2_elem[:-4]
				if sr_col2[0] == 'Y':
					sr_col2 = sr_col2[0:3]
				elif sr_col2[0] == 'N':
					sr_col2 = sr_col2[0:2]
				else:
					sr_col2 = sr_col2
				print(sr_col2)				
				srs.append(sr_col2)

			#yss = ['Post your resume for employers to see','Get help in preparing for job interviews','Learn about strategies for finding a job','Find out how to get a work permit','Find out about job openings (including work experience, internships and community service)','Get help preparing your resume','Improve your current job skills','Learn about the world of business','Learn new job skills','Improve your English skills (ESL)','Improve your reading, writing and math skills','Get information about schools and training programs','Prepare for a high school equivalency (HSE) exam','Learn about financial aid for training','Get help finding child care','Get help with living expenses while in training','Get information about employers in your local area','Assess your reading and math skills','Learn about jobs and careers suitable for you','Learn about what employers expect of their workers','Assess your career interests and skills','Learn about jobs in demand and rates of pay','Find out about summer learning opportunities','Get help in finding a summer job']
			yss = []
			for i in range(1,25):
				ys_col1_link ='//*[@id="YS"]/table/tbody/tr['+str(i)+']/td[1]'	
				ys_col1_elem = driver.find_elements_by_xpath(ys_col1_link)[0].get_attribute("innerHTML")
				if ys_col1_elem == []:
					ys_col = ''
				else:
					ys_col1      = ys_col1_elem[4:-4]
				print(ys_col1)
				yss.append(ys_col1)

				ys_col2_link ='//*[@id="YS"]/table/tbody/tr['+str(i)+']/td[2]'
				ys_col2_elem = driver.find_elements_by_xpath(ys_col2_link)[0].get_attribute("innerHTML")
				if ys_col2_elem == []:
					ys_col2 = ''
				else:
					ys_col2 = ys_col2_elem[:-4]
				if ys_col2 == 'Y':
					ys_col2 = ys_col2[0:3]
				elif ys_col2 == 'N':
					ys_col2 = ys_col2[0:2]
				else:
					ys_col2 = ys_col2
				print(ys_col2)
				yss.append(ys_col2)

			#wss = ['File Unemployment Insurance (UI) Claim','Get help in coping with the stress of job loss','Get help coping financially with job loss','Learn about community resources','Share job-search strategies with other job seekers (job club)','Get help preparing your resume','Learn about strategies for finding a job','Find out about job openings','Get help in preparing for job interviews','Post your resume for employers to see','Get information about education and training schools, such as their tuition and success in placing students in jobs','Prepare for a high school equivalency (HSE) exam','Improve your current job skills','Improve your English skills (ESL)','Improve your reading writing and math skills','Learn how to start your own business','Receive training in new job skills','Get help finding childcare','Get help with living expenses while in training','Assess your reading and math skills','Learn about jobs in demand and rates of pay','Learn about what employers expect of their workers','Get information about employers in your local area','Learn about jobs and careers suitable for you','Assess your career interests']	
			wss = []
			for i in range(1,27):
				ws_col1_link ='//*[@id="WS"]/table/tbody/tr['+str(i)+']/td[1]'
				ws_col1_elem = driver.find_elements_by_xpath(ws_col1_link)[0].get_attribute("innerHTML")
				if ws_col1_elem == []:
					ws_col1 = ''
				else:
					ws_col1 = ws_col1_elem[4:-4]
				print(ws_col1)
				wss.append(ws_col1)


				ws_col2_link ='//*[@id="WS"]/table/tbody/tr['+str(i)+']/td[2]'
				ws_col2_elem = driver.find_elements_by_xpath(ws_col2_link)[0].get_attribute("innerHTML")
				if ws_col2_elem == []:
					ws_col2 = ''
				else:
					ws_col2 = ws_col2_elem[:-4]
				if ws_col2 == 'N':
					ws_col2 = ws_col2[0:2]
				elif ws_col2 == 'Y':
					ws_col2 = ws_col2[0:3]
				else:
					ws_col2 = ws_col2
				print(ws_col2)
				wss.append(ws_col2)

			#bss = ['Get outplacement services for employees you are laying off','Get information on employment, wage and salary trends','Receive information on the Work Opportunity Tax Credit and other hiring incentives','Learn about legal requirements for hiring and firing workers','Learn about EEO and ADA requirements','Get your employee training needs analyzed','Learn about Unemployment Insurance taxes and eligibility rules','Get training costs reimbursed for qualified job candidates','Develop programs to train new workers for your business','Get help in analyzing and writing job descriptions','Learn how to interview job applicants effectively','Learn about strategies for recruiting workers','Have job applicants` skills tested','Get job applicants pre-screened','Get access to resumes posted by job applicants','Post your job openings','Have background checks conducted on job applicants','Use on-site facilities for recruiting and interviewing job applicants']
			bss = []
			for i in range(1,19):
				bs_col1_link ='//*[@id="BS"]/table/tbody/tr['+str(i)+']/td[1]'
				bs_col1_elem = driver.find_elements_by_xpath(bs_col1_link)[0].get_attribute("innerHTML")
				if bs_col1_elem == []:
					bs_col1 = ''
				else:
					bs_col1 = bs_col1_elem[4:-4]
				print(bs_col1)
				bss.append(bs_col1)


				bs_col2_link ='//*[@id="BS"]/table/tbody/tr['+str(i)+']/td[2]'
				bs_col2_elem = driver.find_elements_by_xpath(bs_col2_link)[0].get_attribute("innerHTML")
				if bs_col2_elem == []:
					bs_col2 = ''
				else:
					bs_col2 = bs_col2_elem[:-4]
				if bs_col2 == 'N':
					bs_col2 = bs_col2[0:2]
				elif bs_col2 == 'Y':
					bs_col2 = bs_col2[0:3]
				else:
					bs_col2 = bs_col2
				print(bs_col2)
				bss.append(bs_col2)

			print(center_name)
			print('Website : ',website)
			print('Google Maps : ',google_maps_link)
			print('Address : ',address)
			print('Phone : ',phone)
			body  = [zipcode,'Center_Name',center_name,'Website',website,'Google_Maps_Link',google_maps_link,'Address',address,'Phone',phone]
			body = body + grs + srs + yss + bss
			header = ['Zipcode']

			for i in range(1,len(body)):
				header.append('col'+str(i))
		
			writer = csv.DictWriter(file, fieldnames = header)

			dict_csv = {}
			for i in range(len(body)):
				dict_csv[header[i]] = body[i]
			writer.writerow(dict_csv)	
			print("Row added")
			driver.back()
			from time import sleep
			sleep(3)

print('csv created')
