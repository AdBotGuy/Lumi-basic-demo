Lumi: Solana Voice Assistant Demo
This is a demo of Lumi, a voice-activated assistant for Solana blockchain interactions. With Lumi, you can execute basic blockchain transactions like sending tokens through simple voice commands.

Demo Features
Voice Command Interaction: Listen for commands like "Send tokens."
Solana Blockchain Integration: Executes token transfer transactions using Solana.
Text-to-Speech Feedback: Lumi responds to your commands with spoken feedback.
Requirements
Python 3.x
Install the required libraries:
bash
Copy code
pip install speechrecognition solana pyttsx3
Setup & Running the Demo
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/lumi.git
cd lumi
Install the dependencies:

bash
Copy code
pip install speechrecognition solana pyttsx3
Replace the recipient wallet public key in the execute_transaction function with a real Solana public key.

Run the demo:

bash
Copy code
python lumi_demo.py
Speak simple commands such as:

"Send tokens"
"Check balance" (future feature)
Example Output:
Command: "Send tokens"
Lumi: "Sending tokens..."
The demo will execute a token transfer (using Solana devnet).

License
This project is licensed under the MIT License.
