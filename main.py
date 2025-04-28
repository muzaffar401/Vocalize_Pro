# Import necessary libraries
import streamlit as st  # For creating the web app
import pyttsx3  # For text-to-speech conversion
from streamlit_extras.colored_header import colored_header  # For styled headers
from streamlit_extras.stylable_container import stylable_container  # For custom containers
from streamlit_extras.let_it_rain import rain  # For fun animations
import time  # For adding delays

# Function to convert text to speech
def speak(text, voice_type='female', rate=200):
    """Convert text to speech with given parameters"""
    # Create a new text-to-speech engine each time
    engine = pyttsx3.init()
    
    # Get available voices from the system
    voices = engine.getProperty('voices')
    
    # Set male or female voice based on selection
    if voice_type == 'male':
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice
    
    # Set speech speed (words per minute)
    engine.setProperty('rate', rate)
    
    # Queue the text to be spoken
    engine.say(text)
    
    # Show a loading spinner while speaking
    with st.spinner('Speaking...'):
        engine.runAndWait()  # Make the engine speak the text
    
    # Stop the engine when done
    engine.stop()

# Main function where the app is built
def main():
    # Configure the page settings
    st.set_page_config(
        page_title="Vocalize Pro | Text to Speech",  # Browser tab title
        page_icon="🎙️",  # Browser tab icon
        layout="wide",  # Use full page width
        initial_sidebar_state="expanded"  # Show sidebar by default
    )
    
    # Add custom CSS styling for the whole app
    st.markdown("""
    <style>
        /* Import a nice font from Google */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        /* Use the font everywhere */
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Background color for main area */
        .main {
            background-color: #f5f7fa;
        }
        
        /* Style the text input box */
        .stTextArea textarea {
            min-height: 200px;
            border-radius: 12px !important;
            border: 1px solid #e0e0e0 !important;
            padding: 15px !important;
            font-size: 16px !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
            transition: all 0.3s ease !important;
        }
        
        /* When text box is clicked */
        .stTextArea textarea:focus {
            border-color: #6366f1 !important;
            box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
        }
        
        /* Style the main button */
        .speak-btn {
            background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
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
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 8px rgba(99, 102, 241, 0.4) !important;
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
        
        /* Sample button hover effect */
        .sample-btn:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        }
        
        /* Style for voice setting cards */
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
        
        /* Footer styling */
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
    """, unsafe_allow_html=True)
    
    # Create a colorful header with title and description
    colored_header(
        label="🎙️ Vocalize Pro",
        description="Transform text into natural sounding speech with beautiful voices",
        color_name="violet-70",
    )
    
    # Store the text input in session state (memory) if it doesn't exist
    if 'text_input' not in st.session_state:
        st.session_state.text_input = ""
    
    # Create two columns - main content (3/4) and sidebar (1/4)
    col1, col2 = st.columns([3, 1], gap="large")
    
    # Main content area
    with col1:
        # Create a styled container for the text input
        with stylable_container(
            key="text_input_container",
            css_styles="""
                {
                    border-radius: 16px;
                    padding: 25px;
                    background: white;
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05);
                    border: 1px solid #f0f0f0;
                    margin-bottom: 20px;
                }
            """
        ):
            # Add a heading with floating emoji
            st.markdown("""
            <h3 style="color: #6366f1; margin-bottom: 20px;">
                <span class="floating">✍️</span> Your Text
            </h3>
            """, unsafe_allow_html=True)
            
            # Create a large text input area
            text_input = st.text_area(
                " ",  # Empty label
                placeholder="Type or paste your text here...\n\nTry something like: 'Hello, welcome to Vocalize Pro! This text will be converted to beautiful speech.'",
                height=250,  # Height in pixels
                value=st.session_state.text_input,  # Get text from memory
                key="text_area",  # Unique identifier
                label_visibility="collapsed"  # Hide the label
            )
            
            # Create a row for buttons
            col_btn1, col_btn2, _ = st.columns([2, 1, 1])
            
            # First button column (Convert to Speech)
            with col_btn1:
                if st.button(
                    "🎙️ Convert to Speech",
                    key="speak",
                    use_container_width=True,  # Make button full width
                    type="primary"  # Make it the primary button
                ):
                    # Check if text is empty
                    if not text_input.strip():
                        st.error("Please enter some text to convert to speech.")
                    else:
                        # Show the output in a styled container
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
                            
                            # Display the text that will be spoken
                            st.write(text_input)
                            
                            try:
                                # Get voice settings from memory
                                voice_type = st.session_state.voice_type
                                rate = st.session_state.rate
                                
                                # Show loading animation
                                with st.spinner('Generating beautiful speech...'):
                                    # Create a progress bar
                                    progress_bar = st.progress(0)
                                    # Animate the progress bar
                                    for percent_complete in range(100):
                                        time.sleep(0.01)  # Small delay
                                        progress_bar.progress(percent_complete + 1)
                                    
                                    # Convert the text to speech
                                    speak(text_input, voice_type, rate)
                                
                                # Show success message
                                st.success("✨ Speech generated successfully!")
                                # Add celebration animation
                                rain(
                                    emoji="🎉",
                                    font_size=20,
                                    falling_speed=5,
                                    animation_length=1,
                                )
                                
                                # Add fun quotes based on content
                                if "python" in text_input.lower():
                                    st.balloons()  # Show balloons animation
                                    st.markdown("> *Python is the second best language for everything.* - Someone wise")
                                elif "hello" in text_input.lower():
                                    st.markdown("> *Hello there! Have a wonderful day!*")
                            except Exception as e:
                                # Show error if something goes wrong
                                st.error(f"An error occurred: {str(e)}")
            
            # Second button column (Clear)
            with col_btn2:
                if st.button(
                    "🧹 Clear",
                    key="clear",
                    use_container_width=True,
                    help="Clear the text area"
                ):
                    # Empty the text input
                    st.session_state.text_input = ""
                    # Refresh the page
                    st.rerun()
    
    # Sidebar area
    with col2:
        # Create a styled container for voice settings
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
            # Voice settings heading
            st.markdown("""
            <h3 style="color: #6366f1; margin-bottom: 20px;">
                ⚙️ Voice Settings
            </h3>
            """, unsafe_allow_html=True)
            
            # Radio buttons to select voice type (male/female)
            voice_type = st.radio(
                "Select Voice:",
                ('female', 'male'),
                index=0,  # Default to female
                key="voice_type",  # Store in memory
                format_func=lambda x: f"👩 {x.capitalize()}" if x == "female" else f"👨 {x.capitalize()}",  # Add emojis
                horizontal=True  # Show side by side
            )
            
            # Custom slider styling
            st.markdown("""
            <style>
                .stSlider [data-testid="stTickBar"] div {
                    background: linear-gradient(90deg, #e0e7ff, #6366f1) !important;
                    height: 6px !important;
                    border-radius: 3px !important;
                }
                
                .stSlider [role="slider"] {
                    background: #6366f1 !important;
                    border: 2px solid white !important;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
                }
            </style>
            """, unsafe_allow_html=True)
            
            # Slider to adjust speech speed
            rate = st.slider(
                "🗣️ Speech Speed:",
                min_value=100,  # Slowest
                max_value=300,  # Fastest
                value=200,  # Default
                step=10,  # Increment size
                key="rate"  # Store in memory
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
            
            # First column of sample buttons
            with sample_col1:
                if st.button(
                    "👋 Hello",
                    key="sample1",
                    use_container_width=True,
                    help="Insert a friendly greeting"
                ):
                    st.session_state.text_input = "Hello, how are you today? I hope you're enjoying Vocalize Pro!"
                    st.rerun()
                
                if st.button(
                    "🚀 Welcome",
                    key="sample2",
                    use_container_width=True,
                    help="Insert welcome message"
                ):
                    st.session_state.text_input = "Welcome to Vocalize Pro - your premium text to speech solution!"
                    st.rerun()
            
            # Second column of sample buttons
            with sample_col2:
                if st.button(
                    "💖 Love",
                    key="sample3",
                    use_container_width=True,
                    help="Insert loving message"
                ):
                    st.session_state.text_input = "I just wanted to say I appreciate you. Have a wonderful day!"
                    st.rerun()
                
                if st.button(
                    "📝 Lorem Ipsum",
                    key="sample4",
                    use_container_width=True,
                    help="Insert sample text"
                ):
                    st.session_state.text_input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris."
                    st.rerun()
            
            # Add a fun animated microphone icon
            st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <div class="pulse" style="font-size: 24px;">🎙️</div>
                <p style="color: #64748b; font-size: 12px;">Try different voices!</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer at the bottom of the page
    st.markdown("""
    <div class="footer">
        <p>Built with ❤️ using Streamlit and pyttsx3 | © 2025 <span style="color: #6366f1;">Vocalize Pro</span></p>
        <div style="margin-top: 10px;">
            <span style="display: inline-block; animation: bounce 2s infinite;">✨</span>
            <span style="display: inline-block; animation: bounce 2s infinite 0.2s;">🎤</span>
            <span style="display: inline-block; animation: bounce 2s infinite 0.4s;">🔊</span>
        </div>
    </div>
    
    <style>
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
    </style>
    """, unsafe_allow_html=True)

# Run the app when this script is executed
if __name__ == "__main__":
    main()