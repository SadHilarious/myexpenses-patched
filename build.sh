#!/bin/bash
set -e

echo "=> Cloning MyExpenses repository..."
if [ ! -d "src" ]; then
    git clone --depth 1 https://github.com/mtotschnig/MyExpenses src
else
    echo "Directory 'src' already exists. Pulling latest changes..."
    cd src
    git pull
    cd ..
fi

echo "=> Running patch script..."
python patch.py src/myExpenses/src/main/java/org/totschnig/myexpenses/util/licence/LicenceHandler.kt

echo "=> Enabling Cloud backup module and Dynamic Features..."
cd src

# Uncomment drive module in settings.gradle
sed -i "s/\/\/include ':drive'/include ':drive'/g" settings.gradle

# Add drive to dynamicFeatures in myExpenses/build.gradle
sed -i "s/dynamicFeatures = \[':ocr'/dynamicFeatures = \[':drive', ':ocr'/g" myExpenses/build.gradle

# Add play-services-auth to the base module to fix missing google_play_services_version
# Note: Check if it's already added to avoid appending multiple times
if ! grep -q "libs.play.services.auth" myExpenses/build.gradle; then
    echo "; dependencies { implementation libs.play.services.auth }" >> myExpenses/build.gradle
fi

echo "=> Building Universal Debug APK..."
chmod +x gradlew
./gradlew myExpenses:packageExternDebugUniversalApk

echo ""
echo "=========================================================="
echo "=> Build complete! The APK can be found at:"
echo "   src/myExpenses/build/outputs/apk/extern/debug/"
echo "=========================================================="
