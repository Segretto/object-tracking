import Adafruit_BBIO.PWM as PWM

motor1 = "P8_19"
  #Motor conectado em PWM Output;
  
PWM.start(motor1,2,50)
  #O valor 2 acima representa a porcentagem da frequência, 50HZ, aplicada no início;
  #Este valor pode ser recalibrado para uma nova posição inicial do servo;

while(1):
  angulo=input("Insira ângulo desejado: ")
  ciclo= 8./180.*angulo + 2
    #Equação relacionando o valor do ângulo com a porcentagem de frequência para o motor;
    #Tem de se achar o valor da porcentagem para a qual
    #a posição do servo é diametralmente oposta à inicial;
    #Considera-se aqui esse valor como 10. Para a equação se usa 10-2=8;
  PWM.set_duty_cycle(motor1,ciclo)
