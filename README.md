

# AI Resume Screening & Ranking System

**Project:** AI Resume Screening & Ranking System
**Developer:** Kajal Dadas
**Contact:** +91 7972244559 | [kajaldadas149@gmail.com](mailto:kajaldadas149@gmail.com)

---

## **Project Overview**

The **AI Resume Screening & Ranking System** is a Python-based tool that automates resume screening for recruiters and HR professionals. It scans PDF resumes, matches keywords from a job description, ranks resumes based on relevance, and moves shortlisted resumes to a separate folder for further review.

**Key Features:**

* Upload multiple PDF resumes at once
* Input keywords for screening
* Automatic keyword matching and ranking
* Moves shortlisted resumes to a `screened_resumes` folder
* Displays both pending and screened resumes
* Simple, user-friendly UI built with **Streamlit**

---

## **Project Structure**

```
AI-Resume-Screening/
│
├── AI Resume Screening.py      # Main Python app
├── uploaded_resumes/          # Folder to store uploaded resumes
├── screened_resumes/          # Folder where screened resumes are moved
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## **Requirements**

* Python 3.8 or above
* Packages:

  * streamlit
  * PyPDF2
  * pandas
  * shutil, os (standard library)

**requirements.txt example:**

```
streamlit
PyPDF2
pandas
```

---

## **Installation Steps**

1. **Clone or download the repository** to your local machine:

```bash
git clone <repository_url>
cd AI-Resume-Screening
```

2. **Install Python packages**:

```bash
pip install -r requirements.txt
```

3. **Create folders** (if not already present):

```bash
mkdir uploaded_resumes
mkdir screened_resumes
```

---

## **Running the App**

1. Open your terminal or PowerShell and navigate to the project folder:

```bash
cd AI-Resume-Screening
```

2. Run the Streamlit app:

```bash
streamlit run "AI Resume Screening.py"
```

3. The UI will open in your browser. **Steps to use:**

   * **Step 1:** Enter the screening keywords (comma-separated)
   * **Step 2:** Upload resumes (PDF format)
   * **Step 3:** Click **Scan & Screen Resumes**
   * **Step 4:** View ranked results and see which resumes have been moved to `screened_resumes/`

---

## **Creating Executable (.exe)**

To generate a Windows executable:

```bash
python -m pip install pyinstaller
python -m PyInstaller --noconfirm --onefile --windowed "AI Resume Screening.py"
```

* Executable will be available in the `dist` folder.

---


## **License**

This project is for personal and educational use. Commercial use requires developer consent.

---
