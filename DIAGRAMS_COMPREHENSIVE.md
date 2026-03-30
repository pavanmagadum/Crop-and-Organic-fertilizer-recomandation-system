# 📊 Comprehensive System Diagrams

This document contains professional diagrams for your **Climate-Aware Crop & Organic Fertilizer Recommendation System**.

## 1. 🖼️ High-Level System Concept
A futuristic visual representation of how your AI connects the farmer with the land.
![Climate-Aware Architecture](/brain/a4ef2882-960b-4bb5-9636-a7614191c76d/system_architecture_diagram_climate_aware_1774894482136.png)

---

## 2. 🧱 Functional Block Diagram
This shows the logical flow of data between the different modules of your application.

```mermaid
graph LR
    subgraph UI ["User Experience (Streamlit)"]
        A[🏠 Dashboard] --> B[🌱 Crop Recommendation]
        A --> C[🧪 Fertilizer Suggester]
        A --> D[🌥️ Weather Insights]
        A --> E[💬 Community Portal]
    end

    subgraph ENGINE ["Intelligence Middle Layer"]
        B --> F{🧠 ML Models}
        C --> F
        F --> G[(💾 Joblib Models)]
        F --> H[(🗄️ SQLite DB)]
    end

    subgraph EXTERNAL ["Remote Connectors"]
        D --> I[🌤️ OpenWeather API]
        A --> J[📺 YouTube API]
    end

    subgraph OUTPUT ["Outcome Advisory"]
        F --> K[✅ Smart Advice]
        I --> L[🌨️ Alerts]
        J --> M[🎥 Tutorials]
    end
```

---

## 3. 🔄 User Journey Sequence Diagram
This shows how the system processes a single crop recommendation request.

```mermaid
sequenceDiagram
    participant User as 👨‍🌾 Farmer
    participant UI as 🖥️ Streamlit App
    participant Model as 🧠 ML Classifier
    participant API as 🌤️ Weather API

    User->>UI: Enters Soil N-P-K & pH
    UI->>API: Fetches Local Climate (Temp/Rain)
    API-->>UI: Returns Weather Data
    UI->>Model: Sends Combined Features (Soil + Weather)
    Model->>Model: Random Forest Processing
    Model-->>UI: Best Suitability: [CROP NAME]
    UI->>UI: Calculates Fertilizer Deficiencies
    UI-->>User: Displays Dashboard (Crop + Plan + Tutorials)
```

---

## 4. 🗃️ Data Schema Relationship
This explains how your Community database connects the different user roles.

```mermaid
erDiagram
    USER ||--o{ POST : writes
    USER ||--o{ QUESTION : asks
    EXPERT ||--o{ ANSWER : provides
    ADMIN ||--o{ USER : manages
    QUESTION ||--|{ ANSWER : contains
    USER {
        string username
        string role
        string password
    }
    POST {
        string title
        string content
        string author
        datetime created_at
    }
```

---

### 📂 Accessing these Diagrams:
*   **Mermaid Code:** [ARCHITECTURE_DIAGRAM.md](file:///c:/Users/sw/Desktop/climate_aware_final_project/ARCHITECTURE_DIAGRAM.md)
*   **Interactive View:** [architecture_diagram.html](file:///c:/Users/sw/Desktop/climate_aware_final_project/architecture_diagram.html)
