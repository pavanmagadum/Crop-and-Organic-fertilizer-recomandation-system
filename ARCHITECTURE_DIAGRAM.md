# 🏢 System Architecture Diagram

This document outlines the high-level architecture of the **Climate-Aware Crop & Organic Fertilizer Recommendation System**.

## 🏗️ Architecture Overview

The system follows a typical **Client-Server architecture** with a specialized **Machine Learning Processing Layer**. It is designed to be modular, ensuring that data acquisition, core logic, and user advisory are decoupled.

### 📊 Mermaid Diagram

```mermaid
graph TD
    %% Define Professional Styles
    classDef actor fill:#e8eaf6,stroke:#1a237e,stroke-width:2px;
    classDef external fill:#fff3e0,stroke:#e65100,stroke-width:2px,stroke-dasharray: 5 5;
    classDef component fill:#ffffff,stroke:#37474f,stroke-width:2px;
    classDef database fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;
    classDef output fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;

    %% Actors & External Services
    User("👨‍🌾 Farmer / User"):::actor
    Admin("🛡️ Admin / Expert"):::actor
    WeatherAPI["🌤️ OpenWeatherMap API"]:::external
    YouTube["🎥 YouTube Tutorial Engine"]:::external

    %% Main System Boundary
    subgraph System_Scope ["Climate-Aware Farming System"]
        direction TB

        %% 1. Input Layer
        subgraph Input_Layer ["1. Data Acquisition (Streamlit UI)"]
            direction TB
            SoilData["Soil Parameters (N, P, K, pH)"]:::component
            LocData["Location & Climate Data"]:::component
            CommInput["Community Queries/Posts"]:::component
        end

        %% 2. Processing Layer
        subgraph Core_Logic ["2. Core Processing Logic (Python Backend)"]
            direction TB
            PreProcess["Data Preprocessing & Validation"]:::component
            
            subgraph ML_Engine ["3. Intelligence Layer (Machine Learning)"]
                direction TB
                RF_Crop["Random Forest Classifier (Crop Recommendation)"]:::component
                RF_Fert["Random Forest / Logic Engine (Fertilizer Recommendation)"]:::component
            end a-id ("ML_Engine")

            DB[("🗄️ SQLite Database (Community & Analytics)")]:::database
        end

        %% 3. Output Layer
        subgraph Output_Layer ["4. Advisory & Results"]
            direction TB
            Out_Crop["✅ Recommended Crop Result"]:::output
            Out_Fert["🧪 Soil-Specific Fertilizer Plan"]:::output
            Out_Weather["🌡️ Real-time Weather Insights"]:::output
            Out_Video["📺 Curated Agri-Tutorials"]:::output
        end
    end

    %% Connections
    User -->|Enters Parameters| SoilData
    User -->|Grants Location| LocData
    User -->|Interacts| CommInput

    WeatherAPI -.->|Fetch Climate| LocData
    LocData --> PreProcess
    SoilData --> PreProcess
    
    PreProcess --> RF_Crop
    RF_Crop --> RF_Fert
    
    %% Database Links
    CommInput <--> DB
    Admin <-->|Manage Users/Content| DB
    RF_Crop -->|Log Analytics| DB

    %% Output Flow
    RF_Crop --> Out_Crop
    RF_Fert --> Out_Fert
    LocData --> Out_Weather
    YouTube -.->|Search Relevant Videos| Out_Video
```

---

## 🧩 Component Descriptions

### 1. **Data Acquisition Layer (UI)**
*   **Streamlit Frontend:** Provides a responsive, glassmorphism-themed interface for farmers to input soil data (Nutrients, pH) and location.
*   **Location Awareness:** Captures weather data dynamically via the browser or manual entry.
*   **Community Interface:** A social layer for farmers to ask questions and experts to provide answers.

### 2. **Core Processing Logic**
*   **Preprocessing:** Validates user inputs, handles missing data, and scales features for the ML models.
*   **Machine Learning Engine:** 
    *   **Crop Model:** Uses a Random Forest algorithm (trained on `crop_data.csv`) to predict the most suitable crop based on soil and climate conditions.
    *   **Fertilizer Logic:** Dynamically calculates organic and chemical fertilizer requirements based on the predicted crop and current soil nutrient deficiencies.

### 3. **Intelligence Layer**
*   **Model Storage:** Models are serialized as `.joblib` files for instant loading and inference.
*   **Data Models:** Maps raw N-P-K values to actionable agricultural advice.

### 4. **Data Persistence Layer**
*   **SQLite3:** Stores user profiles, community posts, expert sessions, and system analytics.
*   **Joblib Artifacts:** Stores the trained weights of the predictive models.
*   **Environment Variables:** Manages sensitive API keys and administrator credentials securely.

### 5. **Advisory & Results Layer**
*   **Visual Dashboards:** Provides 3D pie charts and interactive cards showing result breakdowns.
*   **External Integration:** Fetches real-time weather forecasts and dynamically searches YouTube for relevant "how-to" farming tutorials.
