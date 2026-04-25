from pathlib import Path
import zipfile
import gdown

FILES = {
    "animals.zip": {
        "id": "14yuKcpUMqZjrlsymswOxEcdiIL2oLMyJ",
        "extract_to": "images",
    },
    "digits.zip": {
        "id": "1XWbVjoOs60D7EW-zy2qVwYe2z3vm-jqN",
        "extract_to": "digits",
    },
}

DATA_DIR = Path("data")


def unzip_file(zip_path: Path, extract_to: Path):
    print(f"Extracting {zip_path} → {extract_to}")
    extract_to.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_to)


def main():
    DATA_DIR.mkdir(exist_ok=True)

    for filename, meta in FILES.items():
        file_id = meta["id"]
        extract_to = Path(meta["extract_to"])

        zip_path = DATA_DIR / filename
        url = f"https://drive.google.com/uc?id={file_id}"

        # Download
        print(f"\nDownloading {filename}...")
        gdown.download(url, str(zip_path), quiet=False)

        # Unzip
        unzip_file(zip_path, extract_to)

        # Optional: remove archive after extraction
        zip_path.unlink()
        print(f"Removed archive {zip_path}")

    print("\nAll datasets ready.")


if __name__ == "__main__":
    main()