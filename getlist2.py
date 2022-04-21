import json
import time
from selenium import webdriver
from time import sleep
from resolution import pw
from resolution import un
from resolution import unt2
from pushbullet import Pushbullet

API_key = 'o.qH3WYqaPcvRsCGXSWWRbflqCJGry8n1H'
PATH = "C:\Program Files (x86)\chromedriver.exe"
# username, password and target username in resolution.py
text = '2'

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/accounts/login")
sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(un)
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw)
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div').click()
sleep(10)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
driver.get(f"https://www.instagram.com/{unt2}")
sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span').click()
sleep(3)

"""é un po un casino, ma praticamente per fare in modo di avere tutti i follower, bisogna scrollare finche tutti non 
sono stati caricati. praticamente quello che faccio é scrollare in giu permanentemente per costringere instagram a 
caricare tutti i follower, e quando mi accorgo che non ne arrivano altri mi segno quelli che sono stati caricati e 
finisco il programma 

mi sono anche preso la liberta di togliere quella class inutile. se proprio ci tieni puoi mettere tutto in una 
funzione ma una classe é superflua """

# elemnto del popup
popup = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")
# Elemento che sta dentro il popup ma contiene tutti gli altri elementi che rappresentano un follower.
# Non possiamo interagire con questo elemento qui per qusto esisteste la variable popup che sta sopra
container = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div")

# nummero totale di follower nel container
total_children = 0
# quanto tempo é passato dal ultima volta che si sono aggiunti dei nuovo follower
time_since_last_children_increase = 0
# il momento in cui abbiamno fatto partire il timer
timer_start = time.time()
# Controlliamo se sono passati piu di 10 secondi dall ultima volta che si é aggiunto un follower. Se si vuol dire che
# la pagina ha finito di caricare tutti i follower e possiamo fermare il loop e passare a leggerli e metterli in una
# lista
while time_since_last_children_increase < 10:

    # qui selezioniamo lultinmo elemento nel container, quindi lultimo follower che é stato caricato e scrolliamo
    # finche non é visibile
    element = container.find_elements_by_xpath("./*")[-1]
    try:
        driver.execute_script("return arguments[0].scrollIntoView();", element)
    except:
        pass

    # adesso contiamo quanti follower sono stati caricati in tutto
    current_children = len(container.find_elements_by_xpath("./*"))

    # se i follower che sono stati caricati adesso sono piu grandi dell ultima volta
    # che abbiamo controllato (quindi il loop precedente), resettiamo il timer
    # senno segnamo il nuovo tempo e finiamo il loop
    if len(container.find_elements_by_xpath("./*")) > total_children:
        total_children = current_children
        timer_start = time.time()
        time_since_last_children_increase = 0
    else:
        time_since_last_children_increase = time.time() - timer_start

accs = []
# adesso che tutti i follower sono stati scaricati loopiamo attraverso ognuno di loro e ci segnamo lo username e il nome
for elm in container.find_elements_by_xpath("./*"):
    username = elm.find_element_by_xpath("div/div[1]/div[2]/div[1]/span/a/span").text
    name = elm.find_element_by_xpath("div/div[1]/div[2]/div[2]").text
    accs.append(username)
print(accs)
with open('list2.json', 'w') as f:
    json.dump(accs, f)

pb = Pushbullet(API_key)
pb.push_note('code executed', text)

