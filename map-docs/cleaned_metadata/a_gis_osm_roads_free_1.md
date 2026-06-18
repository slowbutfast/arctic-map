# **Alaska Roads**

**Theme:** Infrastructure
**Subtheme:** Transportation
**Layer Name in Database:** `a_gis_osm_roads_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Transportation** subcategory.
3. Check the box next to **Alaska Roads** to display it on the map.

--- 

**Title:** gis_osm_roads_free_1  
**Abstract:** This dataset represents roads in the state of Alaska. All of the entries contain info about the code, existence of bridges and tunnels, and feature type, and most of the roads have a name.   
**Purpose:**The dataset aims to provide the locations and identities of roads throughout Alaska to aid with development, transportation, and spatial reference.   
**Keywords:** Alaska, OSM, Roads, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.386462 deg; Bottom: 51.591498 deg; Left: \-177.200845 deg; Right: \-129.872230 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
The attribute “ref” was deleted because it contained many long codes, or were blank, that are difficult to understand its meaning as they don’t have much in common.

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
| gis_osm_roads_free_1 | WGS 1984 | Shapefile, Polyline | 97,177 | 11 | FID | double |  |
|  |  |  |  |  | Shape | Polyline |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many unique identifying codes, each beginning with 5\. |
|  |  |  |  |  | fclass | Text (28) | Cycleway, path, track_grade3, busway, etc. Corresponds to code attribute. |
|  |  |  |  |  | name | Text (100) | Name of the road. Many are blank.  |
|  |  |  |  |  | oneway | Text (1) | B, F, or T. Unsure what B corresponds to..maybe both? |
|  |  |  |  |  | maxspeed | Short | Seems to be maxspeed of road, but does not follow even numbers (ex. 88, 96, 104, 64, 72).  |
|  |  |  |  |  | layer | Double (12, 0\) | \-2. \-1, 0, 1, 2, or 5\. Not sure what this corresponds to. |
|  |  |  |  |  | bridge | Text (1) | T or F corresponding to true or false.  |
|  |  |  |  |  | tunnel | Text (1) | T or F corresponding to true or false.  |