from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r'C:\Users\verbi\chromedriver_win32\chromedriver.exe')
driver.get("https://www.cecb-tool.ch/experts?ln=fr#/")
elemAll = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='expertsGrid']/div/div[6]/div/div/div/div/table")))
#elemAll = driver.find_element_by_xpath("//*[@id='expertsGrid']/div/div[6]/div/div/div/div/table")
elemAllTr = elemAll.find_elements_by_tag_name('tr')
list_of_experts = []
names = ['nom', 'prenom', 'societe', 'informations', 'code', 'npa','ville']
#for num in range(len(elemAllTr)):
#	gens = [e.text for e in elemAllTr[num].find_elements_by_tag_name('td')]
#	list_of_experts.append(dict(zip(names, gens)))
list_of_experts_add = []
for num in range(len(elemAllTr)):
	gens_add = [e.text for e in elemAllTr[num].find_elements_by_tag_name('td')]
	list_of_experts_add.append(gens_add)

wb = openpyxl.load_workbook(r"C:\Users\verbi\Desktop\BIM\CRM\Experts.xlsx")
sheet = wb.active
for x in range(len(names)):
	
	cell = sheet.cell(row = 1, column = x + 1)
	cell.value = names[x]
	
for y in range(len(list_of_experts_add)):
	for x in range(len(list_of_experts_add[1])):
		cell = sheet.cell(row = y + 2, column = x + 1)
		cell.value = list_of_experts_add[y][x]

wb.save(r"C:\Users\verbi\Desktop\BIM\CRM\Experts.xlsx")


#>>> a = elemAllTr[9].find_element_by_tag_name('a')
#>>> a.click()
#>>> driver.current_url
#'https://www.cecb-tool.ch/experts/details/DieterAffeltranger-4462#/'
#>>> b = driver.find_element_by_link_text('Vers la liste des experts')
#>>> b.click()
