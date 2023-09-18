import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("user-data-dir=C:\\Users\\lukek\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(driver_path, options= options)

def dellFunctionSerialAndWarranty(serial):
    try:
        driver.get("https://www.dell.com/support/home/en-us")
        driver.find_element(By.ID, 'mh-search-input').click()
        driver.find_element(By.ID, 'mh-search-input').send_keys(serial)
        time.sleep(.2)
        driver.find_element(By.ID, 'mh-search-input').send_keys(Keys.RETURN)
        time.sleep(1.5)
        el = driver.find_element(By.XPATH, '//*[@id="site-wrapper"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/h1').text
        time.sleep(.2)
        expDate = driver.find_element(By.XPATH, '//*[@id="ps-inlineWarranty"]/div[1]/div/p').text
        return(el, expDate)
    
    except:
        driver.get("https://www.dell.com/support/home/en-us")
        driver.find_element(By.ID, 'mh-search-input').click()
        driver.find_element(By.ID, 'mh-search-input').send_keys(serial)
        time.sleep(.2)
        driver.find_element(By.ID, 'mh-search-input').send_keys(Keys.RETURN)
        time.sleep(1.5)
        el = driver.find_element(By.XPATH, '//*[@id="site-wrapper"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/h1').text
        print(el)
        time.sleep(.2)
        expDate = driver.find_element(By.XPATH, '//*[@id="ps-inlineWarranty"]/div[1]/div/p').text
        return(el, expDate)
    
def hpFunctionSerialAndWarranty(serial):
    try:
        driver.get("https://support.hp.com/us-en")
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').click()
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').send_keys(serial)
        time.sleep(.2)
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').send_keys(Keys.RETURN)
        time.sleep(1.5)
        el = driver.find_element(By.XPATH, '//*[@id="pdp"]/div[1]/app-pdp-product-card/div/div[2]/div[2]/h1').text
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="fulldetails"]/div/div').click()
        time.sleep(5)
        el2 = driver.find_element(By.XPATH, '/html/body/app-root/div/app-layout/app-check-warranty/div/div/div[2]/app-warranty-details/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/div[5]/div[2]').text
        print(el2)
        return(el, el2)
    except:

        driver.get("https://support.hp.com/us-en")
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').click()
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').send_keys(serial)
        time.sleep(.2)
        driver.find_element(By.XPATH, '//*[@id="searchQueryField"]').send_keys(Keys.RETURN)
        time.sleep(1.5)
        el = driver.find_element(By.XPATH, '//*[@id="pdp"]/div[1]/app-pdp-product-card/div/div[2]/div[2]/h1').text
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="fulldetails"]/div/div').click()
        time.sleep(5)
        el2 = driver.find_element(By.XPATH, '/html/body/app-root/div/app-layout/app-check-warranty/div/div/div[2]/app-warranty-details/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/div[5]/div[2]').text
        return(el, el2)

def lenovoFunctionSerialAndWarranty(serial):
    try:
        driver.get("https://pcsupport.lenovo.com/us/en/")
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').click()
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').send_keys(serial)
        time.sleep(.5)
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').send_keys(Keys.RETURN)
        time.sleep(1)
        el = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[2]/div[1]/h4').text
        driver.find_element(By.XPATH, '//*[@id="serviceidMp"]/div/div[1]/div[1]/h2/span[3]').click()
        time.sleep(5)
        el2 = driver.find_element(By.XPATH, '//*[@id="app-psp-warranty"]/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[5]/span[2]').text
        return(el, el2)
    except:
        driver.get("https://pcsupport.lenovo.com/us/en/")
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').click()
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').send_keys(serial)
        time.sleep(.5)
        driver.find_element(By.XPATH, '//*[@id="home-search"]/div/span[1]/input').send_keys(Keys.RETURN)
        time.sleep(1)
        el = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[2]/div[1]/h4').text
        driver.find_element(By.XPATH, '//*[@id="serviceidMp"]/div/div[1]/div[1]/h2/span[3]').click()
        time.sleep(1)
        el2 = driver.find_element(By.XPATH, '//*[@id="app-psp-warranty"]/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[5]/span[2]').text
        return(el, el2)


def pullSnSupportPageMasterAndWarranty(path_to_file):
    data = pd.read_excel(path_to_file)
    df = pd.DataFrame(data)
    serial = []
    modelList = []
    warrantyDateList = []
    if 'Support Page model' not in df:
        df['Support Page model'] = ''
        df.to_excel(path_to_file, index = False)
    print('got here')

    if 'LK Warranty' not in df:
        df['LK Warranty'] = ''
        df.to_excel(path_to_file, index = False)
    print('still going')
    
    data = pd.read_excel(path_to_file)
    df = pd.DataFrame(data)

    null_SPM_df = df[df['Support Page model'].isnull()]
    LenOfData = len(null_SPM_df.index)

    for j in range(LenOfData):
        index = null_SPM_df.index[j]
        if((null_SPM_df.loc[index, 'Category'] == 'LAPTOP') and (null_SPM_df.loc[index, 'Manufacturer'] == 'DELL')):
            try:
                supp, warrant = (dellFunctionSerialAndWarranty(null_SPM_df.loc[index, 'Serial']))
            except Exception as e:
                print(e)
                supp = ("i dropped my spaghetti")
                warrant = ("i dropped my spaghetti")
        elif(null_SPM_df.loc[index, 'Category'] == 'MONITOR_LCD') and (null_SPM_df.loc[index, 'Manufacturer'] == 'DELL'):
            try:
                supp, warrant = (dellFunctionSerialAndWarranty(null_SPM_df.loc[index, 'SupplementalSerials']))
            except:
                supp = ("i dropped my spaghetti")
                warrant = ("i dropped my spaghetti")
        elif(null_SPM_df.loc[index, 'Manufacturer'] == 'HPE') and ((null_SPM_df.loc[index, 'Category'] == 'LAPTOP') or (null_SPM_df.loc[index, 'Category'] == 'DESKTOP')):
                try:
                    supp, warrant =((hpFunctionSerialAndWarranty(null_SPM_df.loc[index, 'Serial'])))
                except Exception as e:
                    print(e)
                    supp = ("i dropped my spaghetti")
                    warrant = ("i dropped my spaghetti")

        elif(null_SPM_df.loc[index, 'Manufacturer'] == 'LENOVO') and ((null_SPM_df.loc[index, 'Category'] == 'LAPTOP') or (null_SPM_df.loc[index, 'Category'] == 'DESKTOP')):
            try:
                supp, warrant = (lenovoFunctionSerialAndWarranty(null_SPM_df.loc[index, 'Serial']))
            except Exception as e:
                supp = ("i dropped my spaghetti")
                warrant = ("i dropped my spaghetti")
                    
        elif null_SPM_df.loc[index, 'Category'] == 'DESKTOP' and (null_SPM_df.loc[index, 'Manufacturer'] == 'DELL'):
            try:
                supp, warrant =(dellFunctionSerialAndWarranty(null_SPM_df.loc[index, 'Serial']))
            except:
                supp =("i dropped my spaghetti")
                warrant =("i dropped my spaghetti")
        else:
            
            supp = ('')
            warrant = ('')

        serial.append(null_SPM_df.loc[index, 'Serial'])
        modelList.append(supp)
        warrantyDateList.append(warrant)
           
        data = {"Serial" : serial,
            "model" : modelList,
            "Warrant Date" : warrantyDateList}
        
        df = pd.DataFrame(data)
        df.to_excel(path_to_file, index = False)

    return df['Support Page model'].values, df['Model #'].values
