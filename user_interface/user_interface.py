import requests
from textwrap import dedent

def pol_debug_test(question):
    res = requests.post('https://chatbotdevbranch.herokuapp.com/question', json={"text": question})
    if res.ok:
        rtn = res.json()["text"]
        # print(f"Query return = {rtn} \n")


class TextHandler:
    def __init__(self):
        self.counter = 0

    def print_text_output(self, text):
        print(dedent(text))
        
    def text_intake(self, text):
        self.counter += 1
        return input(dedent(text))

example = TextHandler()


def welcome_message():
    """
    Display a text prompt to the user to describe intended input.
    """
    example.print_text_output("""
    Welcome to the Code Fellows chatbot app! 
    Please enter your question about Code Fellows or their course offerings below, or 
    enter 'q' or 'quit' to exit the app. \n
    """)

def query_prompt():
    """
    Prompts for user query input.
    """
    while True:
        try:
            if example.counter == 0:
                question = example.text_intake("What would you like to know about Code Fellows? \n")
            else:
                question = example.text_intake("What else would you like to know about Code Fellows? \n")

            if question == 'quit' or question == 'q':
                example.print_text_output("\nThanks for using our app!  Hope to see you at Code Fellows soon!\n")
                quit()
            else:
                pol_debug_test(question)
            #     CaptureInput(question)
        except KeyboardInterrupt:
            example.print_text_output("\nThanks for using our app!  Hope to see you at Code Fellows soon!\n")
            exit()

class CaptureInput:
    """
    Capture command-line input in text form and post it to the server.
    """
    def __init__(self, input_mode="text"):
        self.input_mode = input_mode

    def capture_text_input(self):
        if self.input_mode == "text":
            pass
            
# ***********************************************************
# Lee's content
# ***********************************************************

# def voice_input_fn():
#   audio_file = some_fancyness()
#   return audio_file

# input_type =  input("voice or text?")





# class Input:
#   def __init__(self, input_type = "text"):
#     self.input_type = input_type
#   def accept_input(self):
#     if self.input_type == "text":
#       holder = console_receive_input()
#     return holder

# user_session = Input()
# user_session.accept_input()


# ditto = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

# print(ditto.json()["abilities"][0]["ability"])

# body = {
#   "message": "How long is javascript 401?"
# }
# response = requests.post(flask_server_url, body=body)



def main():
    welcome_message()
    query_prompt()

if __name__ == "__main__":
    # pol_debug_test()
    # welcome_message()
    # query_prompt()
    main()


