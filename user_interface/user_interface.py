import requests

def pol_debug_test():
    res = requests.post('https://chatbotdevbranch.herokuapp.com/proof_of_life', json={"text":"json test"})
    print(dir(res))

    # if res.ok:
    #     print(res.json())


def welcome_message():
    """
    Display a text prompt to the user to describe intended input.
    """
    print(dedent("""
    Welcome to the Code Fellows chatbot app! 
    Please enter your question about Code Fellows or their course offerings below. \n
    """))

def query_prompt():
    """
    Promts for user query input.
    """
    pass
    # while True:
    # print(dedent("What would you like to know about Code Fellows? \n"))



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
# def console_print_text(text: str) -> None:
#   print(text)

# def console_receive_input() -> str:
#   output = input("Ask the computer a question")
#   return output

# def some_fancyness():
#   pass

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



if __name__ == "__main__":
    pol_debug_test()
