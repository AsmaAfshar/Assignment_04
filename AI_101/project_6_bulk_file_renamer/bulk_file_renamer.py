import os

def bulk_rename(folder_path, prefix="file_", start_index=1):
    try:
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        print(f"Found {len(files)} files. Starting renaming...")

        for count, filename in enumerate(files, start=start_index):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}{count}{ext}"
            src = os.path.join(folder_path, filename)
            dst = os.path.join(folder_path, new_name)
            os.rename(src, dst)
            print(f"Renamed: {filename} → {new_name}")

        print("✅ Renaming complete.")

    except FileNotFoundError:
        print("❌ The specified folder does not exist.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# Example usage
if __name__ == "__main__":
    folder = input("Enter the full path to the folder: ").strip()
    prefix = input("Enter a prefix for the new filenames (default: 'file_'): ").strip() or "file_"
    start = input("Enter starting index (default: 1): ").strip()
    start = int(start) if start.isdigit() else 1

    bulk_rename(folder, prefix, start)
