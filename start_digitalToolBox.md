# checklist for environment#
---------------------------
PS C:\Users\gupta\Documents\DailyToolbox> python --version
Python 3.13.4
PS C:\Users\gupta\Documents\DailyToolbox> node --version
v20.19.2
PS C:\Users\gupta\Documents\DailyToolbox> npm --version
10.8.2

# run backend Server #
-------------------
##Create a Virtual Environment#
# Navigate to the backend directory
PS C:\Users\gupta\Documents\DailyToolbox> cd backend
# Create a virtual environment named 'venv'
PS C:\Users\gupta\Documents\DailyToolbox\backend> python -m venv venv
# Activate the virtual environment on Windows
PS C:\Users\gupta\Documents\DailyToolbox\backend> .\venv\Scripts\activate

(venv) PS C:\Users\gupta\Documents\DailyToolbox\backend> python manage.py migrate

(venv) PS C:\Users\gupta\Documents\DailyToolbox\backend> python manage.py runserver
--http://127.0.0.1:8000/api/health-check/

# run front Server #
# #open New Terminal #
PS C:\Users\gupta\Documents\DailyToolbox> cd .\frontend\

PS C:\Users\gupta\Documents\DailyToolbox\frontend> npm run dev

http://localhost:5173/