import re
import sys
import os

def patch_licence_handler(file_path):
    print(f"Patching {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Patch 1: Make isEnabledFor always return true
        pattern_is_enabled = r'open fun isEnabledFor\(licenceStatus: LicenceStatus\)\s*=\s*\([^)]*\)\s*>=\s*0'
        replacement_is_enabled = 'open fun isEnabledFor(licenceStatus: LicenceStatus) = true'
        
        new_content, count1 = re.subn(pattern_is_enabled, replacement_is_enabled, content, count=1)
        if count1 > 0:
            print("Successfully patched 'isEnabledFor' function.")
        else:
            print("Warning: Could not find 'isEnabledFor' pattern to patch.")

        # Patch 2: Make init() set licenceStatus to PROFESSIONAL and hasOurLicence to true
        pattern_init = r'(open fun init\(\) \{)(.*?)(restoreAddOnFeatures\(\)\s*\})'
        replacement_init = r'\1\n        this.licenceStatus = LicenceStatus.PROFESSIONAL\n        hasOurLicence = true\n        \3'

        new_content, count2 = re.subn(pattern_init, replacement_init, new_content, count=1, flags=re.DOTALL)
        if count2 > 0:
            print("Successfully patched 'init' function.")
        else:
            print("Warning: Could not find 'init' pattern to patch.")

        # Save the patched content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("Patching complete!")

    except Exception as e:
        print(f"Error during patching: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python patch.py <path_to_LicenceHandler.kt>")
        sys.exit(1)
    
    target_file = sys.argv[1]
    if not os.path.exists(target_file):
        print(f"File not found: {target_file}")
        sys.exit(1)
        
    patch_licence_handler(target_file)
