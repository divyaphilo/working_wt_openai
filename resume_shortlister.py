import PyPDF2
import openai
import os


# Function to interact with ChatGPT
def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" if preferred
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {e}"

# create a function to read JD and return content
def pdf_reader(file_path:str):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        # Loop through each page and extract text
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

        #print(text)
        return text


# Define the directory containing the resumes
resume_directory = 'C:\\divya_workspace\\resumes\\'

# Find all PDF files in the directory, if there are more volume of resume files. below code is the optimised.
resume_paths = [os.path.join(resume_directory, filename)
                for filename in os.listdir(resume_directory)
                if filename.endswith('.pdf')]

# Use a loop to read each resume and store them in a list
my_jd = pdf_reader('C:\divya_workspace\jd\JD.pdf')
resumes = [pdf_reader(path) for path in resume_paths]


# create your full prompt
prompt='Your task is to compare and shortlist best one profile who can join immediate for a given JD\n'
prompt='Attaching JD below:\n'
prompt+=my_jd  +'\n'
prompt+='Attaching Resumes below. Resume contents are seperated by ####\n'
prompt+=resumes[0] +'\n'
prompt+='####\n'
prompt+=resumes[1]  +'\n'
prompt+='####\n'
prompt+=resumes[2]
print(prompt)



# response = chat_with_gpt(prompt)
# print("ChatGPT:", response)


