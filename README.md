# 🌍 NDVI Time-Series Explorer

Satellite-based vegetation monitoring using Sentinel-2 data and Google Earth Engine.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Earth Engine](https://img.shields.io/badge/Earth_Engine-API-green.svg)

---

## 📖 Overview

This project analyzes vegetation changes over time using:
- **Sentinel-2** satellite imagery (10m resolution)
- **NDVI** (Normalized Difference Vegetation Index)
- **Google Earth Engine** for cloud-based processing

**Use cases:**
- 🌲 Forest monitoring & deforestation detection
- 🔥 Post-fire vegetation recovery
- 🌾 Crop health monitoring
- 🏙️ Urban expansion tracking

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ndvi-time-series-explorer.git
cd ndvi-time-series-explorer
```

### 2. Install dependencies
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
```

### 3. Setup Google Earth Engine
```bash
earthengine authenticate
```

### 4. Run the comparison script
```bash
python src/compare_images.py
```

Or open the Jupyter notebook:
```bash
jupyter notebook notebooks/ndvi_comparison_tutorial.ipynb
```

---

## 📁 Project Structure
```
ndvi-time-series-explorer/
├── data/
│   └── *.png                   # Generated visualizations
├── notebooks/
│   └── ndvi_comparison_tutorial.ipynb  # Interactive tutorial
├── src/
│   ├── compare_images.py       # Before/after comparison
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Google Earth Engine API** - Cloud geospatial processing
- **Sentinel-2** - ESA satellite data (10m resolution)
- **Matplotlib** - Visualization
- **Pandas** - Data manipulation
- **Jupyter Notebook** - Interactive analysis

---

## 🌱 What is NDVI?

**NDVI** (Normalized Difference Vegetation Index) measures vegetation health:
```
NDVI = (NIR - Red) / (NIR + Red)
```

**Interpretation:**
- `0.6 - 1.0` → Dense vegetation (forests) 🌲
- `0.3 - 0.6` → Moderate vegetation (grassland) 🌾
- `0.0 - 0.3` → Sparse vegetation 🏜️
- `< 0.0` → Water, snow, bare soil

---

## 📊 Example Results

### Poikilo Oros Forest, Athens (2020 vs 2024)

![Example Output](data/example_result.png)

---

## 📚 Documentation

### Earth Engine Resources:
- [Python API Guide](https://developers.google.com/earth-engine/guides/python_install)
- [Sentinel-2 Dataset](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR)
- [NDVI Tutorial](https://developers.google.com/earth-engine/tutorials/tutorial_api_04)

---

## 🎯 Features

- ✅ Automated Sentinel-2 data fetching from Google Earth Engine
- ✅ Cloud filtering (<20% cloud coverage)
- ✅ NDVI calculation and visualization
- ✅ Multi-temporal comparison (before/after analysis)
- ✅ Interactive Jupyter notebook tutorial
- ✅ Exportable PNG visualizations

---

## 🔄 Example Use Cases

### 1. Forest Monitoring
Track deforestation or reforestation in protected areas.

### 2. Post-Fire Recovery
Monitor vegetation regrowth after wildfires (e.g., Greece 2018, 2021 fires).

### 3. Agricultural Monitoring
Assess crop health and irrigation effectiveness.

### 4. Urban Expansion
Quantify green space loss due to urbanization.

---

## 👤 Author

**Pantelis Kouridakis**
- 🔗 [LinkedIn](https://www.linkedin.com/in/pantelis-kouridakis/)
- 📧 kouridakispantelis@gmail.com
- 🌐 [Portfolio](https://pantkour-com.vercel.app/)

---

## 🙏 Acknowledgments

- **ESA** - Sentinel-2 satellite data
- **Google Earth Engine** - Cloud processing platform
- **Prometheus Space Technologies** - Wildfire prediction work experience

---

## 📝 License

MIT License

---

**⭐ If you find this useful, please star the repository!**