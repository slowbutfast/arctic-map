# **10m Scale Railroads**

**Theme:** Infrastructure
**Subtheme:** Transportation
**Layer Name in Database:** `a_clean_ne_10m_railroads`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Transportation** subcategory.
3. Check the box next to **10m Scale Railroads** to display it on the map.

--- 

**Title:** Railroads  
**Abstract:** This dataset represents railroad locations throughout the world. It includes information on the continent, whether the train is electric, and whether it utilizes a multi-track system.  
**Purpose:**The dataset aims to provide an overview of global railroad systems to assist with mapping the transit routes for both people and goods.  
**Keywords:** trains, railroads, electric, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 69.604375 deg; Bottom: \-51.895278 deg; Left: \-150.112222 deg; Right: 179.357778 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**

* Accuracy: Considering the high spatial resolution and low tolerance of 0.00000000898315284119521 Degree, this is an accurate dataset.  
* Completeness: Names of the railroads and length attributes could have been helpful, as well as the owner of each railroad.   
* Consistency: Each row has each field filled out, creating a consistent set of information for each railroad. 

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
| ne_10m_railroads.shp | WGS 1984 | line | 25,413 | 14 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | mult_track | Short | 2, 1, or 0 |
|  |  |  |  |  | electric | Short | 2, 1, or 0 |
|  |  |  |  |  | category | Short | 0-9 |
|  |  |  |  |  | disp_scale | Text (5) | 1:10m to 1:80m |
|  |  |  |  |  | featurecla | Text (50) | “railroad” for all of them |
|  |  |  |  |  | scalerank | Short | 4-10 |
|  |  |  |  |  | natlscale | Double (10, 3\) |  |
|  |  |  |  |  | continent | Text (50) | Continent, including oceana |

#