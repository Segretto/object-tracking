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
  The source code must be available for download and public contribution, according to the MIT License.
### 3.2 Cost
  The materials must cost the least convenient amount, that is, among the viable options, the one which costs less. 
### 3.3 Performance
  The computer vision code must run without dependencies on external computing resources relative to the beaglebone; the camera must be capable of tracking the object without losing it, considering moderate velocity (if the ball doesn't get further than half the FOV of the camera in one frame).
### 3.4 Real time
  The program must send commands to the motor in fixed time intervals that are close or smaller than the camera's FPS, considering the speed of the image processing methods being used.  
## 4. Interfaces
### 4.1 Hardware
### 4.2 Mechanical
### 4.3 User Interface
