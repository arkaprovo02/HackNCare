# HackNCare
 A web app in conjunction with desktop app which aims for betterment in health of the users.  
## *1. Application link :zipper_mouth_face:*
- Webpage link - https://arkaprovo02.github.io/HackNCare/
- Demonstration Link - https://youtu.be/RCGPIq1an1Y
## *2. Description :thinking:*
  - 1. Home Page<br/> 
  
  The above link shows the main website of HackNCare. The website shows all our services and principles and you can register here as well as download our application from here.

  - 2. For exercise model
    
We used Mediapipe library for Pose detection. The distance between the landmarks of the figure are used to calculate the count of the exercise and that count is multiplied with the calories burnt in one count of that specific exercise to get the overall calories burnt in one set.<br/>

  - 3. Disease detection models

We used a kaggle dataset where various parameters(eg BP, Cholestrol level etc) were given. We used SVM classifier(kernel=linear) and trained the model. The accuracy of the model was 87.5 %. Using streamlit we took the data of the user in terms of the parameters the model was trained in and accordingly the model will predict whether the patient is suffering from heart disease or not.<br/> 
Similarly for the kidney detection model we used SVM(kernel=linear) which gave us an accuracy of 98 %.<br/>
For the both the models of diabetes we used Random Forest Classifier which gave us an accuracy of 93 %.<br/>

  - 4. Reminder for taking medicine
       - The user first register with personal details and name of the prescibed medicine and their specfic times of consumption along with an email id and mobile no.<br/>
       - These information are stored in a Google Spread-Sheet.<br/>

    -MAIL<br/>

      - Used Simple Mail Transfer Protocol(SMTP) to send an email with a proper format to the user end.<br/>
      - Firstly a SMTP server is set up using registered mail id and password.<br/>
      - Mails will be send to the users' mail ids(collected from Google Spread-sheet) at those specfic times(given that the SMTP server is running).<br/>
     
    -SMS<br/>

      - Used TWILIO Api to send SMS to the users.<br/>
      - TWILIO account is first created and the account sid and authentication tokens are used to set up a client server.<br/>
      - SMS will be send to the users' mobile no.(connected from Google Spread Sheet) at those specific times of medication.<br/>
   

 ## *3. Dataset*
  - Datasets taken from ![Logo](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white).<br/>
 ## *4. Used*
 ![Logo](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
 ![Logo](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
 ![Logo](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
 ![Logo](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
 ![Logo](https://img.shields.io/badge/SciPy-654FF0?style=for-the-badge&logo=SciPy&logoColor=white)
 ![Logo](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
 ![Logo](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
 ## *5. IDE*
 ![Logo](https://img.shields.io/badge/Visual_Studio-5C2D91?style=for-the-badge&logo=visual%20studio&logoColor=white)
 ![Logo](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
 ![Logo](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
 ## *5. Future Improvements :raised_eyebrow:*
Features like virtual meet with doctors (online) and location of availability of blood donors and blood banks are to be added.<br/>
 ## *6. Contributers :nerd_face:*
  - Ayush Roy<br/>
  - Arkaprovo Acharya<br/>

