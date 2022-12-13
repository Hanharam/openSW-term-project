# **1. Project Overview**
1. **Project Topic**: A program to identify the number of people after recognizing whether or not to wear a mask
2. **Program function**: Check if a mask is worn, recognize a person's face, identify the number of people, and take a picture of the person without a mask
3. **Progress**:
```sh
First, check how to use the git hub
Second, pick a topic
Third, role-sharing
Fourth, write the code and push, merge
Fifth, combining codes
Sixth, write a report
```

4. **Role sharing**:
```sh
Kim Jin-won: Write parts 2 and 3 of the report, make a model code, count how many people are wearing masks, and upload tensorflow files
Han Haram: Write part 1 of the report, code the preprocessing function, and count how many people are wearing masks and not wearing masks
Jiwoo Choi: Write part 4 of the report, code the predict function, capture people without masks and save image files
Heo Dong-hyuk: Write part 5 of the report, create a detection code, and capture people without masks and save image files
```

# 2. Demonstration Image
![test1](https://github.com/Hanharam/openSW-term-project/blob/main/test1.jpg)
![test2](https://github.com/Hanharam/openSW-term-project/blob/main/test2.jpg)


# 3. package & version

## 1) Python 3.9 

install python, version doesn't matter (We install python 3.9)

### how to install 
- window
    https://www.python.org/downloads/
- mac
    Mac already has Python installed
    but if you need latest version, download on site

## 2) Opencv / Tensorflow

### how to install


- Enter the following in terminal
    **pip install opencv-python**
    **pip install --upgrade tensorflow==2.5.0**

# 4. How to run
---
##### 1. Go to teachablemachine.withgoogle.com, click Start, and select an image project, standard image model
##### 2. Upload a picture of a person wearing a mask and a picture of a person without a mask on class 1 and class 2, respectively
##### 3. Click learn model and select export model after test
##### 4. Press Tensorflow to download the model and decompress the file
##### 5. Run the program after installing opencv and tensorflow via "pip install opencv-python" and "pip install --upgrade tensorflow==2.5.0"


# 5. Reference materials

[blog](https://codeonweb.com/entry/5f15bf8e-d704-49e0-909a-db4450433b74)<-- acquiring ideas
[program](https://teachablemachine.withgoogle.com)<-- simple execution
[mask picture](https://search.naver.com/search.naver?where=image&sm=tab_jum&query=마스크+쓴+사람)<-- utilization data
[no mask picture](https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=얼굴&oquery=사람+얼굴&tqi=hHNd3wprvxsss6XJU4Zssssss2Z-093696)<-- utilization data
