# **Alaska Places (point)**

**Theme:** Socioeconomic
**Subtheme:** Human Settlements
**Layer Name in Database:** `a_gis_osm_places_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Human Settlements** subcategory.
3. Check the box next to **Alaska Places (point)** to display it on the map.

--- 

**Title:** gis_osm_places_free_1  
**Abstract:** This dataset represents places, such as cities, towns, or islands, in the state of Alaska. All of the entries contain info about the code and feature type, and nearly all places have a name. Many also include population data.  
**Purpose:**The dataset aims to provide the locations and identities of populous places throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Island, Population, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.360450 deg; Bottom: 51.815832 deg; Left: \-177.947960 deg; Right: \-129.897266 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which 5 rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis_osm_places_free_1 | WGS 1984 | Shapefile, Point | 1,060 | 7 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of 8 unique 4-digit codes beginning with 1: 1001, 1002, 1003, 1004, 1010, 1020, 1041, 1050 |
|  |  |  |  |  | fclass | Text (28) | City, county, hamlet, Island, village, locality, suburb or town. Corresponds to code. |
|  |  |  |  |  | population | Long | 291,247 as max and 0 for many as min |
|  |  |  |  |  | name | Text (100) | Every place except for 5 have a name.  |