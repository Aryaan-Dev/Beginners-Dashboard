# **Crime Statistics Dashboard** 🌟📊

***Welcome to the Crime Statistics Dashboard project ! This is a sleek web app built with Streamlit and Plotly to dive into crime data across regions and years. Let’s get you started with easy steps to set it up, run it and troubleshoot like a pro !*** 🕵️‍♂️

## Screenshots 🎉📸

![Alt text](https://github.com/Aryaan-Dev/Beginners-Dashboard/blob/0df6e91231d41045f4dabba8c84745e6080421a7/1.png)
![Alt text](https://github.com/Aryaan-Dev/Beginners-Dashboard/blob/1cb4f36fd640bd2a3e86e94a80f569d69621e43c/2.png)

### Prerequisites 🛠️

Before you begin, ensure you have:

- Python 3.7 or higher
- pip (Python package manager)

### Installation 🛡️

1. **Clone the Repository**

   - Open your terminal or command prompt.
   - Run: `git clone https://github.com/Aryaan-Dev/crime-statistics-dashboard.git`
   - Navigate to the project folder: `cd crime-statistics-dashboard`

2. **Install Dependencies** 🔧

   - Create a virtual environment (optional but recommended): `python -m venv venv`
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - Mac/Linux: `source venv/bin/activate`
   - Install the required packages: `pip install -r requirements.txt`

3. **Prepare the Data** 📋

   - Place the `crime_data1.xlsx` file in the project directory. This file powers the dashboard !

### Running the Dashboard

1. **Start the Application** 🚀

   - In the terminal, run: `streamlit run crime_dashboard.py`
   - Watch it launch in your default web browser !

2. **Explore the Dashboard** 🔍

   - Use the sidebar filters to pick a year and state/UT.
   - Check out charts and tables for murder cases, auto theft and more !

### Folder Structure 📂

To ensure everything runs smoothly, structure your project folder like this:

```
crime-statistics-dashboard/
│
├── crime_dashboard.py         # Main dashboard script
├── requirements.txt           # Dependency file
├── crime_data1.xlsx           # Crime data file
└── venv/                      # Virtual environment (optional)
```

### Troubleshooting 🛠️

- **Error: ModuleNotFoundError**
  - Reinstall packages: `pip install -r requirements.txt`
- **Dashboard Not Loading**
  - Verify `crime_data1.xlsx` is in the right spot. Update the file path in `crime_dashboard.py` if needed.
  - Update Streamlit: `pip install --upgrade streamlit`
- **Charts Not Displaying**
  - Install Plotly: `pip install plotly`
  - Restart the app after installing.
- **Performance Issues**
  - Shrink `crime_data1.xlsx` or reduce charts in the code.

## Contributing 🌱

Fork this repo, add your magic, and send a pull request! 🎁 Ideas for new features or bug fixes are super welcome !

## Made By 👨‍💻

Created with ❤️ by B P ARYAAN \[ Aryaan-Dev \]. Special thanks to the open-source community !
