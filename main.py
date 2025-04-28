# Import necessary libraries
import streamlit as st  # For creating the web app
from gtts import gTTS  # Google Text-to-Speech library
from io import BytesIO  # For handling binary data in memory
import base64  # For encoding/decoding data (not actually used in this code)
from streamlit_extras.colored_header import colored_header  # For fancy headers
from streamlit_extras.stylable_container import stylable_container  # For styled containers
from streamlit_extras.let_it_rain import rain  # For fun celebration effects
import time  # For adding delays

# Function to convert text to speech
def speak(text, voice_type='female', rate=200):
    """Convert text to speech with gTTS and return audio data"""
    try:
        # Adjust speed - gTTS only has fast/slow options
        # If rate is low (<=150), use slow speed
        slow_speed = False if rate > 150 else True
        
        # Create text-to-speech object
        # lang='en' means English
        tts = gTTS(text=text, lang='en', slow=slow_speed)
        
        # Save audio to memory instead of a file
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)  # Write audio to memory
        audio_bytes.seek(0)  # Go back to start of the audio data
        
        return audio_bytes  # Return the audio data
        
    except Exception as e:
        st.error(f"Error generating speech: {str(e)}")  # Show error if something goes wrong
        return None

# Main function where the app runs
def main():
    # Set up the page configuration
    st.set_page_config(
        page_title="Vocalize Pro | Text to Speech",  # Browser tab title
        page_icon="🎙️",  # Browser tab icon
        layout="wide",  # Use full width of the screen
        initial_sidebar_state="expanded"  # Show sidebar by default
    )
    
    # Add custom CSS styles to make the app look nice
    st.markdown("""
    <style>
        /* Import a nice font from Google */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        /* Use this font everywhere */
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Background color for main area */
        .main {
            background-color: #f5f7fa;
        }
        
        /* Style the text input box */
        .stTextArea textarea {
            min-height: 200px;  /* Make it taller */
            border-radius: 12px !important;  /* Rounded corners */
            border: 1px solid #e0e0e0 !important;  /* Light gray border */
            padding: 15px !important;  /* Add space inside */
            font-size: 16px !important;  /* Bigger text */
            box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;  /* Soft shadow */
            transition: all 0.3s ease !important;  /* Smooth changes */
        }
        
        /* When text box is clicked */
        .stTextArea textarea:focus {
            border-color: #6366f1 !important;  /* Purple border */
            box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;  /* Glow effect */
        }
        
        /* Style the main button */
        .speak-btn {
            background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;  /* Purple gradient */
            border: none !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 12px 24px !important;
            border-radius: 12px !important;
            font-size: 16px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 6px rgba(99, 102, 241, 0.3) !important;
        }
        
        /* Button hover effect */
        .speak-btn:hover {
            transform: translateY(-2px) !important;  /* Move up slightly */
            box-shadow: 0 6px 8px rgba(99, 102, 241, 0.4) !important;  /* Bigger shadow */
        }
        
        /* Style for sample buttons */
        .sample-btn {
            border-radius: 10px !important;
            padding: 10px 15px !important;
            margin-bottom: 10px !important;
            transition: all 0.2s ease !important;
            border: 1px solid #e0e0e0 !important;
            background-color: white !important;
        }
        
        /* Sample button hover */
        .sample-btn:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        }
        
        /* Style for voice cards */
        .voice-card {
            border-radius: 16px;
            padding: 20px;
            background: white;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
            border: 1px solid #f0f0f0;
        }
        
        /* Sidebar background */
        .sidebar .sidebar-content {
            background-color: #f8fafc;
        }
        
        /* Footer style */
        .footer {
            text-align: center;
            padding: 20px;
            color: #64748b;
            font-size: 14px;
            margin-top: 40px;
        }
        
        /* Pulsing animation */
        .pulse {
            animation: pulse 2s infinite;
        }
        
        /* Keyframes for pulse animation */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        /* Floating animation */
        .floating { 
            animation-name: floating;
            animation-duration: 3s;
            animation-iteration-count: infinite;
            animation-timing-function: ease-in-out;
        }
        
        /* Keyframes for floating animation */
        @keyframes floating {
            0% { transform: translate(0,  0px); }
            50%  { transform: translate(0, 10px); }
            100%   { transform: translate(0, -0px); }
        }
    </style>
    """, unsafe_allow_html=True)  # Need this to allow HTML in Streamlit
    
    # Create a fancy colored header at the top
    colored_header(
        label="🎙️ Vocalize Pro",  # Title with microphone emoji
        description="Transform text into natural sounding speech with beautiful voices",  # Subtitle
        color_name="violet-70",  # Purple color
    )
    
    # Create a place to store the user's text if it doesn't exist yet
    if 'text_input' not in st.session_state:
        st.session_state.text_input = ""
    
    # Split the page into two columns (3:1 ratio)
    col1, col2 = st.columns([3, 1], gap="large")
    
    # Left column (main content)
    with col1:
        # Create a styled container for the text input
        with stylable_container(
            key="text_input_container",
            css_styles="""
                {
                    border-radius: 16px;  # Rounded corners
                    padding: 25px;  # Space inside
                    background: white;  # White background
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05);  # Soft shadow
                    border: 1px solid #f0f0f0;  # Light border
                    margin-bottom: 20px;  # Space below
                }
            """
        ):
            # Add a heading with a floating emoji
            st.markdown("""
            <h3 style="color: #6366f1; margin-bottom: 20px;">
                <span class="floating">✍️</span> Your Text
            </h3>
            """, unsafe_allow_html=True)
            
            # Create the big text box where users type
            text_input = st.text_area(
                " ",  # Empty label
                placeholder="Type or paste your text here...\n\nTry something like: 'Hello, welcome to Vocalize Pro! This text will be converted to beautiful speech.'",
                height=250,  # Height of the box
                value=st.session_state.text_input,  # Get saved text
                key="text_area",  # Unique identifier
                label_visibility="collapsed"  # Hide the label
            )
            
            # Create a row for buttons
            col_btn1, col_btn2, _ = st.columns([2, 1, 1])
            with col_btn1:
                # Main button to convert text to speech
                if st.button(
                    "🎙️ Convert to Speech",
                    key="speak",
                    use_container_width=True,  # Make button fill the column
                    type="primary"  # Make it the primary button
                ):
                    # Check if text box is empty
                    if not text_input.strip():
                        st.error("Please enter some text to convert to speech.")
                    else:
                        # Show the output in a nice container
                        with stylable_container(
                            key="output_container",
                            css_styles="""
                                {
                                    border-radius: 16px;
                                    padding: 20px;
                                    background: linear-gradient(135deg, #f5f7fa, #ffffff);
                                    border-left: 4px solid #6366f1;
                                    margin-top: 20px;
                                    animation: fadeIn 0.5s ease-in-out;
                                }
                                
                                @keyframes fadeIn {
                                    from { opacity: 0; transform: translateY(10px); }
                                    to { opacity: 1; transform: translateY(0); }
                                }
                            """
                        ):
                            # Output section heading
                            st.markdown("""
                            <h3 style="color: #6366f1; margin-bottom: 15px;">
                                🔊 Speech Output
                            </h3>
                            """, unsafe_allow_html=True)
                            
                            # Show the text that will be spoken
                            st.write(text_input)
                            
                            try:
                                # Get voice settings from memory
                                voice_type = st.session_state.get('voice_type', 'female')
                                rate = st.session_state.get('rate', 200)
                                
                                # Show loading animation
                                with st.spinner('Generating beautiful speech...'):
                                    # Create a progress bar that fills up
                                    progress_bar = st.progress(0)
                                    for percent_complete in range(100):
                                        time.sleep(0.01)  # Small delay
                                        progress_bar.progress(percent_complete + 1)
                                    
                                    # Convert the text to speech
                                    audio_bytes = speak(text_input, voice_type, rate)
                                
                                # If we got audio back
                                if audio_bytes:
                                    # Show success message
                                    st.success("✨ Speech generated successfully!")
                                    # Add celebration animation
                                    rain(
                                        emoji="🎉",
                                        font_size=20,
                                        falling_speed=5,
                                        animation_length=1,
                                    )
                                    
                                    # Play the audio
                                    st.audio(audio_bytes, format='audio/mp3')
                                    
                                    # Add fun messages based on content
                                    if "python" in text_input.lower():
                                        st.balloons()  # More celebration
                                        st.markdown("> *Python is the second best language for everything.* - Someone wise")
                                    elif "hello" in text_input.lower():
                                        st.markdown("> *Hello there! Have a wonderful day!*")
                            except Exception as e:
                                st.error(f"An error occurred: {str(e)}")  # Show errors
            
            with col_btn2:
                # Clear button to empty the text box
                if st.button(
                    "🧹 Clear",
                    key="clear",
                    use_container_width=True,
                    help="Clear the text area"
                ):
                    st.session_state.text_input = ""  # Empty the text
                    st.rerun()  # Refresh the page
    
    # Right column (sidebar content)
    with col2:
        # Voice settings in a styled container
        with stylable_container(
            key="settings_container",
            css_styles="""
                {
                    border-radius: 16px;
                    padding: 25px;
                    background: white;
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05);
                    border: 1px solid #f0f0f0;
                }
            """
        ):
            # Settings heading
            st.markdown("""
            <h3 style="color: #6366f1; margin-bottom: 20px;">
                ⚙️ Voice Settings
            </h3>
            """, unsafe_allow_html=True)
            
            # Voice type selection (disabled because free gTTS doesn't support it)
            voice_type = st.radio(
                "Select Voice:",
                ('female', 'male'),
                index=0,
                key="voice_type",
                format_func=lambda x: f"👩 {x.capitalize()}" if x == "female" else f"👨 {x.capitalize()}",
                horizontal=True,
                disabled=True,  # Can't change this in free version
                help="Voice selection requires premium API (not available in free gTTS)"
            )
            
            # Custom slider style
            st.markdown("""
            <style>
                /* Style the slider track */
                .stSlider [data-testid="stTickBar"] div {
                    background: linear-gradient(90deg, #e0e7ff, #6366f1) !important;
                    height: 6px !important;
                    border-radius: 3px !important;
                }
                
                /* Style the slider handle */
                .stSlider [role="slider"] {
                    background: #6366f1 !important;
                    border: 2px solid white !important;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
                }
            </style>
            """, unsafe_allow_html=True)
            
            # Speech speed slider
            rate = st.slider(
                "🗣️ Speech Speed:",
                min_value=100,  # Slowest
                max_value=300,  # Fastest
                value=200,  # Default
                step=10,  # Increment size
                key="rate",
                help="Note: gTTS only supports two speed modes (normal/slow)"
            )
            
            # Divider line
            st.markdown("---")
            # Quick samples section
            st.markdown("""
            <h3 style="color: #6366f1; margin-bottom: 15px;">
                🎧 Quick Samples
            </h3>
            """, unsafe_allow_html=True)
            
            # Create two columns for sample buttons
            sample_col1, sample_col2 = st.columns(2)
            with sample_col1:
                # Sample button 1
                if st.button(
                    "👋 Hello",
                    key="sample1",
                    use_container_width=True,
                    help="Insert a friendly greeting"
                ):
                    st.session_state.text_input = "Hello, how are you today? I hope you're enjoying Vocalize Pro!"
                    st.rerun()  # Refresh to show the text
                
                # Sample button 2
                if st.button(
                    "🚀 Welcome",
                    key="sample2",
                    use_container_width=True,
                    help="Insert welcome message"
                ):
                    st.session_state.text_input = "Welcome to Vocalize Pro - your premium text to speech solution!"
                    st.rerun()
            
            with sample_col2:
                # Sample button 3
                if st.button(
                    "💖 Love",
                    key="sample3",
                    use_container_width=True,
                    help="Insert loving message"
                ):
                    st.session_state.text_input = "I just wanted to say I appreciate you. Have a wonderful day!"
                    st.rerun()
                
                # Sample button 4
                if st.button(
                    "📝 Lorem Ipsum",
                    key="sample4",
                    use_container_width=True,
                    help="Insert sample text"
                ):
                    st.session_state.text_input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris."
                    st.rerun()
            
            # Fun animated element
            st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <div class="pulse" style="font-size: 24px;">🎙️</div>
                <p style="color: #64748b; font-size: 12px;">Try different texts!</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer at the bottom of the page
    st.markdown("""
    <div class="footer">
        <p>Built with ❤️ using Streamlit and gTTS | © 2023 <span style="color: #6366f1;">Vocalize Pro</span></p>
        <div style="margin-top: 10px;">
            <span style="display: inline-block; animation: bounce 2s infinite;">✨</span>
            <span style="display: inline-block; animation: bounce 2s infinite 0.2s;">🎤</span>
            <span style="display: inline-block; animation: bounce 2s infinite 0.4s;">🔊</span>
        </div>
    </div>
    
    <style>
        /* Bouncing animation for footer icons */
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
    </style>
    """, unsafe_allow_html=True)

# Start the app when this script is run
if __name__ == "__main__":
    main()