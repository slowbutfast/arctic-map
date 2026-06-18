# **Alaska Water A**

**Theme:** Environmental
**Subtheme:** Water Resources
**Layer Name in Database:** `a_gis_osm_water_a_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Environmental** category.
2. Expand the **Water Resources** subcategory.
3. Check the box next to **Alaska Water A** to display it on the map.

--- 

**Title:** gis_osm_water_a_free_1  
**Abstract:** This dataset represents water bodies in the state of Alaska. All of the entries contain info about the code and feature type, and many of the places have a name.   
**Purpose:** The dataset aims to provide the locations and identities of water bodies/sources in Alaska to aid with development, conservation, and spatial reference.   
**Keywords:** Alaska, OSM, Water, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.387297 deg; Bottom: 51.232347 deg; Left: \-179.126616 deg; Right: \-129.518398 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which many rows are blank, has each attribute filled, creating a nearly complete dataset.   
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
| gis_osm_water_a_free_1 | WGS 1984 | Shapefile, Polygon | 239,264 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 8200, 8201, 8202, 8203, 8211, or 8221\. |
|  |  |  |  |  | fclass | Text (28) | Dock, Glacier, reservoir, wetland, water, or riverbank. Corresponds to code attribute.  |
|  |  |  |  |  | name | Text (100) | Name of the water body. Many are blank.  |