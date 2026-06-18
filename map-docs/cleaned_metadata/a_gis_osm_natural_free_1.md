# **Alaska Natural Features (point)**

**Theme:** Environmental
**Subtheme:** Land Cover
**Layer Name in Database:** `a_gis_osm_natural_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Environmental** category.
2. Expand the **Land Cover** subcategory.
3. Check the box next to **Alaska Natural Features (point)** to display it on the map.

--- 

**Title:** gis_osm_natural_free_1  
**Abstract:** This dataset represents natural features in the state of Alaska. All of the entries contain info about the name of the feature, code, and feature type.   
**Purpose:**The dataset aims to provide the locations and identities of natural features throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Nature, Beach, Glacier, Volcano, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 70.170434 deg; Bottom: 51.223554 deg; Left: \-179.109405 deg; Right: \-129.518398 deg

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
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: OpenStreetMap (OSM)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gis_osm_natural_free_1 | WGS 1984 | Shapefile, Point | 4,876 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm_id | Text (12) |  |
|  |  |  |  |  | code | Short | One of 8 unique 4-digit codes defining type of land feature |
|  |  |  |  |  | fclass | Text (28) | Beach, cave_entrance, volcano, cliff, glacier, peak, spring, or tree. Correlates to code attribute |
|  |  |  |  |  | name | Text (100) | Name of feature. Each feature has a name here.  |