import RPi.GPIO as gpio # Import do Raspberry
import os
import json
import cv2
import time
from random import randint
from datetime import datetime
from dateutil.relativedelta import relativedelta
import subprocess
import threading

ATTEMPTS = 20

### Funções ###

def feedback_msg(custom_string):
    print(custom_string)
    write_log(custom_string) # Salva o feedback em um log? 

def error_feedback_msg(custom_string):
    print(custom_string)
    write_log(custom_string)
    errors_log(custom_string)

def errors_log(custom_string):
    if not os.path.isfile('errors_log'):
        f = open('errors_log', 'a')
        f.write(f'{str(datetime.now())[:-7]} - Log criado\n')
        f.close()

def error_feedback(): # Função chamada em caso de erro nos testes
    if os.path.isfile('TESTE_EM_ANDAMENTO.txt'):
        os.remove('TESTE_EM_ANDAMENTO.txt')
    error_feedback_msg('Testes falhos! Iniciando protocolo de aviso!')
    gpio.output(green_led_pin, gpio.LOW)
    gpio.output(buzzer_pin, gpio.HIGH) # Som ativa por três segundos
    time.sleep(3)
    gpio.output(buzzer_pin, gpio.LOW) # Som desativa
    #error_flag()
    os.system('sudo service sistg_main restart') # Sistema reinicia

    for _ in range(5) :
        gpio.output(red_led_pin, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(red_led_pin, gpio.LOW)
        time.sleep(0.5)

    os._exit(1)

def positive_feedback(): # Chamada ao fim do teste
    feedback_msg('Teste concluído com sucesso! O programa de testes será '\
                    'finalizado e apagado.')
    gpio.output(buzzer_pin, gpio.HIGH)
    time.sleep(2)
    gpio.output(buzzer_pin, gpio.LOW)
    gpio.output(red_led_pin, gpio.LOW)
    gpio.output(green_led_pin, gpio.HIGH)

def write_log(custom_string):
    if not os.path.isfile('tests_log'):
        f = open('tests_log', 'a')
        f.write(f'{str(datetime.now())[:-7]} - Log criado\n')
        f.close()

def read_config():
    """ Read config for variables in source code """
    with open('/usr/share/sistg/config.json', 'r') as f:
        data = json.loads(f.read())
    return data

def get_rasp_model(): # created
    cmd = "cat /proc/cpuinfo | grep 'Model'"
    return os.popen(cmd).read().split('Raspberry Pi')[1].strip()

def open_close_door(n1, n2, n3):
    print('Acionando o rele para abrir a fechadura... ')
    gpio.output(relay_pin, gpio.HIGH) # High abre a fechadura
    time.sleep(5)
    if not door_is_open():
        error_feedback_msg('PROBLEMA: Porta não foi reconhecida aberta!')
        error_feedback()
    else:
        print('Porta aberta: OK') # Porta foi aberta
    print('Acionando o rele para fechar a fechadura... ')
    gpio.output(relay_pin, gpio.LOW) # Low fecha a fechadura
    time.sleep(5)
    if door_is_open(): # Testa se a porta foi fechada
        error_feedback_msg('PROBLEMA: Porta não foi reconhecida fechada!')
        error_feedback()
    else:
        print('Porta fechada: OK')

def door_is_open() -> bool:
    data = read_config()
    pull_up = data['pull_up']

    if pull_up:
        return gpio.input(door_pin) == gpio.HIGH # HIGH abre a porta
    else:
        return gpio.input(door_pin) == gpio.LOW # LOW fecha a porta

### Teste ###

print('~' * 12)
print('Iniciando teste...')
print('~' * 12)

data = read_config() # Chama a função com o arquivo de configs?
machine = data['machine']
always_capture = data['always_capture']
usb_ports = [port for port in data['cameras'].values()]
processing = data['processing']
beta = data['beta']
delay_cameras = data.get('delay_cameras', False)
camera = data.get('camera','1')
mode_ia = data.get('mode_ia','BEERns')
rfid = data.get('card',False)
rasp_model = get_rasp_model()
door_pin = data['door_pin']
red_led_pin = data['red_led_pin']
green_led_pin = data['green_led_pin']
blue_led_pin = data.get('blue_led_pin', 13)
relay_pin = data['relay_pin']
buzzer_pin = data['buzzer_pin']
pull_up = data['pull_up']

n_cameras = int(data.get('cameras_quantity', 4))

default_urls = {} # Conexão das câmeras?
for n in range(1, n_cameras + 1):
    default_urls[f'camera{n}'] = f'rtsp://admin:Cerveja1@192.168.200.20{n}/554'
urls = data.get('cam_urls', default_urls)

gpio.setmode(gpio.BCM)           # Configurações das saídas dos pinos do Raspberry? 
gpio.setup(relay_pin, gpio.OUT)
gpio.setup(red_led_pin, gpio.OUT)
gpio.setup(green_led_pin, gpio.OUT)
gpio.setup(buzzer_pin, gpio.OUT)
gpio.setup(door_pin, gpio.IN, pull_up_down=gpio.PUD_UP)

gpio.output(relay_pin, gpio.LOW)
time.sleep(0.2)
gpio.output(red_led_pin, gpio.LOW)
gpio.output(green_led_pin, gpio.LOW)

os.system('sudo service sistg_main stop') # Pausa o sistg_main

start_time = datetime.now() # Marca o início dos testes
cam_urls = urls
caps = {}

for i in range(ATTEMPTS): 
    print('-----------------------------------------------')
    feedback_msg(f'Captura de teste número {i+1}\n')
    gpio.output(buzzer_pin, gpio.HIGH) # Ativa o som
    time.sleep(1)
    gpio.output(buzzer_pin, gpio.LOW) # Desliga o som
    time.sleep(1)
    gpio.output(green_led_pin, gpio.LOW) # Desliga o led verde
    time.sleep(1)
    gpio.output(green_led_pin, gpio.HIGH) # Liga o led verde
    time.sleep(1)
    gpio.output(green_led_pin, gpio.LOW)
    time.sleep(2)
    open_close_door(randint(1, 2), randint(1, 2), randint(1, 2)) # Teste da porta
    time.sleep(2)
    gpio.output(red_led_pin, gpio.LOW) # Desliga o led vermelho
    time.sleep(1)
    gpio.output(red_led_pin, gpio.HIGH) # Liga o led vermelho
    time.sleep(1)
    gpio.output(red_led_pin, gpio.LOW)
    print('A nova repetição será realizada em 5 segundos.')
    time.sleep(5)

final_time = datetime.now()
duration_time = relativedelta(final_time, start_time)

feedback_msg('Teste finalizado!')
feedback_msg(f'Duração do teste: {duration_time.hours}h {duration_time.minutes}m {duration_time.seconds}s')