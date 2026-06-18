# **Public Marine Points**

**Theme:** Environmental
**Subtheme:** Water Resources
**Layer Name in Database:** `a_clean_public_marine_points`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Environmental** category.
2. Expand the **Water Resources** subcategory.
3. Check the box next to **Public Marine Points** to display it on the map.

--- 

**Title**: a_clean_public_marine_points  
**Abstract**: This dataset includes various categories of protected areas, such as marine reserves, national parks, wildlife refuges, and public access points along coastlines and within marine environments. The dataset serves as an essential tool for environmental management, conservation planning, and public education, providing critical information on the spatial distribution of protected marine areas.  
**Purpose**: The shapefile attempts to provide a comprehensive geospatial representation of protected marine areas and public marine points. It can be used in various fields: conservation planning, environmental management, policy decision making  
**Keywords:** Marine Conservation, Public Marine Points, Coastal Management, Environmental Protection  
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 60.729709 degree Bottom: \-25.349865 degree Left: \-172.666797 degree Right: 144.235736 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** No attributes are removed. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 172 records.   
- **Consistency**: The dataset is consistent with 29 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:**   
**Organization:** [Protected Planet](https://www.protectedplanet.net/en/search-areas?geo_type=region)  
**Position:** NA  
**Email:** NA  
**Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| a_clean_public_marine_points.shp | WGS 1984 | Point | 11 | 33 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID_clean_ | Integer |  |
|  |  |  |  |  | WDPAID | Double | “Assigned by UNEP-WCMC. Unique identifier for a protected Area” |
|  |  |  |  |  | PA_DEF | Text | “Allowed values: 1 (meets IUCN and CBD protected area definitions)/Allowed values: 0 (meets the CBD definition of an OECM)” |
|  |  |  |  |  | NAME | Text | “Name of the protected area (PA) as provided by the data provider.” |
|  |  |  |  |  | ORIG_NAME | Text | “Name of the protected area in original language.” |
|  |  |  |  |  | DESIG | Text | “Name of designation.” |
|  |  |  |  |  | DESIG_ENG | Text | Describes types of designations allowed |
|  |  |  |  |  | DESIG_TYPE | Text | “Allowed values: National, Regional, International, Not Applicable” |
|  |  |  |  |  | IUCN_CAT | Text | “Allowed values: Ia, Ib, II, III, IV, V, VI, Not Applicable, Not Assigned, Not Reported” –not sure what this means though |
|  |  |  |  |  | INT_CRIT | Text | “Assigned by UNEP-WCMC. For World Heritage and Ramsar sites only.” |
|  |  |  |  |  | MARINE | Text | “Allowed values: 0 (predominantly or entirely terrestrial), 1 (Coastal: marine and terrestrial), and 2 (predominantly or entirely marine). The value ‘1’ is only used for polygons.” |
|  |  |  |  |  | REP_M_AREA | Double | “Marine area in square kilometres.” |
|  |  |  |  |  | REP_AREA | Double | “Area in square kilometres.” |
|  |  |  |  |  | NO_TAKE | Text | “Allowed values: All, Part, None, Not Reported, Not Applicable (if no marine component).” |
|  |  |  |  |  | NO_TK_AREA | Double | “Area of the no-take area in square kilometres.” |
|  |  |  |  |  | STATUS | Text | “Allowed values: Proposed, Inscribed, Adopted, Designated, Established” |
|  |  |  |  |  | STATUS_YR | Long | “Year of enactment of status (STATUS field).” |
|  |  |  |  |  | GOV_TYPE | Text | Describes governemnt in place |
|  |  |  |  |  | OWN_TYPE | Text | “Allowed values: State, Communal, Individual landowners, For-profit organisations, Non-profit organisations, Joint ownership, Multiple ownership, Contested, Not Reported.” |
|  |  |  |  |  | MANG_AUTH | Text | “ndividual or group that manages the protected area.” |
|  |  |  |  |  | MANG_PLAN | Text | “Link or reference to the protected area’s management plan.” |
|  |  |  |  |  | VERIF | Text | “Assigned by UNEP-WCMC. Fixed values: State Verified, Expert Verified, Not Reported (for unverified data that was already in the WDPA prior to the inclusion of the ‘Verification’ field).” |
|  |  |  |  |  | METADATAID | Long | “Assigned by UNEP-WCMC. Link to source table.” |
|  |  |  |  |  | SUB_LOC | Text | “Allowed values: ISO 3166-2 sub-national code where the PA is located. Separated by a semi-colon if multiple.” |
|  |  |  |  |  | PARENT_ISO | Text | “Allowed values: ISO 3166-1 Alpha-3 character code of country where the PA is located. Separated by a semi-colon if multiple.” |
|  |  |  |  |  | ISO3 | Text | “Allowed values: ISO 3166-1 Alpha-3 character code of country or territory where the PA is located. Separated by a semi-colon if multiple.” |
|  |  |  |  |  | FID_arctic | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape_Leng | Double |  |
|  |  |  |  |  | Shape_Area | Doubble |  |

#