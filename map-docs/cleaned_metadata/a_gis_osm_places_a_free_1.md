# **Alaska A Places (polygon)**

**Theme:** Socioeconomic
**Subtheme:** Human Settlements
**Layer Name in Database:** `a_gis_osm_places_a_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Human Settlements** subcategory.
3. Check the box next to **Alaska A Places (polygon)** to display it on the map.

--- 

**Title:** gis_osm_places_a_free_1  
**Abstract:** This dataset represents places, such as towns or islands, in the state of Alaska. All of the entries contain info about the name of the feature, code, and feature type. Many also include population data.  
**Purpose:**The dataset aims to provide the locations and identities of places throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Island, Population, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 74.102874 deg; Bottom: 51.214590 deg; Left: \-179.148286 deg; Right: \-124.393980 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row has each attribute filled, creating a complete dataset.   
* Consistency: 

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: N/A  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: OpenStreetMap (OSM)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gis_osm_places_a_free_1 | WGS 1984 | Shapefile, Polygon | 1,268 | 7 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of 6 unique 4-digit codes beginning with 1: 1001, 1002, 1003, 1004, 1020, 1050 |
|  |  |  |  |  | fclass | Text (28) | City, hamlet, Island, village, locality, or town. Corresponds to code. |
|  |  |  |  |  | population | Long | Many say 0, max says 569 |
|  |  |  |  |  | name | Text (100) | Name of place. Each row has a name.  |