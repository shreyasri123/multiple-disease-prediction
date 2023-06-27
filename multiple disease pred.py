import pickle
import sklearn
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/Akshita/OneDrive/Desktop/ML/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/Akshita/OneDrive/Desktop/ML/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/Akshita/OneDrive/Desktop/ML/saved models/parkinsons_model.sav', 'rb'))

cancer_model= pickle.load(open('C:/Users/Akshita/OneDrive/Desktop/ML/saved models/cancer_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',

                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction'
                           ],
                           
                          icons=['activity','heart','person'],
                          default_index=0)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Detection')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('**Diabetes Test Result**'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = '**The person is diabetic**'
          st.write("As a diabetes person, it's important to take control of your health by managing your blood sugar levels through a combination of medication, diet, and exercise. Work with your healthcare team to create a personalized plan that fits your lifestyle and health needs. Make sure to monitor your blood sugar regularly, and take steps to prevent complications like nerve damage, heart disease, and kidney problems. It's also important to communicate openly with your loved ones about your condition and how they can support you. By taking these steps, you can live a healthy and fulfilling life with diabetes.")
          st.write('**You can use the following link to book an appointment [BOOK HERE](https://www.google.com/aclk?sa=l&ai=DChcSEwih39LhmOT9AhUEJSsKHfL_BWAYABAFGgJzZg&ase=2&ei=5QEVZM-PLISMseMPlrKH-A4&sig=AOD64_36j0Ha3BegYTHB_C23raceYcxUiA&q&sqi=2&nis=4&adurl&ved=2ahUKEwiPls7hmOT9AhUERmwGHRbZAe8Q0Qx6BAgGEAE).**')

        else:
          diab_diagnosis = '**The person is not diabetic**'
          st.write("YOU'RE HEALTHY!😎")
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Detection')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('**Heart Disease Test Result**'):
        heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg),int(thalach),int(exang),int(oldpeak),int(slope),int(ca),int(thal)]])
        
        if (heart_prediction[0]== 1):
          heart_diagnosis = '**The person is having heart disease**'
          st.write("As a heart disease patient, eat a heart-healthy diet rich in fruits, veggies, whole grains, and lean proteins.If you're still smoking, stop, and stay away from people who are.Get regular exercise, but first consult your healthcare professional to find out what activities are suitable for you.Utilize relaxation methods to reduce tension, such as deep breathing exercises or meditation.To help your doctor monitor your situation, take any prescribed medications as instructed and show up for all of your appointments.")
          st.write('**You can use the following link to book an appointment [BOOK HERE](https://www.google.com/aclk?sa=l&ai=DChcSEwih39LhmOT9AhUEJSsKHfL_BWAYABAFGgJzZg&ase=2&ei=5QEVZM-PLISMseMPlrKH-A4&sig=AOD64_36j0Ha3BegYTHB_C23raceYcxUiA&q&sqi=2&nis=4&adurl&ved=2ahUKEwiPls7hmOT9AhUERmwGHRbZAe8Q0Qx6BAgGEAE).**')

        else:
          heart_diagnosis = '**The person does not have any heart disease**'
          st.write("YOU'RE HEALTHY!")
        
        st.success(heart_diagnosis)


# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Detection")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("**Parkinson's Test Result**"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "**The person has Parkinson's disease**"
          st.write("As a parkinson's disease patient, eat a heart-healthy diet rich in fruits, veggies, whole grains, and lean proteins.If you're still smoking, stop, and stay away from people who are.Get regular exercise, but first consult your healthcare professional to find out what activities are suitable for you.Utilize relaxation methods to reduce tension, such as deep breathing exercises or meditation.To help your doctor monitor your situation, take any prescribed medications as instructed and show up for all of your appointments.")
          st.write('**You can use the following link to book an appointment [BOOK HERE](https://www.google.com/aclk?sa=l&ai=DChcSEwih39LhmOT9AhUEJSsKHfL_BWAYABAFGgJzZg&ase=2&ei=5QEVZM-PLISMseMPlrKH-A4&sig=AOD64_36j0Ha3BegYTHB_C23raceYcxUiA&q&sqi=2&nis=4&adurl&ved=2ahUKEwiPls7hmOT9AhUERmwGHRbZAe8Q0Qx6BAgGEAE).**')

        else:
          parkinsons_diagnosis = "**The person does not have Parkinson's disease**"
          st.write("YOU'RE HEALTHY!")
        
    st.success(parkinsons_diagnosis)

if (selected == 'Breast Cancer Prediction'):

    # page title
    st.title('Breast Cancer Detection')

    # getting the input data from the user
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        meanradius = st.text_input('Mean Radius')

    with col2:
        meantexture = st.text_input('Mean Texture')

    with col3:
        meanperimeter = st.text_input('Mean Perimeter')

    with col4:
        meanarea = st.text_input('Mean Area')

    with col5:
        meansmoothness = st.text_input('Mean Smoothness')

    with col1:
        meancompactness = st.text_input('Mean Compactness')

    with col2:
        meanconcavity = st.text_input('Mean Concavity')

    with col3:
        meanconcavepoints = st.text_input('Concave Points')

    with col4:
        meansymmetry = st.text_input('Mean Symmetry')

    with col5:
        meanfractaldimension = st.text_input('Mean Fractal Dimension')

    with col1:
        radiuserror = st.text_input('Radius Error')

    with col2:
        textureerror = st.text_input('Texture Error')

    with col3:
        perimetererror = st.text_input('Permiter Error')

    with col4:
        areaerror = st.text_input('Area Error')

    with col5:
        smoothnesserror = st.text_input('Smoothness Error')

    with col1:
        compactnesserror = st.text_input('Compactness Error')

    with col2:
        concavityerror = st.text_input('Concavity Error')

    with col3:
        concavepointserror = st.text_input('Concave Points Error')

    with col4:
        symmetryerror = st.text_input('Symmetry Error')

    with col5:
         fractaldimensionerror= st.text_input('Fractal Dimension Error')

    with col1:
        worstradius = st.text_input('Worst Radius')

    with col2:
        worsttexture = st.text_input('Worst Texture')

    with col3:
        worstperimeter = st.text_input('Worst perimeter ')

    with col4:
        worstarea = st.text_input('Worst Area')

    with col5   :
        worstsmoothness = st.text_input('Worst Smoothness')

    with col1:
        worstcompactness = st.text_input('Worst Compactness')

    with col2:
        worstconcavity= st.text_input('Worst Concavity')

    with col3:
        worstconcavepoints = st.text_input('Worst Concave points')

    with col4:
        worstsymmetry = st.text_input('Worst Symmetry')

    with col5:
        worstfractaldimension = st.text_input('Worst Fractal Dimension')
    # code for Prediction
    cancer_diagnosis = ''

    # creating a button for Prediction

    if st.button('**Breast Cancer Test Result**'):
        cancer_prediction = cancer_model.predict(
            [[int(meanradius),int(meantexture),int(meanperimeter),int(meanarea),int(meansmoothness),int(meancompactness),int(meanconcavity),int(meanconcavepoints),int(meansymmetry),int(meanfractaldimension),int(radiuserror),int(textureerror),int(perimetererror),int(areaerror),int(smoothnesserror),int(compactnesserror),int(concavityerror),int(concavepointserror),int(symmetryerror),int(fractaldimensionerror),int(worstradius),int(worsttexture),int(worstperimeter),int(worstarea),int(worstsmoothness),int(worstcompactness),int(worstconcavity),int(worstconcavepoints),int(worstsymmetry),int(worstfractaldimension)]])

        if (cancer_prediction[0] == 1):
            cancer_diagnosis = '**The Breast Cancer is Maligant**'
            st.write("If you have been diagnosed with breast cancer, it's important to work closely with your healthcare team to develop a personalized treatment plan. Treatment options may include surgery, radiation, chemotherapy, hormone therapy, or a combination of these. It's also important to maintain a healthy lifestyle, including eating a balanced diet, getting regular exercise, and managing stress. Support from family, friends, and support groups can also be helpful during this time. Remember to take care of yourself both physically and emotionally.")
            st.write('**You can use the following link to book an appointment [BOOK HERE](https://www.google.com/aclk?sa=l&ai=DChcSEwih39LhmOT9AhUEJSsKHfL_BWAYABAFGgJzZg&ase=2&ei=5QEVZM-PLISMseMPlrKH-A4&sig=AOD64_36j0Ha3BegYTHB_C23raceYcxUiA&q&sqi=2&nis=4&adurl&ved=2ahUKEwiPls7hmOT9AhUERmwGHRbZAe8Q0Qx6BAgGEAE).**')

        else:
            cancer_diagnosis = '**The Breast Cancer is Benign**'
            st.write("YOU'RE HEALTHY!")

    st.success(cancer_diagnosis)














