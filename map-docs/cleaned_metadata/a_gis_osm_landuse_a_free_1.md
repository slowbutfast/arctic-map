# **Alaska Land Use **

**Theme:** Environmental
**Subtheme:** Land Cover
**Layer Name in Database:** `a_gis_osm_landuse_a_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Environmental** category.
2. Expand the **Land Cover** subcategory.
3. Check the box next to **Alaska Land Use ** to display it on the map.

--- 

**Title:** gis_osm_landuse_a_free_1  
**Abstract:** This dataset represents land use for parcels in the state of Alaska. Some of the entries contain info about the building name, while all contain information about the code and land designation.   
**Purpose:**The dataset aims to provide the locations, identities, and uses of parcels throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Land use, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Min Y: \-400.00 deg; Max Y: 400.00 deg; Min X: \-400.00 deg; Max X: 400.00 deg

**Spatial Resolution**: XY resolution: 0.000000000000088817841970012 Degree  
**Coordinate Reference Systems:** D WGS 1984  
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
| gis_osm_landuse_a_free_1 | WGS 1984 | Shapefile, Polygon | 18,272 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 7201-7229: Maybe a land use code? |
|  |  |  |  |  | fclass | Text (28) | Forest, park, retail etc describing land designation. Seems to be tied to code |
|  |  |  |  |  | name | Text (100) | Name of land piece, if applicable |