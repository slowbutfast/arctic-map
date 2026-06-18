# **Reptile Species**

**Theme:** Environmental
**Subtheme:** Animal & Plant Distribution
**Layer Name in Database:** `iucn_reptiles`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Environmental** category.
2. Expand the **Animal & Plant Distribution** subcategory.
3. Check the box next to **Reptile Species** to display it on the map.

--- 

**Title:** iucn_reptiles  
**Abstract:** This dataset represents the known range of reptile species from the class Reptilia on the IUCN Red List of Threatened Species, which contains global assessments for more than 169,400 species. More than 87.5% of these (\>148,900 species) have spatial data.  
**Purpose:**  
**Keywords:** reptile species  
**Temporal Extent:**

* **Date**: March 2025  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box:   
  * Top	4,392,355.501400	m  
  * Bottom	\-3,088,166.340929	m  
  * Left	\-4,347,138.984400	m  
  * Right	3,091,949.918300	m

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** WGS 1984 Arctic Polar Stereographic  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefiles  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: IUCN 2025\. The IUCN Red List of Threatened Species. 2025-1.  
* https://www.iucnredlist.org. Downloaded on April 2025\.

**Metadata Contact:**

* Organization: International Union for Conservation of Nature’s Red List of Threatened Species, [IUCN Red List Unit](https://www.iucnredlist.org/resources/spatial-data-download)  
* Position: \[Position of the contact person\]  
* Email: [RedListGIS@iucn.org](mailto:RedListGIS@iucn.org)

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| iucn_reptiles.shp | WGS 1984 | Shapefile | 10 | 32 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | id_no | Integer |  |
|  |  |  |  |  | sci_name | String |  |
|  |  |  |  |  | presence | Integer |  |
|  |  |  |  |  | origin | Integer |  |
|  |  |  |  |  | seasonal | Integer |  |
|  |  |  |  |  | compiler | String |  |
|  |  |  |  |  | yrcompiled | Integer |  |
|  |  |  |  |  | citation | String |  |
|  |  |  |  |  | subspecies | String |  |
|  |  |  |  |  | subpop | String |  |
|  |  |  |  |  | source | String |  |
|  |  |  |  |  | island | String |  |
|  |  |  |  |  | tax_comm | String |  |
|  |  |  |  |  | dist_comm | String |  |
|  |  |  |  |  | generalisd | Integer |  |
|  |  |  |  |  | legend | String |  |
|  |  |  |  |  | kingdom | String |  |
|  |  |  |  |  | phylum | String |  |
|  |  |  |  |  | class | String |  |
|  |  |  |  |  | order_ | String |  |
|  |  |  |  |  | family | String |  |
|  |  |  |  |  | genus | String |  |
|  |  |  |  |  | category | String |  |
|  |  |  |  |  | marine | String |  |
|  |  |  |  |  | terrestria | String |  |
|  |  |  |  |  | freshwater | String |  |
|  |  |  |  |  | SHAPE_Leng | Double |  |
|  |  |  |  |  | Shape_Le_1 | Double |  |
|  |  |  |  |  | Shape_Area | Double |  |
|  |  |  |  |  | area_km2 | Double |  |

#