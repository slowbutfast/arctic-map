# **Alaska Places of Worship (point)**

**Theme:** Socioeconomic
**Subtheme:** Human Settlements
**Layer Name in Database:** `a_gis_osm_pofw_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Human Settlements** subcategory.
3. Check the box next to **Alaska Places of Worship (point)** to display it on the map.

--- 

**Title:** gis_osm_pofw_free_1  
**Abstract:** This dataset represents places of worship in the state of Alaska. All of the entries contain info about the code and religion type, and almost all places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of places of worship throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Worship, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 66.898244 deg; Bottom: 51.866767 deg; Left: \-176.666724 deg; Right: \-131.681143 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which 7 rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis_osm_pofw_free_1 | WGS 1984 | Shapefile, Point | 48 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of 6 unique 4-digit codes, each beginning with 3 |
|  |  |  |  |  | fclass | Text (28) | Religion type of place of worship (christian_catholic, christian_lutheran, etc) corresponding to code attribute |
|  |  |  |  |  | name | Text (100) | Name of place of worship. 7 do not have names. |