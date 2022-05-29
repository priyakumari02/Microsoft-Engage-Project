# <h1 align="center"> Microsoft-Engage-Project <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/480px-Microsoft_logo.svg.png" alt="Logo" width="25" height="25">

  > [Live Demo](https://youtu.be/w6271lMbUZY) <br>
  > [Desktop App](https://drive.google.com/drive/folders/1lyTn19RgnyZkyFGtCHysfAXCH_7_m-AU?usp=sharing) <br>
  > [Workflow](https://drive.google.com/drive/folders/1mYyBT904klHHc_wApRjrhLz7jtPlqjzX?usp=sharing)<br/>
</h1>
<br>
Face Recognition for Tracking Attendance<br>
A browser-based application to demonstrate application of Face Recognition technology.
<br>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>📋Table of Contents</summary>
  <ol>
    <li>
      <a href="#About-The-Project">About The Project</a>
      <ul>
        <li><a href="#Introduction">Introduction</a></li>
        <li><a href="#Features">Features</a></li>
        <li><a href="#Technologies-used"> Technologies used</a></li>
      </ul>
    </li>
      <a href="#Getting-Started">Getting Started</a>
      <ul>
        <li><a href="#Requirements">Requirements</a></li>
        <li><a href="#Installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#Documentation">Documentation</a>
      <ul>
        <li><a href="#How-it-works?">How it works?</a></li>
        <li><a href="#resources-used">Resources Used</a></li>
      </ul>
  </ol>
</details>

## Introduction

Detect & Recognize Faces from Live Feed, Static Image. Attendace is marked & saved in Csv format. Graphical User Interface is designed & build using [Tkinter](https://docs.python.org/3/library/tkinter.html) GUI and Library [OpenCV](https://opencv.org/).

## Features
### Landing Page
![gifmain](https://user-images.githubusercontent.com/77202746/170883600-d3371c8e-6548-4f1f-92cb-6e567e9d61dd.gif)

### Student Details 
|------|------|------|------|------|
#### Save data| Update data| Delete data | Reset data |Take Photo Samples
![gifstudentdetails](https://user-images.githubusercontent.com/77202746/170884146-9cd73ed4-2732-4a2f-b327-dcfb01f143df.gif)

### Train data
![giftraindata](https://user-images.githubusercontent.com/77202746/170884503-e513f6b3-9dd7-49c2-8ea1-1fc0c8777274.gif)

### Attendance with Face Detection
![gif face recognition](https://user-images.githubusercontent.com/77202746/170884228-7b25dc69-48cf-4c43-b5ab-75849c644dec.gif)

### Attendance Panel
#### Attendance is written in Csv File with Name and Time and shown
![gif attendance pannel](https://user-images.githubusercontent.com/77202746/170884657-c40a854e-a457-40c0-914a-2f201294c133.gif)

### Photos 
### Exit System

## 💻Technologies used

#### Programming Languages : <img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="Python">

#### Databases : <img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">

#### Libraries : [OpenCV](https://opencv.org/).

#### Frameworks :[Tkinter](https://docs.python.org/3/library/tkinter.html)

#### Version Control : <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>

# 🏃Getting Started

## Requirements

- Python 3.3+
- macOs or Linux or Windows

## Installation

### Get it up & running

- Download the program from [here](https://github.com/priyakumari02/Microsoft-Engage-Project/archive/master.zip)
- Unzip the downloaded zip file
- Install all the dependencies from the requirement.txt
- Start the server

### Building the source code

#### 1. Clone the repository

```sh
git clone https://github.com/priyakumari02/Microsoft-Engage-Project.git
```

#### 3. Download & Install all the Dependencies

```sh
pip install -r requirements.txt
```

or

```sh
pip install --user -r requirements.txt
```
#### 4. Start the server
```sh
python main.py
```

# 📚Documentation

### 🤔 How it works?
- Face is detected by Haar Cascade algorithm
- Face detected is encoded and saved for recognition
- If encodings are matched from the datset, Attendance is written in Csv File with Name and Time

### 📗Resources Used

### Algorithm

- [Haar Cascade](https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08#:~:text=So%20what%20is%20Haar%20Cascade,Simple%20Features%E2%80%9D%20published%20in%202001.)
- [LBPH Algorithm](https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b)

<hr>
Thank you ! Microsoft Team for such a wonderful mentorship program ❤️
