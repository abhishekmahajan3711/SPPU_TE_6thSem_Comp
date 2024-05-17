from datetime import date, datetime
import webbrowser


#you can change questions of dictionary as per your need 
disc = {
    "hello": "hi I am Career Guider!!!",
    "what is your name?": "My name is Career chatbot",
    "what is date today?": str(date.today()),
    "what is time?": str(datetime.now().strftime("%H:%M:%S")),
    "Please open google": ["https://www.google.com"],
    "what are trending careers?": "Some trending careers include data science, cybersecurity, artificial intelligence, healthcare, and renewable energy.",
    "what is engineering?": "Engineering is the application of science and mathematics to solve problems and design structures, machines, and processes.",
    "list out top engineering colleges": "Some of the top engineering colleges include MIT, Stanford University, Harvard University, California Institute of Technology, and University of Cambridge.",
    "what is medical?": "The medical field involves the study and practice of diagnosing, treating, and preventing diseases and injuries. It includes various specializations like surgery, pediatrics, and psychiatry.",
    "list out top medical colleges": "Some of the top medical colleges include Harvard Medical School, Johns Hopkins University, Stanford University School of Medicine, University of California--San Francisco, and Mayo Clinic Alix School of Medicine.",
    "what is data science?": "Data science is a multidisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data.",
    "what is cybersecurity?": "Cybersecurity involves protecting computer systems, networks, and data from digital attacks, theft, and damage. It is crucial for safeguarding sensitive information.",
    "what is artificial intelligence?": "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. AI is used in various applications such as speech recognition, decision-making, and autonomous vehicles.",
    "what are the top careers in healthcare?": "Top careers in healthcare include physician, nurse practitioner, pharmacist, physical therapist, and medical and health services manager.",
    "what is renewable energy?": "Renewable energy comes from sources that are naturally replenished, such as solar, wind, and hydroelectric power. Careers in this field focus on developing and managing sustainable energy solutions.",
    "list out top colleges for computer science": "Some of the top colleges for computer science include MIT, Stanford University, Carnegie Mellon University, University of California--Berkeley, and Harvard University.",
    "what is business management?": "Business management involves planning, organizing, directing, and controlling the activities of an organization to achieve its objectives. It encompasses various aspects like finance, marketing, and human resources.",
    "list out top business schools": "Some of the top business schools include Harvard Business School, Stanford Graduate School of Business, University of Pennsylvania (Wharton), MIT Sloan School of Management, and University of Chicago (Booth).",
}
to_con = ""
while to_con.lower() != "bye":
    to_con = input("YOU : ")
    if to_con.lower() != "bye":
        flag = False
        for k in disc:
            if k.lower() == to_con.lower():
                if isinstance(disc[k], str):  
                    print("Bot :" + disc[k])
                else:
                    webbrowser.open(disc[k][0])
                flag = True
                break
        if not flag:
            print("Can't understand, please repeat")
print("Bot : Thank you!!")
