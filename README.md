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

| Extracted Data & Summary | CSV Upload View | Processed Rows |
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
