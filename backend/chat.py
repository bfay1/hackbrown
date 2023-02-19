import os
import openai

try:
    from keys import *
except:
    API_KEY = input("OpenAI Key: ")

openai.api_key = API_KEY

def fetch_open_ai_response(prompt):
    start_sequence = "\nAI:"
    restart_sequence = "\nStudent: "
    print(prompt)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Student:", " AI:"]
    )

    return response['choices'][0]['text'].strip()

primer = """
You are an AI model that is trained on a classroom lecture in a university setting.
I will feed you the transcript of your lecture today.
At irregular intervals I will feed you questions from students in the lecture.
These questions will begin with " Student: ".
You will repsond concisely from the perspective of the professor teaching the course.
The lecture transcript follows: """.replace("\n", " ")

class professor():
    def __init__(self, lecture):
        self.prompt = primer + "\n" + lecture
        self.prompt = " ".join(self.prompt.split(" ")[:4000])
        self.prompt += "\n"
        self.last = []
    
    def add(self, text):
        x = "Student: " + text + "\nAI: "
        self.last.append(x)
        self.prompt += x
    
    def submit(self, ai_part=True):
        r = openai.fetch_openai_response(self.prompt)
        if ai_part:
            return "AI: " + r
        return r
    
    def add_and_submit(self, text):
        self.add_to_prompt(text)
        temp = self.prompt.split(" ")
        x = self.prompt.index("followed: ")

        while len(temp) > 3000:
            try:
                temp.pop(x + 1)
            except:
                temp.pop(-1)
        self.prompt = " ".join(temp)

        y = self.submit(False)
        
        while len(y) == 0:
            print("REPEATING FOR SOME REASON")
            y = self.submit(False)
        self.prompt += y + "\nStudent: "
        return y