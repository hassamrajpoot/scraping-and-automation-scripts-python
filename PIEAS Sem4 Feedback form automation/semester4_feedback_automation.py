from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

option = Options()
option.add_argument('--headless')
driver = webdriver.Firefox(options=option)
driver.get("http://111.68.99.200/SRA%2Dn/lgn.aspx")
driver.implicitly_wait(5)
find_program = driver.find_element_by_id("ddlDegreeProg")
find_program.find_element_by_xpath("//option[@value='BSPhy']").click()
driver.find_element_by_id("chkRollNoAllow").click()
roll_no = ""
Access_code = ""
driver.find_element_by_id("txtRegNo").send_keys(roll_no)
driver.find_element_by_id("a63542B5").send_keys(Access_code)
driver.find_element_by_id("a63542B5").send_keys(Keys.RETURN)
driver.implicitly_wait(8)

driver.find_element_by_id("cmdViewTranscript").click()
driver.implicitly_wait(8)
driver.find_element_by_id("btnfeedback").click()
driver.implicitly_wait(8)

# Pakstudies
courses = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
courses.find_element_by_xpath("//option[@value='CMS-103^02-2021']").click()
driver.implicitly_wait(5)
teachers = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor")
time.sleep(2)
teachers.find_element_by_xpath("//option[@value='mirfan']").click()
driver.implicitly_wait(3)


def evaluation():
    name_of_evaluations = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"]
    for letter in name_of_evaluations:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txt{}".format(letter)).send_keys(4)
        driver.implicitly_wait(5)


evaluation()
driver.implicitly_wait(3)
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

# Principles of managment
courses = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
courses.find_element_by_xpath("//option[@value='CMS-201^02-2021']").click()
teachers = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor")
time.sleep(2)
teachers.find_element_by_xpath("//option[@value='ArshadZ']").click()
driver.implicitly_wait(3)
evaluation()
driver.implicitly_wait(3)
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

# Basic Nuclear engineering
courses = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
courses.find_element_by_xpath("//option[@value='NE-404 ^02-2021']").click()
teachers = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor")
time.sleep(2)
teachers.find_element_by_xpath("//option[@value='matloob89']").click()
driver.implicitly_wait(3)
evaluation()
driver.implicitly_wait(3)
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

# Ordinary Differential equations
courses = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
courses.find_element_by_xpath("//option[@value='PAM-256^02-2021']").click()
teachers = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor")
time.sleep(2)
teachers.find_element_by_xpath("//option[@value='pieas@19']").click()
driver.implicitly_wait(3)
evaluation()
driver.implicitly_wait(3)
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

# Probability and statistics
courses = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
courses.find_element_by_xpath("//option[@value='PAM-267^02-2021']").click()
teachers = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor")
time.sleep(2)
teachers.find_element_by_xpath("//option[@value='naadi001']").click()
driver.implicitly_wait(3)
evaluation()
driver.implicitly_wait(3)
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

# Optics
courses = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
courses.find_element_by_xpath("//option[@value='PAM-270^02-2021']").click()
teachers = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor")
time.sleep(2)
teachers.find_element_by_xpath("//option[@value='afshiihsan']").click()
driver.implicitly_wait(3)
evaluation()
driver.implicitly_wait(3)
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

# Optics Lab
courses = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
courses.find_element_by_xpath("//option[@value='PAM-271^02-2021']").click()
teachers = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor")
time.sleep(2)
teachers.find_element_by_xpath("//option[@value='afshiihsan']").click()
driver.implicitly_wait(3)
evaluation()
driver.implicitly_wait(3)
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

# -----------Linear Algebra course was in semester 3 ------------------------------!
# Linear algebra
# courses = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
# courses.find_element_by_xpath("//option[@value='PAM-242^09-2020']").click()
# teachers = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor")
# time.sleep(2)
# teachers.find_element_by_xpath("//option[@value='pieas@19']").click()
# driver.implicitly_wait(3)
# evaluation()
# driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
# driver.implicitly_wait(3)
# time.sleep(8)


driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdCourseEvaluation2").click()
driver.implicitly_wait(8)
time.sleep(5)

#Pakstudies
course = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
course.find_element_by_xpath("//option[@value='CMS-103^02-2021']").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").send_keys("Sir Najam us Saqib")


def detailed_evaluation():
    lista = [1, 2, 3]
    for num in lista:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtA{}".format(num)).send_keys(4)
        driver.implicitly_wait(3)
    listb = [1, 2, 3]
    for number in listb:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtB{}".format(number)).send_keys(4)
        driver.implicitly_wait(3)
    listc = [1, 2, 3, 4]
    for n in listc:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtC{}".format(n)).send_keys(4)
        driver.implicitly_wait(3)
    listd = [1, 2, 3, 4]
    for num1 in listd:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtD{}".format(num1)).send_keys(4)
        driver.implicitly_wait(3)
    liste = [1, 2, 3]
    for num2 in liste:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtE{}".format(num2)).send_keys(4)
        driver.implicitly_wait(3)
    listf = [1, 2, 3]
    for num3 in listf:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtF{}".format(num3)).send_keys(4)
        driver.implicitly_wait(3)
    listg = [1, 2, 3, 4]
    for num4 in listg:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtG{}".format(num4)).send_keys(4)
        driver.implicitly_wait(3)
    listh = [1, 2, 3]
    for num5 in listh:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtH{}".format(num5)).send_keys(4)
        driver.implicitly_wait(3)
    listi = [1, 2]
    for nums in listi:
        driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtI{}".format(nums)).send_keys(4)
        driver.implicitly_wait(3)


detailed_evaluation()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

#Principles of management
course = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
course.find_element_by_xpath("//option[@value='CMS-201^02-2021']").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").clear()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").send_keys("DR Arshad zaheer")
detailed_evaluation()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

#Baisc nuclear engineering
course = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
course.find_element_by_xpath("//option[@value='NE-404 ^02-2021']").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").clear()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").send_keys("Sir Matloob hussain")
detailed_evaluation()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

#Differential equations
course = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
course.find_element_by_xpath("//option[@value='PAM-256^02-2021']").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").clear()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").send_keys("DR Zaheer , Mam Amna")
detailed_evaluation()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

#Probability and statistics
course = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
course.find_element_by_xpath("//option[@value='PAM-267^02-2021']").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").clear()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").send_keys("DR Nadeem shoukat , DR Muhammad Ali")
detailed_evaluation()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

#Optics
course = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
course.find_element_by_xpath("//option[@value='PAM-270^02-2021']").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").clear()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").send_keys("DR Afshan irshad ")
detailed_evaluation()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

#Optics Lab
course = driver.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")
course.find_element_by_xpath("//option[@value='PAM-271^02-2021']").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").clear()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").send_keys("DR Afshan irshad")
detailed_evaluation()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
driver.implicitly_wait(8)
time.sleep(8)

# -----------Linear Algebra course was in semester 3 ------------------------------!
# Linear Algebra
#course.find_element_by_xpath("//option[@value='PAM-242^09-2020']").click()
#driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").clear()
#driver.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").send_keys("Sir Zaheer Asghar")
#detailed_evaluation()
#driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit").click()
#driver.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").click()
#driver.implicitly_wait(8)
#driver.find_element_by_id("_ctl0_lnkBtnLogout").click()
driver.quit()
print(">Success!")
