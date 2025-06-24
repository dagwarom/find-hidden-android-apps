@echo off
echo [🔄] Extracting installed app list to app.txt...
adb shell pm list packages > app.txt

echo [🔄] Extracting launchable app list to launcher.txt...
adb shell cmd package query-intent-activities -a android.intent.action.MAIN -c android.intent.category.LAUNCHER > launcher.txt

echo [✅] All done. Files saved:
echo - app.txt (all installed apps)
echo - launcher.txt (apps visible in launcher)

pause
