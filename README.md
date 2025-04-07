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
- Language: Python 3.9+
- Containerization: Docker

## Setup

### Option 1: Local Setup

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

### Option 2: Docker Setup (Recommended)

1. Create a `.env` file with your environment variables:
   ```
   GOOGLE_API_KEY=your_api_key_here
   MODEL_NAME=gemini-2.0-flash
   ```

2. Build the Docker image:
   ```bash
   docker build -t slogan-generator .
   ```

3. Run the container using the environment file:
   ```bash
   docker run -p 8501:8501 --env-file .env slogan-generator  
   ```
Then go to http://localhost:8501/

Alternative ways to run the container:

1. Using command line arguments:
   ```bash
   docker run -p 8501:8501 \
     -e GOOGLE_API_KEY=your_api_key_here \
     -e MODEL_NAME=gemini-pro \
     slogan-generator
   ```

2. Using Docker Compose (recommended for development):
   Create a `docker-compose.yml` file:
   ```yaml
   version: '3'
   services:
     slogan-generator:
       build: .
       ports:
         - "8501:8501"
       env_file:
         - .env
   ```
   Then run:
   ```bash
   docker-compose up
   ```

**Security Best Practices:**
- Never commit your `.env` file to version control
- Add `.env` to your `.gitignore` file
- Use different API keys for development and production
- Consider using Docker secrets for production environments
- Use environment variables for sensitive data instead of hardcoding them in the Dockerfile

## Environment Variables

Create a `.env` file with the following content:
```
GOOGLE_API_KEY=your_api_key_here
```

## System Requirements

- Python 3.9 or higher (for local setup)
- Docker (for containerized setup)
- Google API Key
- Internet connection

## Author

RayLin

## License

MIT License
