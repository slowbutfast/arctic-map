# **Country Political Boundaries**

**Theme:** Socioeconomic
**Subtheme:** Administrative & Geographic Boundaries
**Layer Name in Database:** `political_boundaries_cleaned`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Administrative & Geographic Boundaries** subcategory.
3. Check the box next to **Country Political Boundaries** to display it on the map.

--- 

**Title:** Political_Boundaries_Cleaned  
**Abstract:** This 2020 country political boundary data is from Garmin International and the United States Central Intelligence Agency The World Factbook and compiled by Esri.   
**Purpose:** To represent administrative boundaries separating countries.  
**Keywords:** country, countries, international boundaries, borders, coastlines, boundaries  
**Temporal Extent:**

* **Date**: 2020  
* **Time Period**: 

**Geographic Extent:** 

* Bounding Box:   
  * Top	18,460,513.247014	m  
  * Bottom	6,664,298.128677	m  
  * Left	\-20,037,507.067162	m  
  * Right	20,037,507.067138	m

**Spatial Resolution**: XY Resolution: 0.00000000671487310199837 Meters  
**Coordinate Reference Systems:** 

* Projected Coordinate System: WGS 1984 Web Mercator (auxiliary sphere)

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: All features have values for each of the attributes.  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization: Esri (within the ArcGIS Living Atlas, linked [here](https://www.arcgis.com/home/item.html?id=30b5ef2245cb47bdb05ca83df7fd93b5)); Garmin International, Inc.; U.S. Central Intelligence Agency (The World Factbook)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Political_Boundaries_Cleaned.shp | WGS 1984 Web Mercator (auxiliary sphere) | Polygon | 35 | 8 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | COUNTRY | String |  |
|  |  |  |  |  | ISO_CC | String | 3 letter long abbreviation of the countryr |
|  |  |  |  |  | CONTINENT | String |  |
|  |  |  |  |  | LAND_TYPE | String | Description of country’s main geography (ex: small island, primary land) |
|  |  |  |  |  | Shape_Leng | Double |  |
|  |  |  |  |  | Shape_Area | Double |  |