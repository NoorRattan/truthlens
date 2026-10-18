# Fake-news-Detector (TruthLens)

TruthLens is an AI-powered fake news and misinformation detection platform. It uses advanced language models to analyze news articles, headlines, and URLs to provide a credibility score and detailed reasoning.

## Project Structure

This repository is organized into the following components:

- **[truthlens/backend](truthlens/backend)**: A FastAPI-based backend that handles the analysis pipeline, integrating with Google Gemini AI for advanced misinformation detection.
- **[truthlens/frontend](truthlens/frontend)**: A modern React 18 frontend built with Vite, featuring an editorial-style UI with Three.js visualizations and Framer Motion animations.

## Getting Started

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd truthlens/backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and configure Groq (primary), Cohere (fallback), and Serper (web search) as needed.
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd truthlens/frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Set up your `.env.local` to point to the backend API.
4. Run the development server:
   ```bash
   npm run dev
   ```

## Live Deployment
- **Frontend**: [https://truthlens-omega.vercel.app](https://truthlens-omega.vercel.app)
- **Backend API**: [https://truthlens-api-4vou.onrender.com](https://truthlens-api-4vou.onrender.com)

### Render configuration

Use `truthlens/backend` as the service root directory, `pip install -r requirements.txt`
as the build command, and `uvicorn main:app --host 0.0.0.0 --port $PORT` as the start
command. Set the health check path to `/api/health`. The Blueprint is at
`truthlens/render.yaml`; its paths are relative to the repository root.

The backend requires the `html-clean` extra for lxml. It supplies the HTML cleaner
used by article extraction; omitting it causes the application import to fail
before a port is opened. CI exercises application startup and the health endpoint
in addition to pipeline tests.

## Repository
- **Current Home**: [NoorRattan/truthlens](https://github.com/NoorRattan/truthlens)
