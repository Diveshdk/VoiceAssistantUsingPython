import openai
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import pywhatkit
import webbrowser
import datetime

print("Hey.I am Your Voice Assistant")
my_secret = 'API_KEY_HERE'

openai.api_key = my_secret

user_input = input("Please say something...\n")
def main():
  user_input = input("Please say something...\n")
  recognizer = sr.Recognizer()
  

chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":
            "user",
            "content":
            "Here is syllabus of Engineering Mathematics/maths 3, There are 6 modules in semester 3 as follows: 1.Laplace Transform , 2.Inverse ,Laplace Transform ,3.Fourier Series: ,4.Complex Variables: ,5.Statistical Techniques ,6.Probability .Here is syllabus of engineering Discrete Structures and Graph Theory (DSGT):There are 6 modules in semester 3 as follows:1. Logic2. Relations and Functions3. Posets and Lattice4. Counting5. Algebraic Structures6. Graph Theory.Here is syllabus of engineering Digital Logic & Computer Organization and Architecture(DLCA):There are 6 modules in semester 3 as follows:1. Computer Fundamentals.2. Data Representation and Arithmetic algorithms.3. Processor Organization and Architecture.4. Control Unit Design.5. Memory Organization.6. Principles of Advanced Processor and Buses.Here is syllabus of engineering Computer Graphics(CG):There are 6 modules in semester 3 as follows:1. Introduction and Overview of Graphics System:2. Output Primitives:3. Two Dimensional Geometric Transformations4. Two-Dimensional Viewing and Clipping5. Three Dimensional Geometric Transformations, Curves and Fractal Generation6. Visible Surface Detection and Animation.Here are roll no of students:1.Rushikesh,2.Devendra,3.Bhavesh,4.Anjali,5.Kabir,6.Karan,7.Amit,8.Mahek,9.Divesh ,10.Levin ,11.Aditya,12.Pooja,13.Vikas,14.Neha,15.Ayush ,16.Vipra,17.Shivam,18.Roshni,19.Satyam,20.Satyaprakash ,21.Luvkush.Here is attendance of students starting with their roll number. 1.Rushikesh - 96.88%,2.Devendra - 81.77%,3.Bhavesh - 69.27%,4.Anjali - 93.75%,5.Kabir - 78.65%,6.Karan - 85.42%,7.Amit - 64.06%,8.Mahek - 80.73%,9.Divesh - 94.79%,10.Levin - 79.17%,11.Aditya - 61.46%,12.Pooja - 94.79%,13.Vikas - 75.00%,14.Neha - 90.10%,15.Ayush - 61.46%,16.Vipra - 95.83%,17.Shivam - 94.79%,18.Roshni - 65.10%,19.Satyam - 90.10%,20.Satyaprakash - 91.15%,21.Luvkush - 72.40%.I will give sem1 result data noe in this order:(Name,Seat Number,CGPA/Number if KT),(Rushikesh Bhogale,6181709,CGPA-7.83),(Devendra Chaurasiya,6181710,backlog- 1 ),(Bhavesh Chaudhary,5222966,CGPA-6.42),(Anjali Divate,6181711,backlog-1 ),(Kabir Dubey,6181712,backlog-3 ),(Karan Gonbare,5222969,CGPA-6.97),(Amit Jadhawar,6181714,backlog-4),(Mahek Jamadar,6181715,backlog-1),(Divesh Kankani,6181717,CGPA-7.22),(Levin Verghese,6181716,backlog-2),(Aditya Maurya,6181718,backlog-5),(Pooja Mhatre, 6181719,backlog-3),(Vikas Mishra,6181720,backlog-2),(Neha Narkhede,6181721,backlog-1),(Ayush Navale,6181722,backlog-3),(Vipra Nehte,5222980,CGPA-7.94),(Shivam Nigam,522982,CGPA-8.00),(Roshani Pal,6181723,backlog-2),(Satyam Pal,6181724,CGPA-6.78),(Satyaprakash Pal,5222985,CGPA-6.89).I will give semester 1 result data in this order:(Name,Seat Number,CGPA/Number if KT),(Rushikesh Bhogale,6159436,CGPA-7.25),(Devendra Chaurasiya,6159437,backlog- 2 )(Bhavesh Chaudhary,6159438,CGPA-7.18),(Anjali Divate,6159439,backlog-1 ),(Kabir Dubey,6159440,backlog-2 ),(Karan Gonbare,6159441,CGPA-6.75),(Amit Jadhawar,6159443,backlog-3),(Mahek Jamadar,6159444,backlog-1),(Divesh Kankani,6159446,CGPA-6.60),(Levin Verghese,6159445,backlog-1),(Aditya Maurya,6159448,backlog-5),(Pooja Mhatre,6159449 ,backlog-2),(Vikas Mishra,6159450,backlog-4),(Neha Narkhede,6159451,backlog-1),(Ayush Navale,6159452,backlog-4),(Vipra Nehte,6159453,backlog-1),(Shivam Nigam,6159454,CGPA-7.65),(Roshani Pal,6159455,backlog-2),(Satyam Pal,6159456,backlog-2),(Satyaprakash Pal,6159457,CGPA-7.90).Here are ERP ID according to roll no wise : (220600244,220600133,220600457,220600160,220600166,220600134,220600541,220600459,220600157,220600008,220600540,220600154,220600139,220600158,220600544,220600007,220600246,220600136,220600384,220600135).I will say about our timetable. We have lectures of 1 hour starting from 9:30 to 4 having lunch break from 12.30 to 1 on 5 days i.e.Monday to Friday. we have holiday on Saturday and sunday.(On Monday, we have practicals from 9.30 to 11.30,2nd lecture starts from 11.30 of DSGT ,3rd is OOP 4th is DS, last is Maths)(On Tuesday,1st lecture is maths, we have practicals from 10.30 to 12.30,and next 3 lectures are CG DLCA and MP 1A),(On Wednesday, first three lectures are DSGT, CG and DS and after break we have 2 hour practicals),(On Thursday First lecture is DLCA. Then we have 2 hour practical, Then after break, there are only 2 lecture till 3 i,e. maths and DS),(On Friday, first 4 lecture are as follow:CG,DSGT,DLCA,OOP and then we have 2 hour practical). "
        }, {
            "role": "user",
            "content": (f"{user_input}")
        }])
print(chat_completion.choices[0].message['content'])


 


while True:
    main()
