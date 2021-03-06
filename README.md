# Object Tracking
---
## 1. Overall Description
### 1.1 Objective
> Track colored objects utilizing computer vision and camera positioning control within an embedded system.

### 1.2 Tools and Environment
* Linux Angstron or Ubuntu
* Beaglebone Black
* WebCam Logitech c270 30fps
* DC Motor **TBD**
* Mechanical Structure **TBD**
* Encoder **TBD**
* EPOS Controller

### 1.3 Dependecies
#### 1.3.1 Vision and Control
* OpenCV
* Python
* GTK
* CMake
* ARM Embedded GCC
* Numpy

#### 1.3.2 User Interface
* TotalCross
* Java 8
* Maven

### 1.4 Assumptions
- The chosen objects will be of different sets of simple geometric shapes
- The object trajectory will be within a reasonable distance from the camera
- The object will be moved by a person whom will apply different acceleration within human capacity

---
## 2. Features
### 2.1 Vision Module [1]
#### 2.1.1 Description:
An image processing algorithm that will extract information about the object's shape, color, position and speed.

#### 2.1.2 Functional Requirements
>**FR 1.1** &emsp;Use camera parameterization functions related to the frame capturing.

>**FR 1.2** &emsp;Apply detection (trigger), pre-processing and threshold functions to analyze a specific image area according to color and shape. 

>**FR 1.3** &emsp;Apply noise removal functions and polygonal approximation algorithms in order to determine the object center's postion and velocity.

>**FR 1.4** &emsp;Send the position and velocity values to the controller module.


### 2.2 Control System Module [2] 
#### 2.2.1 Description:
This module will receive the object center position and velocity from the vision module and compute the desired Motor positioning.

#### 2.2.2 Functional Requirements
>**FR 2.1** &emsp;Receive the objects center posistion and velocity from vision module.

>**FR 2.2** &emsp;Receive and configure the user defined PID Controller parameters.

>**FR 2.3** &emsp;Compute DC Motor positions using a proportional-derivative-integrative (PID) control algorithm.

>**FR 2.4** &emsp;Return camera to default position when no data is received from the vision module.

>**FR 2.5** &emsp;Send the desired Motor position to the EPOS Controller.

### 2.3 Mechanical System [3]
#### 2.3.1 Description:
A 2 DoF mechanism actuated by two DC motors coupled in a rigid rod mechanism, with a camera attached at one of it´s end.  

#### 2.3.2 Functional Requirements
>**FR 3.1** &emsp;Vertical rotational actuation.

>**FR 3.2** &emsp;Horizontal rotational actuation.

### 2.4 User Interface **TBD** [4]
#### 2.4.1 Description:
An Android application which will display performance metrics of the system in real time. 
It will also display controller parameters input slots for real time controller configuration.

#### 2.4.2 Functional Requirements
>**FR 4.1** &emsp;Open communication link with the beaglebone (TCP, Bluetooth,...). **TBD**

>**FR 4.2** &emsp;Receive performance metrics from the beaglebone MC.

>**FR 4.3** &emsp;Send sets of controller parameters inputs defined by the user.

---
## 3. System Qualities
### 3.1 Open Source  
The source code must be available for download and public contribution, under the MIT License.

### 3.2 Cost
The materials must cost the least convenient amount, that is, among all the viable systems, the one which costs less with the minimum required performance. 

### 3.3 Performance
The computer vision code must run without dependencies on external computing resources relative to the beaglebone. The camera must be capable of tracking the object without losing it, considering a moderate velocity (if the object doesn't get further than half of the FoV of the camera in one frame).

### 3.4 Real time    
The program must send the updated positions to the motor in fixed time intervals that are close or smaller than the camera's FPS, considering the speed of the image processing methods being used. It also must communicate with the android device and change the PID parameters during duty.   

### 3.5 Field of view
The field of view will be delimited by the mechanical structure and the environment itself, such as the support surface. To an object be identified, it must enter the camera's field of view and stay as already described.

---
## 4. Interfaces
### 4.1 Hardware
- Logitech -- Beaglebone: USB 3.0
- Beaglebone -- EPOS: CNU
- Beaglebone -- Android Device: **TBD**
---
*[TBD]: To Be Defined

1. Thiago Segreto
2. Rodrigo Reis Arrais          9393127
3. Matheus Henrique de Oliveira 9805185 
4. Marcelo Spedine Moreno Filho 9760206
