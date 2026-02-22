🏛️ Dual Portal Architecture
Nagrik Seva is built as a two-sided platform — one for citizens, one for government officials.

👤 Citizen Portal	🏛️ Government Portal
Users	Indian citizens	District Collectors, Taluk Officers, Village Accountants
View	My applications, bills, documents	All pending applications across jurisdiction
Action	Apply, track, pay	Approve, reject, escalate, assign
Analytics	Personal status	District-level bottleneck heatmaps
AI Feature	Face verification	Auto-priority scoring & fraud detection
🤖 AI & Analytics Engine
The government portal uses an intelligent analysis layer to cut bureaucratic delays:

🔴 Bottleneck Detection — Flags which stage (Field Verification, DC Approval, etc.) is causing delays using percentile analysis
📊 Officer Workload Balancing — Detects overloaded officials and suggests redistribution
🚨 SLA Breach Alerts — Auto-escalates applications breaching the 30-day threshold
🔍 Fraud Pattern Recognition — Flags duplicate applications and suspicious document patterns
📈 District-Level Heatmaps — Visual maps showing application density and processing speed by taluk
🎯 Auto-Priority Scoring — ML-based urgency scoring (senior citizens, scholarships get bumped up)
🏗️ System Architecture
🎨 Frontend
Technology	Usage
HTML5	Structure & semantic layout
CSS3	Styling, animations, responsive design
JavaScript (Vanilla)	Interactivity, DOM manipulation, section routing
⚙️ Backend
Technology	Usage
Python	Core backend language
Flask API	REST API server, routing endpoints
JSONify	API response formatting
🗄️ Database & APIs
Technology	Usage
Python Database API (DB-API)	Database connectivity layer
Groq API	LLM-powered intelligence & natural language processing
UIDAI (Aadhaar)	Identity verification integration
🤖 AI & ML Modules
Library	Usage
OpenCV (cv2)	Camera feed processing, image capture
face_recognition	Face detection & biometric matching
PyTesseract	OCR — extract text from document images
spaCy	NLP — parse and validate document text
NumPy	Numerical processing for face embeddings
🔄 Data Flow Architecture
👤 CITIZEN / 🏛️ GOVT OFFICER
        ↓
[ HTML + CSS + JS Frontend ]
        ↓  HTTP Requests
[ Flask REST API (Python) ]
        ↓              ↓
[ DB-API Database ]  [ AI Pipeline ]
                          ↓
              ┌───────────────────────┐
              │  cv2 → face_recog     │  Face Verification
              │  PyTesseract → spaCy  │  Document OCR & NLP
              │  NumPy                │  Embedding Processing
              │  Groq API             │  Smart Insights & LLM
              └───────────────────────┘
                          ↓
              [ JSONify → API Response ]
                          ↓
              [ Frontend renders result ]