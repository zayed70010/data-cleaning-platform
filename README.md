
# data-cleaning-platform




# 🧠# Intelligent Data Preprocessing Platform

This project is an interactive platform for automated data preprocessing, built with **Streamlit**.

The platform allows the user to:
- Upload CSV or JSON files.
- Automatically clean the data (remove duplicates, drop empty rows/columns).
- Handle missing values (mean, median, mode).
- Encode categorical columns (Label Encoding).
- Remove outliers (IQR or Z-Score).
- Normalize data (Min-Max scaling or Z-Score normalization).
- Select columns to exclude from preprocessing.
- Download the processed dataset.

---



## 📂 Project Structure


>>>>>>> fe6fdee752c45465bd2561c895cedb0abf20db48
preprocessing/

├── cleaning.py

├── encode.py

├── missing.py

├── normalize.py

├── outliers.py

├── reader.py

frontend.py

requirements.txt


---

## How to Run the Project

# 1️⃣ Clone the repository

```bash
>>>>>>> fe6fdee752c45465bd2561c895cedb0abf20db48
git clone https://github.com/zayed70010/data-cleaning-platform.git
cd data-cleaning-platform



# 2️⃣ Create and activate virtual environment 
>>>>>>> fe6fdee752c45465bd2561c895cedb0abf20db48
# Create virtual environment
python -m venv venv

# Activate the virtual environment:

# On Windows:
venv\Scripts\activate

# On Linux/MacOS:
source venv/bin/activate


>>>>>>> fe6fdee752c45465bd2561c895cedb0abf20db48
# 3️⃣ Install required dependencies

pip install -r requirements.txt

### 4️⃣ Run the Streamlit app
streamlit run frontend.py





