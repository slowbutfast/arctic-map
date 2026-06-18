# Arctic Map Dataset Documentation

This directory contains the documentation, registry, and metadata for the geospatial datasets displayed in the Arctic Map Explorer. 

Below is a plain English guide to the files uploaded here, what they represent, and how they relate to the map visualization.

---

## 1. The Datasets We Uploaded

### A. The Layer Registry (CSV)
* **File**: `CPAD Datasets Theme & Subtheme Organization V2 - CPAD WebGIS App.csv`
* **What it shows**: This is the master index of the **83 active layers** visible on the website. For every layer, it defines:
  * **Theme**: The top-level category (e.g., *Socioeconomic*, *Environmental*, *Infrastructure*).
  * **Subtheme**: The sub-category (e.g., *Education*, *Water Resources*, *Transportation*).
  * **Layer Name**: The database table identifier (e.g., `a_alaska_schools`).
  * **Display Name**: The readable label shown to users in the sidebar (e.g., `Alaska Schools`).

### B. The Metadata Record (Markdown)
* **File**: `Meta Data based on ISO 19115 Standards.md`
* **What it shows**: This file contains detailed background information (based on the international ISO 19115 geographic metadata standard) for the datasets. It answers key questions researchers have:
  * **Abstract & Purpose**: What the dataset measures and why it was collected.
  * **Geographic Extent**: The latitude/longitude boundaries (bounding box) of the data.
  * **Coordinate Reference System (CRS)**: Almost all layers use **WGS 1984**, ensuring they align perfectly when overlaid on the map.
  * **Data Dictionary**: A list of attributes (columns) inside each layer and a description of what they represent (e.g., the `primary_fu` column in the Global Power Plants layer represents the primary fuel type).

---

## 2. How the Datasets Are Displayed on the Map

The map explorer uses Mapbox GL JS to render these datasets on an interactive 3D globe. They are organized to match the Theme and Subtheme structure:

1. **Sidebar Navigation**: In the left-hand panel of the website, datasets are grouped hierarchically:
   * **Theme Accordion**: Clicking **Socioeconomic**, **Environmental**, or **Infrastructure** expands the theme.
   * **Subtheme Group**: Inside the theme, layers are grouped under headers (e.g., *Education*, *Energy*, *Animal & Plant Distribution*).
2. **Interactive Toggles**: Checking a box next to a layer's display name loads its spatial geometry onto the map:
   * **Points**: Used for specific locations (e.g., *Alaska Schools*, *Global Power Plants*, *Alaskan Airports*).
   * **Lines**: Used for networks and linear paths (e.g., *Oil Pipelines*, *10m Scale Railroads*, *Shipping Routes*).
   * **Polygons**: Used for areas and boundaries (e.g., *Alaska Land Use*, *Arctic Regions*, *Extended Continental Shelf Claims Areas*).

---

## 3. Cleaned Metadata for the AI Chatbot

To help the RAG chatbot answer questions accurately without getting confused by a single massive file, we split and cleaned these resources using `process_metadata.py`. 

The self-contained, per-dataset markdown files are stored in the **[cleaned_metadata/](cleaned_metadata/)** folder. These are indexed by the AI to retrieve both descriptive text and database schemas instantly.
