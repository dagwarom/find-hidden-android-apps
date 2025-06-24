🖥️ Automate with Batch Script (Windows)
To make it easier, you can use the included generate_app_lists.bat to automate data extraction:

How to Use:
Place the .bat file inside your platform-tools folder (where adb.exe is located)

Double-click the file — it will generate:

app.txt: all installed apps

launcher.txt: launchable (visible) apps

Then run the Python script:
bash
python find_hidden_apps.py
Output (optional): You can save hidden apps list:
python
with open("hidden_apps.txt", "w") as out:
    for pkg in sorted(hidden_apps):
        out.write(f"{pkg}\n")
Optional: Add hidden_apps.txt as Example Output
Create a dummy example like:
com.example.hiddenapp
com.test.supervision
com.spy.stealthlauncher

# Find Hidden Apps on Android

This Python script helps detect hidden Android apps that are **not visible in the launcher**, which are often used for parental supervision, background services, or system-level operations.

---

## 📦 Requirements

### 🖥️ System Requirements
- **Python 3.x**
- **ADB (Android Debug Bridge)**  
  Download: [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)  
  Make sure `adb` is added to your system PATH

### 📚 Python Dependencies
Install required packages with:

```bash
pip install -r requirements.txt

Note: Requires adb to be in your system PATH. 
