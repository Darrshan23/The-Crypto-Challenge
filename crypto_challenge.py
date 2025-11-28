import random
import string
from cryptography.fernet import Fernet
import base64
import hashlib
from itertools import cycle

class CryptoChallenge:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.fernet_key = Fernet.generate_key()
        self.fernet = Fernet(self.fernet_key)
        
    def clear_screen(self):
        print("\n" * 50)
        
    def display_header(self):
        print("=" * 60)
        print("           🛡️  CYBERSECURITY CRYPTO CHALLENGE 🛡️")
        print("=" * 60)
        print(f"Level: {self.level} | Score: {self.score}")
        print("-" * 60)
        
    def caesar_cipher(self, text, shift, encrypt=True):
        result = ""
        for char in text:
            if char.isalpha():
                shift_amount = shift if encrypt else -shift
                if char.isupper():
                    result += chr((ord(char) - 65 + shift_amount) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + shift_amount) % 26 + 97)
            else:
                result += char
        return result
    
    def vigenere_cipher(self, text, key, encrypt=True):
        result = ""
        key_cycle = cycle(key.upper())
        for char in text:
            if char.isalpha():
                key_char = next(key_cycle)
                shift = ord(key_char) - 65
                if not encrypt:
                    shift = -shift
                
                if char.isupper():
                    result += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += char
        return result
    
    def base64_encode(self, text):
        return base64.b64encode(text.encode()).decode()
    
    def base64_decode(self, text):
        return base64.b64decode(text.encode()).decode()
    
    def xor_cipher(self, text, key):
        result = ""
        key_cycle = cycle(key)
        for char in text:
            result += chr(ord(char) ^ ord(next(key_cycle)))
        return result
    
    def level_1_caesar(self):
        """Level 1: Caesar Cipher"""
        messages = [
            "HELLO CYBER SECURITY",
            "PYTHON IS AWESOME",
            "CRYPTOGRAPHY IS FUN",
            "PROTECT YOUR DATA",
            "STAY SECURE ONLINE"
        ]
        message = random.choice(messages)
        shift = random.randint(1, 10)
        encrypted = self.caesar_cipher(message, shift)
        
        print("🔐 LEVEL 1: CAESAR CIPHER")
        print("Decrypt this message using Caesar cipher:")
        print(f"Encrypted: {encrypted}")
        print("Hint: Each letter is shifted by a fixed number of positions")
        
        try:
            guess = input("\nYour decryption: ").strip().upper()
            if guess == message:
                print("✅ Correct! Well done!")
                self.score += 10
                return True
            else:
                print(f"❌ Incorrect. The message was: {message}")
                print(f"Shift was: {shift}")
                return False
        except:
            return False
    
    def level_2_vigenere(self):
        """Level 2: Vigenère Cipher"""
        messages = [
            "ATTACK AT DAWN",
            "MEET ME TONIGHT",
            "SECRET MESSAGE",
            "CODE BREAKER PRO",
            "CYBER DEFENSE"
        ]
        message = random.choice(messages)
        key = "KEY"
        encrypted = self.vigenere_cipher(message, key)
        
        print("🔐 LEVEL 2: VIGENÈRE CIPHER")
        print("Decrypt this message using Vigenère cipher:")
        print(f"Encrypted: {encrypted}")
        print("Hint: The key is 'KEY'")
        
        try:
            guess = input("\nYour decryption: ").strip().upper()
            if guess == message:
                print("✅ Correct! Excellent work!")
                self.score += 20
                return True
            else:
                print(f"❌ Incorrect. The message was: {message}")
                return False
        except:
            return False
    
    def level_3_base64(self):
        """Level 3: Base64 Encoding"""
        messages = [
            "BASE64 ENCODING",
            "DECODE THIS TEXT",
            "CYBERSECURITY 101",
            "PYTHON PROGRAMMING",
            "HASH FUNCTIONS"
        ]
        message = random.choice(messages)
        encoded = self.base64_encode(message)
        
        print("🔐 LEVEL 3: BASE64 DECODING")
        print("Decode this Base64 encoded message:")
        print(f"Encoded: {encoded}")
        
        try:
            guess = input("\nYour decoding: ").strip().upper()
            if guess == message:
                print("✅ Correct! Great decoding skills!")
                self.score += 15
                return True
            else:
                print(f"❌ Incorrect. The message was: {message}")
                return False
        except:
            return False
    
    def level_4_xor(self):
        """Level 4: XOR Cipher"""
        messages = [
            "XOR CIPHER",
            "BITWISE MAGIC",
            "SECURE COMMS",
            "BINARY OPERATION",
            "CRYPTO MASTER"
        ]
        message = random.choice(messages)
        key = "SECRET"
        encrypted = self.xor_cipher(message, key)
        
        print("🔐 LEVEL 4: XOR CIPHER")
        print("Decrypt this XOR encrypted message:")
        print(f"Encrypted (hex): {encrypted.encode().hex()}")
        print("Hint: The key is 'SECRET'")
        
        try:
            guess = input("\nYour decryption: ").strip().upper()
            if guess == message:
                print("✅ Correct! XOR mastery achieved!")
                self.score += 25
                return True
            else:
                print(f"❌ Incorrect. The message was: {message}")
                return False
        except:
            return False
    
    def level_5_fernet(self):
        """Level 5: Fernet (AES) Encryption"""
        messages = [
            "ADVANCED ENCRYPTION",
            "AES IS SECURE",
            "FINAL CHALLENGE",
            "CRYPTO EXPERT",
            "MISSION COMPLETE"
        ]
        message = random.choice(messages)
        encrypted = self.fernet.encrypt(message.encode()).decode()
        
        print("🔐 LEVEL 5: FERNET ENCRYPTION")
        print("This message is encrypted with Fernet (AES):")
        print(f"Encrypted: {encrypted}")
        print("Hint: This uses symmetric key cryptography")
        
        try:
            # For educational purposes, we'll let them try to guess
            # In real scenario, they'd need the key
            print("\nSince this requires the decryption key, let's reveal it:")
            decrypted = self.fernet.decrypt(encrypted.encode()).decode()
            print(f"Decrypted message: {decrypted}")
            
            confirm = input("Did you understand how Fernet encryption works? (y/n): ").lower()
            if confirm == 'y':
                print("✅ Great! You've completed the advanced level!")
                self.score += 30
                return True
            else:
                print("ℹ️  Fernet provides secure symmetric encryption using AES.")
                self.score += 20
                return True
        except:
            return False
    
    def bonus_crypto_quiz(self):
        """Bonus round: Cryptography knowledge quiz"""
        questions = [
            {
                "question": "What is the main weakness of Caesar cipher?",
                "options": ["A) Too slow", "B) Limited keyspace", "C) Uses too much memory", "D) Requires internet"],
                "answer": "B"
            },
            {
                "question": "Which cipher uses multiple Caesar ciphers with different shifts?",
                "options": ["A) XOR cipher", "B) Vigenère cipher", "C) Base64", "D) Fernet"],
                "answer": "B"
            },
            {
                "question": "What does Base64 encoding primarily do?",
                "options": ["A) Encrypt data", "B) Compress data", "C) Encode binary as text", "D) Hash passwords"],
                "answer": "C"
            },
            {
                "question": "Which is considered the most secure method here?",
                "options": ["A) Caesar cipher", "B) Vigenère cipher", "C) XOR cipher", "D) Fernet (AES)"],
                "answer": "D"
            }
        ]
        
        print("🎯 BONUS ROUND: CRYPTOGRAPHY QUIZ")
        print("Answer these questions to earn extra points!")
        
        correct_answers = 0
        for i, q in enumerate(questions, 1):
            print(f"\nQ{i}: {q['question']}")
            for option in q['options']:
                print(f"  {option}")
            
            answer = input("Your answer (A/B/C/D): ").upper().strip()
            if answer == q['answer']:
                print("✅ Correct!")
                correct_answers += 1
            else:
                print(f"❌ Incorrect. The answer was {q['answer']}")
        
        bonus_points = correct_answers * 10
        self.score += bonus_points
        print(f"\n🎉 You got {correct_answers}/4 correct! +{bonus_points} points!")
        
        return correct_answers > 0
    
    def play_game(self):
        self.clear_screen()
        self.display_header()
        
        print("Welcome to Crypto Challenge!")
        print("Decrypt messages and learn about cryptography techniques.")
        print("Each level introduces a new encryption method.")
        print("\nPress Enter to begin...")
        input()
        
        levels = [
            self.level_1_caesar,
            self.level_2_vigenere,
            self.level_3_base64,
            self.level_4_xor,
            self.level_5_fernet
        ]
        
        for level_func in levels:
            self.clear_screen()
            self.display_header()
            
            success = level_func()
            self.level += 1
            
            print("\n" + "="*50)
            if success:
                print("🎉 Level completed! Moving to next level...")
            else:
                print("💡 Don't worry! Learning from mistakes is part of the process!")
            
            print("Press Enter to continue...")
            input()
        
        # Bonus round
        self.clear_screen()
        self.display_header()
        self.bonus_crypto_quiz()
        
        # Game completion
        self.clear_screen()
        self.display_header()
        print("🎊 CONGRATULATIONS! 🎊")
        print("You've completed all crypto challenges!")
        print(f"Final Score: {self.score}")
        
        if self.score >= 100:
            print("🏆 CRYPTO MASTER - Outstanding performance!")
        elif self.score >= 70:
            print("🥈 CRYPTO EXPERT - Great job!")
        else:
            print("🥉 CRYPTO LEARNER - Keep practicing!")
        
        print("\nCryptography techniques you learned:")
        print("• Caesar Cipher - Simple substitution cipher")
        print("• Vigenère Cipher - Polyalphabetic substitution")
        print("• Base64 Encoding - Binary-to-text encoding")
        print("• XOR Cipher - Bitwise operation cipher")
        print("• Fernet (AES) - Modern symmetric encryption")
        
        print("\nThanks for playing! Stay secure! 🔐")

def main():
    try:
        # Check if required packages are installed
        try:
            from cryptography.fernet import Fernet
        except ImportError:
            print("❌ Required package 'cryptography' is not installed.")
            print("Please install it using: pip install cryptography")
            return
        
        game = CryptoChallenge()
        game.play_game()
        
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()