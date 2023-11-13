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
2) Download Libraries for Python Scripts: (3 methods: A, B, *C)
   2.A:If this doesn't work because Error: "externally managed environment" go to 2.B
     ->sudo apt-get install python3-pip
     ->python3 -m pip install python-dotenv
     ->pip3 install openai dotenv SpeechRecognition pyttsx3 gtts PyAudio
     ->sudo apt install python3-pyaudio flac python3-espeak espeak python3-dotenv
     ->pip uninstall dotenv
     ->pip install python-dotenv
   
    2.B)If 1.1 did not work, we will download libraries through virtual environment. You might have seen the error code:
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
