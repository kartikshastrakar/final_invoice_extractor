
# 📄 Final Invoice Extractor

This project uses a **Local LLM (Ollama)** to extract and summarize invoice data dynamically from a CSV file. It processes each row and generates structured JSON output and summary for better understanding.

---

## 🎯 **Project Overview**

The project involves:
- Extracting key invoice information.
- Summarizing data for quick review.
- Processing multiple rows dynamically using a Streamlit interface.
- Displaying the extracted information and summary for each row in JSON format.

---

## 🚀 **Tech Stack**

- **Python 3.8+**
- **LangChain** for agent-based data extraction.
- **Ollama** for local LLM inference.
- **Streamlit** for interactive UI.
- **Pandas** for data handling.
- **FastAPI** (optional for API setup).

---

## 📸 **Screenshots**

Below are screenshots of the application interface:

| CSV Upload View   | Processed Rows | Extracted Data & Summary  |
|--------------------------|-----------------|----------------|
| ![Screenshot1](screenshots/Screenshot%202025-03-18%20210925.png) | ![Screenshot2](screenshots/Screenshot%202025-03-18%20211422.png) | ![Screenshot3](screenshots/Screenshot%202025-03-18%20211628.png) |
| ![Screenshot4](screenshots/Screenshot%202025-03-18%20212637.png) | ![Screenshot5](screenshots/Screenshot%202025-03-18%20212709.png) | ![Screenshot6](screenshots/Screenshot%202025-03-18%20212818.png) |
| ![Screenshot7](screenshots/Screenshot%202025-03-18%20212858.png) | ![Screenshot8](screenshots/Screenshot%202025-03-18%20213252.png) | ![Screenshot9](screenshots/Screenshot%202025-03-18%20230310.png) |

---

## 📦 **Installation**

### 1. Clone the Repository
```bash
git clone https://github.com/kartikshastrakar/final_invoice_extractor.git
cd final_invoice_extractor
```

### 2. Create a Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Pull Ollama Model
```bash
# Pull Mistral or any preferred model
ollama pull mistral
```

---

## ▶️ **Usage**

### Run the Streamlit Application
```bash
streamlit run api.py
```

### Access the Application in Your Browser
```
http://localhost:8501
```

---

## 📚 **Project Structure**
```
final_invoice_extractor/
├── api.py                   # Streamlit application
├── requirements.txt         # Required packages
├── README.md                # Project documentation
├── /screenshots/            # Application screenshots
└── /src/
    ├── extract.py           # Extraction logic using LLM
    └── summarize.py         # Summarization logic
```

---

## 🧠 **Key Functionalities**
- Upload a CSV file with invoice data.
- Process and extract structured information using an LLM.
- Summarize the invoice content and display it dynamically.
- View extracted JSON data side-by-side with the summarized text.

---

## 🔥 **Troubleshooting Tips**
- Make sure the Ollama model is pulled correctly.
- Check if the virtual environment is activated properly.
- If errors persist, refer to [LangChain Documentation](https://python.langchain.com/docs/troubleshooting/errors/OUTPUT_PARSING_FAILURE).

---

## 🤝 **Contributing**
Feel free to fork the repository, create a new branch, and submit a pull request to enhance the application.

---

## 📄 **License**
This project is licensed under the MIT License.
