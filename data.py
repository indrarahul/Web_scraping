from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pandas as pd
from time import sleep	
import operator
opts = Options()
opts.set_headless()
browser = Firefox(options = opts)
browser.get('https://knoema.com/zhziwrg/bangalore-census-data-ward-wise?variable=Illiterate%20Female#')

# citz = browser.find_element_by_id('sel0IF_chzn')

def get():
	a = browser.find_elements_by_class_name('member-name')
	b = browser.find_elements_by_class_name('member-value')
	# cz = browser.find_element_by_id('sel0IF_chzn')
	filename = 'k.csv'
	m = {}
	k = []
	for i in range(0,len(a)):
		m[int(b[i].text.replace(',',''))]= a[i].text[24:] 
	sort = sorted(m.items(),key=operator.itemgetter(1))
	for i in range(0,len(sort)):
		k.append(sort[i][0])
	df= pd.DataFrame(k)
	df.to_csv(filename, sep='\t', encoding='utf-8',index=False)
	print ("Done " + filename)
get()

# for i in range(1,85):
# 	citz.click()
# 	kk = browser.find_element_by_id('sel0IF_chzn_o_{}'.format(i))
# 	kk.click()
# 	sleep(2)
# 	get()
browser.close()