from bs4 import BeautifulSoup, Tag
import csv
import urllib.request
import pandas as pd
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)
def visit(pnames, langarg):
	for i in range(0, len(pnames)):
		pnames[i] = pnames[i].lower()
		pnames[i] = pnames[i].replace(" ", "-")
		pnames[i] = pnames[i].replace(",", "")
	print(pnames)
	

	driver.get("https://www.hollandamerica.com/")
	time.sleep(1)
	urls = []
	info = {}
	if langarg == "de":
		dropdown = driver.find_element_by_class_name('dropdown-label')
		dropdown.click()
		items = driver.find_elements_by_class_name('dropdown-item')
		for item in items:
			if '-3' in str(item):
				item.click()
				for name in pnames:
					info[name] = {}
					url = "http://www.hollandamerica.com/de_DE/ports/"+name+".html?"
					info[name]["uri"] = url
					driver.get(url)
					if len(driver.find_elements_by_class_name('image-lazy-loader')) != 0:
						info[name]["heropresent"] = "y"
					else:
						info[name]["heropresent"] = "n"
					if len(driver.find_elements_by_class_name('desc')) != 0:
						info[name]["textpresent"] = "y"
					else:
						info[name]["textpresent"] = "n"
	elif langarg == "en":
		for name in pnames:
			info[name] = {}
			url = "http://www.hollandamerica.com/en_US/ports/"+name+".html?"
			info[name]["uri"] = url
			driver.get(url)
			if len(driver.find_elements_by_class_name('image-lazy-loader')) != 0:
				info[name]["heropresent"] = "y"
			else:
				info[name]["heropresent"] = "n"
			if len(driver.find_elements_by_class_name('desc')) != 0:
				info[name]["textpresent"] = "y"
			else:
				info[name]["textpresent"] = "n"
	elif langarg == "es":
		dropdown = driver.find_element_by_class_name('dropdown-label')
		dropdown.click()
		items = driver.find_elements_by_class_name('dropdown-item')
		for item in items:
			if '-4' in str(item):
				item.click()
				for name in pnames:
					info[name] = {}
					url = "http://www.hollandamerica.com/es_ES/ports/"+name+".html?"
					info[name]["uri"] = url
					driver.get(url)
					if len(driver.find_elements_by_class_name('image-lazy-loader')) != 0:
						info[name]["heropresent"] = "y"
					else:
						info[name]["heropresent"] = "n"
					if len(driver.find_elements_by_class_name('desc')) != 0:
						info[name]["textpresent"] = "y"
					else:
						info[name]["textpresent"] = "n"
	else:
		dropdown = driver.find_element_by_class_name('dropdown-label')
		dropdown.click()
		items = driver.find_elements_by_class_name('dropdown-item')
		for item in items:
			if '-5' in str(item):
				item.click()
				for name in pnames:
					info[name] = {}
					url = "http://www.hollandamerica.com/nl_NL/ports/"+name+".html?"
					info[name]["uri"] = url
					driver.get(url)

					if len(driver.find_elements_by_class_name('image-lazy-loader')) != 0:
						info[name]["heropresent"] = "y"
					else:
						info[name]["heropresent"] = "n"
						
					if len(driver.find_elements_by_class_name('desc')) != 0:
						info[name]["textpresent"] = "y"
					else:
						info[name]["textpresent"] = "n"
						
					
	with open("new.txt", "a") as f:
		f.write(str(info))
		
			


def read(filename):
	with open(filename) as csvfile:
		reader = pd.read_csv(filename)
		firstcol = reader['pname']
		print(firstcol)
		items = []
		for item in firstcol:
			items.append(item)
		visit(items, "de")

read("asia.csv")
