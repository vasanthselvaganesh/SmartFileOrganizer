# SmartFileOrganizer

Smart File Organizer – A simple tool to automatically scan, categorize, and organize files using C++ and Python.  

Installation & Usage  
For macOS/Linux  
```
# Install dependencies  
brew install gcc python3  # macOS  
sudo apt install g++ python3  # Linux  

# Clone the repository  
git clone https://github.com/your-username/SmartFileOrganizer.git  
cd SmartFileOrganizer  

# Compile and run the C++ scanner  
g++ -std=c++17 file_scanner.cpp -o scanner && ./scanner  

# Run the Python organizer  
python3 file_organizer.py  
```
Automate with crontab:**  
```
crontab -e  
```
Add this line:  
```
0 10 * * * /path/to/SmartFileOrganizer/run.sh  
```  

For Windows  
1. Install Python (python.org) and MinGW-w64 (mingw-w64.org)  
2. Clone the repository:  
   ```
   git clone https://github.com/your-username/SmartFileOrganizer.git  
   cd SmartFileOrganizer  
   ```  
3. Compile and run:  
   ```
   g++ -std=c++17 file_scanner.cpp -o scanner.exe && scanner.exe  
   python file_organizer.py  
   ```  
4. Automate with Task Scheduler – Schedule `run.bat` to run daily at 10 AM.  


