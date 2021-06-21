import os
import sys

# Here we create our virtualenv and activate it
if sys.platform.startswith('win'):
    # needs implementation to activate virtualenv
    pass

else:
    try:
        os.system('python3 -m venv env')
        os.system('source env/bin/activate')
    except:
        print('No virtualenv found: "sudo apt-get install python3-venv" to resolve this issue!')
        exit()

    try:
        # Install all neccesary libaries
        os.system('pip install -r requirements.txt')

        # after build import nltk so we can download punkt from nltk
        import nltk

        nltk.download('punkt')

    except:
        print('no installation of pip found: "sudo apt install python3-pip" to resolve this issue!')
