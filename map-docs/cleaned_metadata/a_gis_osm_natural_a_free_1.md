# **Alaska Natural A Features (polygon)**

**Theme:** Environmental
**Subtheme:** Land Cover
**Layer Name in Database:** `a_gis_osm_natural_a_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Environmental** category.
2. Expand the **Land Cover** subcategory.
3. Check the box next to **Alaska Natural A Features (polygon)** to display it on the map.

--- 

**Title:** gis_osm_natural_a_free_1  
**Abstract:** This dataset represents natural features of beaches, cliffs, and glaciers in the state of Alaska. Some of the entries contain info about the name of the feature, while all contain information about the code and feature type.   
**Purpose:**The dataset aims to provide the locations and identities of natural features throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Nature, Beach, Glacier, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Min Y: \-400.00 deg; Max Y: 400.00 deg; Min X: \-400.00 deg; Max X: 400.00 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Not every row has a name attribute.   
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

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gis_osm_natural_a_free_1 | D WGS 1984 | Shapefile, Polygon | 4,149 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 4103, 4112, or 4141 |
|  |  |  |  |  | fclass | Text (28) | Beach, cliff, or glacier–correlates to code attribute |
|  |  |  |  |  | name | Text (100) | Name of natural attribute, if applicable |