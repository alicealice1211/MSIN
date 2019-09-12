# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:32:45 2019

@author: alice
"""
import os
import time
import csv
import shutil
import random 
import urllib
import getpass
import unittest
import pandas as pd
#from datetime import datetime
from selenium import webdriver
from time import gmtime, strftime
from collections import OrderedDict
from urllib.request import urlretrieve
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

def setUp():
    global driver
    try:
        driver.quit()
    except:
        pass
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get("https://msin.wested.org/accounts/login")  

def pupUp():
    try:
        time.sleep(1)
        driver.find_element_by_xpath('//button[@ng-click="removeOtherSessions()"]').click()
        print('closed pop up')
        time.sleep(1)
    except:
        print('no pop up')
def logIn():   
    userName = 'brandon'
    password = 'J@newild3'
   
    userEntry = driver.find_element_by_xpath('//input[@ng-model="user_details.user_id"]')
    userEntry.send_keys(str(userName))
    time.sleep(1)
    
    passwordEntry = driver.find_element_by_xpath('//input[@type="password"]')
    passwordEntry. send_keys(str(password))    
    time.sleep(1)
    
    #click Login button
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(5)


#-------------------------------------    

def start():
    setUp()
    logIn()
    pupUp()
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
def childrenPage():
    print('go to children page')
    url = 'https://msin.wested.org/children/search'
    driver.get(url)
    time.sleep(3)
  
def MSD(msdNum):
    print('enter MSD#')
    #open option
    driver.find_element_by_xpath('//div[@ng-click="toggleAdvancedOptions()"]').click()
    time.sleep(1)
    #msd entry
    msdEntry = driver.find_element_by_xpath('//input[@id="studentMsdNumber"]')
    msdEntry.send_keys(msdNum)
    time.sleep(1)
    #click search button
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(1)

def loadingBar():
    while True:
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//div[@value="progress"]')
            print('loading bar')
        except:
            time.sleep(1)
            print('loaded')
            break
    
def eyeIcon():
    #click eye icon
    print('click eye')
    driver.find_element_by_xpath('//i[@class="fa fa-eye fa-lg fa-fw"]').click()
    time.sleep(8)
    
def serviceParticipation():
    print('service participation tap')
    navs = driver.find_elements_by_xpath('//a[@class="nav-link"]')
    for nav in navs:
        if nav.text == 'Service Participation':
            nav.click()
            time.sleep(1)
            break
    
def editButton():
    print('click edit button')
    driver.find_element_by_xpath('//button[@ng-click="editStudentTab()"]').click()
    time.sleep(1)

def enterNewButton():
    print('click enter new service')
    buttons = driver.find_elements_by_xpath('//button[@ng-disabled="ngDisabled"]')
    for button in buttons:
        if button.text == 'Enter New Service':
            button.click()
            time.sleep(3)
            break
        
def schoolYear(schoolYearValue): 
    schoolYearValue = schoolYearValue[:2]+'-'+schoolYearValue[2:]
    print('selecting school year...'+str(schoolYearValue))
    #open drop down
    driver.find_element_by_xpath('//select[@name="SchoolYear"]').click()
    options = driver.find_elements_by_xpath('//select[@name="SchoolYear"]//option') 
    for option in options:
        if schoolYearValue in option.text:
            print(option.text)
            option.click()
            time.sleep(1)
            break
    #clsoe drop down
    driver.find_element_by_xpath('//select[@name="SchoolYear"]').click()
    
def servicePeriod(option):
    print('enter service period')
    entry = driver.find_element_by_xpath('//select[@name="enrollmentPeriod"]')
    entry.click()
    time.sleep(1)
    entry.send_keys(str(option))
    time.sleep(1)
    entry.click()
    time.sleep(1)
    
def schoolEnrollment(option):
    print('enter school enrollment')
    entry = driver.find_element_by_xpath('//select[@name="SCHOOL_ENROLLMENT"]')
    entry.click()
    time.sleep(1)
    entry.send_keys(str(option))
    time.sleep(1)
    entry.click()
    time.sleep(1)
#-------------------------------
def enterYear(yearOption):
    buttons = driver.find_elements_by_xpath('//button[@type="button"]')
    for b in buttons :
        try:
            if b.text.strip() == yearOption:
                print(str(b.text.strip())+' found')
                b.click()
                time.sleep(1)
        except:
            pass

def enterMonth(monthOption):
    buttons = driver.find_elements_by_xpath('//button[@type="button"]')
    for b in buttons :
        try:
            if b.text.strip() == str(monthOption):
                print(str(b.text.strip())+' found')
                b.click()
                time.sleep(1)
        except:
            pass

def enterDate(dateOption):
    buttons = driver.find_elements_by_xpath('//button[@type="button"]')
    for b in buttons :
        try:
            if b.text.strip() == str(dateOption):
                print(str(b.text.strip())+' found')
                b.click()
                time.sleep(1)
        except:
            pass
           
#------------
def startDate(yearOption, monthOption, dateOption):
     driver.find_element_by_xpath('//button[@ng-click="startDateOpen = !startDateOpen"]').click()
     enterYear(yearOption)
     enterMonth(monthOption)
     enterDate(dateOption)

def endDate(yearOption, monthOption, dateOption):
     driver.find_element_by_xpath('//button[@ng-click="endtDateOpen = !endtDateOpen"]').click()
     enterYear(yearOption)
     enterMonth(monthOption)
     enterDate(dateOption)    
#------------     
     
def serviceNameDropDownOpen():
    buttons = driver.find_elements_by_xpath('//button[@type="button"]')
    for b in buttons :
        if b.text.strip() == 'Select Services':
            b.click()
            print('click select services')
            time.sleep(3)
            break

def serviceNameDropDownClose():
    buttons = driver.find_elements_by_xpath('//button[@type="button"]')
    for b in buttons[:5] :
        print(b.text)
        if 'Services:' in b.text.strip():
            print(b.text)
            b.click()
            time.sleep(3)
            break
        
def serviceName(serviceOption):
#    sNumber = str(serviceOption.split(' - ')[0])
    sName = str(serviceOption.split(' - ')[1])
    
    serviceNameDropDownOpen()
    
    entry = driver.find_element_by_xpath('//input[@id="serviceFilter"]')
    entry.send_keys(str(sName))
     
    serviceNames = driver.find_elements_by_xpath('//li[@class="cursor-pointer"]')
    for item in serviceNames:
        if sName.lower() in item.text.lower():
            print(item.text)
            item.click()
            time.sleep(2)
            break
    serviceNameDropDownClose()
     
     
def enterHour(hourValue):   
    #open drop down
    driver.find_element_by_xpath('//select[@id="SERVICE_HOURS0"]').click()
    options = driver.find_elements_by_xpath('//select[@id="SERVICE_HOURS0"]//option') 
    for option in options:
        if hourValue in option.text:
            print(option.text)
            option.click()
            time.sleep(1)
            break
    #clsoe drop down
    driver.find_element_by_xpath('//select[@id="SERVICE_HOURS0"]').click()

def createButtonClick():#TESTING
    create = driver.find_element_by_xpath('//button[@ng-click="confirmServicePage(form.$valid)"]')
    print('click create button')
    create.click()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@class="confirm"]').click()
    print('data finished')
    time.sleep(2)
    
#-------------------------------------
def readDate(x):
    global year
    global month
    global day
    year = x.split('-')[0][2:4]
    month = int(x.split('-')[1].replace('0',''))
    day = x.split('-')[2]
    
    
    monthinteger = month
    month = datetime.date(1900, monthinteger, 1).strftime('%B')
    print('cover date:'+str(month))
    

def enterInformation(msdNum,schoolYearValue,periodValue, startDateValue, endDateValue, serviceOption ):
#    msdNum = '06002891699' 
#    schoolYearValue = '1819'
#    periodValue = 'summer'#service period
    enrollOption = '[r'
#    serviceOption = '901 - Nutrition'
##    hourValue = '10 - 14'
#    dateValue = '2019-06-10'
#    
    
    
 
    childrenPage()
    MSD(msdNum)
    loadingBar()
    eyeIcon()
    serviceParticipation()
    editButton()
    enterNewButton()
    
    schoolYear(schoolYearValue)
    servicePeriod(periodValue)

    readDate(startDateValue)
    startDate(year, month, day)
    readDate(endDateValue)
    endDate(year,month,day)

    serviceName(serviceOption)
    schoolEnrollment(enrollOption)
#CURRENTLY DON"T HAVE TO ACTIVE ENTERHOUR
#    enterHour(hourValue)
    
    createButtonClick()
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

def main():
    for row in rows:
    
        msdNum = row[0]
        schoolYearValue = row[0]
        startDateValue = row[0]
        endDateValue = row[0]
        serviceOption = row[0]

      
        start()
        enterInformation(msdNum,schoolYearValue,periodValue, startDateValue, endDateValue, serviceOption )
   
            

    

#msdNum = '06002893876' 
#schoolYearValue = '1819'
#periodValue = 'Summer'#service period
#serviceOption = '11 - MONITORING AND FOLLOW-UP'
#startDateValue = '2019-06-10'
#endDateValue = '2019-06-13'
##
#start()
#enterInformation(msdNum,schoolYearValue,periodValue, startDateValue, endDateValue, serviceOption )
##
##
##
#












