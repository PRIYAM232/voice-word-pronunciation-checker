import speech_recognition as sr
from difflib import SequenceMatcher
import json
from typing import List, Tuple
import sys

class VoiceWordChecker:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.target_words = []
        self.spoken_words = []
        self.correct_words = []
        self.incorrect_words = []
        
    def get_target_words(self) -> List[str]:
        """Get target words from user input"""
        print("\n=== Target Word Input ===")
        print("Enter target words (comma-separated):")
        print("Example: apple, banana, orange, grape")
        
        words_input = input("\nYour words: ").strip()
        self.target_words = [word.strip().lower() for word in words_input.split(',') if word.strip()]
        
        print(f"\n✓ Loaded {len(self.target_words)} target words")
        return self.target_words
    
    def similarity_score(self, word1: str, word2: str) -> float:
        """Calculate similarity between two words (0-1 scale)"""
        return SequenceMatcher(None, word1.lower(), word2.lower()).ratio()
    
    def get_microphone_list(self):
        """List available microphones"""
        print("\n=== Available Microphones ===")
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print(f"{index}: {name}")
    
    def record_voice(self) -> str:
        """Record voice and convert to text"""
        print("\n=== Voice Recording ===")
        
        # Check if PyAudio is available
        try:
            import pyaudio
            has_pyaudio = True
        except ImportError:
            has_pyaudio = False
        
        if not has_pyaudio:
            print("⚠️  PyAudio is not installed - Microphone recording not available")
            print("\n📁 Using Audio File Mode instead")
            print("\nYou can:")
            print("1. Record audio using Windows Voice Recorder")
            print("2. Save as WAV file")
            print("3. Provide the file path below")
            return self.record_from_file()
        
        print("Preparing to record...")
        
        try:
            # Try to get default microphone
            with sr.Microphone() as source:
                print("Adjusting for ambient noise... Please wait.")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                print("\n🎤 Recording started! Please speak the words clearly.")
                print("(Recording will automatically stop after you finish speaking)\n")
                
                try:
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)
                    print("✓ Recording complete! Processing...")
                    
                    # Convert speech to text using Google
                    text = self.recognizer.recognize_google(audio)
                    print(f"\nTranscribed text: \"{text}\"")
                    return text
                    
                except sr.WaitTimeoutError:
                    print("❌ No speech detected. Please try again.")
                    return ""
                except sr.UnknownValueError:
                    print("❌ Could not understand the audio. Please try again.")
                    return ""
                except sr.RequestError as e:
                    print(f"❌ Could not request results from speech recognition service: {e}")
                    print("Make sure you have an active internet connection.")
                    return ""
                    
        except (OSError, AttributeError) as e:
            print(f"\n❌ Microphone Error: {e}")
            print("\nTroubleshooting:")
            print("1. Make sure a microphone is connected")
            print("2. Grant microphone permissions to Python")
            print("3. Try using an audio file instead (see alternative method below)")
            
            # Offer alternative method
            print("\n=== Alternative: Use Audio File ===")
            choice = input("Would you like to use an audio file instead? (y/n): ").strip().lower()
            if choice == 'y':
                return self.record_from_file()
            return ""
    
    def record_from_file(self) -> str:
        """Process audio from a file"""
        print("\nSupported formats: WAV, AIFF, FLAC")
        file_path = input("Enter the path to your audio file: ").strip().strip('"')
        
        try:
            with sr.AudioFile(file_path) as source:
                print("Processing audio file...")
                audio = self.recognizer.record(source)
                
                print("Converting speech to text...")
                text = self.recognizer.recognize_google(audio)
                print(f"\nTranscribed text: \"{text}\"")
                return text
                
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
            return ""
        except Exception as e:
            print(f"❌ Error processing audio file: {e}")
            return ""
    
    def extract_spoken_words(self, transcribed_text: str) -> List[str]:
        """Extract individual words from transcribed text"""
        # Remove punctuation and split into words
        words = transcribed_text.lower().replace(',', ' ').replace('.', ' ').split()
        self.spoken_words = [word.strip() for word in words if word.strip()]
        return self.spoken_words
    
    def compare_words(self, similarity_threshold: float = 0.8) -> Tuple[List[str], List[str]]:
        """
        Compare spoken words with target words
        Returns: (correct_words, incorrect_words)
        """
        self.correct_words = []
        self.incorrect_words = []
        matched_spoken_words = set()
        
        # For each target word, find best match in spoken words
        for target_word in self.target_words:
            best_match = None
            best_score = 0
            best_index = -1
            
            for idx, spoken_word in enumerate(self.spoken_words):
                if idx in matched_spoken_words:
                    continue
                    
                score = self.similarity_score(target_word, spoken_word)
                if score > best_score:
                    best_score = score
                    best_match = spoken_word
                    best_index = idx
            
            # Check if match is good enough
            if best_score >= similarity_threshold:
                self.correct_words.append(target_word)
                if best_index != -1:
                    matched_spoken_words.add(best_index)
            else:
                self.incorrect_words.append(target_word)
        
        return self.correct_words, self.incorrect_words
    
    def display_results(self):
        """Display detailed results"""
        print("\n" + "="*60)
        print("                    RESULTS SUMMARY")
        print("="*60)
        
        print("\n📋 TARGET WORDS:")
        print("   " + ", ".join(self.target_words))
        
        print("\n🎤 SPOKEN WORDS (Transcribed):")
        print("   " + ", ".join(self.spoken_words) if self.spoken_words else "   (none detected)")
        
        print("\n✅ CORRECTLY SPOKEN WORDS:")
        if self.correct_words:
            print("   " + ", ".join(self.correct_words))
        else:
            print("   (none)")
        
        print("\n❌ INCORRECTLY SPOKEN / MISSING WORDS:")
        if self.incorrect_words:
            print("   " + ", ".join(self.incorrect_words))
        else:
            print("   (none)")
        
        print("\n📊 STATISTICS:")
        total_target = len(self.target_words)
        correct_count = len(self.correct_words)
        percentage = (correct_count / total_target * 100) if total_target > 0 else 0
        
        print(f"   Correctly Spoken: {correct_count} / {total_target} words")
        print(f"   Accuracy: {percentage:.1f}%")
        
        print("\n" + "="*60)
    
    def save_results(self, filename: str = "results.json"):
        """Save results to a JSON file"""
        results = {
            "target_words": self.target_words,
            "spoken_words": self.spoken_words,
            "correct_words": self.correct_words,
            "incorrect_words": self.incorrect_words,
            "statistics": {
                "total_target_words": len(self.target_words),
                "correctly_spoken": len(self.correct_words),
                "incorrectly_spoken": len(self.incorrect_words),
                "accuracy_percentage": (len(self.correct_words) / len(self.target_words) * 100) 
                                      if len(self.target_words) > 0 else 0
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n💾 Results saved to '{filename}'")
    
    def run(self):
        """Main application flow"""
        print("="*60)
        print("         VOICE WORD PRONUNCIATION CHECKER")
        print("="*60)
        
        # Step 1: Get target words
        self.get_target_words()
        
        if not self.target_words:
            print("❌ No target words provided. Exiting.")
            return
        
        # Step 2: Record voice
        input("\nPress Enter when ready to record...")
        transcribed_text = self.record_voice()
        
        if not transcribed_text:
            print("❌ No speech was recognized. Exiting.")
            return
        
        # Step 3: Extract spoken words
        self.extract_spoken_words(transcribed_text)
        
        # Step 4: Compare words
        print("\n🔍 Analyzing pronunciation...")
        self.compare_words(similarity_threshold=0.8)
        
        # Step 5: Display results
        self.display_results()
        
        # Step 6: Save results
        save_option = input("\nWould you like to save the results? (y/n): ").strip().lower()
        if save_option == 'y':
            filename = input("Enter filename (default: results.json): ").strip()
            if not filename:
                filename = "results.json"
            self.save_results(filename)


def main():
    """Entry point of the application"""
    try:
        # Check if PyAudio is available
        try:
            import pyaudio
            print("✓ PyAudio detected - Microphone support enabled")
        except ImportError:
            print("⚠️  PyAudio not installed - Limited microphone support")
            print("   You can still use audio files for input\n")
        
        checker = VoiceWordChecker()
        checker.run()
        
        # Option to run again
        print("\n" + "="*60)
        again = input("Would you like to check more words? (y/n): ").strip().lower()
        if again == 'y':
            main()
        else:
            print("\nThank you for using Voice Word Pronunciation Checker! 👋")
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Application interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
