import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#options = webdriver.ChromeOptions()
#options.add_experimental_option("useAutomationExtension", False)
#options.add_experimental_option("excludeSwitches",["enable-automation"])
#options.add_argument("user-data-dir=C:\\Users\\lukek\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
#driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
#driver = webdriver.Chrome(driver_path, options= options)
options = Options()
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(r"--user-data-dir=C:\Users\lukek\AppData\Local\Google\Chrome\User Data\Profile 1")
options.add_argument(r'--profile-directory=Default')
driver = webdriver.Chrome(options=options)

def dellFunctionSerialAndWarranty(serial):
    try:
        driver.get("https://www.dell.com/support/home/en-us")
        time.sleep(.1)
        serial_input = driver.find_element(By.ID, 'mh-search-input')
        serial_input.click()
        time.sleep(.1)
        serial_input.send_keys(serial)
        time.sleep(.1)
        serial_input.send_keys(Keys.RETURN)
        time.sleep(.1)
        wait = WebDriverWait(driver, 10)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="site-wrapper"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/h1')))
        expDate = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ps-inlineWarranty"]/div[1]/div/p')))
        el_text = el.text
        expDate_text = expDate.text
        print(el_text,expDate_text)
        return(el_text,expDate_text)
    
    except:
        driver.get("https://www.dell.com/support/home/en-us")
        time.sleep(.1)
        serial_input = driver.find_element(By.ID, 'mh-search-input')
        serial_input.click()
        time.sleep(.1)
        serial_input.send_keys(serial)
        time.sleep(.1)
        serial_input.send_keys(Keys.RETURN)
        time.sleep(.1)
        wait = WebDriverWait(driver, 10)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="site-wrapper"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/h1')))
        expDate = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ps-inlineWarranty"]/div[1]/div/p')))
        el_text = el.text
        expDate_text = expDate.text
        return(el_text,expDate_text)
    
def lenovoFunctionSerialAndWarranty(serial):
        wait = WebDriverWait(driver, 10)
        driver.get("https://pcsupport.lenovo.com/us/en/")
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').click()
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').send_keys(serial)
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').send_keys(Keys.RETURN)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-psp-home"]/div/div[2]/div[2]/section/div/div/div[2]/h2')))
        el_text = el.text
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="app-psp-home"]/div/div[2]/div[2]/section/div/div/div[5]/div[2]/button').click()
        el2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-psp-warranty"]/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[5]/span[2]')))
        time.sleep(.1)
        el2_text = el2.text
        print(el_text, el2_text)
        return(el_text, el2_text)
    
def hpFunctionSerialAndWarranty(serial):
        wait = WebDriverWait(driver, 10)
        driver.get("https://support.hp.com/us-en")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="searchQueryField"]')))
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').click()
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').send_keys(serial)
        time.sleep(.2)
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').send_keys(Keys.RETURN)
        wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/app-root/div/app-layout/app-pdp/div/div[1]/app-pdp-product-card/div/div[2]/div[2]/h1')))
        time.sleep(.1)
        el = driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout/app-pdp/div/div[1]/app-pdp-product-card/div/div[2]/div[2]/h1').text
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="fulldetails"]/div/div').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/app-layout/app-check-warranty/div/div/div[2]/app-warranty-details/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/div[5]/div[2]')))
        time.sleep(.1)
        el2 = driver.find_element(By.XPATH, '/html/body/app-root/div/app-layout/app-check-warranty/div/div/div[2]/app-warranty-details/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/div[5]/div[2]').text

        print(el, el2)
        return(el, el2)
    # for specs
    #/html/body/app-root/div/app-layout/app-pdp/div/div[3]/app-pdplanding/div/div/div/app-vn-support-category-options/div/div/a[5]/div


#DEll EVERYTHING
def detialSystemConfig(rows):
    value = ''
    for row in rows:
        if row.get_attribute('class') == 'border-top border-platinum bg-white rounded-bottom js-original-config-details collapse show':
            ts = row.find_elements(By.ID, 'OriginalConfigContent-table')
            for t in ts:
                tbody = t.find_elements(By.TAG_NAME, 'tbody')
                for tbs in tbody:
                    trs = tbs.find_elements(By.TAG_NAME, 'tr')
                    for tr in trs:
                        tds = tr.find_elements(By.TAG_NAME, 'td')
                        for td in tds:
                            value += td.text
                        return value
def dellEverything(serial):
        driver.get("https://www.dell.com/support/home/en-us")
        time.sleep(.1)
        serial_input = driver.find_element(By.ID, 'mh-search-input')
        serial_input.click()
        time.sleep(.1)
        serial_input.send_keys(serial)
        time.sleep(.1)
        serial_input.send_keys(Keys.RETURN)
        time.sleep(.1)
        wait = WebDriverWait(driver, 10)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="site-wrapper"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/h1')))
        expDate = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ps-inlineWarranty"]/div[1]/div/p')))
        el_text = el.text
        expDate_text = expDate.text
        time.sleep(.5)
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div[16]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a').click()
        time.sleep(.5)
        wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="expandAllLink"]')))
        time.sleep(.1)
        driver.find_element(By.XPATH,'//*[@id="expandAllLink"]').click()
        table  = driver.find_element(By.XPATH, '//*[@id="systab_originalconfig"]')
        cells = table.find_elements(By.TAG_NAME, 'div')
        elRam = ''
        elDrive = ''
        elCpu = ''

        for cell in cells:
            if cell.get_attribute('class') == 'card mb-4':
                rows = cell.find_elements(By.TAG_NAME, 'div')
                for row in rows:
                    if row.get_attribute('class') == 'd-flex align-items-start bg-mist py-3 px-6':
                        texts = row.find_elements(By.TAG_NAME, 'span')
                        for text in texts:
                            if text.text.__contains__("State Drive") or (text.text.__contains__('Hard Drive') or text.text.__contains__('SSD') and not(text.text.__contains__('No Additional'))):
                                elDrive = (text.text)

                            if text.text.__contains__("Intel Core") or text.text.__contains__("Intel Xeon"):
                                elCpu = (text.text)

                            if ((text.text.__contains__("DDR") or text.text.__contains__("DIMM")) and not(text.text.__contains__("Intel Xeon"))):
                                elRam += (text.text)

        print(el_text, expDate_text, elCpu, elDrive, elRam)
        return(el_text, expDate_text, elCpu, elDrive, elRam)

         
def dellEverythingII(serial):
        driver.get("https://www.dell.com/support/home/en-us")
        time.sleep(.1)
        serial_input = driver.find_element(By.ID, 'mh-search-input')
        serial_input.click()
        time.sleep(.1)
        serial_input.send_keys(serial)
        time.sleep(.1)
        serial_input.send_keys(Keys.RETURN)
        time.sleep(.1)
        wait = WebDriverWait(driver, 10)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="site-wrapper"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/h1')))
        expDate = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ps-inlineWarranty"]/div[1]/div/p')))
        el_text = el.text
        expDate_text = expDate.text
        time.sleep(.5)
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div[16]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a').click()
        time.sleep(.5)
        wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="expandAllLink"]')))
        time.sleep(.1)
        driver.find_element(By.XPATH,'//*[@id="expandAllLink"]').click()
        table  = driver.find_element(By.XPATH, '//*[@id="systab_originalconfig"]')
        cells = table.find_elements(By.TAG_NAME, 'div')
        elRam = ''
        elDrive = ''
        elCpu = ''
        descriptionRam = ''
        descriptionCPU = ''
        descriptionDrive = ''
        for cell in cells:
            if cell.get_attribute('class') == 'card mb-4':
                rows = cell.find_elements(By.TAG_NAME, 'div')
                for row in rows:
                    if row.get_attribute('class') == 'd-flex align-items-start bg-mist py-3 px-6':
                        texts = row.find_elements(By.TAG_NAME, 'span')
                        for text in texts:
                            if text.text.__contains__("State Drive") or (text.text.__contains__('Hard Drive') or text.text.__contains__('SSD') and not(text.text.__contains__('No Additional'))):
                                elDrive = (text.text)
                                descriptionDrive = detialSystemConfig(rows)

                            if text.text.__contains__("Intel Core") or text.text.__contains__("Intel Xeon"):
                                elCpu = (text.text)
                                descriptionCPU = detialSystemConfig(rows)

                            if ((text.text.__contains__("DDR") or text.text.__contains__("DIMM")) and not(text.text.__contains__("Intel Xeon"))):
                                elRam += (text.text)
                                descriptionRam = detialSystemConfig(rows)
        print(el_text, expDate_text, elRam, descriptionRam, elCpu, descriptionCPU, descriptionDrive ,elDrive)
        return(el_text, expDate_text, elRam, descriptionRam, elCpu, descriptionCPU, descriptionDrive ,elDrive)
    
def lenovoEverything(serial):
        wait = WebDriverWait(driver, 10)
        driver.get("https://pcsupport.lenovo.com/us/en/")
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').click()
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').send_keys(serial)
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').send_keys(Keys.RETURN)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-psp-home"]/div/div[2]/div[2]/section/div/div/div[2]/h2')))
        el_text = el.text
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="app-psp-home"]/div/div[2]/div[2]/section/div/div/div[4]/div[3]/div[2]/div/span').click()
        div = driver.find_element(By.XPATH, '//*[@id="app-psp-home"]/div/div[2]/div[2]/section/div/div/div[4]/div[3]/div[2]/div/div/div[2]/div')
        rows = div.find_elements(By.TAG_NAME, 'div')
        count = 0
        for e in rows:
            count += 1
            if(e.text.__contains__ ('Processor')):
                vCounter = 0
                value = ''
                while (rows[count + vCounter].get_attribute('class') == "desc-config-detail"):
                    value = rows[count + vCounter].text + " " + value
                    vCounter += 1
                cpu = (value)

            if(e.text.__contains__ ('Memory')):
                vCounter = 0
                value = ''
                while (rows[count + vCounter].get_attribute('class') == "desc-config-detail"):
                    value = rows[count + vCounter].text + " " + value
                    vCounter += 1
                    ram = (value)

            if(e.text.__contains__ ('Hard Drive')):
                vCounter = 0
                value = ''
                while (rows[count + vCounter].get_attribute('class') == "desc-config-detail"):
                    value = rows[count + vCounter].text + " " + value
                    vCounter += 1
                ssd = (value)

        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="app-psp-home"]/div/div[2]/div[2]/section/div/div/div[4]/div[3]/div[2]/div/span').click()
        time.sleep(.5)
        driver.find_element(By.XPATH, '//*[@id="app-psp-home"]/div/div[2]/div[2]/section/div/div/div[5]/div[2]/button').click()
        el2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-psp-warranty"]/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[5]/span[2]')))
        time.sleep(.1)
        el2_text = el2.text
        print(el_text, el2_text, cpu, ram, ssd)
        return(el_text, el2_text, cpu, ram, ssd)

def hpEverything(serial):
        
        wait = WebDriverWait(driver, 20)
        driver.get("https://support.hp.com/us-en")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="searchQueryField"]')))
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').click()
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').send_keys(serial)
        time.sleep(.2)
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').send_keys(Keys.RETURN)
        wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/app-root/div/app-layout/app-pdp/div/div[1]/app-pdp-product-card/div/div[2]/div[2]/h1')))
        time.sleep(.1)
        el = driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout/app-pdp/div/div[1]/app-pdp-product-card/div/div[2]/div[2]/h1').text
        time.sleep(.1)
        driver.find_element(By.XPATH, '//*[@id="Product_specifications"]/div').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/app-layout/app-pdp/div/div[4]/app-product-spec/div/div[2]/a/span[2]')))
        time.sleep(.1)
        viewMore = driver.find_element(By.XPATH, '/html/body/app-root/div/app-layout/app-pdp/div/div[4]/app-product-spec/div/div[2]/a/span[2]')
        driver.execute_script("arguments[0].scrollIntoView();", viewMore)
        time.sleep(.3)
        viewMore.click()
        time.sleep(.1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="productSpecContainer"]/div[1]/div')))
        time.sleep(.1)
        div = driver.find_element(By.XPATH, '//*[@id="productSpecContainer"]/div[1]/div')
        rows = div.find_elements(By.TAG_NAME, 'div')
        count = 0
        for row in rows:
             count += 1
             if(row.text.__eq__("Processor")):
                  cpu = (rows[count].text)
             if(row.text.__eq__("Internal drive")):
                  ssd = (rows[count].text)
             if(row.text.__eq__("Memory")):
                  ram = (rows[count].text)

        
        driver.find_element(By.XPATH, '//*[@id="fulldetails"]/div/div').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/app-layout/app-check-warranty/div/div/div[2]/app-warranty-details/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/div[5]/div[2]')))
        time.sleep(.1)
        el2 = driver.find_element(By.XPATH, '/html/body/app-root/div/app-layout/app-check-warranty/div/div/div[2]/app-warranty-details/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/div[5]/div[2]').text
        time.sleep(.1)
        print(el, el2)

        return(el, el2, cpu, ssd, ram)

    # for specs
    #/html/body/app-root/div/app-layout/app-pdp/div/div[3]/app-pdplanding/div/div/div/app-vn-support-category-options/div/div/a[5]/div
   

#hpFunctionSerialAndWarranty('5CG1354MBZ')
#hpFunctionSerialAndWarranty('2UA64822LX')
#lenovoFunctionSerialAndWarranty('MJ0ATA8Y')
#lenovoFunctionSerialAndWarranty('MP1D9J8S)
#dellEverything('8BYQQ53')
#lenovoEverything('PF25FTVM')
#lenovoEverything('MJ0ATA8Y')
#hpEverything("5CG1354MBZ")
