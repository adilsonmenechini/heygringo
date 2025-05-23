# Suggestions for Improvement: "Projeto Hey Gringo"

## 1. Introduction

This report synthesizes findings and suggestions to enhance the "Projeto Hey Gringo!" AI, focusing on making it a more polite and helpful companion for users learning English for daily-life situations. The goal is to improve user engagement, practical learning, and overall satisfaction by refining the AI's persona, expanding relevant content, and ensuring the technical architecture supports these enhancements.

## 2. Backend Improvements

### Persona Enhancement (`config.py` - `SYSTEM_PROMPT`)

*   **Current State (Assumed):** The existing `SYSTEM_PROMPT` might be too generic, focusing on basic tutoring without explicit instructions on tone, politeness, or specific daily-life conversational strategies.
*   **Suggested Additions for Politeness and Helpfulness:**
    *   Incorporate phrases that instruct the AI to be consistently encouraging, patient, and empathetic.
    *   Emphasize gentle corrections and positive reinforcement.
    *   Instruct the AI to use phrases that acknowledge the user's effort.
    *   **Example additions to `SYSTEM_PROMPT`:**
        ```
        "Always maintain a friendly, patient, and encouraging tone. You are 'Gringo', a helpful guide."
        "When correcting, be gentle. Start with positive feedback before offering a suggestion. For example: 'That's a good attempt! A more common way to say that is...' or 'You're on the right track! Just a small tip: ...'"
        "Use phrases like 'No worries!', 'Great question!', 'Let's try that together.', 'You're doing great!'"
        "Acknowledge user feelings if they express frustration: 'I understand this can be tricky, but you're making good progress!'"
        "Proactively offer to explain things further or provide more examples if the user seems unsure."
        ```
*   **Rationale:** A well-defined, polite, and supportive AI persona can significantly reduce learning anxiety, build user confidence, and make the learning experience more enjoyable and effective.

### Expanding Daily-Life Scenarios (`config.py` - `SYSTEM_PROMPT`)

*   **Current Scenarios (Assumed):** The AI might currently handle general conversation but may lack depth in specific, practical daily-life scenarios beyond basic greetings or simple Q&A.
*   **Suggestions for New Scenarios:**
    The `SYSTEM_PROMPT` should also be updated to inform the AI about its capabilities in handling these new scenarios, encouraging it to proactively engage or guide users within these contexts when appropriate.

    *   **Asking for and Understanding Directions:**
        *   **Goal:** Help users ask for directions and understand responses.
        *   **Vocabulary:** `turn left/right`, `go straight`, `opposite`, `next to`, `block`, `landmarks`.
        *   **Phrases:** "Excuse me, how do I get to...?", "Could you show me on the map?", "Is it far from here?".
        *   **Cultural Notes:** Common ways people give directions (e.g., using landmarks vs. street names).
    *   **Making Phone Calls:**
        *   **Goal:** Practice formal and informal phone conversations, including making appointments or inquiries.
        *   **Vocabulary:** `speaking`, `hold on`, `I'd like to speak to...`, `call back`, `leave a message`.
        *   **Phrases:** "Hello, this is [Name]. May I speak to [Name/Department]?", "I'm calling about...".
    *   **Using Public Transport:**
        *   **Goal:** Navigate buying tickets, asking about routes, and understanding announcements.
        *   **Vocabulary:** `bus stop`, `train station`, `platform`, `fare`, `route map`, `transfer`.
        *   **Phrases:** "Which bus goes to...?", "How much is a ticket to...?", "Does this train stop at...?".
    *   **Basic Health Interactions:**
        *   **Goal:** Describe simple symptoms, understand basic advice from a pharmacist, or make a doctor's appointment.
        *   **Vocabulary:** `headache`, `sore throat`, `prescription`, `appointment`, `feel dizzy`.
        *   **Phrases:** "I have a [symptom].", "I'd like to make an appointment to see Dr. [Name].", "What do you recommend for a cold?".
    *   **Social Small Talk & Interactions:**
        *   **Goal:** Practice initiating and maintaining light conversations in social settings (e.g., weather, hobbies, weekend plans).
        *   **Vocabulary:** Phrases related to common topics.
        *   **Phrases:** "Lovely weather, isn't it?", "Do you have any plans for the weekend?", "How was your day?".
        *   **Cultural Notes:** Appropriate topics for small talk, turn-taking in conversation.
*   **Rationale:** Expanding the range of scenarios makes the AI a more versatile and practical tool for learners preparing for real-world interactions in English.

### Vocabulary Expansion (`vocabulary/contexts.py`)

*   **Current Structure (Assumed):** `contexts.py` might define a dictionary mapping context keys to lists of vocabulary, examples, and notes.
*   **How to Add New Contexts and Vocabulary:**
    *   For each new scenario (Directions, Phone Calls, etc.), add a new key to the `VOCABULARY_CONTEXTS` dictionary in `contexts.py`.
    *   The value for each key will be a list of dictionaries, where each dictionary contains `term`, `example` (showing polite usage), and `notes` (e.g., politeness level, cultural nuance).
    *   **Code Structure Example (`vocabulary/contexts.py`):**
        ```python
        VOCABULARY_CONTEXTS = {
            # ... existing contexts ...
            "directions_asking": [
                {"term": "Excuse me", "example": "Excuse me, could you help me?", "notes": "Polite way to get attention."},
                {"term": "How do I get to...?", "example": "How do I get to the nearest post office?", "notes": "Direct question for directions."},
                {"term": "Is it far?", "example": "Is it far from here?", "notes": "Asking about distance."},
            ],
            "directions_understanding": [
                {"term": "Turn left/right at...", "example": "Turn left at the next corner.", "notes": "Common instruction."},
                {"term": "Go straight ahead for...", "example": "Go straight ahead for two blocks.", "notes": "Common instruction."},
            ],
            "phone_calls_formal": [
                {"term": "May I speak to...", "example": "Hello, this is John Doe. May I speak to Ms. Smith?", "notes": "Formal request."},
                {"term": "I'm calling regarding...", "example": "I'm calling regarding the job advertisement.", "notes": "Stating purpose of call."},
            ],
            # ... more contexts for public transport, health, small talk ...
        }
        ```
*   **Rationale:** Centralizing scenario-specific vocabulary in `contexts.py` provides a structured and maintainable way to manage and expand the learning content.

### Lesson Structure (`vocabulary/lessons.py` or new `daily_life_lessons.py`)

*   **Current Structure (Assumed):** Lessons might be a simple list or dictionary, perhaps lacking specific ties to daily-life scenarios or interactive exercise structures.
*   **Proposal for `DAILY_LIFE_LESSONS` list:**
    *   Create a new list, potentially in a new file `daily_life_lessons.py` or within `lessons.py`, named `DAILY_LIFE_LESSONS`.
    *   Each lesson in this list will be a dictionary with a clear structure.
    *   **Example Structure (`daily_life_lessons.py`):**
        ```python
        DAILY_LIFE_LESSONS = [
            {
                "id": "dl_001",
                "title": "Ordering Coffee Politely",
                "description": "Learn how to order your favorite coffee and snacks with polite English phrases.",
                "icon": "☕", # Emoji or path to an icon image
                "context_keys": ["ordering_food", "greetings_polite"], # Relates to VOCABULARY_CONTEXTS
                "target_phrases": [
                    "I would like a latte, please.",
                    "Could I also get a croissant?",
                    "Thank you, that's all.",
                    "Have a good day!"
                ],
                "exercises": [
                    {"type": "role_play_prompt", "prompt": "You are at a cafe. Greet the barista and order a cappuccino and a muffin."},
                    {"type": "fill_in_the_blank", "sentence": "Excuse me, ___ I have a glass of water?", "answer": "could"},
                    {"type": "politeness_check", "user_input_needed": True, "feedback_prompt": "How could you make that request more polite?"}
                ]
            },
            {
                "id": "dl_002",
                "title": "Asking for Directions",
                "description": "Practice asking for and understanding directions to common places.",
                "icon": "🗺️",
                "context_keys": ["directions_asking", "directions_understanding", "greetings_polite"],
                "target_phrases": [
                    "Excuse me, how do I get to the library?",
                    "Is it far from here?",
                    "Could you point me in the right direction?"
                ],
                "exercises": [
                    {"type": "scenario_chat", "scenario_description": "You are lost and need to find the train station. Ask Gringo for help."},
                    {"type": "comprehension_task", "directions_given": "Go straight for two blocks, then turn right at the supermarket. It's next to the bank.", "question": "What is the train station next to?"}
                ]
            },
            # ... more lessons for other scenarios
        ]
        ```
*   **Rationale:** A structured lesson list allows the frontend to dynamically render lesson options and provides a clear framework for content creators to add new, interactive daily-life scenarios. The `exercises` array allows for varied interactions beyond simple chat.

### Chat Handling (`core/chat_handler.py`)

*   **How to use `current_scenario` from frontend:**
    *   The frontend will send the `id` of the active lesson/scenario (e.g., `"dl_001"`) with each chat message.
    *   In `chat_handler.py`, the `handle_chat_message` function (or equivalent) should receive this `current_scenario` ID.
    *   Based on this ID, the AI can:
        *   Adjust its `SYSTEM_PROMPT` or add context-specific instructions to Ollama. For example, if `current_scenario == "dl_001"`, the AI might be prompted: "The user is currently practicing ordering at a cafe. Act as a friendly barista and guide them."
        *   Access relevant `target_phrases` or `context_keys` from `DAILY_LIFE_LESSONS` to tailor its responses, vocabulary suggestions, and corrections.
        *   Guide the conversation according to the lesson's objectives or exercise types.
*   **Rationale:** This allows the AI to provide more relevant and contextualized responses, making the learning experience more focused and effective for the specific daily-life scenario being practiced.

### API for Lessons (New Route)

*   **Suggestion for a new `/api/lessons` endpoint:**
    *   This endpoint will serve the `DAILY_LIFE_LESSONS` list (and potentially other lesson types in the future) to the frontend.
*   **Example Route Code (`core/routes.py`):**
    ```python
    from flask import Blueprint, jsonify
    # Assuming DAILY_LIFE_LESSONS is imported from vocabulary.daily_life_lessons
    from backend.vocabulary.daily_life_lessons import DAILY_LIFE_LESSONS
    # Or from backend.vocabulary.lessons import DAILY_LIFE_LESSONS

    lessons_bp = Blueprint('lessons_api', __name__)

    @lessons_bp.route('/api/lessons', methods=['GET'])
    def get_lessons():
        # In the future, could filter by type, difficulty, etc.
        # For now, returns all daily life lessons.
        return jsonify(DAILY_LIFE_LESSONS)

    # Register this blueprint in app.py:
    # from backend.core.routes import lessons_bp
    # app.register_blueprint(lessons_bp)
    ```
*   **Rationale:** A dedicated API endpoint for lessons decouples the frontend from direct backend file structures and allows for easier updates and management of lesson content.

## 3. Frontend Improvements

### Dynamic Lesson Loading (`App.js`)

*   **Current Hardcoded State (Assumed):** Lesson data or scenario context might be hardcoded or minimally managed in `App.js`.
*   **Fetching Lessons from `/api/lessons`:**
    *   Use `useEffect` on component mount to fetch the list of lessons from the new `/api/lessons` backend endpoint.
    *   Store these lessons in the React state (e.g., `const [lessons, setLessons] = useState([]);`).
*   **Managing `currentActiveScenario` state:**
    *   Add a new state variable, e.g., `const [currentActiveScenario, setCurrentActiveScenario] = useState(null);`.
    *   When a user selects a lesson (e.g., from a list of lesson cards), update `currentActiveScenario` with the lesson's `id`.
*   **Code Snippets for `useEffect` and `handleSendMessage` modifications:**
    ```javascript
    // App.js
    import React, { useState, useEffect } from 'react';
    import { fetchLessons, fetchAIResponse } from './services/api'; // Updated api.js

    function App() {
        const [lessons, setLessons] = useState([]);
        const [currentActiveScenario, setCurrentActiveScenario] = useState(null); // e.g., "dl_001"
        const [messages, setMessages] = useState([]);
        // ... other states

        useEffect(() => {
            // Fetch lessons when the app loads
            const loadLessons = async () => {
                try {
                    const lessonsData = await fetchLessons();
                    setLessons(lessonsData);
                } catch (error) {
                    console.error("Failed to load lessons:", error);
                    // Handle error, e.g., show a message to the user
                }
            };
            loadLessons();
        }, []);

        const handleSendMessage = async (userInput) => {
            // ... (add user message to messages state) ...

            try {
                const aiResponse = await fetchAIResponse(userInput, currentActiveScenario); // Pass scenario
                // ... (add AI message to messages state, including any tips or corrections) ...
            } catch (error) {
                console.error("Error fetching AI response:", error);
                // ... (handle error in UI) ...
            }
        };

        const handleSelectLesson = (lessonId) => {
            setCurrentActiveScenario(lessonId);
            // Optionally, clear messages or add a system message like "Starting lesson: [Lesson Title]"
            setMessages([{ sender: 'system', text: `Starting lesson: ${lessons.find(l => l.id === lessonId)?.title}` }]);
        };

        // ... (render lesson selection UI, chat UI, etc.) ...
    }
    ```
*   **Rationale:** Dynamically loading lessons makes the application more scalable and easier to update with new content without frontend redeployments. Passing the `currentActiveScenario` tailors AI interaction to the selected lesson.

### API Service (`services/api.js`)

*   **New `fetchLessons` function:**
    *   To retrieve the list of lessons from the backend.
*   **Modification to `fetchAIResponse` to include `current_scenario`:**
    *   The chat request to the backend should include the `current_scenario` ID.
*   **Code Snippets:**
    ```javascript
    // services/api.js
    import axios from 'axios';

    const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

    export const fetchLessons = async () => {
        try {
            const response = await axios.get(`${API_BASE_URL}/lessons`);
            return response.data;
        } catch (error) {
            console.error('Error fetching lessons:', error);
            throw error; // Re-throw to be caught by the caller
        }
    };

    export const fetchAIResponse = async (message, scenarioId = null) => { // scenarioId is optional
        try {
            const response = await axios.post(`${API_BASE_URL}/chat`, {
                message: message,
                user_id: 'currentUser', // Replace with actual user management if implemented
                current_scenario: scenarioId // Send the current scenario ID
            });
            return response.data; // Expecting { response: "AI text", corrections: [], tips: [] }
        } catch (error) {
            console.error('Error fetching AI response:', error);
            throw error;
        }
    };
    ```
*   **Rationale:** Encapsulating API calls in a dedicated service module keeps the codebase organized and makes it easier to manage API interactions and error handling.

### User Interface Enhancements (Optional but Recommended)

*   **`ChatMessage.js`: Styling for corrections/tips:**
    *   If the AI response includes corrections or tips (e.g., `response.data.corrections`), display them distinctly.
    *   **Example:** Prefix a correction with a tag like `[Dica do Gringo ✨]` or `[Sugestão]`. Style this tag differently (color, font weight).
        ```javascript
        // ChatMessage.js (conceptual)
        // if (message.correction) {
        //   return <div className="message ai-message"><span className="correction-tag">[Dica do Gringo ✨]</span> {message.text} <span className="correction-text">{message.correction}</span></div>;
        // }
        ```
*   **`ChatInput.js`: Softer placeholder text, optional quick polite phrases:**
    *   Change placeholder from "Type your message..." to something more inviting like "Say hello or ask a question..." or "Practice your English here...".
    *   Optionally, add buttons for quick polite phrases like "Hello", "Thank you", "Excuse me" that users can click to send.
*   **`RewardFeedback.js`: Ensuring messages align with persona:**
    *   Review messages in `RewardFeedback.js` to ensure they are encouraging and use language consistent with the polite AI persona (e.g., "Great job!", "You're learning fast! Keep it up!").
*   **Rationale:** These small UI tweaks reinforce the AI's persona, make corrections feel more like helpful hints, and improve the overall user experience, making it more welcoming and supportive.

## 4. General Structural Considerations

*   **Backend - Managing Growing Content:**
    *   As `VOCABULARY_CONTEXTS` and `DAILY_LIFE_LESSONS` grow, consider splitting them into multiple JSON files or a simple file-based database structure within the `vocabulary` directory. These can be loaded and merged at application startup. This keeps individual Python files cleaner.
*   **Frontend - Robust State Management:**
    *   For more complex applications with many lessons, user progress tracking, and settings, consider a dedicated state management library (like Zustand, which is already in use, or Redux if complexity significantly increases) to manage global state for lessons, current scenario, user progress, etc., more effectively than just `useState` in `App.js`. Ensure Zustand stores are well-organized.

## 5. Conclusion

Implementing these suggestions for backend and frontend enhancements is expected to deliver significant benefits:

*   **Improved User Engagement:** A more polite, empathetic, and scenario-aware AI will make interactions more enjoyable and less intimidating.
*   **Enhanced Practical Learning:** Focusing on daily-life scenarios and vocabulary directly addresses common user needs, making the learned English more immediately applicable.
*   **Increased Learner Confidence:** Gentle corrections and positive reinforcement will create a more supportive learning environment.
*   **Greater Application Utility:** The expanded range of topics and structured lessons will make "Projeto Hey Gringo!" a more comprehensive and valuable tool for English language learners.
*   **Scalable Content Management:** The proposed structures for vocabulary and lessons allow for easier expansion and maintenance of learning content.

By systematically refining the AI's persona, enriching the content with practical daily-life scenarios, and ensuring the UI/UX supports these changes, "Projeto Hey Gringo!" can significantly elevate the learning experience it offers.
