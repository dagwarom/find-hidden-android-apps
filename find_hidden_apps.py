# Load both files
with open("all_packages.txt", "r") as f_all:
    all_packages = set(line.strip().split('=')[-1] for line in f_all if '=' in line)

with open("launchable_apps.txt", "r") as f_launchable:
    launchable_packages = set(line.strip().split(':')[-1] for line in f_launchable if ':' in line)

# Find hidden apps
hidden_apps = all_packages - launchable_packages

# Print result
print("\n🔎 Hidden Apps Detected (Not visible in launcher):")
if hidden_apps:
    for pkg in sorted(hidden_apps):
        print(f" - {pkg}")
else:
    print("✅ No hidden apps found!")
