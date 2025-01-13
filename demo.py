import speech_recognition as sr
import pyttsx3
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.system_program import TransferParams, transfer


engine = pyttsx3.init()


client = Client("https://api.devnet.solana.com")


def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the command. Please try again.")
        return None
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return None


def execute_transaction():
    sender_keypair = Keypair.from_secret_key(bytes([42] * 64))  
    recipient_address = "RecipientWalletPublicKeyHere"  
    amount = 1000000  

    transfer_transaction = transfer(
        TransferParams(
            from_pubkey=sender_keypair.public_key,
            to_pubkey=recipient_address,
            lamports=amount,
        )
    )

    
    transaction = client.send_transaction(transfer_transaction, sender_keypair)
    print(f"Transaction sent: {transaction['result']}")


def process_command(command):
    if "send" in command and "tokens" in command:
        print("Sending tokens...")
        engine.say("Sending tokens...")
        engine.runAndWait()
        execute_transaction()
    else:
        print("Sorry, I didn't understand the command.")
        engine.say("Sorry, I didn't understand the command.")
        engine.runAndWait()


def main():
    while True:
        command = listen_for_command()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
