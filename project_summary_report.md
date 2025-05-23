# Projeto Hey Gringo: Project Overview

This report provides a comprehensive overview of "Projeto Hey Gringo," an English language learning application. It covers the project's purpose, architecture, structure, setup, execution, and potential future developments, based on information extracted from the project's README and Architectural Decision Record (ADR) documents.

## 1. Project Purpose and Core Functionalities

**Main Goal:** "Projeto Hey Gringo" is an English language learning application designed to provide an interactive and efficient learning experience.

**Key Features:**

*   **Learning Domain:** English language education.
*   **AI Integration:** Utilizes Ollama for AI-powered interactions, likely for conversation practice, feedback, and didactic suggestions.
*   **User Interactions:**
    *   **Chat Interface:** Simulates a conversation with a virtual English tutor, allowing users to send text messages.
    *   **Audio Processing:** Supports voice input via audio recording (MediaRecorder API) and transcription (Whisper). It also includes Text-to-Speech (TTS) functionality (Web Audio API) for pronunciation learning.
    *   **Inline Corrections:** Provides immediate feedback with highlighted corrections and didactic suggestions within the chat interface.
    *   **Progress Tracking:** Displays student progress, potentially using a CEFR (A1-C2) based system, to motivate users.
*   **Offline Functionality:** The frontend is designed to work offline, with data persistence and eventual synchronization with the backend.
*   **User Profile:** Supports persistent user configurations for a personalized learning experience.

## 2. Backend Architecture

The backend of "Projeto Hey Gringo" is built to manage business logic, user requests, AI integration, and data processing.

*   **Programming Language & Framework:** Python with the Flask framework (v2.3.x). Flask was chosen for its lightweight nature, flexibility, and suitability for RESTful API development.
*   **Key Libraries and Their Roles:**
    *   **Whisper (v20231117):** For audio processing, specifically transcribing spoken language into text.
    *   **Ollama (v0.1.x):** Integrates with an AI model for interactive learning features.
    *   **PyJSON-Logger (v2.0.x):** Implements structured logging in JSON format for monitoring and debugging.
    *   **Python-dotenv (v1.0.x):** Manages environment variables and application configurations.
    *   **Pytest (v7.4.x):** Serves as the testing framework for automated backend tests.
    *   **Flask-CORS:** Manages Cross-Origin Resource Sharing (CORS).
*   **Modularity & Structure:**
    *   The backend follows a modular structure using Flask Blueprints for better organization and scalability.
    *   **`core/`**: Contains main configurations, core application logic, request handlers (chat, speech), API routes, and session management.
    *   **`utils/`**: Houses utility modules, such as the structured logging system.
    *   **`vocabulary/`**: Manages didactic content like vocabulary lists, lesson materials, and conversational contexts.
    *   **`tests/`**: Includes all automated tests for backend components.
*   **Session Management:** A custom session management system is implemented, with session data persisted in JSON files.

## 3. Frontend Architecture

The frontend provides an interactive user interface for the English learning application.

*   **Framework & Build Tool:** React 18 with Vite. React was chosen for its performance and ecosystem, while Vite provides fast builds and Hot Module Replacement (HMR).
*   **Key Libraries, APIs, and Tools:**
    *   **Styling:**
        *   **TailwindCSS:** A utility-first CSS framework for responsive design.
        *   **ShadCN/UI:** Provides accessible and customizable UI components.
    *   **State Management:**
        *   **Zustand:** A lightweight solution for global state management, supporting persistence for offline functionality.
    *   **Backend Communication:**
        *   **Axios (v1.6.x):** An HTTP client for making REST API calls to the backend, with support for interceptors and caching.
    *   **Audio Handling:**
        *   **Web Audio API:** Native browser API for audio manipulation, including Text-to-Speech (TTS) playback.
        *   **MediaRecorder API:** Native browser API for recording audio from the user's microphone.
    *   **Routing:**
        *   **React Router (v6.x):** Manages client-side routing.
    *   **Schema Validation:**
        *   **Zod (v3.x):** Used for data validation.
    *   **Testing:**
        *   **Jest (v29.x) & React Testing Library:** For unit and component testing.
*   **Modularity & Structure (`src/` directory):**
    *   **`components/`**: Contains reusable UI components.
    *   **`features/`**: Organizes modules related to specific application functionalities.
    *   **`services/`**: Manages communication with the backend API.
    *   **`hooks/`**: Stores reusable custom React hooks for stateful logic.
*   **Main UI Features:**
    *   **Chat Interface:** Simulates a conversation with message components, avatars, and timestamps.
    *   **Voice Recording:** Captures user audio with visual feedback.
    *   **Text-to-Speech (TTS) Playback:** For pronunciation practice.
    *   **Inline Corrections:** Highlights errors and provides tooltips for immediate feedback.
    *   **Progress Bar:** Visual indicator of student progress (e.g., CEFR A1-C2 levels).
    *   **User Profile:** Allows for persistent user settings.

## 4. Project Structure

The project is organized into distinct top-level directories:

*   **Root Directory:**
    *   `.gitignore`, `LICENSE`, `README.md`
    *   `backend/`: Contains all backend code.
    *   `frontend/`: Contains all frontend code.
    *   `docs/`: Contains project documentation, including Architectural Decision Records (`adr/`).

*   **Backend (`backend/`):**
    *   `app.py`: Main Flask application file.
    *   `requirements.txt`: Python dependencies.
    *   `core/`: Core logic, configurations, handlers, routes.
    *   `utils/`: Utilities (e.g., logging).
    *   `vocabulary/`: Didactic content.
    *   `tests/`: Backend automated tests.

*   **Frontend (`frontend/`):**
    *   `package.json`, `package-lock.json`: Project metadata and dependencies.
    *   `public/`: Static assets (e.g., `index.html`).
    *   `src/`: Main React application source code.
        *   `App.js`: Main application component.
        *   `index.js`: React application entry point.
        *   `components/`: Reusable UI components.
        *   `features/`: Modules for specific application functionalities.
        *   `services/`: Backend API communication logic.
        *   `hooks/`: Reusable custom React hooks.

## 5. Setup and Execution

**Prerequisites:**

*   Python 3.x
*   Node.js (LTS version)
*   NPM or Yarn

**Initial Step:**

1.  **Clone the repository:** `git clone [URL_DO_REPOSITÓRIO]`

**Backend Setup:**

1.  Navigate to the backend directory: `cd backend`
2.  Create a Python virtual environment: `python -m venv venv`
3.  Activate the virtual environment:
    *   macOS/Linux: `source venv/bin/activate`
    *   Windows: `.\venv\Scripts\activate`
4.  Install Python dependencies: `pip install -r requirements.txt`

**Frontend Setup:**

1.  Navigate to the frontend directory: `cd frontend`
2.  Install Node.js dependencies: `npm install` (or `yarn install`)

**Running the Application:**

1.  **Start the Backend:**
    *   In the `backend` directory (with venv activated): `flask run`
2.  **Start the Frontend:**
    *   In the `frontend` directory: `npm start` (or `yarn start`)

## 6. Potential Future Development and Improvements

Based on the ADR documents, potential future enhancements include:

**Backend:**

*   **Session Management Enhancement:** Transition from manual JSON file-based sessions to a more robust solution (e.g., database-backed sessions or a dedicated session store) as the application scales.
*   **Scalability Planning:** Develop strategies for horizontal scaling to handle increased user load.
*   **Database Integration:** Consider integrating a dedicated database (SQL or NoSQL) for more complex data persistence needs beyond current session and vocabulary file storage.

**Frontend:**

*   **Cross-Device Testing:** Conduct thorough testing across various devices, browsers, and screen sizes.
*   **Offline Cache Management:** Refine and optimize caching strategies for a seamless offline mode.
*   **Backend Synchronization Strategy:** Implement a robust strategy for synchronizing offline data with the backend, including conflict resolution.
*   **Advanced Lesson System:**
    *   Implement a structured CEFR progression tree for lessons.
    *   Develop an achievement system to enhance user engagement.
*   **Multiple User Profiles:**
    *   Utilize IndexedDB for client-side storage to support multiple user profiles on the same device.
    *   Implement background synchronization for these profiles.
*   **Enhanced Text-to-Speech (TTS):**
    *   Integrate multiple voice options.
    *   Provide user controls for TTS accent and speed.
*   **New Study Modes:** Leverage the extensible design to add new types of exercises and learning activities.
