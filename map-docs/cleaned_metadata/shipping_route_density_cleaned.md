# **Global Shipping Route Density**

**Theme:** Infrastructure
**Subtheme:** Transportation
**Layer Name in Database:** `shipping_route_density_cleaned`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Transportation** subcategory.
3. Check the box next to **Global Shipping Route Density** to display it on the map.

--- 

**Title:** Shipping_Route_Density_Cleaned  
**Abstract:** This dataset provides a comprehensive spatial representation of global maritime activity by quantifying the intensity of vessel traffic across the world's oceans. Each grid cell's value (represented by the gridcode attribute) indicates the total cumulative number of Automatic Identification System (AIS) positions reported by all vessels within that cell. The dataset was generated from an analysis of hourly AIS positions by the International Monetary Fund (IMF) as part of their World Seaborne Trade Monitoring System, with support from the World Bank's ESMAP and PROBLUE programs.  
**Purpose:** To be used in analysis and visualization. This datatset can be used to summarize the total values within a polygon (using zonal statistics) to obtain statistical measures like minimum, maximum, mean, and standard deviation; this could be useful for comparing different areas.  
**Keywords:** trade, transport, transportatio, offshore wind, seaborne trade, shipping density, shipping routes, vessel traffic, AIS, oceans, marine, marine spatial planning, esri_oceans  
**Temporal Extent:**

* **Date**: Last updated May 3, 2021  
* **Time Period**: January 2015 \- February 2021

**Geographic Extent:** 

* Bounding Box:   
  * Top	85.003744	deg  
  * Bottom	51.255673	deg  
  * Left	\-180.002618	deg  
  * Right	180.001993	deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** 

* Projected Coordinate System: WGS 1984

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: All features have values for each of the attributes.  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization:  
  * Primary Data Analysis & Provider: International Monetary Fund (IMF), as part of their World Seaborne Trade Monitoring System.  
  * Supporting Programs: World Bank's ESMAP (Energy Sector Management Assistance Program) and PROBLUE programs.  
  * Compiled & Published by: Esri (within the ArcGIS Living Atlas, linked [here](https://www.arcgis.com/home/item.html?id=2f72eb72cc0b403bb19a7cd1853f3d94)).  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Shipping_Route_Density_Cleaned.shp | WGS 1984 | Polygon | 8,726,963 | 5 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | gridcode | Integer | total number of AIS (Automatic Identification System) positions reported by all vessels within that specific grid cell (or pixel |
|  |  |  |  |  | Shape_Leng | Double |  |
|  |  |  |  |  | Shape_Area | Double |  |