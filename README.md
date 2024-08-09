![youtube-gemini](https://github.com/user-attachments/assets/aea8df0d-70de-4713-a612-dfad98dbda0e)
# YouTube Assistant Desktop App

This desktop application is powered by Google Gemini AI, designed to be your ultimate YouTube assistant, helping you optimize your video content for better visibility and engagement. With this tool, you can easily generate time stamps, titles, and descriptions that are SEO-optimized for your videos. Whether you're a content creator looking to streamline your workflow or boost your channel's performance, this app provides the tools you need to succeed.

  

## 🛠️ Features

Automatic Time Stamps: Powered by Google Gemini AI, the app generates precise time marks for your videos to enhance viewer navigation and engagement.

SEO-Optimized Titles: Receive AI-driven title suggestions that are tailored for maximum search engine visibility.

Description Generator: Create detailed, keyword-rich descriptions that help improve your video's ranking on YouTube, thanks to the power of Google Gemini AI.

User-Friendly Interface: Easy to navigate and designed for efficiency, helping you focus more on content creation and less on optimization.

Cross-Platform Support: Available on Windows, macOS, and Linux.

## 🚀 Prerequisites

- Python 3.8+
- Google API Key with access to Gemini AI
- FFmpeg (for audio extraction)


## How It Works

1. Upload or link your video.

2. Add your Gemini API key.

3. Select if you want to analyze the full video or audio only.

4. The app, powered by Google Gemini AI, analyzes the content and generates time stamps, titles, and descriptions.


## Installation

Clone the repository:

```git clone git@github.com:alarcon7a/gemini-youtube-assistant.git```

```cd gemini-youtube-assistant```

  

Create a virtual environment and activate it:

```python3.10 -m venv youtube_assistant_env```

```source youtube_assistant_env/bin/activate # On Windows, use `youtube_assistant_env\Scripts\activate` ```

  
Install the required packages:

```pip install -r requirements.txt```

  
Copy .env.example to .env and add your Google API Key:

```cp .env.example .env```

Then edit .env and add your API key.

  
## Usage

Run the Streamlit app:
**change the 2000 parameter if you want to upload bigger files**

```streamlit run src/main.py --server.maxUploadSize 2000```

## 🤝 Contributing
Contributions are welcome! If you have improvements or corrections, feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📧 Contact
If you have questions or need additional support, you can contact the author via email or @alarcon7a in all social networks
