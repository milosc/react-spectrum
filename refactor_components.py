import os
import json
import shutil
import re

manifest_path = 'component-library/manifests/components.json'
src_path = 'component-library/src'
specs_api_path = 'component-library/specs/api'
specs_a11y_path = 'component-library/specs/accessibility'
specs_test_path = 'component-library/specs/test'

with open(manifest_path, 'r') as f:
    manifest = json.load(f)

components = list(manifest['components'].keys())

# Helper to update imports
def update_imports(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace from './' with from '../'
    # Use regex to match exact import patterns to avoid false positives
    # Matches: from './Something' or from "./Something"
    new_content = re.sub(r"from\s+['\"](\./)([^'\"]+)['\"]", r"from '../\2'", content)
    
    if content != new_content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated imports in {file_path}")

for component in components:
    # 1. Create Directory
    comp_dir = os.path.join(src_path, component)
    if not os.path.exists(comp_dir):
        os.makedirs(comp_dir)
    
    # 2. Move Source File
    # Check for .tsx or .ts
    src_file_tsx = os.path.join(src_path, f"{component}.tsx")
    src_file_ts = os.path.join(src_path, f"{component}.ts")
    
    target_src = None
    
    if os.path.exists(src_file_tsx):
        target_src = os.path.join(comp_dir, f"{component}.tsx")
        shutil.move(src_file_tsx, target_src)
    elif os.path.exists(src_file_ts):
        target_src = os.path.join(comp_dir, f"{component}.ts")
        shutil.move(src_file_ts, target_src)
    
    if target_src:
        # Create index.ts
        with open(os.path.join(comp_dir, 'index.ts'), 'w') as f:
            f.write(f"export * from './{component}';\n")
        
        # Update imports in the moved source file
        update_imports(target_src)
        
    else:
        print(f"Warning: Source for {component} not found.")

    # 3. Move Specs
    # API
    api_file = os.path.join(specs_api_path, f"{component}.md")
    if os.path.exists(api_file):
        shutil.move(api_file, os.path.join(comp_dir, f"{component}.api.md"))
    
    # Accessibility
    a11y_file = os.path.join(specs_a11y_path, f"{component}.mdx")
    if os.path.exists(a11y_file):
        shutil.move(a11y_file, os.path.join(comp_dir, f"{component}.a11y.mdx"))

    # Tests (Pattern matching)
    # Move files starting with ComponentName.test or ComponentName.ssr.test
    if os.path.exists(specs_test_path):
        for f in os.listdir(specs_test_path):
            if f.startswith(f"{component}."):
                 shutil.move(os.path.join(specs_test_path, f), os.path.join(comp_dir, f))

print("Refactoring complete.")
