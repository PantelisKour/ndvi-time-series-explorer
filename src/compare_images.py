import ee
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# Initialize Earth Engine
ee.Initialize(project='643379335949') # your project id

# Forest Poikilo Mountain, Chaidari
# Coordinates of the area
area = ee.Geometry.Rectangle([23.660, 38.030, 23.690, 38.055])

print("🌲 Analysis: Forest Poikilo Mountain, Chaidari")
print("Download images Sentinel-2...")

# Image from 2020
image_2020 = ee.ImageCollection('COPERNICUS/S2_SR') \
    .filterBounds(area) \
    .filterDate('2020-06-01', '2020-08-31') \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10)) \
    .median()  # Median to remove clouds

# Image from 2025
image_2025 = ee.ImageCollection('COPERNICUS/S2_SR') \
    .filterBounds(area) \
    .filterDate('2025-01-01', '2025-02-15') \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10)) \
    .median()

# Calculate NDVI
ndvi_2020 = image_2020.normalizedDifference(['B8', 'B4']) # Near Infrared band(NIR) - Red / NIR + Red
ndvi_2025 = image_2025.normalizedDifference(['B8', 'B4']) # Near Infrared band(NIR) - Red / NIR + Red

# Calculate change
ndvi_change = ndvi_2025.subtract(ndvi_2020) # ndvi_2025 - ndvi_2020

# Visualization parameters
ndvi_params = {
    'min': 0, # min value of ndvi
    'max': 1, # max value of ndvi
    'palette': ['brown', 'yellow', 'lightgreen', 'darkgreen'] # color palette
}

change_params = {
    'min': -0.5, # min value of change
    'max': 0.5, # max value of change
    'palette': ['red', 'white', 'green'] # color palette
}

rgb_params = {
    'bands': ['B4', 'B3', 'B2'], # Red, Green, Blue
    'min': 0, # min value of rgb
    'max': 3000, # max value of rgb
    'gamma': 1.4 # gamma correction
}

print("Creating visualization...")

# Get URLs for the images
url_rgb_2020 = image_2020.visualize(**rgb_params).getThumbURL({'region': area.getInfo(), 'dimensions': 512})
url_rgb_2025 = image_2025.visualize(**rgb_params).getThumbURL({'region': area.getInfo(), 'dimensions': 512})
url_ndvi_2020 = ndvi_2020.visualize(**ndvi_params).getThumbURL({'region': area.getInfo(), 'dimensions': 512})
url_ndvi_2025 = ndvi_2025.visualize(**ndvi_params).getThumbURL({'region': area.getInfo(), 'dimensions': 512})
url_change = ndvi_change.visualize(**change_params).getThumbURL({'region': area.getInfo(), 'dimensions': 512})

# Download images
def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

img_rgb_2020 = download_image(url_rgb_2020)
img_rgb_2025 = download_image(url_rgb_2025)
img_ndvi_2020 = download_image(url_ndvi_2020)
img_ndvi_2025 = download_image(url_ndvi_2025)
img_change = download_image(url_change)

# Calculate statistics
stats_2020 = ndvi_2020.reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=area,
    scale=10
).getInfo()

stats_2025 = ndvi_2025.reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=area,
    scale=10
).getInfo()

mean_2020 = stats_2020['nd']
mean_2025 = stats_2025['nd']
change = mean_2025 - mean_2020

print(f"\n📊 RESULTS:")
print(f"Mean NDVI Summer 2020: {mean_2020:.3f}")
print(f"Mean NDVI Summer 2025: {mean_2025:.3f}")
print(f"Change: {change:.3f} ({change*100:.1f}%)")

# Create the plot
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Row 1: RGB images
axes[0, 0].imshow(img_rgb_2020)
axes[0, 0].set_title('RGB - Summer 2020', fontweight='bold', fontsize=12)
axes[0, 0].axis('off')

axes[0, 1].imshow(img_rgb_2025)
axes[0, 1].set_title('RGB - Summer 2025', fontweight='bold', fontsize=12)
axes[0, 1].axis('off')

axes[0, 2].imshow(img_change)
axes[0, 2].set_title('NDVI Change\n(Red=Decrease, Green=Increase)', fontweight='bold', fontsize=12)
axes[0, 2].axis('off')

# Row 2: NDVI images
axes[1, 0].imshow(img_ndvi_2020)
axes[1, 0].set_title(f'NDVI - Summer 2020\n(Mean: {mean_2020:.3f})', fontweight='bold', fontsize=12)
axes[1, 0].axis('off')

axes[1, 1].imshow(img_ndvi_2025)
axes[1, 1].set_title(f'NDVI - Summer 2025\n(Mean: {mean_2025:.3f})', fontweight='bold', fontsize=12)
axes[1, 1].axis('off')

# Statistics panel
axes[1, 2].axis('off')
stats_text = f"""
🌲 Forest Poikilo Mountain
   Chaidari, Attica

📊 Statistics:

Summer 2020:
  NDVI = {mean_2020:.3f}

Summer 2025:
  NDVI = {mean_2025:.3f}

Change:
  {change:+.3f} ({change*100:+.1f}%)

{'✅ Increase in vegetation' if change > 0 else '⚠️ Decrease in vegetation'}

"""
axes[1, 2].text(0.1, 0.5, stats_text, fontsize=11, verticalalignment='center',
                family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.suptitle('NDVI Comparison: Forest Poikilo Mountain, Chaidari', 
             fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()

# Save
output_file = '../data/poikilo_oros_comparison.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"\n💾 Image saved: {output_file}")

plt.show()