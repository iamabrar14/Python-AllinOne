import os

def find_file(filename, search_path):
    matches = []
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            full_path = os.path.join(root, filename)
            matches.append(full_path)
    return matches

# --- User input ---
file_to_find = input("Enter the file name to search (with extension): ").strip()
start_directory = input("Enter the directory to start search (leave empty for current folder): ").strip()

if not start_directory:
    start_directory = os.getcwd()  # default to current directory

# --- Search operation ---
results = find_file(file_to_find, start_directory)

# --- Output ---
if results:
    print(f"\n✅ Found {len(results)} file(s):")
    for path in results:
        print(path)
else:
    print("❌ File not found.")
