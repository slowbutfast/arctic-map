# **Alaska Buildings**

**Theme:** Infrastructure
**Subtheme:** General
**Layer Name in Database:** `a_gis_osm_buildings_a_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **General** subcategory.
3. Check the box next to **Alaska Buildings** to display it on the map.

--- 

**Title:** gis_osm_buildings_a_free_1  
**Abstract:** This dataset represents buildings in the state of Alaska. Some of the buildings contain info about the building name or type.   
**Purpose:**The dataset aims to provide the locations and identities of buildings throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, buildings, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.378496 deg; Bottom: 51.714799 deg; Left: \-177.421022 deg; Right: \-129.970366 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
The attributes of code and flcass have been deleted from the original dataset due to each row having the same values of “1500” and “building”, respectively, to create this cleaned dataset.   
**Quality Information:**

* Accuracy:  
* Completeness: Not every row has a name or type, leading to an incomplete dataset.   
* Consistency: 

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: OpenStreetMap (OSM)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of record | Number of attributes | List of Attributes | Data Type | Notes-Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gis_osm_buildings_a_free_1.shp | WGS 1984 | Shapefile, polygon | 143,330 | 7 | FID | double | number |
|  |  |  |  |  | Shape | Polygon |   |
|  |  |  |  |  | osm_id | Text (12) | Long number |
|  |  |  |  |  | name | Text (100) | Name of building, or blank for most |
|  |  |  |  |  | type | Text (20) | Type of building, but most are blank |