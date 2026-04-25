from pathlib import Path

EXTS = {".jpg", ".jpeg", ".png"}
MAX_PER_FOLDER = 100


def folders_with_images(root: Path):
    """Yield folders that directly contain images."""
    for path in root.rglob("*"):
        if path.is_dir():
            images = [p for p in path.iterdir() if p.suffix.lower() in EXTS]
            if images:
                yield path


def limit_images_per_folder(root: Path, max_per_folder: int):
    print(f"\nLimiting images under {root}")

    for folder in folders_with_images(root):
        images = sorted([p for p in folder.iterdir() if p.suffix.lower() in EXTS])

        if len(images) <= max_per_folder:
            continue

        for p in images[max_per_folder:]:
            p.unlink()

        print(f"{folder}: trimmed to {max_per_folder}")


def rename_with_folder_prefix(root: Path):
    print(f"\nRenaming images under {root}")

    for folder in folders_with_images(root):
        prefix = folder.name  # cow, dog, lion, digit class, etc.
        images = sorted([p for p in folder.iterdir() if p.suffix.lower() in EXTS])

        # temp rename to avoid collisions
        temp_paths = []
        for i, img_path in enumerate(images, start=1):
            tmp = folder / f"__tmp__{i}{img_path.suffix.lower()}"
            img_path.rename(tmp)
            temp_paths.append(tmp)

        # final rename
        for i, tmp in enumerate(temp_paths, start=1):
            final = folder / f"{prefix}_{i}{tmp.suffix.lower()}"
            tmp.rename(final)

        print(f"{folder}: renamed {len(images)} files")


def main():
    digits_root = Path("./digits")
    animals_root = Path("./images")

    # digits need limiting
    limit_images_per_folder(digits_root, MAX_PER_FOLDER)

    # rename everywhere (any depth)
    rename_with_folder_prefix(animals_root)
    rename_with_folder_prefix(digits_root)

    print("\nData preparation completed.")


if __name__ == "__main__":
    main()