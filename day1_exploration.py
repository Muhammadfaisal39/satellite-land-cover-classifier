# Satellite Land Cover Classifier
# Day 1 — Dataset Exploration and Visualization
# Author: Muhammad Faisal
# GitHub: github.com/Muhammadfaisal39

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import random

# -----------------------------------------------
# PART 1 — Setup
# -----------------------------------------------

dataset_path = '/content/drive/MyDrive/satellite-project/EuroSAT'

# Load only valid image class folders
classes = sorted([
    c for c in os.listdir(dataset_path)
    if os.path.isdir(os.path.join(dataset_path, c))
    and len(os.listdir(os.path.join(dataset_path, c))) > 0
    and not c.startswith('.')
    and not c.startswith('_')
])

print("Total classes:", len(classes))
print("Classes:", classes)

# -----------------------------------------------
# PART 2 — Count Images Per Class
# -----------------------------------------------

total = 0
class_counts = {}

for class_name in classes:
    class_path = os.path.join(dataset_path, class_name)
    image_files = [
        f for f in os.listdir(class_path)
        if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.tif')
    ]
    class_counts[class_name] = len(image_files)
    total += len(image_files)

print("\n=== IMAGE COUNTS ===")
for name, count in class_counts.items():
    print(f"  {name:<25} {count} images")
print(f"\nTotal images: {total}")

# -----------------------------------------------
# PART 3 — Visualize One Sample Per Class
# -----------------------------------------------

fig, axes = plt.subplots(2, 5, figsize=(15, 7))
fig.suptitle('EuroSAT Dataset — One Sample Per Class',
             fontsize=16, fontweight='bold')

for idx, class_name in enumerate(classes):
    row = idx // 5
    col = idx % 5
    class_path = os.path.join(dataset_path, class_name)
    image_files = [
        f for f in os.listdir(class_path)
        if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.tif')
    ]
    image_file = random.choice(image_files)
    img = mpimg.imread(os.path.join(class_path, image_file))
    axes[row, col].imshow(img)
    axes[row, col].set_title(class_name, fontsize=10, fontweight='bold')
    axes[row, col].axis('off')

plt.tight_layout()
plt.savefig('sample_images.png', dpi=150, bbox_inches='tight')
plt.show()
print("Sample images saved!")

# -----------------------------------------------
# PART 4 — Class Distribution Chart
# -----------------------------------------------

plt.figure(figsize=(12, 5))
plt.bar(class_counts.keys(), class_counts.values(),
        color='steelblue', edgecolor='navy', linewidth=0.5)
plt.title('EuroSAT — Class Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Land Cover Class', fontsize=12)
plt.ylabel('Number of Images', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('class_distribution.png', dpi=150, bbox_inches='tight')
plt.show()
print("Class distribution saved!")
