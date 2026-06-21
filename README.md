# MyExpenses Patched

A repository containing an automated CI/CD pipeline and local build script to patch the premium features (paywall) of the [MyExpenses](https://github.com/mtotschnig/MyExpenses) Android application. This is created for educational purposes

## Features
- **Paywall Bypass**
- **Cloud Backup Fix** (Google Drive, Onedrive broken)

## How to Build Locally

### Prerequisites
- Python
- Java JDK 21
- Git

### Usage
```bash
chmod +x build.sh
./build.sh
```

The compiled APK will be available in the `src/myExpenses/build/outputs/apk/extern/debug/` directory

## GitHub Actions (CI/CD)
Fork repo and trigger action to build latest apk