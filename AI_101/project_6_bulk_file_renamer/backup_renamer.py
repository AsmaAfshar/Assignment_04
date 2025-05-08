import os
import json

BACKUP_FILE = "rename_backup.json"

def bulk_rename(folder_path, prefix="file_", start_index=1):
    try:
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        original_names = {}

        for count, filename in enumerate(files, start=start_index):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}{count}{ext}"
            src = os.path.join(folder_path, filename)
            dst = os.path.join(folder_path, new_name)
            os.rename(src, dst)
            original_names[new_name] = filename
            print(f"Renamed: {filename} → {new_name}")

        # Save original names for restoration
        with open(os.path.join(folder_path, BACKUP_FILE), "w") as f:
            json.dump(original_names, f)

        print("✅ Renaming complete. Backup saved.")

    except Exception as e:
        print(f"❌ Error: {e}")


def restore_names(folder_path):
    try:
        backup_path = os.path.join(folder_path, BACKUP_FILE)
        if not os.path.exists(backup_path):
            print("❌ No backup file found.")
            return

        with open(backup_path, "r") as f:
            name_map = json.load(f)

        for new_name, original_name in name_map.items():
            src = os.path.join(folder_path, new_name)
            dst = os.path.join(folder_path, original_name)
            if os.path.exists(src):
                os.rename(src, dst)
                print(f"Restored: {new_name} → {original_name}")

        os.remove(backup_path)
        print("✅ Restore complete and backup file deleted.")

    except Exception as e:
        print(f"❌ Error during restore: {e}")


def main():
    print("Bulk File Renamer")
    action = input("Type 'rename' to rename files or 'restore' to undo renaming: ").strip().lower()
    folder = input("Enter the full path to the folder: ").strip()

    if action == "rename":
        prefix = input("Enter a prefix for the new filenames (default: 'file_'): ").strip() or "file_"
        start = input("Enter starting index (default: 1): ").strip()
        start = int(start) if start.isdigit() else 1
        bulk_rename(folder, prefix, start)
    elif action == "restore":
        restore_names(folder)
    else:
        print("❌ Invalid action.")

if __name__ == "__main__":
    main()
