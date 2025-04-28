Here's the updated README.md with the gTTS module instead of pyttsx3:

# � Vocalize Pro - Text to Speech Converter

![Vocalize Pro Screenshot](/assets/image.png) 

## 🌟 Introduction

Vocalize Pro is an ultra-modern, visually stunning text-to-speech application that transforms written text into natural sounding speech. With its beautiful interface, engaging animations, and high-quality voice synthesis using Google's Text-to-Speech API, it provides an exceptional user experience for converting text to audio.

## ✨ Features

- 🌍 Multiple language support (via gTTS)
- 🎭 Various voice accents and styles
- 🏎️ Adjustable speech speed (slow/normal/fast)
- ✨ Beautiful modern UI with animations
- 🎉 Celebration effects on successful conversion
- 📋 Sample text buttons for quick testing
- 🎙️ MP3 audio generation and playback
- 📱 Fully responsive design

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Text-to-Speech Engine**: gTTS (Google Text-to-Speech)
- **Audio Playback**: IPython.display.Audio
- **UI Enhancements**: streamlit-extras
- **Styling**: Custom CSS with animations

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/muzaffar401/Vocalize_Pro.git
   cd Vocalize_Pro
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run main.py
   ```

## 🏗️ Project Structure

```
vocalize-pro/
├── main.py                # Main application file
├── requirements.txt      # Dependencies file
├── README.md             # Project documentation
└── assets/               # For storing images and audio files
```

## 🔧 How It Works

### 🧩 Core Components

1. **Text Input Module**:
   - Provides a large text area for user input
   - Includes placeholder text with examples
   - Clear button to reset the input

2. **Language Settings Module**:
   - Language selection dropdown (English, Spanish, French, etc.)
   - Speech speed selection (slow/normal/fast)
   - Settings are preserved during session

3. **Sample Text Module**:
   - Quick-insert buttons for common phrases
   - Each button has a helpful tooltip
   - Sample text includes greetings in different languages

4. **Speech Generation Module**:
   - Converts text to speech using gTTS
   - Generates MP3 files for playback
   - Shows progress during conversion
   - Displays audio player for output

5. **UI/UX Enhancements**:
   - Animated buttons and elements
   - Success celebrations with confetti
   - Smooth transitions between states

### 🔄 Workflow

1. **User Input**:
   - User enters text in the input area or selects a sample
   - Selects language and speed preferences

2. **Speech Generation**:
   - User clicks "Convert to Speech" button
   - System validates input (shows error if empty)
   - gTTS generates MP3 audio file

3. **Audio Output**:
   - Audio player appears for playback
   - Success message appears with optional celebration
   - Temporary MP3 file is created (can be downloaded)

4. **Feedback Loop**:
   - User can adjust settings and regenerate
   - Clear button resets the input
   - Sample buttons provide quick new content

## 📝 Code Explanation

### � Main Function (`main()`)

1. **Initialization**:
   - Sets up page configuration
   - Applies custom CSS styles
   - Initializes session state

2. **UI Layout**:
   - Creates two main columns (3:1 ratio)
   - Left column for text input/output
   - Right column for settings and samples

3. **Event Handling**:
   - Button click handlers
   - Text input validation
   - Audio file generation and cleanup

### 🔊 Speech Engine (gTTS Integration)

1. **Audio Generation**:
   - Uses gTTS to convert text to speech
   - Supports multiple languages
   - Adjusts speech speed (slow/normal/fast)

2. **Playback**:
   - Saves temporary MP3 file
   - Uses IPython.display.Audio for playback
   - Handles file cleanup after session

3. **Error Handling**:
   - Manages API limitations
   - Handles invalid text inputs
   - Provides user feedback

## 🌈 UI/UX Highlights

- **Animated Elements**:
  - Floating emojis
  - Pulsing buttons
  - Bouncing success indicators

- **Visual Feedback**:
  - Progress indicators
  - Success/error messages
  - Celebration effects

- **Responsive Design**:
  - Works on different screen sizes
  - Adaptive layouts
  - Mobile-friendly components

## 📜 License

MIT License - Free for personal and commercial use

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Google for the gTTS library
- Open source community for inspiration

Key changes made:
- Replaced pyttsx3 references with gTTS
- Updated features to reflect gTTS capabilities (languages instead of genders)
- Modified the speech engine explanation
- Added MP3 file handling details
- Updated the workflow to reflect gTTS's file-based approach
- Kept all the UI/UX elements that aren't engine-dependent