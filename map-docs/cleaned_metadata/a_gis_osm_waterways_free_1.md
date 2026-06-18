# **Alaska Waterways**

**Theme:** Environmental
**Subtheme:** Water Resources
**Layer Name in Database:** `a_gis_osm_waterways_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Environmental** category.
2. Expand the **Water Resources** subcategory.
3. Check the box next to **Alaska Waterways** to display it on the map.

--- 

**Title:** gis_osm_waterways_free_1  
**Abstract:** This dataset represents waterways in the state of Alaska. All of the entries contain info about the code and feature type, and many of the waterways have a name.   
**Purpose:** The dataset aims to provide the locations and identities of waterways in Alaska to aid with development, conservation, water drainage, and spatial reference.   
**Keywords:** Alaska, OSM, Water, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.322976 deg; Bottom: 51.610800 deg; Left: \-178.872271 deg; Right: \-129.796996 deg

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
| gis_osm_waterways_free_1 | WGS 1984 | Shapefile, Polyline | 429,548 | 7 | FID | double |  |
|  |  |  |  |  | Shape | Polyline |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 8101, 8102, 8103, or 8104\. |
|  |  |  |  |  | fclass | Text (28) | canal, drain, river, or stream. Corresponds to code attribute.  |
|  |  |  |  |  | width | Long | Width of waterway. Many are 0, and no units are given. Values range from whole numbers 1-10, and 12, 15, 20, 22, 30, and 60\. |
|  |  |  |  |  | name | Text (100) | Name of the waterway. Many are blank.  |