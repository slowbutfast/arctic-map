# **Alaska Railways**

**Theme:** Infrastructure
**Subtheme:** Transportation
**Layer Name in Database:** `a_gis_osm_railways_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Transportation** subcategory.
3. Check the box next to **Alaska Railways** to display it on the map.

--- 

**Title:** gis_osm_railways_free_1  
**Abstract:** This dataset represents railways in the state of Alaska. All of the entries contain info about the code, existence of bridges and tunnels, and feature type, and many of the railways have a name.   
**Purpose:**The dataset aims to provide the locations and identities of railroads throughout Alaska to aid with development, transportation, and spatial reference.   
**Keywords:** Alaska, OSM, Railways, Trains, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 64.941199 deg; Bottom: 53.883157 deg; Left: \-166.531653 deg; Right: \-131.641250 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which many rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis_osm_railways_free_1 | WGS 1984 | Shapefile, Polyline | 1144 | 9 | FID | double |  |
|  |  |  |  |  | Shape | Polyline |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 6101, 6106, 6107, or 6108 |
|  |  |  |  |  | fclass | Text (28) | Funicular, minuature_railway, narrow_gauge, or rail. Corresponds to code attribute. |
|  |  |  |  |  | name | Text (100) | Name of the railway. Many are blank.  |
|  |  |  |  |  | layer | Double (12, 0\) | \-1, 0, or 1\. Not sure what this corresponds to. |
|  |  |  |  |  | bridge | Text (1) | T or F corresponding to true or false.  |
|  |  |  |  |  | tunnel | Text (1) | T or F corresponding to true or false.  |