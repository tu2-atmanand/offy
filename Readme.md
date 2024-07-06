## Offy: An Offline AI Assistant and Chatbot

![ReadmeDiagrams.png](Assets/ReadmeDiagrams.png)

### Overview

Offy is an offline AI assistant and chatbot designed to provide a friendly and convenient way to interact with your computer. It leverages speech recognition and text-to-speech capabilities to allow for natural conversation-like interactions. Unlike traditional voice assistants, Offy keeps your conversations private by functioning entirely offline. 

This project is ideal for users who:

* Value privacy and security.
* Desire a seamless and continuous conversation experience.
* Seek a basic assistant for tasks like opening applications or searching the web.

**Key Features:**

* **Offline Functionality:**  Enjoy complete privacy and avoid reliance on internet connectivity. 
* **Continuous Conversation:** Interact with Offy like a real friend without the need for constant wake words.
* **Assistant Capabilities:** Offy can assist with basic tasks like opening applications and searching the web (requires internet connection).


### Motivation

The inspiration for Offy came from the desire to create a more private and user-friendly alternative to existing voice assistants. By removing the dependency on online services, Offy empowers users to control their data and enjoy a more natural conversation flow. 

The development process presented interesting challenges, such as balancing offline capabilities with providing helpful functionalities. 


### Architecture

Offy is built upon three core components:

1. **Speech Recognition:** This module converts spoken language into text. Offy utilizes the pre-built model from the Vosk project ([https://github.com/topics/vosk](https://github.com/topics/vosk)) to capture and translate audio input from your microphone. (See the [Speech Recognition](https://github.com/tu2-atmanand/Speech_Recognition) project for details)

2. **AI Bot:** This is the brain of Offy, responsible for understanding your requests and generating responses. It utilizes a machine learning model, details of which can be found in the separate [Offy-Brain](https://github.com/tu2-atmanand/Offy-Brain) project.

3. **Text-To-Speech:** This module converts the AI Bot's responses back into spoken language for you to hear. Refer to the [Text_To_Speech](https://github.com/tu2-atmanand/Text_To_Speech) project for more information.

A "divide and conquer" approach was employed to break down the project into smaller, manageable subprojects. This facilitated efficient development and modularity. 


### How to Run

**Prerequisites:**

* Operating System: Compatible with most major operating systems (Windows, macOS, Linux)
* Python: Version 3.8 or later

**Instructions:**

1. Install Python 3.8 if you haven't already.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:

   ```bash
   python main.py
   ```


### TODO

* Integrate functionalities to enable Offy to perform basic tasks on your computer.
* Develop a graphical user interface (GUI) for a more user-friendly experience.


### Future Ideas

* Enhanced Memory : Enhance Offy's AI capabilities to remember past conversations and tailor responses accordingly. This could involve utilizing database storage or exploring advanced neural network architectures.
* Integrate GPT models : Incorporate GPT technology for more advanced and nuanced responses, which should feel more like human.

### Contributing

We welcome contributions from the community! If you'd like to contribute to the project, please review the code style conventions and submit pull requests according to our guidelines.


### License

This project is licensed under the terms of the GNU General Public License (GPL) v3.0. You can find a copy of the license here: https://www.gnu.org/licenses/gpl-3.0.en.html.

In summary, the GPL allows you to freely use, modify, and distribute this software, as long as you adhere to the following conditions:

* You must distribute the source code of any modified version of the software.
* You must distribute the modified software under the same GPL v3.0 license or a compatible license.
* You must include a copy of the GPL license with the software.

We believe the GPL best fosters open source development and collaboration. If you have any questions about the license, feel free to reach out.
