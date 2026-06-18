# **Iceland Transport (point)**

**Theme:** Infrastructure
**Subtheme:** Transportation
**Layer Name in Database:** `a_gis_osm_transport_free_1`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Transportation** subcategory.
3. Check the box next to **Iceland Transport (point)** to display it on the map.

--- 

**Title:** gis_osm_transport_free_1  
**Abstract:** This dataset represents transportation hubs in the state of Alaska. All of the entries contain info about the code and feature type, and many of the places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of transportation hubs in Alaska to aid with development, transportation, and spatial reference.   
**Keywords:** Alaska, OSM, Transport, Airport, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.338604 deg; Bottom: 48.721824 deg; Left: \-174.113611 deg; Right: \-122.512253 deg

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
| gis_osm_transport_free_1 | WGS 1984 | Shapefile, Point | 1277 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many 4-digit classifying codes beginning with 56 |
|  |  |  |  |  | fclass | Text (28) | Airfield, Airport,  bus_station, bus_stop, ferry_terminal, helipad, railway_halt, railway_station, or taxi. Corresponds to code attribute.  |
|  |  |  |  |  | name | Text (100) | Name of the transport location. Many are blank.  |