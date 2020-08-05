import Adafruit_BBIO.PWM as PWM

class Motor():
    def __init__(self):
        setup()
    
    def setup():
        motor1 = "P8_19"
        #Motor conectado em PWM Output;
  
        PWM.start(motor1,2,50)
        #O valor 2 acima representa a porcentagem da frequencia, 50HZ, aplicada no inicio;
        #Este valor pode ser recalibrado para uma nova posicao inicial do servo;

    def rotate(angulo):
        ciclo= 8./180.*angulo + 2
        #Equacao relacionando o valor do angulo com a porcentagem de frequencia para o motor;
        #Tem de se achar o valor da porcentagem para a qual
        #a posicao do servo e diametralmente oposta a inicial;
        #Considera-se aqui esse valor como 10. Para a equacao se usa 10-2=8;
        PWM.set_duty_cycle(motor1,ciclo)
