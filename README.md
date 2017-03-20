# PytchControl
Control your computer through python based pitch detection  

# Explanation
PytchControl allows you to use changes in pitch to control your computer.  
When a series of pitches are detected the change between each pitch is recorded and these changes form a command.  
The three types of changes are:  
+ n - pitch stays the same (within TOLERANCE)  
+ u - pitch increases  
+ d - pitch decreases  
When a command is issued a .bat file will run and an action will occur.  

For example:  
If PytchControl detects three tones of increasing pitch it will create the command 'uu'.  
'uu' is a default command and will run 'web.bat' which opens this github repo.  

#Quickstart guide
1.Ensure you have python 2 installed with numpy and pyaudio
2.Clone the repository
3.Run pytchcontrol.py
4.Whistle three tones of increasing pitch
5.Success! Hopefully at this point this repo will open up in your web browser
