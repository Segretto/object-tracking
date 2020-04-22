# Object Tracking
## 1. Overall Description
### 1.1 Objective
*** Track colored objects utilizing computer vision and camera positioning control within an embedded system.

### 1.2 Operating Environment
Linux Angstron
Beaglebone
WebCam Logitech c270 30fps
DC Motor *TBD*

### 1.3 Dependecies
OpenCV
Python
TotalCross
Java
Numpy
Git
GTK
CMake

### 1.4 Assumptions
The system will be able to track different object colors and shapes
The object trajectory will be within a reasonable distance from the camera
The object will be moved by a person whom will apply different accelerationt within human capacity


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
<<<<<<< HEAD
  
||||||| merged common ancestors
=======
  The source code must be available for download and public contribution, according to the MIT License.
>>>>>>> eb32bafeb89f90853d5304b37007dbe184f51680
### 3.2 Cost
<<<<<<< HEAD
 
### 3.3 Performance
  
||||||| merged common ancestors
### 3.3 Performance  
=======
  The materials must cost the least convenient amount, that is, among the viable options, the one which costs less. 
### 3.3 Performance
  The computer vision code must run without dependencies on external computing resources relative to the beaglebone; the camera must be capable of tracking the object without losing it, considering moderate velocity (if the ball doesn't get further than half the FOV of the camera in one frame).
>>>>>>> eb32bafeb89f90853d5304b37007dbe184f51680
### 3.4 Real time
<<<<<<< HEAD
  
  
||||||| merged common ancestors

=======
  The program must send commands to the motor in fixed time intervals that are close or smaller than the camera's FPS, considering the speed of the image processing methods being used.  
>>>>>>> eb32bafeb89f90853d5304b37007dbe184f51680
## 4. Interfaces
### 4.1 Hardware
### 4.2 Mechanical
### 4.3 User Interface
