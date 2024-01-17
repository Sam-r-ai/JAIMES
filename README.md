# JAIMES

***Voice-Activated Personal Assistant using OpenAI and Raspberry Pi***

#### **Improvements to do:** 

- [ ] THREADING: to improve responsiveness because pyttsx3 blocks program from running until it finishes. There is about a 2 second delay after wake word is acknowledged before you can ask a question to send to openai api

#### Hardware requirements:

- Raspberry pi 
- Microphone for raspberry pi
- Speaker for raspberry pi
- Openai API key ("https://platform.openai.com/apps")
- Python 3.10.1

***This can run locally on a machine*** with python 3.10.1. ***Anything above python 3.10.1 will need to follow the advanced instructions*** where we edit \__init__ file for speechrecognition

### Instructions:

If running locally with system using Python 12+ follow instructions **A**

If running locally (windows, mac, linux computer) follow instruction **B**

If running on **Raspberry Pi**, follow instruction **C**



### (A) Running on system with Python 3.12+

Python 3.12 + has changed it's method of installing packages; removing distutils and using setuptools instead, so we have to edit the \__init__ file of Speechrecognition for this to work. It is pretty simple.

Look into the Python file, install the requirements given in the comments.

After installing Speechrecognition, find where *Speechrecognition* is located, and edit the \__init__ file using vim/nano/vscode etc.

Find its get_pyaudio() function, and replace it with the following code:

    @staticmethod
    def get_pyaudio():
        """
        Imports the pyaudio module and checks its version. Throws exceptions if pyaudio can't be found or a wrong version is installed
        """
        try:
            import pyaudio
        except ImportError:
            raise AttributeError("Could not find PyAudio; check installation")
        from packaging.version import parse as parse_version
        if parse_version(pyaudio.__version__) < parse_version("0.2.11"):
            raise AttributeError("PyAudio 0.2.11 or later is required (found version {})".format(pyaudio.__version__))
        return pyaudio

Now it will work. You can run the python code by copy and pasting, or cloning it from github.

### (B) Running on system with Python 3.10.1 

The *Speechrecognition* Library is made to support versions of Python 3.10.1. 

I suggest you create a virtual environment of Python 3.10.1

Download Python 3.10.1: (https://www.python.org/downloads/release/python-3101/)

Open a virtual environment using Python 3.10.1, and use the Python code and run the program. Follow all library installs from comments


### (C) Running on Raspberry Pi
Setup Raspberry Pi 4 -> 2: Download Python Libraries -> 3: Get chatGPT API Key -> 4: Write the script -> Run.

1) Setting up Raspberry Pi 4
   
   -Image the newest version of PiOS onto your Raspberry Pi, then power up and go through booting, you will then need to download some
   
    configurations. We will need to install libraries to interact with chatGPT
   
   -Run update commands in terminal:
   
     ->sudo apt update
   
     ->sudo apt upgrade
   
     (Python comes preinstalled with RaspbianOS)
   
2) Download Libraries for Python Scripts: (3 methods: A, B, *C)
   
   2.A:If this doesn't work because Error: "externally managed environment" go to 2.B
   
     ->sudo apt-get install python3-pip
   
     ->python3 -m pip install python-dotenv
   
     ->pip3 install openai dotenv SpeechRecognition pyttsx3 gtts PyAudio
   
     ->sudo apt install python3-pyaudio flac python3-espeak espeak python3-dotenv
   
     ->pip uninstall dotenv
   
     ->pip install python-dotenv
   
    2.B)If 1.1 did not work, we will download libraries through virtual environment.
   
   You might have seen the error code:
   
    ***The error "externally managed environment" when trying to install a Python package on a Raspberry Pi (or similar Linux systems)   indicates that the system's package manager,          rather than pip, is managing the Python environment. This is a common scenario in many Linux distributions where Python packages are installed and managed system-wide by tools like       apt.
      We will open the Python virtual environment:
      ->sudo apt-get install python3-venv
      ->sudo apt-get install python3-pip
      ->sudo apt install python3-dotenv
      Open the virtual environment
      ->python3 -m venv myenv
      ->source myenv/bin/activate
      ->sudo apt-get update
      ->pip3 install numpy
      ->python3 -m pip install python-dotenv
      ->sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev python3-pyaudio
      ->pip install openai python-dotenv SpeechRecognition pyttsx3 gtts PyAudio
      ->sudo apt install python3-pyaudio flac python3-espeak espeak python3-dotenv
      
   2.*C This method is not the recommended way as it can cause issues. We will use --break-system-packages to download Python libraries
   

3)Getting your API keys
   ->Go to openai API (https://platform.openai.com/apps)
   ->Login and on the lefthand side of your screen, go to API keys
   ->Click 'Create new secret key'
   ->Copy the key and paste it somewhere (for use later)

4)Writing the python script
   ->Copy and paste the python script
   ->Put your api key into openai.api_key= 'HERE'
   ->Change "NAME" to your name
   ->Run


