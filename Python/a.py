import RPi.GPIO as gpio
import os
import json
import cv2
import time
from random import randint
from datetime import datetime
from dateutil.relativedelta import relativedelta
import subprocess
import threading

FREN_ATTEMPTS = 20
ATTEMPTS = 20
MSG_OPEN_DOOR = 'Porta aberta'
MSG_CLOSE_DOOR = 'Porta fechada'
MSG_OPEN_DOOR_ERROR = 'Problema ao abrir a porta!'
MSG_CLOSE_DOOR_ERROR = 'Problema ao fechar a porta!'
SIZE_LIMIT_MIN: int = 20000  # Bytes
SIZE_LIMIT_MAX: int = 500000
RASPBERRY_MODELS: dict = {
    '3 Model B Rev 1.2': '0424:9514',
    '3 Model B Plus Rev 1.3': '0424:2514',
    '4 Model B Rev 1.1': '2109:3431',
    '4 Model B Rev 1.2': '2109:3431'
}

tg = '/usr/share/sistg'


############## FUNCTIONS #################

def feedback_msg(custom_string):
    print(custom_string)
    write_log(custom_string)

def error_feedback_msg(custom_string):
    print(custom_string)
    write_log(custom_string)
    errors_log(custom_string)

def write_log(custom_string):
    if not os.path.isfile('tests_log'):
        f = open('tests_log', 'a')
        f.write(f'{str(datetime.now())[:-7]} - Log criado\n')
        f.close()

    with open('tests_log', 'a') as f:
        f.write(f'{str(datetime.now())[:-7]} ')
        f.write(f'{custom_string}\n')

def errors_log(custom_string):
    if not os.path.isfile('errors_log'):
        f = open('errors_log', 'a')
        f.write(f'{str(datetime.now())[:-7]} - Log criado\n')
        f.close()

    with open('errors_log', 'a') as f:
        f.write(f'{str(datetime.now())[:-7]} ')
        f.write(f'{custom_string}\n')

def read_config():
    """ Read config for variables in source code """
    with open('/usr/share/sistg/config.json', 'r') as f:
        data = json.loads(f.read())
    return data


def error_feedback():
    if os.path.isfile('TESTE_EM_ANDAMENTO.txt'):
        os.remove('TESTE_EM_ANDAMENTO.txt')
    error_feedback_msg('Testes falhos! Iniciando protocolo de aviso!')
    gpio.output(green_led_pin, gpio.LOW)
    gpio.output(buzzer_pin, gpio.HIGH)
    time.sleep(3)
    gpio.output(buzzer_pin, gpio.LOW)
    #error_flag()
    os.system('sudo service sistg_main restart')

    for _ in range(5) :
        gpio.output(red_led_pin, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(red_led_pin, gpio.LOW)
        time.sleep(0.5)

    os._exit(1)


def positive_feedback():
    feedback_msg('Teste concluído com sucesso! O programa de testes será '\
                    'finalizado e apagado.')
    gpio.output(buzzer_pin, gpio.HIGH)
    time.sleep(2)
    gpio.output(buzzer_pin, gpio.LOW)
    gpio.output(red_led_pin, gpio.LOW)
    gpio.output(green_led_pin, gpio.HIGH)

def get_ip_and_port(url):
        """Returns ip and port for a url.
        For example, for rtsp://admin:Cerveja1@192.168.200.201/554
        returns ('192.168.200.201', '554')
        """
        try:
            ip_and_port = url.split('Cerveja1@')[1].split('/')
            return ip_and_port[0], ip_and_port[1]
        except Exception as ex:
            feedback_msg(f'Não foi possível recuperar ip e porta da url {url}')
            return None, None

def get_cameras_off():
    """Update cameras_status, turning to False cameras OFF"""
    
    if str(camera) == '3':
        for key, _ in caps.items():
            ip, port = get_ip_and_port(cam_urls[key])
            test_camera = f'nc -vz -w 10 {ip} {port}'.split()
            if not subprocess.call(test_camera, 
                    stdout=open(os.devnull, "w"),stderr=subprocess.STDOUT) == 0:
                cameras_status[key] = False
                error_feedback_msg(f'Camera {key} off')
                error_feedback()
            else:
                cameras_status[key] = True

    else:
        cameras_with_error = []
        for usb in range(len(usb_ports)):
            cmd = f"v4l2-ctl --list-devices | grep -A 2 '\-{usb_ports[usb]}' | sed -n 3p"
            linhas = os.popen(cmd).read().strip('\n')
            if linhas == '':
                cameras_with_error.append(usb+1)    

        return cameras_with_error

def reset_usb_cameras():
    os.system(f'usbreset {RASPBERRY_MODELS[rasp_model]}')

def cameras_check(from_blur_check=False) -> None:

    if str(camera) == '3':
        global caps

        for _, cap in caps.items():
            cap.release()

        get_cameras_off()

        cameras_with_error = [k for k in cameras_status.keys() 
                                if cameras_status[k] == False]
        cameras_with_error = ', '.join([str(camera) for camera in cameras_with_error])

        if cameras_with_error:
            started_with_cameras_off = True
            feedback_msg(f'Câmeras OFF: {cameras_with_error}')
        else:
            started_with_cameras_off = False

        begin_time = datetime.now()
        while False in cameras_status.values():
            #feedback.display_error(3)
            if (datetime.now() - begin_time).total_seconds()/60 >= 5:
                feedback_msg('Mais de 5 minutos sem câmeras...')
            get_cameras_off()
            new_cameras_error = [k for k in cameras_status.keys() 
                                    if cameras_status[k] == False]
            new_cameras_error = ', '.join([str(camera) for camera in new_cameras_error])

            if new_cameras_error != cameras_with_error and new_cameras_error:
                feedback_msg(f'Câmeras OFF: {new_cameras_error}')
            cameras_with_error = new_cameras_error

        caps = {}

        feedback_msg('Inicializando câmeras...')
        for cam, url in cam_urls.items():
            caps[cam] = cv2.VideoCapture(url)
            ret, frame = caps[cam].read()
            if ret:
                print(f'{cam} conectada!')
            else:
                print(f'PROBLEMA: não foi possível iniciar a {cam}')
                error_feedback()
        
    else:
        times_reset = 0
        counter = 0
        error = False
        resets_or_reboots_done = []

        cameras_error = get_cameras_off()

        if cameras_error:
            error = True
            cameras_error = ', '.join([str(camera) for camera in cameras_error])
            error_feedback(f'Cameras off: {cameras_error}')

        t1 = time()
        while True:
            if not cameras_error:
                break
            # 60 x 5seg = 300seg | counter%60 = 0 when counter = 0, 60, 120...
            if counter%60 == 0 and times_reset < 2: 
                t1 = time()
                print('Resetando câmeras...')
                reset_usb_cameras()
                counter = 1
                times_reset += 1
                resets_or_reboots_done.append('reset')
            else:
                time.sleep(5)
                counter += 1

            new_cameras_error = get_cameras_off()
            new_cameras_error = ', '.join([str(camera) for camera in new_cameras_error])

            if new_cameras_error != cameras_error:
                n_cams_off = len(new_cameras_error.replace(',','').replace(' ', ''))
                if n_cams_off != num_cameras:
                    print(f'Cameras off: {new_cameras_error}')
                elif counter >= 2: # print all cams off only after 2x5 seconds
                                    # after reset
                    print(f'Cameras off: {new_cameras_error}')
                cameras_error = new_cameras_error

        print(f'Câmeras OK.')


def check_cameras_ports() -> dict:
    """ Return a dict with cameras ids, checking usb cameras ports """
    cameras_ids = {}

    for n, usb_port in enumerate(usb_ports, 1):
        try:
            cmd = f"v4l2-ctl --list-devices | grep -A 1 '\\-{usb_port})' | sed -n 2p | grep -o '.$'"
            cameras_ids[f'camera{n}'] = int(os.popen(cmd).read().strip('\n'))
        except:
            cameras_ids[f'camera{n}'] = None
        time.sleep(0.1)  # Stabilize ports after scan

    return cameras_ids


def capture_and_save() -> bool:
        """ Capture and save images and return error. 
        If error, return true, if not, false
        """
        tg = '/usr/share/sistg'
        
        if str(camera) == '3':
            cameras_check()
            cameras_with_error = set()

            for cam, cap in caps.items():
                for _ in range(10):  # Try 20 times
                    ret, frame = cap.read()  # return a single frame in variable 'frame'
                    if ret:  # If got an image
                        feedback_msg(f'Imagem da {cam} capturada com sucesso!')
                        break
                    else:
                        feedback_msg(f'PROBLEMA: imagem da {cam} não pode ser '\
                                        'capturada. Tentando novamente...')
                        cameras_check()
                        cameras_with_error.add(cam)
    
        else:
            cameras_ids = check_cameras_ports()
            cameras_with_error = set([cam for cam, cam_id in cameras_ids.items() if cam_id == None])

            for cam, cam_id in cameras_ids.items():
                if os.path.exists(f'/dev/video{cam_id}') and cam not in cameras_with_error:
                    for _ in range(10):  # Try 20 times
                        cap = cv2.VideoCapture(cam_id)  # video capture source camera
                        ret, frame = cap.read()  # a single frame in variable 'frame'
                        cap.release()

                        if ret:  # If got an image
                            feedback_msg(f'Imagem da {cam} capturada com sucesso!')
                            break
                    else:
                        feedback_msg(f'PROBLEMA: imagem da {cam} não pode ser '\
                                        'capturada. Tentando novamente...')
                        cameras_check()
                        cameras_with_error.add(cam)
                else:
                    cameras_with_error.add(cam)

        if cameras_with_error:
            cameras_with_error = ', '.join([str(camera) for camera in cameras_with_error])
            feedback_msg(f'\n\nImagens com erro: {cameras_with_error}\n')
            error_feedback()


def open_close_door(n1, n2, n3):
    print('Acionando o rele para abrir a fechadura... ')
    gpio.output(relay_pin, gpio.HIGH)
    time.sleep(5)
    if not door_is_open():
        error_feedback_msg('PROBLEMA: Porta não foi reconhecida aberta!')
        error_feedback()
    else:
        print('Porta aberta: OK')
    print('Acionando o rele para fechar a fechadura... ')
    gpio.output(relay_pin, gpio.LOW)
    time.sleep(5)
    if door_is_open():
        error_feedback_msg('PROBLEMA: Porta não foi reconhecida fechada!')
        error_feedback()
    else:
        print('Porta fechada: OK')

def door_is_open() -> bool:
    data = read_config()
    pull_up = data['pull_up']

    if pull_up:
        return gpio.input(door_pin) == gpio.HIGH
    else:
        return gpio.input(door_pin) == gpio.LOW

def create_flag():
    return
    # if os.path.isfile('TESTE_EM_ANDAMENTO.txt'):
    #     error_feedback_msg('Arquivo de inicialização existente - Teste anterior falhou ou foi interrompido')
    #     error_feedback()
    # else:
    #     flag = open('TESTE_EM_ANDAMENTO.txt', 'w')
    #     flag.write('Teste em andamento ou o teste foi interrompido')
    #     flag.close()

def error_flag():
    # error_flag = open('TESTES_FALHOS.txt', 'w')
    # error_flag.write('Falha nos testes - verifique o log')
    # error_flag.close()
    return


def delete_flag():
    try:
        os.remove('TESTE_EM_ANDAMENTO.txt')
    except:
        error_feedback_msg('Falha ao excluir a flag de inicialização!')
        error_feedback()

def get_rasp_model(): # created
    cmd = "cat /proc/cpuinfo | grep 'Model'"
    return os.popen(cmd).read().split('Raspberry Pi')[1].strip()

########## MAIN ##########

print('\n\n\nIniciando...')


data = read_config()
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

default_urls = {}
for n in range(1, n_cameras + 1):
    default_urls[f'camera{n}'] = f'rtsp://admin:Cerveja1@192.168.200.20{n}/554'
urls = data.get('cam_urls', default_urls)

gpio.setmode(gpio.BCM)
gpio.setup(relay_pin, gpio.OUT)
gpio.setup(red_led_pin, gpio.OUT)
gpio.setup(green_led_pin, gpio.OUT)
gpio.setup(buzzer_pin, gpio.OUT)
gpio.setup(door_pin, gpio.IN, pull_up_down=gpio.PUD_UP)

gpio.output(relay_pin, gpio.LOW)
time.sleep(0.2)
gpio.output(red_led_pin, gpio.LOW)
gpio.output(green_led_pin, gpio.LOW)

os.system('sudo service sistg_main stop') # Pausando o sistg_main
#create_flag() # Criar a flag para marcar o inicio dos testes

start_time = datetime.now()
cam_urls = urls
caps = {}

feedback_msg('-----------------------------------------------')

if camera == '3':
    feedback_msg('Inicializando câmeras multilaser...')
    for cam, url in cam_urls.items():
        caps[cam] = cv2.VideoCapture(url)
        ret, frame = caps[cam].read()
        if ret:
            feedback_msg(f'{cam} Iniciada com sucesso!')
        else:
            feedback_msg(f'{cam} Não põde ser inicializada! Verificar se ela está'\
                ' corretamente conectada e funcionando com sucesso em outro módulo.'\
                ' Caso esteja, encaminhar para equipe de formatação ou de desenvolvimento'\
                ' dos módulos para verificar configuração. Caso contrário, testar com outra câmera.')


num_cameras = 4
cameras_status = {f'camera{n}': False for n in range(1, num_cameras + 1)}

feedback_msg(f'PRIMEIRA ETAPA DE TESTES INICIADA: {ATTEMPTS} capturas de imagens de teste')

for i in range(ATTEMPTS):
    print('-----------------------------------------------')
    feedback_msg(f'Captura de teste número {i+1}\n')
    gpio.output(green_led_pin, gpio.LOW) # Desliga o led verde
    gpio.output(red_led_pin, gpio.LOW) # Desliga o led vermelho
    get_cameras_off()
    capture_and_save()
    
feedback_msg('\PRIMEIRA ETAPA DE TESTES FINALIZADA\n')    
    
feedback_msg(f'\nSEGUNDA ETAPA DE TESTES INICIADA: {ATTEMPTS} tentativas de'\
                ' abrir a fechadura serão realizadas\n')

for _ in range(ATTEMPTS):
    open_close_door(randint(1, 2), randint(1, 2), randint(1, 2)) # Teste da porta
    print('A nova repetição será realizada em 10 segundos.')
    time.sleep(10)

feedback_msg('\nSEGUNDA ETAPA DE TESTES FINALIZADA\n')

#delete_flag() # Exclui a flag de inicio dos testes

final_time = datetime.now()
duration_time = relativedelta(final_time, start_time)

feedback_msg('Testes finalizados!')
feedback_msg(f'Duração do teste: {duration_time.hours}h {duration_time.minutes}m {duration_time.seconds}s')

positive_feedback()

os.system('sudo service sistg_main restart')