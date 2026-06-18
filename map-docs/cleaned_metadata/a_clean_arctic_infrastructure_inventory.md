# **Arctic Infrastructure Inventory**

**Theme:** Infrastructure
**Subtheme:** General
**Layer Name in Database:** `a_clean_arctic_infrastructure_inventory`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **General** subcategory.
3. Check the box next to **Arctic Infrastructure Inventory** to display it on the map.

--- 

**Title**: Arctic Infrastructure Inventory   
**Abstract**: The "Arctic Infrastructure Inventory" shapefile provides a comprehensive spatial dataset of key infrastructural elements within the Arctic region. The shapefile is designed to support research, planning, and management activities by providing a detailed geographic representation of existing infrastructure. It is particularly valuable for stakeholders involved in environmental monitoring, resource management, and community planning, offering insights into the spatial distribution and potential vulnerabilities of infrastructure in the context of the Arctic's unique environmental challenges.  
**Purpose**: This shapefile serves as a critical tool for government agencies, researchers, policymakers, and other stakeholders involved in the Arctic region, facilitating informed decision-making and strategic planning.  
**Keywords:** arctic infrastructure, resource management, arctic region   
**Temporal Extent:** 

- **Date: NA**  
- **Time Period: NA**

**Geographic Extent:** 

- **Bounding Box: Top: 179.045833  Bottom: \-176.636389  Left: \-179.433300 Right: 179.293000**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: additional, Coordinate, Lat2, Long2, Lat3, Long3 are removed because these geographical information is repetitive. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 8323 records.   
- **Consistency**: The dataset is consistent with 26 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:**   
**Organization:** Wilson Center  
**Position:** NA  
**Email:** NA  
**Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Arctic Infrastructure Inventory.shp | WGS 1984 | Point | 8323 | 30 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | ID | Long |  |
|  |  |  |  |  | Name | Text | Name of port/airport/location etc |
|  |  |  |  |  | Description | Text | Description of infrastructure |
|  |  |  |  |  | Status | Text | Says whether the infrastructure project is completed, suspended, proposed, terminated, etc |
|  |  |  |  |  | Country | Text |  |
|  |  |  |  |  | Province_S | Text |  |
|  |  |  |  |  | Category | Text | Civil, transportation, communications, or a combo |
|  |  |  |  |  | Subtype | Text | Agriculture, tourism, etc |
|  |  |  |  |  | Initiative | Text | If this feature is part of a specific intiative |
|  |  |  |  |  | Lat | Double |  |
|  |  |  |  |  | Long | Double |  |
|  |  |  |  |  | Estimated | Long | Under a dozen have values |
|  |  |  |  |  | Actual_Cos | Double | Under a dozen have values |
|  |  |  |  |  | Source_s_ | Text | Link to source or source name |
|  |  |  |  |  | Date_Verif | Text | ‘February 2021’ for all |
|  |  |  |  |  | Exclusion | Long | 1 or 0 |
|  |  |  |  |  | IATA | Text | 3 letter code for airports |
|  |  |  |  |  | LOCODE | Text | Empty, or alphabetical code |
|  |  |  |  |  | WEPP_ID | Text | Number code, or Empty |
|  |  |  |  |  | GPPD_ID | Text | Alphanumebric code, or Empty |
|  |  |  |  |  | ICAO | Text | “four-letter alphanumeric codes that identify airports, airlines, aircraft types, and other aviation facilities around the world” or empty |
|  |  |  |  |  | AMATII | Long | 3 number code, or empty |
|  |  |  |  |  | World_Port | Long | Up to 5-digit number |
|  |  |  |  |  | Contact_In | Text | Contact information |
|  |  |  |  |  | FID_arctic | Integer |  |
|  |  |  |  |  | Id_1 | Integer |  |
|  |  |  |  |  | Shape_Leng | Double |  |
|  |  |  |  |  | Shape_Area | Double |  |