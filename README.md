# Object Tracking
## 1. Overall Description
### 1.1 Objective

### 1.2 Operating Environment

### 1.3 Dependecies

### 1.4 Assumptions

## 2. Features

### 2.1 Vision
#### 2.1.1 Description:
  Indentifies the edges and calculate object geometric center position and velocity
#### 2.1.2 Functional Requirements
  Pre-processing  
  Output control  
  OpenCv  
  WebCam Logitech c270 30fps  

### 2.2 Control System 
 
#### 2.2.1 Description:
  Determines the next desired position of the camera using the vision feature output

#### 2.2.2 Functional Requirements

### 2.3 Mechanics

#### 2.3.1 Description:
  Mechanism for camera posiotining.  

#### 2.3.2 Functional Requirements
  Vertical rotational actuator  
  Horizontal rotational actuator

## 3. System Qualities
### 3.1 Open Source
  O código-fonte deverá estar disponível para download e contribuição pública, de acordo com a MIT License.
### 3.2 Cost
  Os materiais deverão custar o mínimo conveniente para cumprirem suas funções, isto é, dentre as opções viáveis, possuir o menor custo.
### 3.3 Performance
  O código de computação visual deverá rodar sem depender de recursos computacionais alheios à beaglebone; a câmera deverá ser capaz de seguir o objeto sem perdê-lo de vista, considerando velocidades moderadas (considerando que a bolinha não percorra mais da metade do fov da câmera em 1 frame)
### 3.4 Real time
  O programa deverá enviar comandos ao motor em intervalos fixos que se aproximem ou superem o fps da câmera, respeitando a capacidade dos métodos de processamento de imagem.
  
## 4. Interfaces
### 4.1 Hardware
### 4.2 Mechanical
### 4.3 User Interface
