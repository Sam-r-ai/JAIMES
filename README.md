# JAIMES
Continuous voice command chatGPT on a Raspberry Pi (better version of Alexa)

Steps involved:
1: Setup Raspberry Pi 4 -> 2: Download Python Libraries -> 3: Get chatGPT API Key -> 4: Write the script -> Run.

1) Setting up Raspberry Pi 4
   -Image the newest version of PiOS onto your Raspberry Pi, then power up and go through booting, you will then need to download some 
    configurations. We will need to install libraries to interact with chatGPT
   -Run update commands in terminal:
     ->sudo apt update
     ->sudo apt upgrade
     (Python comes preinstalled with Raspbian)
3) Download Libraries for Python Scripts: (2 methods: A, B, *C)
   2.A:If this doesn't work because Error: "externally managed environment" go to 2.B
     ->sudo apt-get install python3-pip
     ->sudo apt install python3-dotenv                 OR (python3 -m pip install python-dotenv) 
     ->sudo apt install                       OR pip3 install openai dotenv SpeechRecognition pyttsx3 gtts PyAudio
     ->                                                OR sudo apt install python3-pyaudio flac python3-espeak espeak python3-dotenv
     ->                                                OR pip uninstall dotenv
     ->                                                ORpip install python-dotenv
   
    2.B)If 1.1 did not work, we will download libraries through virtual environment
***The error "externally managed environment" when trying to install a Python package on a Raspberry Pi (or similar Linux systems)   indicates that the system's package manager, rather than pip, is managing the Python environment. This is a common scenario in many Linux distributions where Python packages are installed and managed system-wide by tools like apt. 
   2.*C This method is not the recommended way as it can cause issues. We will use --break-system-packages to download Python libraries
   
We will use: sudo apt to install:
             sudo apt install python3-dotenv 
             sudo apt install <install instructions>
**
