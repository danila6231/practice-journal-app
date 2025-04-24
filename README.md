# AI Journal App

A web application that helps users maintain a journal with AI-powered insights. The app uses Gemini AI to summarize entries and suggest mood tags.

## Features

- Submit daily journal entries
- AI-powered summarization of entries
- Mood tag suggestions
- View and manage past entries
- Modern, responsive UI

## Prerequisites

- Python 3.8+
- Node.js 14+
- MongoDB
- Gemini API key

## Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory with:
   ```
   MONGODB_URL=your_mongodb_url
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Enter your thoughts in the journal entry form
3. Submit the entry to get AI-generated summary and mood tag
4. View your past entries in the list below

## Project Structure

```
ai-journal/
├── backend/
│   ├── main.py                # FastAPI app entry
│   ├── routes/
│   │   └── entries.py         # Handles POST/GET endpoints
│   ├── services/
│   │   └── gemini.py          # Calls Gemini API for summarization & tagging
│   ├── models/
│   │   └── entry.py           # Pydantic + MongoDB model
│   ├── database.py            # MongoDB connection setup
│   └── requirements.txt       # Python dependencies
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── JournalForm.jsx       # Form to submit new entry
│   │   │   ├── EntryList.jsx         # Displays journal entries
│   │   ├── App.jsx
│   │   └── index.js
│   └── package.json
```

## License

MIT 