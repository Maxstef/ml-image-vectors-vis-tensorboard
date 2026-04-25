from pathlib import Path
from PIL import Image
import torch
import torchvision.models as models
import numpy as np
import csv

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
IMG_SIZE = 100
EXTS = {".jpg", ".jpeg", ".png"}


def load_model():
    weights = models.ResNet18_Weights.DEFAULT
    base = models.resnet18(weights=weights)
    model = torch.nn.Sequential(*list(base.children())[:-1])
    model.to(DEVICE).eval()
    transform = weights.transforms()
    return model, transform


def get_image_paths(root: str):
    paths = sorted(
        [p for p in Path(root).rglob("*") if p.suffix.lower() in EXTS]
    )
    if not paths:
        raise ValueError(f"No images found in {root}")
    return paths


def extract_vectors(model, transform, image_paths):
    vecs = []

    for p in image_paths:
        with Image.open(p) as img:
            img = img.convert("RGB")
            batch = transform(img).unsqueeze(0).to(DEVICE)
            with torch.no_grad():
                vec = model(batch)

        vecs.append(vec.squeeze().cpu().numpy())

    return vecs


def save_metadata(image_paths, out_path):
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["label", "file"])

        for p in image_paths:
            w.writerow([p.parent.name, p.name])


def save_sprite(image_paths, out_path):
    images = []
    for p in image_paths:
        with Image.open(p) as img:
            images.append(img.resize((IMG_SIZE, IMG_SIZE)))

    grid = int(np.ceil(np.sqrt(len(images))))
    sprite = Image.new("RGB", (IMG_SIZE * grid, IMG_SIZE * grid))

    for idx, img in enumerate(images):
        r, c = divmod(idx, grid)
        sprite.paste(img, (c * IMG_SIZE, r * IMG_SIZE))

    sprite.save(out_path)


def save_vectors(vecs, out_path):
    with open(out_path, "w") as f:
        csv.writer(f, delimiter="\t").writerows(vecs)


def build_dataset(root: str, name: str, model, transform):
    print(f"\nProcessing dataset: {name}")

    image_paths = get_image_paths(root)
    vecs = extract_vectors(model, transform, image_paths)

    vis = Path("vis")
    vis.mkdir(exist_ok=True)

    save_vectors(vecs, vis / f"{name}_feature_vecs.tsv")
    save_metadata(image_paths, vis / f"{name}_metadata.tsv")
    save_sprite(image_paths, vis / f"{name}_sprite.jpg")


def main():
    model, transform = load_model()

    build_dataset("images", "animals", model, transform)
    build_dataset("digits", "digits", model, transform)

    print("\nProjector files created in ./vis")


if __name__ == "__main__":
    main()