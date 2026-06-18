# **Alaska A Places of Interest (polygon)**

**Theme:** Socioeconomic
**Subtheme:** Human Settlements
**Layer Name in Database:** `a_gis_osm_pois_a_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Human Settlements** subcategory.
3. Check the box next to **Alaska A Places of Interest (polygon)** to display it on the map.

--- 

**Title:** gis_osm_pois_a_free_1  
**Abstract:** This dataset represents places of public interest in the state of Alaska. All of the entries contain info about the code and feature type, and almost all places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of places of interest throughout Alaska to aid with development, public interest, and spatial reference.   
**Keywords:** Alaska, OSM, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.332432 deg; Bottom: 51.715068 deg; Left: \-177.200597 deg; Right: \-129.896222 deg

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
| gis_osm_pois_a_free_1 | WGS 1984 | Shapefile, Polygon | 6174 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many unique 4-digit identifying codes beginning with 2\. |
|  |  |  |  |  | fclass | Text (28) | Describes the business or public place type (bakery, artwork, university, water_well, zoo, etc) |
|  |  |  |  |  | name | Text (100) | Name of location. Most places have a name but many are empty |