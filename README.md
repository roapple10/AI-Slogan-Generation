# AI Advertising Slogan Generator

A multi-agent collaborative AI system that automatically generates, analyzes, and optimizes advertising slogans based on product information.

## Demo
Watch our demo video to see the AI Advertising Slogan Generator in action:

[![Demo Video](https://img.youtube.com/vi/1YAVS9r9pCQ/0.jpg)](https://www.youtube.com/watch?v=1YAVS9r9pCQ)

## Features

### 🤖 AI Agent Team

1. **Slogan Generator (SloganAgent)**
   - Generates creative advertising slogans based on product information
   - Ensures concise and impactful slogans
   - Highlights core product features

2. **Slogan Inspector (InspectAgent)**
   - Analyzes if slogans effectively reference product features
   - Evaluates slogan relevance
   - Provides detailed analysis reports

3. **Scoring Agent (ScoreAgent)**
   - Provides professional scoring on a 1-5 scale
   - Offers specific scoring rationale
   - Provides improvement suggestions

4. **Optimization Advisor (BestSloganAgent)**
   - Suggests optimization directions based on scores
   - Provides real-time improvement advice
   - Helps enhance slogan quality

### 📊 System Features

- Supports batch generation (1-10 slogans)
- Real-time scoring and analysis
- Traditional Chinese interface
- Intuitive tabbed result display
- Complete progress tracking

## How to Use

1. Input Product Information
   ```
   Describe your product features and advantages in detail in the text box
   ```

2. Select Generation Count
   ```
   Choose the number of slogans to generate (1-10)
   ```

3. View Results
   - Each slogan displays:
     - Generated slogan content
     - Analysis report
     - Score results
     - Optimization suggestions

## Technical Architecture

- Frontend: Streamlit
- AI Model: Google Gemini Pro
- Agent Framework: Phi-agent
- Language: Python 3.8+

## Setup

1. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Configure Environment Variables
   ```bash
   cp .env.example .env
   # Edit .env file and add your GOOGLE_API_KEY
   ```

3. Run Application
   ```bash
   streamlit run app.py
   ```

## System Requirements

- Python 3.8 or higher
- Google API Key
- Internet connection

## Author

RayLin

## License

MIT License
