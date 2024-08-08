# File paths
TEMP_MEDIA_PATH = "temp_media.mp4"
TEMP_AUDIO_PATH = "temp_audio.mp3"

# Streamlit configuration
PAGE_TITLE = "Video/Audio Analysis with Google AI"
PAGE_LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Model names
GEMINI_FLASH_MODEL = "models/gemini-1.5-flash"
GEMINI_PRO_MODEL = "models/gemini-1.5-pro"

# Token limits
MAX_TOKENS = 40000

# System instructions
SYSTEM_INSTRUCTION_BASE = "You are an expert in analyzing and creating content for YouTube."
SYSTEM_INSTRUCTION_AUDIO = SYSTEM_INSTRUCTION_BASE + " The provided file is audio only."
