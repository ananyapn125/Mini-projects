# College Student ChatBot - Fully Expanded Version
import random

print("ByteBot: Hey! I’m your College Assistant. Ask me anything regarding our college!")
print("Type 'bye' anytime to exit.\n")

responses = {

    # --- Greetings ---
    "hi": ["Hey!", "Hi there!", "Hello! How can I help you?"],
    "hello": ["Hello!", "Hi! What’s up?", "Hey! Need something?"],
    "hey": ["Hey! How can I help you today?", "Hi! What do you need?"],

    # --- Acknowledgements ---
    "ok": ["Okay!", "Sure!", "Alright!"],
    "okay": ["Alright!", "Okay then!", "Sure!"],
    "sure": ["Sure!", "Got it!", "Alright!"],
    "alright": ["Okay!", "Sure!", "Alright then!"],
    "thanks": ["You're welcome!", "Anytime!", "Happy to help!"],
    "thank you": ["You're welcome!", "Glad I could help!", "No problem!"],

    # --- Basic Info ---
    "college timings": ["College runs from 9 AM to 4 PM."],
    "class timings": ["Most sections start at 9 AM.", "Check the timetable for exact timings."],
    "timetable": [
        "The timetable is available on the student portal.",
        "You can find the timetable on the class notice board."
    ],

    # --- Attendance ---
    "attendance": ["You must have 75% attendance.", "Check your attendance on the ERP portal."],
    "how to check attendance": [
        "Login to the ERP → Dashboard → Attendance.",
        "Check attendance in the student portal menu."
    ],

    # --- Exams ---
    "exam": [
        "Mid-semester exams happen twice a year.",
        "Exam dates will be posted by the exam cell soon."
    ],
    "when are exams": [
        "Exam timetables will be shared by your department.",
        "Midsems usually happen around November/April."
    ],
    "marks": ["Internal marks will be uploaded soon.", "You can check marks in the ERP."],
    "results": ["Results will be announced on the college portal.", "Wait for official notification."],

    # --- Holidays ---
    "holiday": ["Holiday list is available on the website.", "Ask your class rep for the latest holiday info."],
    "when is holiday": ["Check the notice board for holiday updates.", "Holiday announcements come from admin."],

    # --- Campus Facilities ---
    "library timings": [
        "Library is open from 9 AM to 6 PM.",
        
    ],

    "library book issue":  ["You can borrow books for 14 days with your ID card."],
    
    "canteen timings": [
        "Canteen is open from 9 AM to 5 PM.",
    ],
    
    "what food does canteen have" : ["Snacks, meals and drinks are available."
    ],
    "canteen food": [ "Snacks, meals and drinks are available at reasonable prices."
    ],
    "wifi": [
        "Wi-Fi credentials are given by the IT department.",
        "Wi-Fi is available across academic blocks and hostels."
    ],

    # --- Direction Info ---
    "where is office": [
        "The admin office is in the main block, ground floor.",
        "Ask any staff—they'll point you to the admin office."
    ],
    "where is library": [
        "Library is located next to Canteen .",
    ],
     "where is the library": [
        "Library is located next to the Canteen.",
    ],

    "where is the canteen": [
        "Canteen is located next to the Auditorium .",
    ],

    "where is  canteen": [
        "Canteen is located next to the Auditorium .",
    ],
    
    "washroom": [
        "Washrooms are on every floor near the staircase.",
    ],
    "bathroom": [
        "Bathrooms are beside the stairs on every floor.",
        "You'll find bathrooms at both ends of each block."
    ],

    # --- Hostel Info ---
    "hostel": [
        
        "For hostel issues, contact the warden’s office."
    ],

    "hostel curfew":["Hostels have an 8:30 PM curfew."],
    
    "hostel rules": [
        "No loud music after 9 PM.",
        "Visitors are only allowed during designated hours.",
        "Lights out depends on your block's rules."
    ],

    # --- Transport / Bus ---
    "transport": [
        "Unfortunately the college does not provide transport facility."
    ],
    "bus route": [
        "Unfortunately the college does not provide transport facility."
    ],

    # --- Labs & Academics ---
    "lab": [
        "Lab sessions follow your timetable.",
        "Carry your lab record and required materials!"
    ],
    "assignment": [
        "Submit assignments before the given deadline.",
        "Assignment details will be shared by your faculty."
    ],
    "notes": [
        "Notes are shared on the ERP or class WhatsApp group.",
        "Faculty usually uploads notes after each module."
    ],

    # --- Fees & Certificates ---
    "fee": [
        "You can pay fees online through the ERP portal.",
        "Visit the Accounts Office for fee queries."
    ],
    "scholarship": [
        "Scholarship guidelines are available on the college portal.",
        "Apply with required documents in the admin office."
    ],
    "bonafide": [
        "Apply for a bonafide certificate in the admin office.",
        "Submit a request form to receive a bonafide certificate."
    ],

    # --- Events & Clubs ---
    "event": [
        "Many events are coming this semester—stay tuned!",
        "Check the notice board for event announcements."
    ],
    "fest": [
        "The college fest will be announced soon.",
        "You can register through different student clubs."
    ],
    "club": [
        "You can join coding, dance, music, robotics, NSS, sports and more!",
        "Club registrations open at the start of the semester."
    ],
    "sports": [
        "Sports practice happens after 4 PM.",
        "Meet the sports coordinator to join the team."
    ],

    # --- Department Info ---
    "cse department": [
        "CSE department is in Mechanical Block, 3rd floor."
        
    ],
    "ece department": [
        "ECE department is in ECE block, 3rd floor."
    ],
    "eee department": [
        "EEE department is in ECE block, 2nd floor."
    ],
    "mechanical department": [
        "Mechanical department is in Mechanical block, 1st floor."
    ],
    
    "civil department": [
        "Civil department is in Mechanical block, ground floor."
       
    ],

    #department 
     "stream":[
         "For your stream queries, contact the respective department HOD."
    ],
  
    
    # --- Faculty Contact (General) ---
    "hod": [
        "You can meet your HOD during office hours.",
        "HOD cabin is inside your department block."
    ],
    "faculty": [
        "You can meet faculty during free hours or send a polite email.",
        "Ask your class rep for your faculty timetable."
    ],
    "teacher": [
        "Faculty contacts are available on the department notice board.",
        "You can talk to teachers after class hours."
    ],

    # --- Campus Map / Directions ---
    "map": [
        "Campus maps are displayed at main entrances.",
        "Follow the signboards to easily navigate the campus."
    ],
    "where is": [
        "You can check the campus map or ask nearby staff for directions.",
        "Signboards around the campus help you find any block."
    ],
}

# --- Fallback Replies ---
fallback = [
    "I’m not sure about that. Try asking about exams, fees, timetable, or departments!",
    "Hmm… I don’t have that information yet. Try rephrasing?",
    "You can confirm this from the admin or department office!"
]

def get_response(text):
    text = text.lower()

    for key in responses:
        if key in text:
            return random.choice(responses[key])

    return random.choice(fallback)


# --- Chat Loop ---
while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("StudentBot: Bye! Have a great day!")
        break

    print("StudentBot:", get_response(user))
