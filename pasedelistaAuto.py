from selenium import webdriver
from time import sleep
from datetime import datetime
import os

with open('C:\\Users\\salim\\Desktop\\password.txt', 'r') as f:
    passwor = f.read()
with open('C:\\Users\\salim\\Desktop\\mail.txt','r') as g:
    mail = g.read()

hora = ''
minuto = ''
diaSemana = ''

def condicionales(hora, minuto, diaSemana, horaEjecucion, minutoEjecucion):

    minutoEjecucion = int(minutoEjecucion) + 10
    minuto = int(minuto)

    if hora == horaEjecucion and minuto < minutoEjecucion and diaSemana != "Sunday" and diaSemana != 'Saturday':
        comenzarPase()
            

def comenzarPase():
    
    conditional = False

    driver = webdriver.PhantomJS('D:\\New folder\\New folder\\phanton\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    # entrar a la pagina de la escuela
    driver.get("https://elearning.veracruz.tecnm.mx/login/index.php") 

    # buscamos el elemento para el correo 
    element = driver.find_element_by_id("username") 
    #enviamos los datos del correo
    element.send_keys(mail)
    #buscamos el elemento para la contraseña
    element = driver.find_element_by_id('password')
    #enviamos los datos de la contraseña
    element.send_keys(passwor)
    print("Mande las llaves")
    
    
    for a in driver.find_elements_by_class_name('event'):
        linkPositionOne = a.find_elements_by_xpath('.//a')
        for si in linkPositionOne:
            linkOne = si.get_attribute('href')
            break
        break
    driver.get(linkOne)
    print("Entre y busque el evento")



    linkPositionTwo = driver.find_element_by_class_name('card-link')
    linkTwo = linkPositionTwo.get_attribute('href')
    driver.get(linkTwo)
    print("Entre a las actividades")
    

    try:
        linkPositionThree = driver.find_element_by_link_text('Enviar asistencia')
        linkThree = linkPositionThree.get_attribute('href')
        driver.get(linkThree)
        print("Entre a enviar la asistencia")

        button = driver.find_elements_by_class_name('form-check-input')
        for buttons in button:
            buttons.click()
            break
        print("Envie la asistencia....")
        sendlist = driver.find_element_by_name('submitbutton')
        sendlist.click()
        os.system("cls")
        print("La asistencia se envio, favor de verificar")
        conditional = True
    
    except:
        os.system("cls")
        print('No se ha encontrado la asistencia')    


    print("Saliendo.....")
    sleep(2)
    driver.quit()

    if conditional == True:
        sleep(60*9)


def tiempo():
    global hora
    global minuto
    global diaSemana
    ahora = datetime.now()
    hora = ahora.strftime("%H")
    minuto = ahora.strftime("%M")
    diaSemana = ahora.strftime("%A")

def dias():
    contador = 0
    while True:
        tiempo()
        contador += 1
        print(hora, minuto)
        
        #Calculo
        condicionales(hora,minuto, diaSemana, '12','00')
        
        #Admin
        condicionales(hora,minuto, diaSemana, '16','00')

        #Programacion
        condicionales(hora,minuto, diaSemana, '17','00')

        sleep(60)
        
        if contador > 12:
            os.system("cls")
            print('Pase de lista')
            contador = 0

def main():
    print('Pase de lista')
    dias()


if __name__ == '__main__':
    main()
