# 🎤 Voice Word Pronunciation Checker

A web-based and Python application that records your voice, transcribes it using speech recognition, and compares the spoken words against a target list to evaluate pronunciation accuracy.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)

## ✨ Features

- 🎙️ **Voice Recording** - Live microphone input or audio file processing
- 🔊 **Speech-to-Text** - Automatic transcription using Google Speech Recognition
- 🎯 **Smart Matching** - Fuzzy word matching with 80% similarity threshold
- 📊 **Detailed Results** - Shows correct/incorrect words with statistics
- 🌐 **Web Version** - Browser-based interface with no installation required
- 💾 **Export Results** - Save results to JSON format
- 🖥️ **Cross-Platform** - Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Option 1: Web Version (Recommended)

The easiest way to use this tool - no installation required!

1. Download or clone this repository
2. Open `voice_checker_web.html` in your browser (Chrome, Edge, or Safari)
3. Enter your target words
4. Click "Start Recording" and speak
5. View instant results!

**Requirements:**
- Modern web browser (Chrome, Edge, or Safari)
- Microphone
- Internet connection

### Option 2: Python Version

For audio file processing or command-line usage.

```bash
# Install dependencies
pip install -r requirements_simple.txt

# Run the application
python voice_word_checker_simple.py
```

**Requirements:**
- Python 3.7+
- Internet connection
- Microphone (optional - can use audio files)

## 📋 Usage

### Web Version

1. Open `voice_checker_web.html` in your browser
2. Enter target words separated by commas (e.g., `apple, banana, orange`)
3. Click "Start Recording" and allow microphone access
4. Speak the words clearly
5. View your results with accuracy statistics

### Python Version

```bash
python voice_word_checker_simple.py
```

1. Enter your target words when prompted
2. Press Enter to start recording
3. Provide an audio file path (WAV, FLAC, or AIFF format)
4. View detailed results in the terminal
5. Optionally save results to JSON

## 📊 Example Output

```
============================================================
                    RESULTS SUMMARY
============================================================

📋 TARGET WORDS:
   apple, banana, orange, grape

🎤 SPOKEN WORDS (Transcribed):
   apple, banana, orange, grape

✅ CORRECTLY SPOKEN WORDS:
   apple, banana, orange, grape

❌ INCORRECTLY SPOKEN / MISSING WORDS:
   (none)

📊 STATISTICS:
   Correctly Spoken: 4 / 4 words
   Accuracy: 100.0%

============================================================
```

## 🛠️ Installation

### Web Version

No installation needed! Just open the HTML file in a supported browser.

### Python Version

#### Basic Installation (Audio File Support Only)

```bash
pip install -r requirements_simple.txt
```

#### Full Installation (With Microphone Support)

For microphone recording in Python, you'll need PyAudio:

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-pyaudio portaudio19-dev
pip install pyaudio
```

## 📁 Project Structure

```
voice-word-pronunciation-checker/
├── voice_checker_web.html          # Web version (recommended)
├── voice_word_checker_simple.py    # Python version
├── requirements_simple.txt         # Python dependencies
├── README.md                       # This file
├── LICENSE                         # MIT License
├── QUICK_START.md                  # Detailed usage guide
├── HOW_TO_RECORD_AUDIO.md         # Audio recording tutorial
└── INSTALLATION_GUIDE.md          # Setup instructions
```

## 🎯 How It Works

1. **Speech Recognition**: Uses Google's Speech Recognition API or browser's Web Speech API
2. **Word Extraction**: Parses transcribed text into individual words
3. **Smart Matching**: Uses Levenshtein distance algorithm for fuzzy matching
4. **Similarity Threshold**: 80% similarity required for correct match
5. **Results Display**: Comprehensive feedback with statistics

## 🔧 Configuration

Adjust the similarity threshold in the code:

**Python Version:**
```python
self.compare_words(similarity_threshold=0.8)  # 0.0 to 1.0
```

**Web Version:**
```javascript
if (bestScore >= 0.8) {  // Change 0.8 to your preferred value
```

- `1.0` = Exact match required
- `0.8` = 80% similarity (default, recommended)
- `0.6` = More lenient matching

## 🌐 Browser Compatibility

| Browser | Web Version Support |
|---------|-------------------|
| Chrome  | ✅ Full support   |
| Edge    | ✅ Full support   |
| Safari  | ✅ Full support   |
| Firefox | ❌ Not supported  |

## 📝 Audio File Formats

### Supported (Python Version)
- WAV ✅
- FLAC ✅
- AIFF ✅

### Not Supported
- MP3 ❌ (convert to WAV)
- M4A ❌ (convert to WAV)
- OGG ❌ (convert to WAV)

Use [online-audio-converter.com](https://online-audio-converter.com/) to convert unsupported formats.

## 🐛 Troubleshooting

### Web Version

**Microphone not working:**
- Check browser permissions (click 🔒 in address bar)
- Use Chrome, Edge, or Safari (Firefox not supported)
- Ensure microphone is connected and set as default

**No speech detected:**
- Speak louder and more clearly
- Reduce background noise
- Check microphone volume in system settings

### Python Version

**PyAudio installation fails:**
- Use the web version instead (recommended)
- Or use audio file input mode (no PyAudio needed)
- See INSTALLATION_GUIDE.md for platform-specific instructions

**Audio file error:**
- Convert to WAV format
- Check file path is correct
- Ensure file isn't corrupted

## 💡 Tips for Best Results

1. **Speak clearly** - Enunciate each word
2. **Moderate pace** - Don't rush or speak too slowly
3. **Quiet environment** - Minimize background noise
4. **Good microphone** - Use quality audio input
5. **Proper distance** - 6-12 inches from microphone
6. **Internet connection** - Required for speech recognition

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Speech Recognition API
- Web Speech API
- SpeechRecognition Python library

## 📧 Support

If you encounter any issues or have questions:
- Check the [QUICK_START.md](QUICK_START.md) guide
- Read [TROUBLESHOOTING.md](INSTALLATION_GUIDE.md)
- Open an issue on GitHub

## 🔮 Future Enhancements

- [ ] Offline speech recognition
- [ ] Multiple language support
- [ ] Pronunciation feedback with phonetics
- [ ] Progress tracking over time
- [ ] Mobile app version
- [ ] Real-time pronunciation scoring

---

**Made with ❤️ for language learners and pronunciation practice**

⭐ If you find this helpful, please star the repository!
