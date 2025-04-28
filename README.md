# 🎙️ Vocalize Pro - Text to Speech Converter

![Vocalize Pro Screenshot](/assets/image.png) 

## 🌟 Introduction

Vocalize Pro is an ultra-modern, visually stunning text-to-speech application that transforms written text into natural sounding speech. With its beautiful interface, engaging animations, and high-quality voice synthesis, it provides an exceptional user experience for converting text to audio.

## ✨ Features

- 🎭 Multiple voice options (male/female)
- 🏎️ Adjustable speech speed (100-300 WPM)
- ✨ Beautiful modern UI with animations
- 🎉 Celebration effects on successful conversion
- 📋 Sample text buttons for quick testing
- 🎙️ Real-time speech preview
- 📱 Fully responsive design

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Text-to-Speech Engine**: pyttsx3
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
└── assets/               # For storing images
```

## 🔧 How It Works

### 🧩 Core Components

1. **Text Input Module**:
   - Provides a large text area for user input
   - Includes placeholder text with examples
   - Clear button to reset the input

2. **Voice Settings Module**:
   - Gender selection (male/female) with icons
   - Speech rate slider with custom styling
   - Settings are preserved during session

3. **Sample Text Module**:
   - Quick-insert buttons for common phrases
   - Each button has a helpful tooltip
   - Sample text includes greetings and common phrases

4. **Speech Generation Module**:
   - Converts text to speech using pyttsx3
   - Shows progress bar during conversion
   - Displays the output text being spoken

5. **UI/UX Enhancements**:
   - Animated buttons and elements
   - Success celebrations with confetti
   - Smooth transitions between states

### 🔄 Workflow

1. **User Input**:
   - User enters text in the input area or selects a sample
   - Adjusts voice settings as needed

2. **Speech Generation**:
   - User clicks "Convert to Speech" button
   - System validates input (shows error if empty)
   - Progress bar shows generation status

3. **Audio Output**:
   - Text is converted to speech using selected voice
   - Audio plays through system speakers
   - Success message appears with optional celebration

4. **Feedback Loop**:
   - User can adjust settings and regenerate
   - Clear button resets the input
   - Sample buttons provide quick new content

## 📝 Code Explanation

### 🎯 Main Function (`main()`)

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
   - Session state management

### 🔊 Speech Engine (`speak()` function)

1. **Initialization**:
   - Creates pyttsx3 engine instance
   - Configures voice properties

2. **Voice Selection**:
   - Sets male/female voice based on selection
   - Adjusts speech rate from slider

3. **Execution**:
   - Converts text to speech
   - Shows spinner during processing
   - Properly cleans up resources

## 🌈 UI/UX Highlights

- **Animated Elements**:
  - Floating emojis
  - Pulsing buttons
  - Bouncing success indicators

- **Visual Feedback**:
  - Progress bars
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
- pyttsx3 developers for the TTS engine
- Open source community for inspiration

