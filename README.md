# 💱 Currency Exchange API Project

This Python project retrieves the latest exchange rates from the **OpenExchangeRates API** and converts the JSON response into a **pandas DataFrame**.  
It demonstrates how to securely use API keys with environment variables and handle real-time financial data.

---

## 🚀 Features
- Fetches live exchange rates from OpenExchangeRates
- Uses **dotenv** to keep your API key private
- Displays currency data in a clean pandas DataFrame
- Adds a timestamp column for when the data was retrieved

---

## 🧰 Technologies Used
- Python 3
- requests
- pandas
- python-dotenv
- datetime

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/DovizAPI.git
   cd DovizAPI

2. **Create a virtual environment (optional but recommended)**
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Create a .env file**
my_api=your_api_key_here
