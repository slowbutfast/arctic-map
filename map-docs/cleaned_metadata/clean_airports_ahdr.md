# **AHDR Airports**

**Theme:** Infrastructure
**Subtheme:** Transportation
**Layer Name in Database:** `clean_airports_ahdr`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Transportation** subcategory.
3. Check the box next to **AHDR Airports** to display it on the map.

--- 

**Title:** Airports AHDR  
**Abstract:** This dataset represents mid and major Airport locations throughout the Arctic region. It includes information on the size, name, location of the location (ramp, runway, etc), wdid score, and identifying codes of the airport. .  
**Purpose:**The dataset aims to provide information on larger Arctic Airport locations to assist in transportation decisions in the Arctic while dealing with Arctic development.  
**Keywords:** Arctic, Airports, wdid, IATA, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:**   
Bounding Box: Top: 78.246717 deg; Bottom: 52.926071deg; Left: \-165.441642 deg; Right: 40.713347 deg  
**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: Considering the high spatial resolution and low tolerance of 0.00000000898315284119521 Degree, this is an accurate dataset.  
* Completeness: This is a complete dataset, with the same information provided for each Airport, including a link to a wikipedia page for extra information and multiple identification codes.   
* Consistency: This is a very consistent dataset, with each cell being filled with accurate information in the attribute table. 

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: Natural Earth  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Airports_AHDR.shp | WGS 1984 | point | 30 | 42 | FID | Object ID |  |
|  |  |  |  |  | Shape * | Geometry |  |
|  |  |  |  |  | scalerank | Short |  |
|  |  |  |  |  | featurecla | Text (80) | Says “Airport” for all of them |
|  |  |  |  |  | type | Text (50) | “Mid”, “major”, or “military major”: type of airport |
|  |  |  |  |  | name | Text (200) | Airport name, ex. “Kodiac” or “Iqaluit” |
|  |  |  |  |  | location | Text (50) | “Ramp”, “terminal”, “runway” or “approximate” |
|  |  |  |  |  | iata_code | Text (254) | Same as “abbrev” attribute, except for the one row in which the abbrev is 4 letters, in which case it is empy |
|  |  |  |  |  | wikipedia | Text (254) | Website link |
|  |  |  |  |  | wikidatid | Text (254) |  |
|  |  |  |  |  | wdid_score | Short | May relate to waste discharge identification |
|  |  |  |  |  | ne_id | Long | Natural earth id |