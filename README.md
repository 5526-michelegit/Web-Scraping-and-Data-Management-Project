
# Enhanced Real Estate Listings with Nearby Services Integration

## Description
This project enriches real estate search by combining property listings with information about nearby services (schools, public transportation, shops, etc.). The goal is to provide prospective buyers or renters with a full context of the neighborhood in addition to traditional data like price and size.

## Table of Contents
1. [Objectives](#objectives)  
2. [Repository Structure](#repository-structure)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Usage](#usage)  
7. [Methodology](#methodology)  
8. [Database](#database)  
9. [Visualizations & Reports](#visualizations--reports)  
10. [Presentation](#presentation)  

## Objectives
- **Data Collection**: Scrape real estate listings from Idealista and service points from PagineGialle.  
- **Spatial Integration**: Geolocate each point of interest and calculate its proximity to properties.  
- **Searchable Database**: Build a MongoDB repository where each property document includes its nearby services.  
- **Analysis & Visualization**: Provide notebooks and scripts to explore spatial and price patterns.  
- **Documentation**: Deliver a detailed report and a concise presentation of the project.

## Repository Structure
```text
├── Dataset1 - Idealista/         # Scripts & notebooks for scraping Idealista
├── Dataset2 - PagineGialle/      # Scripts & notebooks for scraping PagineGialle
├── Dataset3 - Final (Merge)/     # Code to merge and clean previous datasets
├── Report/                       # Final report (PDF and/or notebook) with methodology & results
├── Visualization/                # Notebooks & scripts for charts and interactive maps
├── presentation/                 # Presentation slides (PowerPoint or PDF)
└── README.md                     # This documentation file
```

## Requirements

* **Python 3.8+**
* **MongoDB** (local or remote)
* **Python Libraries**:

  * `selenium`
  * `pandas`
  * `requests`
  * `pymongo`
  * `geopy` or `bingmaps-api`
  * `folium` (optional, for maps)
  * `jupyter` (for notebooks)

> **Note**: If `requirements.txt` is missing, install manually:
>
> ```bash
> pip install selenium pandas requests pymongo geopy folium jupyter
> ```

## Installation

1. **Clone** the repository:

   ```bash
   git clone https://github.com/5526-michelegit/Web-Scraping-and-Data-Management-Project.git
   cd Web-Scraping-and-Data-Management-Project
   ```
2. **Configure** environment variables:

   * `MONGODB_URI`: MongoDB connection string.
   * `BING_MAPS_API_KEY`: API key for geocoding (if using Bing Maps).
3. **Create** a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/Mac
   venv\Scripts\activate.bat      # Windows
   ```
4. **Install** dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Dataset1 – Idealista**

   ```bash
   cd "Dataset1 - Idealista"
   python scrape_idealista.py
   jupyter notebook idealista_preprocessing.ipynb
   ```
2. **Dataset2 – PagineGialle**

   ```bash
   cd "../Dataset2 - PagineGialle"
   python scrape_paginegialle.py
   jupyter notebook paginegialle_preprocessing.ipynb
   ```
3. **Dataset3 – Merge & Cleaning**

   ```bash
   cd "../Dataset3 - Final (Merge)"
   python merge_datasets.py
   jupyter notebook final_cleaning.ipynb
   ```
4. **Visualizations**

   ```bash
   cd "../Visualization"
   jupyter notebook data_visualization.ipynb
   ```
5. **Report**
   Open the PDF or notebook in the `Report/` folder to review methodology, analyses, and results.
6. **Presentation**
   Open `presentation/slides.pptx` for a concise project overview.

## Methodology

1. **Web Scraping**

   * Use **Selenium** to navigate pages and bypass anti-bot protections.
   * Extract property details: price, area, surface, address.
2. **Data Preprocessing**

   * Clean missing values and normalize columns.
   * Standardize address formats.
3. **Geocoding**

   * Convert addresses to coordinates (latitude, longitude) via Bing Maps API.
   * Calculate service-to-property distances using the Haversine formula.

## Database

* **MongoDB** as the primary datastore.
* Nested schema: each `property` document contains an array `nearby_services` with details for each service (name, type, distance).
* Sample document:

  ```json
  {
    "address": "Corso Buenos Aires, Milan",
    "price": 250000,
    "coordinates": { "lat": 45.467, "lng": 9.192 },
    "nearby_services": [
      { "name": "Scuola Media Dante", "type": "school", "distance_m": 300 },
      { "name": "Metro Lima", "type": "transport", "distance_m": 450 },
      ...
    ]
  }
  ```

## Visualizations & Reports

* The `Visualization/` directory contains notebooks that produce:

  * Interactive maps with **Folium**.
  * Price distribution charts by neighborhood.
  * Heatmaps of service density.
* The final report in `Report/` summarizes key findings, challenges, and conclusions.

## Presentation

The `presentation/` folder holds slides (PowerPoint or PDF) for both technical and non-technical audiences.
