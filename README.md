# <h1 align="center"> Microsoft-Engage-Project <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/480px-Microsoft_logo.svg.png" alt="Logo" width="25" height="25">

</h1>

Face Recognition for Tracking Attendance<br>
A browser-based application to demonstrate application of Face Recognition technology.

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
      <a href="#Getting-Sttarted">Getting Started</a>
      <ul>
        <li><a href="#Requirements">Requirements</a></li>
        <li><a href="#Installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#Documentation">Documentation</a>
      <ul>
        <li><a href="#How-it-works?">How it works?</a></li>
      </ul>
    <a href="#resources-used">Resources Used</a></li>
  </ol>
</details>

## Introduction

Detect & Recognize Faces from Live Feed, Static Image. Attendace is marked & saved in Csv format. Graphical User Interface is designed & build using [Tkinter](https://docs.python.org/3/library/tkinter.html) GUI and Library [OpenCV](https://opencv.org/).

## Features

## 💻Technologies used

#### Programming Languages : <img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="Python">

#### Databases : <img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">

#### Libraries : [OpenCV](https://opencv.org/).

#### Frameworks :[Tkinter](https://docs.python.org/3/library/tkinter.html)

#### Version Control : <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>

# 🏃Getting Sttarted

## Requirements

- Python 3.3+
- macOs or Linux or Windows

## Installation

### Get it up & running

- Download the program from [here](https://github.com/priyakumari02/Microsoft-Engage-Project/archive/master.zip)
- Unzip the downloaded zip file
- Install all the dependencies from the requirement.txt

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

# 📚Documentation

## 🤔 How it works?
- Face is detected by Haar Cascade algorithm
- Face detected is encoded by 128 measurements & saved for recognition
- When program is initiated User's face is similar detected & encoded by 128 measurements
- Later these encoded measurements are compared for recognizing face from Database
- If encodings are matched, Attendance is written in Csv File with Name & Time

# 📗Resources Used

### Algorithm

- [Haar Cascade](https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08#:~:text=So%20what%20is%20Haar%20Cascade,Simple%20Features%E2%80%9D%20published%20in%202001.)
- [LBPH Algorithm)](https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b)

Thank you ! Microsoft Team for such a wonderful mentorship program ❤️
