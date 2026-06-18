# **Land Use Map of City X**

**Title:** Land Use Map of City X  
**Abstract:** This dataset represents land use categories for City X as of \[year\]. It includes information on residential, commercial, industrial, and recreational areas.  
**Purpose:**The dataset aims to provide an overview of land use patterns within City X to support urban planning and development initiatives.  
**Keywords:** land use, urban planning, zoning, city X, GIS  
**Temporal Extent:**

1. **Date**: \[Date of data collection\]  
   2. **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

3. Bounding Box: \[Coordinates defining the geographic extent of the dataset\]

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:**\[Specify the CRS used, e.g., EPSG:4326\]  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

4. Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
   5. Completeness: \[Describe completeness of the dataset\]  
   6. Consistency: \[Describe consistency measures\]

**Distribution Information:**

7. Format: \[e.g., GeoTIFF, Shapefile\]  
   8. Access Constraints: \[Describe any restrictions on access\]  
   9. Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

10. Organization: \[Name of organization responsible for maintaining the dataset\]  
    11. Position: \[Position of the contact person\]  
    12. Email: \[Contact email address\]  
    13. Phone: \[Contact phone number\]

**Data Dictionary:**

| Column | Data Type | Field size | Description |
| :---- | :---- | :---- | :---- |
| ID | int | 5 | Land Use ID |

1. # **Global Power Plant Database** 

**Title**: GlobalPowerPlant  
**Abstract**: The database aims to illustrate how World Resources Institute (WRI) experts and their partners created the Global Power Plant Database from official government data and independent sources around the world, integrated them with crowdsourced data such as analysis of satellite images, and delivered the final database as an open data resource.   
**Purpose**: The database explains how the experts addressed three challenges: matching plants across databases, keeping the database up to date, and delivering information on the accuracy of the data.   
**Keywords:** sustainability, power plant, technology, fuel, ownership   
**Temporal Extent:** 

* **Date: NA**  
* **Time Period: NA**

**Geographic Extent:** 

* **Bounding Box: Top: 71.292 Bottom: \-77.847 Left: \-179.9777 Right: 179.3887**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The attributes: wepp\_id, year\_of\_ca, generation, other\_fuel, generation\_1, generation\_2, generation\_3, generation\_4, generation\_5 are removed from the original dataset because most of these attributes are blank. If not, they are also not very informative for the audience.  

**Quality Information:** 

* **Accuracy**: NA  
* **Completeness:** The dataset is complete with 34936 records.   
* **Consistency**: The dataset is consistent with 31 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** World Resource Institute   
* **Position:**   
* **Email:** logan.byers@wri.org  
* **Phone:**

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| a\_globalpowerplant.shp | WGS 1984 | Point | 34936 | 31 |  |  |  |
|  |  |  |  |  | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | country | Text | 3-letter abbreviation |
|  |  |  |  |  | country\_lo | Text | Full country name |
|  |  |  |  |  | name | Text | Name of power plant |
|  |  |  |  |  | gppd\_idnr | Text | “10 or 12 character identifier for the power plant” |
|  |  |  |  |  | capacity\_mw | Double | “electrical generating capacity in megawatts” |
|  |  |  |  |  | latitude | Double |  |
|  |  |  |  |  | longitude | Double |  |
|  |  |  |  |  | primary\_fu | Text | “energy source used in primary electricity generation or export” |
|  |  |  |  |  | commission | Double | When it started operating |
|  |  |  |  |  | owner | Text | Who owns power plant |
|  |  |  |  |  | source | Text | Information source |
|  |  |  |  |  | url | Text | Website for power plant |
|  |  |  |  |  | geolocatio | Text |  |
|  |  |  |  |  | wepp\_id | Long | “a reference to a unique plant identifier in the widely-used PLATTS-WEPP database” (from README file) |
|  |  |  |  |  | year\_of\_ca | Long | Many say 0 but others have actual years like 2019 so doesnt seem useful, but data that is there is year capacity data was reported |
|  |  |  |  |  | generation | Text | Empty: *Also not empty if sorted by descending but does not seem to be useful, unless it’s how much energy is generated:* From what i’ve pieced together, this is gWh generated in 2013 |
|  |  |  |  |  | Generati\_7 *Should be generation\_data\_source* | Text | Seems to be source for energy generation  |
|  |  |  |  |  | estimated\_ | Double | estimated electricity generation in gigawatt-hours for the year 2013 |
|  |  |  |  |  | estimated1 | Double | estimated electricity generation in gigawatt-hours for the year 2014 |
|  |  |  |  |  | estimate\_1 | Double | estimated electricity generation in gigawatt-hours for the year 2015 |
|  |  |  |  |  | estimate\_2 | Double | estimated electricity generation in gigawatt-hours for the year 2016 |
|  |  |  |  |  | estimate\_3 | Double | estimated electricity generation in gigawatt-hours for the year 2017 |
|  |  |  |  |  | estimate\_4 | Text | label of the model/method used to estimate generation for the year 2013 |
|  |  |  |  |  | estimate\_5 | Text | label of the model/method used to estimate generation for the year 2014 |
|  |  |  |  |  | estimate\_6 | Text | label of the model/method used to estimate generation for the year 2015 |
|  |  |  |  |  | estimate\_7 | Text | label of the model/method used to estimate generation for the year 2016 |
|  |  |  |  |  | estimate\_8 | Text | label of the model/method used to estimate generation for the year 2017 |

# 

# 

# 

# 

2. # **Infrastructure\_WilsonCenter\\Infrastructure Inventory** 

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
|  |  |  |  |  | Province\_S | Text |  |
|  |  |  |  |  | Category | Text | Civil, transportation, communications, or a combo |
|  |  |  |  |  | Subtype | Text | Agriculture, tourism, etc |
|  |  |  |  |  | Initiative | Text | If this feature is part of a specific intiative |
|  |  |  |  |  | Lat | Double |  |
|  |  |  |  |  | Long | Double |  |
|  |  |  |  |  | Estimated | Long | Under a dozen have values |
|  |  |  |  |  | Actual\_Cos | Double | Under a dozen have values |
|  |  |  |  |  | Source\_s\_ | Text | Link to source or source name |
|  |  |  |  |  | Date\_Verif | Text | ‘February 2021’ for all |
|  |  |  |  |  | Exclusion | Long | 1 or 0 |
|  |  |  |  |  | IATA | Text | 3 letter code for airports |
|  |  |  |  |  | LOCODE | Text | Empty, or alphabetical code |
|  |  |  |  |  | WEPP\_ID | Text | Number code, or Empty |
|  |  |  |  |  | GPPD\_ID | Text | Alphanumebric code, or Empty |
|  |  |  |  |  | ICAO | Text | “four-letter alphanumeric codes that identify airports, airlines, aircraft types, and other aviation facilities around the world” or empty |
|  |  |  |  |  | AMATII | Long | 3 number code, or empty |
|  |  |  |  |  | World\_Port | Long | Up to 5-digit number |
|  |  |  |  |  | Contact\_In | Text | Contact information |
|  |  |  |  |  | FID\_arctic | Integer |  |
|  |  |  |  |  | Id\_1 | Integer |  |
|  |  |  |  |  | Shape\_Leng | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |

3. # **Infrastructure Wilson Center/Places\_P**

**Title**: Places\_P  
**Abstract**: This dataset includes critical infrastructure such as buildings, utilities, along with significant locations that are relevant to the Wilson Center's scope of work and influence. The shapefile serves as an essential tool for visualizing and analyzing the distribution and characteristics of these infrastructural elements and places, facilitating research, planning, and decision-making processes.   
**Purpose**: The purpose of the "Infrastructure Wilson Center/Places\_P" shapefile is to provide a detailed geospatial representation of infrastructure and notable places associated with the Wilson Center. This dataset aims to support a variety of applications, including policy analysis, urban and regional planning.   
**Keywords:** significant places, urban planning, policy analysis, wilson center   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 3,305,034.338342 m  Bottom: 226,939.278930 m  Left: \-2,061,714.468956 m  Right: 3,336,654.810682 m**

**Spatial Resolution:** 0.00000000305360181585002 Meters  
**Coordinate Reference System:** Alaska Albers Equal Area Conic  
**Lineage:** The fields: NAMEPAR, NAMEALT, NAMEASCII, ADM0CAP, CAPIN, WORLDCITY, ADM0NAME, ADM0\_A3, ISO\_A2, NOTE, RANK\_MAX, RANK\_MIN, MEGANAME, LS\_NAME, MIN\_ZOOM, CAPALT, NAME\_EN, NAME\_DE, NAME\_ES, NAME\_FR, NAME\_PT, NAME\_RU, NAME\_ZH, LABEL, NAME\_AR, NAME\_BN, NAME\_EL, NAME\_HI, NAME\_HU, NAME\_ID, NAME\_IT, NAME\_JA, NAME\_KO, NAME\_NL, NAME\_PL, NAME\_SV, NAME\_TR, NAME\_VI, NAME\_FA, NAME\_HE, NAME\_UK, NAME\_UR, NAME\_ZHT, GEONAMESID, FCLASS\_ISO, FCLASS\_US, FCLASS\_FR, FCLASS\_RU, FCLASS\_ES, FCLASS\_CN, FCLASS\_TW, FCLASS\_IN, FCLASS\_NP, FCLASS\_PK, FCLASS\_DE, FCLASS\_GB, FCLASS\_BR, FCLASS\_IL, FCLASS\_PS, FCLASS\_SA, FCLASS\_EG, FCLASS\_MA, FCLASS\_PT, FCLASS\_AR, FCLASS\_JP, FCLASS\_KO, FCLASS\_VN, FCLASS\_TR, FCLASS\_ID, FCLASS\_PL, FCLASS\_GR, FCLASS\_IT, FCLASS\_NL,  FCLASS\_SE, FCLASS\_BD, FCLASS\_UA, FCLASS\_TLC, Cntr, ST, X, Y are removed because most of these attributes are blank. If not, these attributes are not very understandable for the audience.  

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 151 records.   
- **Consistency**: The dataset is consistent with 55 attributes. 

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
| Places\_P.shp | Alaska Albers Equal Area Conic | Point | 854 | 55 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID\_clean\_ | Integer |  |
|  |  |  |  |  | OBJECTID | Long |  |
|  |  |  |  |  | SCALERANK | Long | 0-8 |
|  |  |  |  |  | NATSCALE | Long | 0-300, seems to be multiples |
|  |  |  |  |  | LABELRANK | Long | 0-2 |
|  |  |  |  |  | FEATURECLA | Text | Blank, Admin-1 capital, Historic place, or Populated place |
|  |  |  |  |  | NAME | Text | Name of place, or blank |
|  |  |  |  |  | MEGACITY | Long | 0 or 1 |
|  |  |  |  |  | SOV0NAME | Text | United States, Russia, Canada, or blank |
|  |  |  |  |  | SOV\_A3 | Text | 3-letter country abbreviation |
|  |  |  |  |  | ADM1NAME | Text | State name  |
|  |  |  |  |  | LATITUDE | Double |  |
|  |  |  |  |  | POP\_MAX | Double |  |
|  |  |  |  |  | POP\_MIN | Double |  |
|  |  |  |  |  | POP\_OTHER | Double |  |
|  |  |  |  |  | MAX\_POP10 | Double |  |
|  |  |  |  |  | MAX\_POP20 | Double |  |
|  |  |  |  |  | MAX\_POP50 | Double |  |
|  |  |  |  |  | MAX\_POP300 | Double |  |
|  |  |  |  |  | MAX\_POP310 | Double |  |
|  |  |  |  |  | TIMEZONE | Text |  |
|  |  |  |  |  | UN\_FID | Long |  |
|  |  |  |  |  | POP1950 | Double |  |
|  |  |  |  |  | POP1955 | Double |  |
|  |  |  |  |  | POP1960 | Double |  |
|  |  |  |  |  | POP1965 | Double |  |
|  |  |  |  |  | POP1970 | Double |  |
|  |  |  |  |  | POP1975 | Double |  |
|  |  |  |  |  | POP1980 | Double |  |
|  |  |  |  |  | POP1985 | Double |  |
|  |  |  |  |  | POP1990 | Double |  |
|  |  |  |  |  | POP1995 | Double |  |
|  |  |  |  |  | POP2000 | Double |  |
|  |  |  |  |  | POP2005 | Double |  |
|  |  |  |  |  | POP2010 | Double |  |
|  |  |  |  |  | POP2015 | Double |  |
|  |  |  |  |  | POP2020 | Double |  |
|  |  |  |  |  | POP2025 | Double |  |
|  |  |  |  |  | POP2050 | Double |  |
|  |  |  |  |  | WIKIDATAID | Text |  |
|  |  |  |  |  | WOF\_ID | Double | Long iD |
|  |  |  |  |  | NE\_ID | Double | Cant see how this would be useful |
|  |  |  |  |  | Region | Text | Region, or blank |
|  |  |  |  |  | Code | Text | Many Empty |
|  |  |  |  |  | Sett | Text | Not sure what thjis means |
|  |  |  |  |  | Pop\_2017 | Long | Many are 0 but rest have pop |
|  |  |  |  |  | On\_Perma | Long | 0 or 1 |
|  |  |  |  |  | State | Text | Alaska or Empty |
|  |  |  |  |  | Name2 | Text | Area name or Empty |
|  |  |  |  |  | FID\_arctic | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape\_Leng | Doublee |  |
|  |  |  |  |  | Shape\_Area | Douuble |  |

# 

4. # **ProtectedAreas/Public Marine Points/WDPA\_ProtectedAreasMar2024shp** 

**Title**: a\_clean\_public\_marine\_points  
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
| a\_clean\_public\_marine\_points.shp | WGS 1984 | Point | 11 | 33 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID\_clean\_ | Integer |  |
|  |  |  |  |  | WDPAID | Double | “Assigned by UNEP-WCMC. Unique identifier for a protected Area” |
|  |  |  |  |  | PA\_DEF | Text | “Allowed values: 1 (meets IUCN and CBD protected area definitions)/Allowed values: 0 (meets the CBD definition of an OECM)” |
|  |  |  |  |  | NAME | Text | “Name of the protected area (PA) as provided by the data provider.” |
|  |  |  |  |  | ORIG\_NAME | Text | “Name of the protected area in original language.” |
|  |  |  |  |  | DESIG | Text | “Name of designation.” |
|  |  |  |  |  | DESIG\_ENG | Text | Describes types of designations allowed |
|  |  |  |  |  | DESIG\_TYPE | Text | “Allowed values: National, Regional, International, Not Applicable” |
|  |  |  |  |  | IUCN\_CAT | Text | “Allowed values: Ia, Ib, II, III, IV, V, VI, Not Applicable, Not Assigned, Not Reported” –not sure what this means though |
|  |  |  |  |  | INT\_CRIT | Text | “Assigned by UNEP-WCMC. For World Heritage and Ramsar sites only.” |
|  |  |  |  |  | MARINE | Text | “Allowed values: 0 (predominantly or entirely terrestrial), 1 (Coastal: marine and terrestrial), and 2 (predominantly or entirely marine). The value ‘1’ is only used for polygons.” |
|  |  |  |  |  | REP\_M\_AREA | Double | “Marine area in square kilometres.” |
|  |  |  |  |  | REP\_AREA | Double | “Area in square kilometres.” |
|  |  |  |  |  | NO\_TAKE | Text | “Allowed values: All, Part, None, Not Reported, Not Applicable (if no marine component).” |
|  |  |  |  |  | NO\_TK\_AREA | Double | “Area of the no-take area in square kilometres.” |
|  |  |  |  |  | STATUS | Text | “Allowed values: Proposed, Inscribed, Adopted, Designated, Established” |
|  |  |  |  |  | STATUS\_YR | Long | “Year of enactment of status (STATUS field).” |
|  |  |  |  |  | GOV\_TYPE | Text | Describes governemnt in place |
|  |  |  |  |  | OWN\_TYPE | Text | “Allowed values: State, Communal, Individual landowners, For-profit organisations, Non-profit organisations, Joint ownership, Multiple ownership, Contested, Not Reported.” |
|  |  |  |  |  | MANG\_AUTH | Text | “ndividual or group that manages the protected area.” |
|  |  |  |  |  | MANG\_PLAN | Text | “Link or reference to the protected area’s management plan.” |
|  |  |  |  |  | VERIF | Text | “Assigned by UNEP-WCMC. Fixed values: State Verified, Expert Verified, Not Reported (for unverified data that was already in the WDPA prior to the inclusion of the ‘Verification’ field).” |
|  |  |  |  |  | METADATAID | Long | “Assigned by UNEP-WCMC. Link to source table.” |
|  |  |  |  |  | SUB\_LOC | Text | “Allowed values: ISO 3166-2 sub-national code where the PA is located. Separated by a semi-colon if multiple.” |
|  |  |  |  |  | PARENT\_ISO | Text | “Allowed values: ISO 3166-1 Alpha-3 character code of country where the PA is located. Separated by a semi-colon if multiple.” |
|  |  |  |  |  | ISO3 | Text | “Allowed values: ISO 3166-1 Alpha-3 character code of country or territory where the PA is located. Separated by a semi-colon if multiple.” |
|  |  |  |  |  | FID\_arctic | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape\_Leng | Double |  |
|  |  |  |  |  | Shape\_Area | Doubble |  |

# 

5. # **ProtectedAreas/Public Marine Polygons/WDPA\_WDOECM\_Mar2024\_Public\_marine\_shp**

**Title**: a\_clean\_public\_marine\_0\_polygons  
**Abstract**: This dataset includes various categories of protected areas, such as marine reserves, national parks, wildlife refuges, and public access points along coastlines and within marine environments. The dataset serves as an essential tool for environmental management, conservation planning, and public education, providing critical information on the spatial distribution of protected marine areas.  
**Purpose**: The shapefile attempts to provide a comprehensive geospatial representation of protected marine areas and public marine points. It can be used in various fields: conservation planning, environmental management, policy decision making  
**Keywords:** Marine Conservation, Public Marine Points, Coastal Management, Environmental Protection  
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 81.028006 degree Bottom: \-69.477770 degree Left: \-180.000000 degree Right: 179.999999 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: Supp\_Info and Cons\_obj etc are removed because these attributes are blank. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 6112 records.   
- **Consistency**: The dataset is consistent with 30 attributes. 

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
| a\_clean\_public\_marine\_0\_polygons.shp | WGS 1984 | Polygon | 6112 | 30 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | WDPAID | Double | “Assigned by UNEP-WCMC. Unique identifier for a protected Area. “ |
|  |  |  |  |  | WDPA\_PID | Text | “Assigned by UNEP-WCMC. Unique identifier for parcels or zones within a protected area “ |
|  |  |  |  |  | PA\_DEF | Text | “Allowed values: 1 (meets IUCN and CBD protected area definitions) Allowed values: 0 (meets the CBD definition of an OECM)” |
|  |  |  |  |  | NAME | Text | “Name of the protected area (PA) as provided by the data provider.” |
|  |  |  |  |  | ORIG\_NAME | Text | “Name of the protected area in original language.” |
|  |  |  |  |  | DESIG | Text | “Name of designation.” (such as marine reserve) |
|  |  |  |  |  | DESIG\_ENG | Text | Name of designation in english |
|  |  |  |  |  | DESIG\_TYPE | Text | “Allowed values: National, Regional, International, Not Applicable” |
|  |  |  |  |  | IUCN\_CAT | Text | “Allowed values: Ia, Ib, II, III, IV, V, VI, Not Applicable, Not Assigned, Not Reported” (not sure what this means) |
|  |  |  |  |  | INT\_CRIT | Text | “Assigned by UNEP-WCMC. For World Heritage and Ramsar sites only.” –written in numerals |
|  |  |  |  |  | MARINE | Text | “Allowed values: 0 (predominantly or entirely terrestrial), 1 (Coastal: marine and terrestrial), and 2 (predominantly or entirely marine). The value ‘1’ is only used for polygons.” |
|  |  |  |  |  | REP\_M\_AREA | Double | “Marine area in square kilometres.” |
|  |  |  |  |  | GIS\_M\_AREA | Double | “Assigned by UNEP-WCMC.” |
|  |  |  |  |  | REP\_AREA | Double | “Area in square kilometres. “ |
|  |  |  |  |  | GIS\_AREA | Double | “Assigned by UNEP-WCMC.” |
|  |  |  |  |  | NO\_TAKE | Text | “Allowed values: All, Part, None, Not Reported, Not Applicable (if no marine component).” |
|  |  |  |  |  | NO\_TK\_AREA | Text | “Area of the no-take area in square kilometres.” |
|  |  |  |  |  | STATUS | Text | “Allowed values: Proposed, Inscribed, Adopted, Designated, Established.” |
|  |  |  |  |  | STATUS\_YR | Long | “Year of enactment of status (STATUS field).” |
|  |  |  |  |  | GOV\_TYPE | Text | “llowed values: Federal or national ministry or agency, Sub-national ministry or agency, Government-delegated management, Transboundary governance, Collaborative governance, Joint governance, Individual landowners, Non-profit organisations, For-profit organisations, Indigenous peoples, Local communities, Not Reported.” |
|  |  |  |  |  | OWN\_TYPE | Text | “Allowed values: State, Communal, Individual landowners, For-profit organisations, Non-profit organisations, Joint ownership, Multiple ownership, Contested, Not Reported.” |
|  |  |  |  |  | MANG\_AUTH | Text | “Individual or group that manages the protected area.” |
|  |  |  |  |  | MANG\_PLAN | Text | “Link or reference to the protected area’s management plan.” |
|  |  |  |  |  | VERIF | Text | “Assigned by UNEP-WCMC. Fixed values: State Verified, Expert Verified, Not Reported (for unverified data that was already in the WDPA prior to the inclusion of the ‘Verification’ field).” |
|  |  |  |  |  | METADATAID | Long | “Assigned by UNEP-WCMC. Link to source table.” |
|  |  |  |  |  | SUB\_LOC | Text | “Allowed values: ISO 3166-2 sub-national code where the PA is located. Separated by a semi-colon if multiple.” |
|  |  |  |  |  | PARENT\_ISO | Text | “Allowed values: ISO 3166-1 Alpha-3 character code of country where the PA is located. Separated by a semi-colon if multiple.” |
|  |  |  |  |  | ISO3 | Text | “Allowed values: ISO 3166-1 Alpha-3 character code of country or territory where the PA is located. Separated by a semi-colon if multiple.” |

6. # **Settlements\\Geonames\\allCountries\\CA**

**Title**: CA Geonames   
**Abstract**: This dataset includes various types of geographic features such as cities, towns, natural features (like mountains, lakes, and rivers), and other significant landmarks. The "Canada Geonames" shapefile serves as an essential reference for mapping, navigation, and geographical analysis, providing a detailed catalog of named locations throughout the country.  
**Purpose**: The shapefile is to provide an authoritative and standardized geospatial representation of geographic names across Canada. This dataset aims to support a wide range of applications, including mapping and cartography and geospatial analysis.   
**Keywords:** Canadian Geography, Place Names, Cartography   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 83.122240 degree Bottom: 41.654440 degree Left: \-141.005420 degree Right: \-48.500000 degree**

**Spatial Resolution:** 0.0000000000000154052470779931 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: Field 1, 7, 19 etc are removed because these attributes are blank. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 314328 records.   
- **Consistency**: The dataset is consistent with 18 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:**   
**Organization:** [GeoNames](https://www.geonames.org/export/)  
**Position:** NA  
**Email:** NA  
**Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| CA\_Geonames | WGS 1984  | Point | 314328 | 18  | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Field2 | Text | Name of location, such as “Aarons Hill” |
|  |  |  |  |  | Field3 | Text | Seems to be exactly the same as Field2 |
|  |  |  |  |  | Field4 | Text | Seems to be alternate names for field1. Most rows are blank |
|  |  |  |  |  | Field5 | Double | Seems to be latitude |
|  |  |  |  |  | Field6 | Double | Seems to be longitude |
|  |  |  |  |  | Field8 | Text | Defines the location as the type of country, state, region….steam, lake…with codes defined in the GeoNames\_CODES file located in the GeoNames section of settlements file |
|  |  |  |  |  | Field9 | Text | All say “CA” |
|  |  |  |  |  | Field10 | Text | Only 14 rows have data saying US or CA,US |
|  |  |  |  |  | Field11 | Long | An undefined value 0-14 |
|  |  |  |  |  | Field12 | Long | An undefined long numerical value |
|  |  |  |  |  | Field13 | Long | Another long undefined numerical value |
|  |  |  |  |  | Field14 | Text | Either a two digit number or a two letter code, or blank. 2 letter codes are undefined in the GeoNames\_CODES database.  |
|  |  |  |  |  | Field15 | Long | Long number, or 0 |
|  |  |  |  |  | Field16 | Long | Up to a 4 digit numeric code, or 0 |
|  |  |  |  |  | Field17 | Long | Up to a 4 digit numeric code, or 0 |
|  |  |  |  |  | Field18 | Text | States region, or is blank |

# 

# 

7. # **Settlements\\Geonames\\allCountries\\GL**

**Title**: GreenLand Geonames   
**Abstract**: This dataset includes various types of geographic features such as cities, towns, natural features (like mountains, lakes, and rivers), and other significant landmarks. The "Greenland Geonames" shapefile serves as an essential reference for mapping, navigation, and geographical analysis, providing a detailed catalog of named locations throughout the country.  
**Purpose**: The shapefile is to provide an authoritative and standardized geospatial representation of geographic names across Greenland. This dataset aims to support a wide range of applications, including mapping and cartography and geospatial analysis.   
**Keywords:** GreenLand Geography, Place Names, Cartography   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 83.666670 degree Bottom: 59.723060 degree Left: \-73.167570 degree Right: \-12.133330 degree**

**Spatial Resolution:** 0.0000000000000101642427807746 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: Field 9, 10, 12, 13,14,15,16,17 etc are removed because these attributes are blank, and some numbers are random. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 7527 records.   
- **Consistency**: The dataset is consistent with 13 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** [GeoNames](https://www.geonames.org/export/)  
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| GL\_Geonames | WGS 1984  | Point | 7527 | 13 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Field1 | Long | Long numeric code |
|  |  |  |  |  | Field2 | Text | Name of location, such as “Kap Wynn” |
|  |  |  |  |  | Field3 | Text | Seems to be exactly the same as Field2 |
|  |  |  |  |  | Field4 | Text | Seems to be alternate names for field1. Most rows are blank |
|  |  |  |  |  | Field5 | Double | Seems to be latitude |
|  |  |  |  |  | Field6 | Double | Seems to be longitude |
|  |  |  |  |  | Field7 | Text | Is a letter A, H, T, V, L, P, R, or S not defined anywhere |
|  |  |  |  |  | Field8 | Text | Defines the location as the type of country, state, region….steam, lake…with codes defined in the GeoNames\_CODES file located in the GeoNames section of settlements file |
|  |  |  |  |  | Field11 | Long | An undefined number 0-7, or one of two obscure long numbers |
|  |  |  |  |  | Field18 | Text | Seems to say the region, such as “America/Thule” |
|  |  |  |  |  | Field19 | Date | An unspecified date..maybe when data was collected |

# 

8. # **Settlements\\Geonames\\allCountries\\SE**

**Title**: Sweden Geonames   
**Abstract**: This dataset includes various types of geographic features such as cities, towns, natural features (like mountains, lakes, and rivers), and other significant landmarks. The "Sweden Geonames" shapefile serves as an essential reference for mapping, navigation, and geographical analysis, providing a detailed catalog of named locations throughout the country.  
**Purpose**: The shapefile is to provide an authoritative and standardized geospatial representation of geographic names across Sweden. This dataset aims to support a wide range of applications, including mapping and cartography and geospatial analysis.   
**Keywords:** Sweden Geography, Place Names, Cartography   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 69.050000 degree Bottom: 55.050000 degree Left: 10.816670 degree Right: 24.166670 degree**

**Spatial Resolution:** 0.00000000000000233146835171283 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The field cc2 (alternate country codes) is removed because these attributes are blank. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 7554 records.   
- **Consistency**: The dataset is consistent with 19 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** [GeoNames](https://www.geonames.org/export/)   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| SE\_Geonames | WGS 1984  | Point | 7554 | 19 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | geonameid | Long | Long numeric code |
|  |  |  |  |  | name | Text | Name of location, such as “Kap Wynn” |
|  |  |  |  |  | asciiname | Text | Seems to be exactly the same as Field2, but without any umlauts, other special letter forms |
|  |  |  |  |  | alternatenames | Text | alternate names for the locations. Most rows are blank |
|  |  |  |  |  | latitude | Double | Latitude in decimal degrees |
|  |  |  |  |  | longitude | Double | Longitude in decimal degrees |
|  |  |  |  |  | Feature class | Text | see http://www.geonames.org/export/codes.html |
|  |  |  |  |  | Feature code | Text | Defines the location as the type of country, state, region….stream, lake…see http://www.geonames.org/export/codes.html |
|  |  |  |  |  | Admin1 code | Long | Fipscode, A number 0-28 |
|  |  |  |  |  | Admin2 code | Long | Code for the second administrative division, a county in the US |
|  |  |  |  |  | Admin3 code | Long | Code for the third level administrative division |
|  |  |  |  |  | Admin4 code | Long | Code for the fourth level administrative division, many rows say 0 |
|  |  |  |  |  | population | Long |  |
|  |  |  |  |  | elevation | Text | In meters |
|  |  |  |  |  | dem | Long | Digital elevation model, srtm3 or gtopo30, average |
|  |  |  |  |  | timezone | Text | The iana timezone id |
|  |  |  |  |  | Modification date | Date | Date of last modification in yyyy-MM-dd format |

# 

9. # **Settlements\\Alaska\_multipolygons**

**Title**: Alaska multipolygons  
**Abstract**: The "Alaska\_multipolygons" shapefile is a detailed geospatial dataset that contains multipolygon geometries representing various geographic and administrative boundaries within the state of Alaska. This dataset includes multiple types of polygons such as land parcels, protected areas, municipal boundaries, and other significant regions.  
**Purpose**: The purpose of the "Alaska\_multipolygons" shapefile is to provide a comprehensive geospatial representation of various multipolygonal boundaries within Alaska. This dataset aims to support a wide range of applications, including land management and planning, environmental conservation.   
**Keywords:** Alaska multipolygons, administrative boundaries  
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 66.900787 degree Bottom: 55.205761 degree Left: \-165.398375 degree Right: \-134.632787 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: addr\_unit, building\_l, operator etc are removed because these attributes are blank and do not serve any useful purpose. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 14 records.   
- **Consistency**: The dataset is consistent with 22 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Alaska\_multipolygons.shp | WGS 1984 | Polygon | 14 | 22 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full\_id  | String | If osm\_type is relation, full\_id starts with r. If osm\_type is way, full\_id starts with w.  |
|  |  |  |  |  | osm\_id  | String  | Open Street Map ID, the only difference is that osm\_id doesn’t start with a letter.  |
|  |  |  |  |  | osm\_type  | String | Open Street Map Type. It’s either relation or way.  |
|  |  |  |  |  | amenity  | String  | All the amenity type is university.  |
|  |  |  |  |  | phone  | String  |  |
|  |  |  |  |  | layer  | String |  |
|  |  |  |  |  | building  | String  | Only contains two datapoint: university, yes.  |
|  |  |  |  |  | wikipedia  | String |  |
|  |  |  |  |  | wikidata  | String |  |
|  |  |  |  |  | website  | String |  |
|  |  |  |  |  | operator\_t  | String  | Two datapoints say public.  |
|  |  |  |  |  | addr\_stree  | String | street |
|  |  |  |  |  | addr\_state  | String  | state |
|  |  |  |  |  | addr\_postc  | String | Postal code |
|  |  |  |  |  | addr\_house | String | House Number |
|  |  |  |  |  | addr\_city  | String  | City |
|  |  |  |  |  | type  | String | Geometric types: multipolygons |
|  |  |  |  |  | name  | String |  |

# 

10. # **Settlements\\Alaska\_points**

**Title**: Alaska points  
**Abstract**: The "Alaska Points" shapefile is a comprehensive geospatial dataset containing point data representing various geographic and man-made features across the state of Alaska. This dataset includes points corresponding to locations such as cities, towns, landmarks, natural features (e.g., mountains, lakes), and infrastructure (e.g., airports, schools).  
**Purpose**: The purpose of the "Alaska Points" shapefile is to offer a detailed geospatial representation of significant point features within Alaska. This dataset aims to support a wide range of applications, including mapping and navigation, geographic analysis.   
**Keywords:** Alaska points, infrastructure, mapping  
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 61.576784 degree Bottom: 58.384922 degree Left: \-149.809844 degree Right: \-134.639702 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: wikipedia, internet\_1, internet\_a etc are removed because these attributes are blank and not very useful for the audience. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 4 records.   
- **Consistency**: The dataset is consistent with 18 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Alaska\_points | WGS 1984 | Point | 4 | 18 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full\_id | Text | The ID with the initial letter to represent the geographical property |
|  |  |  |  |  | osm\_id | Text | The ID without the initial letter to represent the geographical property |
|  |  |  |  |  | osm\_type | Text | The word to represent geographical property such as node |
|  |  |  |  |  | amenity | Text | The desirable feature of the point; in this case, university |
|  |  |  |  |  | wheelchair | Text | Whether it is user-friendly to wheelchair users |
|  |  |  |  |  | addr\_house | Text |  |
|  |  |  |  |  | wikidata | Text |  |
|  |  |  |  |  | website | Text | Website information for further research |
|  |  |  |  |  | name | Text | The name of university |
|  |  |  |  |  | internet\_a | Text |  |
|  |  |  |  |  | internet\_1 | Text |  |
|  |  |  |  |  | descriptio | Text | The description of university |
|  |  |  |  |  | addr\_stree | Text | The street of university |
|  |  |  |  |  | addr\_state | Text | The state of university |
|  |  |  |  |  | addr\_postc | Text | The postal code of university |
|  |  |  |  |  | addr\_count | Text | The country of university |
|  |  |  |  |  | addr\_city | Text | The city of university |

11. # **Settlements\\Alaska\_Schools**

**Title**: Alaska schools  
**Abstract**: The "Alaska Schools" shapefile is a specialized geospatial dataset that provides the locations and attributes of educational institutions across the state of Alaska. This dataset includes various types of schools, such as elementary, middle, high schools, and higher education institutions.  
**Purpose**: The purpose of the "Alaska Schools" shapefile is to provide a comprehensive geospatial representation of educational institutions across Alaska. This dataset aims to support a variety of applications, including educational planning.   
**Keywords:** educational institutions, public schools, private schools   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 71.298120 degree Bottom: 52.213020 degree Left: \-174.206891 degree Right: \-131.575503 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: addr\_house, addr\_house\_1, internet\_1, internet\_2, opeartor\_t, internet\_1a, highway etc are removed because these attributes are blank and not very useful for the audience. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 88 records.   
- **Consistency**: The dataset is consistent with 40  attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Alaska\_Schools | WGS 1984 | Point | 88 | 40 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full\_id | Text | The ID with the initial letter to represent the geographical property |
|  |  |  |  |  | osm\_id | Text | The ID without the initial letter to represent the geographical property |
|  |  |  |  |  | osm\_type | Text | The word to represent geographical property such as node |
|  |  |  |  |  | osm\_versio | Text | The version of open street map |
|  |  |  |  |  | osm\_timest | Text | The time when the photo is taken by open street map |
|  |  |  |  |  | osm\_uid | Text | Open Street Map\_ University ID |
|  |  |  |  |  | osm\_user | Text | OpenStreetMap User |
|  |  |  |  |  | osm\_change | Text | OpenStreetMap Change |
|  |  |  |  |  | amenity | Text | The desirable feature of the point; in this case, university |
|  |  |  |  |  | descriptio | Text | The description of school |
|  |  |  |  |  | office | Text | The office of school |
|  |  |  |  |  | short\_name | Text | The abbreviated name of school |
|  |  |  |  |  | contact\_yo | Text | The contact in youtube |
|  |  |  |  |  | contact\_tw | Text | The contact in twiter |
|  |  |  |  |  | contact\_in | Text | The contact in instagram  |
|  |  |  |  |  | contact\_fa | Text | The contact in facebook |
|  |  |  |  |  | level | Text |  |
|  |  |  |  |  | crossing | Text | Whether it has traffic Signals |
|  |  |  |  |  | bicycle | Text | Whether the school is user-friendly to bicycle |
|  |  |  |  |  | barrier | Text | The barrier of school |
|  |  |  |  |  | entrance | Text | Whether the school has entrance |
|  |  |  |  |  | name\_en | Text | English Name |
|  |  |  |  |  | phone | Text |  |
|  |  |  |  |  | email | Text |  |
|  |  |  |  |  | internet\_a | Text | Suggest deleting |
|  |  |  |  |  | operator | Text | The university which operates the school |
|  |  |  |  |  | website | Text |  |
|  |  |  |  |  | addr\_state | Text | State of school |
|  |  |  |  |  | addr\_city | Text | State of city |
|  |  |  |  |  | designatio | Text | The type of school e.g. high school, university |
|  |  |  |  |  | addr\_stree | Text | Street of school |
|  |  |  |  |  | addr\_postc | Text | Postal code of school |
|  |  |  |  |  | wheelchair | Text | Whether it is user-friendly |
|  |  |  |  |  | grades | Text | Grade level of school |
|  |  |  |  |  | check\_date | Text |  |
|  |  |  |  |  | name | Text | Name of school |

# 

12. # **Settlements\\Canada\_Universities**

**Title**: Canada Universities   
**Abstract**: The "Canada\_Universities" shapefile is a comprehensive geospatial dataset that maps the locations of universities across Canada, situated within various urban and rural settlements. This dataset includes detailed information on the geographic coordinates, names, and other relevant attributes of universities, providing a clear representation of higher education institutions across the country.  
**Purpose**: The purpose of the "Canada\_Universities" shapefile is to provide a detailed geospatial representation of universities across Canada, situated within different settlements. This dataset aims to support a range of applications, including educational planning and development  
**Keywords:** higher education, academic planning   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 69.122447 degree Bottom: 51.707152 degree Left: \-135.321977 degree Right: \-66.808629 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: addr\_street1, opeartor\_t, internet\_a etc are removed because these attributes are blank and not very useful for the audience. . 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 157 records.   
- **Consistency**: The dataset is consistent with 39 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Canada\_Universities | WGS 1984 | Point | 157 | 39 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full\_id | Text | Full name of ID |
|  |  |  |  |  | osm\_id | Text | OpenStreetMap ID  |
|  |  |  |  |  | osm\_type | Text | OpenStreetMap type |
|  |  |  |  |  | amenity | Text | College, university |
|  |  |  |  |  | alt\_name | Text | Alternative Name |
|  |  |  |  |  | layer | Text |  |
|  |  |  |  |  | toilets\_wh | Text | Not sure about the meaning. Only two rows say yes.  |
|  |  |  |  |  | old\_name | Text |  |
|  |  |  |  |  | level | Text | Education level |
|  |  |  |  |  | traffic\_ca | Text | Has bump or not |
|  |  |  |  |  | wikipedia\_ | Text |  |
|  |  |  |  |  | wikidata | Text |  |
|  |  |  |  |  | addr\_unit | Text |  |
|  |  |  |  |  | crossing\_r | Text | Several rows say zebra |
|  |  |  |  |  | automatic\_ | Text |  |
|  |  |  |  |  | phone | Text |  |
|  |  |  |  |  | wheelchair | Text | User friendly to wheelchairs |
|  |  |  |  |  | website | Text |  |
|  |  |  |  |  | addr\_postc | Text | Postal code |
|  |  |  |  |  | entrance | Text | Has an entrance or not |
|  |  |  |  |  | crossing | Text | Traffic signals |
|  |  |  |  |  | name | Text |  |
|  |  |  |  |  | addr\_stree | Text |  |
|  |  |  |  |  | addr\_city | Text |  |
|  |  |  |  |  | highway | Text |  |
|  |  |  |  |  | short\_name | Text |  |
|  |  |  |  |  | source\_nam | Text |  |
|  |  |  |  |  | descriptio | Text |  |
|  |  |  |  |  | addr\_provi | Text | Province  |
|  |  |  |  |  | building | Text |  |
|  |  |  |  |  | crop | Text |  |
|  |  |  |  |  | wikipedia | Text |  |
|  |  |  |  |  | type | Text |  |
|  |  |  |  |  | operator | Text |  |
|  |  |  |  |  | addr\_state | Text |  |
|  |  |  |  |  | path | Text |  |

# 

13. # **Settlements\\FIN\_multipolygons**

**Title**: Finland Multipolygons   
**Abstract**: The "Finland Multipolygons" shapefile is a detailed geospatial dataset that encompasses multipolygon geometries representing various geographic, administrative, and land-use boundaries across Finland. This dataset includes a wide range of polygonal features such as national and regional boundaries, protected areas, urban zones, and other significant land divisions.   
**Purpose**: The purpose of the "Finland Multipolygons" shapefile is to offer a comprehensive geospatial representation of various multipolygonal boundaries within Finland. This dataset aims to support a variety of applications, including land and resource management.   
**Keywords:** land use, administrative boundaries   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 69.757117 degree Bottom: 59.973744 degree Left: 19.926804 degree Right: 29.781299 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: man\_made, alt\_name\_f, alt\_name\_e, descript\_1, descript\_2, int\_name, short\_na\_1, short\_na\_2, ref\_vatin, phone\_open, operator\_f, operator\_e, old\_name\_s, old\_name\_1, old\_name\_e, name\_ru, name\_fr, name\_es, isced\_fiel, addr\_pobox, addr\_pob\_1, addr\_pob\_2, addr\_stree, addr\_str\_1, toilets\_wh, old\_name\_r, old\_name\_f, old\_name\_2, old\_name\_3, old\_name\_d, isced\_leve, fax, addr\_posta, addr\_pos\_1, short\_na\_3, name\_sv, name\_fi, name\_en, internet\_a, internet\_1, internet\_2, addr\_str\_2, addr\_postc, addr\_hou\_1 are removed because these attributes are blank and repetitive. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 116 records.   
- **Consistency**: The dataset is consistent with 46 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| FIN\_multipolygons | WGS 1984 | Polygon | 116 | 46 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full\_id | Text | Full name of ID |
|  |  |  |  |  | osm\_id | Text | OpenStreetMap ID |
|  |  |  |  |  | osm\_type | Text | OpenStreetMap Type |
|  |  |  |  |  | amenity | Text |  |
|  |  |  |  |  | faculty | Text | Business, art\_and\_design |
|  |  |  |  |  | operator\_t | Text | Only one row says private. |
|  |  |  |  |  | addr\_house | Text | House Name |
|  |  |  |  |  | covered | Text | Whether it has cover or not |
|  |  |  |  |  | ref | Text | Reference? |
|  |  |  |  |  | addr\_unit | Text | Address Unit |
|  |  |  |  |  | name\_ko | Text | Suggest deleting because the character is not understandable.  |
|  |  |  |  |  | man\_made | Text | Delete |
|  |  |  |  |  | access | Text | Private or not  |
|  |  |  |  |  | descriptio | Text | description |
|  |  |  |  |  | start\_date | Text |  |
|  |  |  |  |  | loc\_name | Text | Location name |
|  |  |  |  |  | layer | Text |  |
|  |  |  |  |  | url | Text |  |
|  |  |  |  |  | short\_name | Text |  |
|  |  |  |  |  | old\_name2 | Text |  |
|  |  |  |  |  | wikimedia\_ | Text |  |
|  |  |  |  |  | name\_de | Text |  |
|  |  |  |  |  | landuse | Text | Landuse Type: Educationon |
|  |  |  |  |  | email | Text |  |
|  |  |  |  |  | phone | Text |  |
|  |  |  |  |  | source\_nam | Text |  |
|  |  |  |  |  | addr\_place | Text | Place address |
|  |  |  |  |  | wikipedia | Text |  |
|  |  |  |  |  | wikidata | Text |  |
|  |  |  |  |  | old\_name | Text | Old Name |
|  |  |  |  |  | alt\_name | Text | Alternative Name |
|  |  |  |  |  | roof\_shape | Text |  |
|  |  |  |  |  | roof\_level | Text |  |
|  |  |  |  |  | building\_l | Text |  |
|  |  |  |  |  | addr\_count | Text |  |
|  |  |  |  |  | wheelchair | Text |  |
|  |  |  |  |  | website | Text |  |
|  |  |  |  |  | type | Text |  |
|  |  |  |  |  | operator | Text |  |
|  |  |  |  |  | name | Text |  |
|  |  |  |  |  | building | Text |  |
|  |  |  |  |  | addr\_city | Text |  |

# 

# 

14. # **Settlements\\Finland\_centroids2**

**Title**: Finland Centroids  
Abstract: The "Finland Centroids" shapefile is a geospatial dataset that contains the centroids of various geographic and administrative regions across Finland. A centroid is the geometric center of a polygon, often used as a representative point for spatial features such as municipalities, land parcels, or other delineated areas.   
**Purpose**: The purpose of the shapefile is to provide a geospatial dataset of centroid points for various regions within Finland. This dataset aims to support a variety of applications, including spatial analysis and mapping and visualization.   
**Keywords:** centroid points, geospatial data   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 69.757054 degree Bottom: 59.974971 degree Left: 19.927540 degree Right: 29.779513 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: operator\_t, addr\_house, addr\_unit, name\_ko, alt\_name\_f, descript\_1, descript\_2, short\_na\_1, short\_na\_2, operator\_f, operator\_e, old\_name\_s, old\_name\_1, old\_name\_e, old\_name2, name\_ru, name\_fr, name\_es, isced\_fiel, addr\_pobox, addr\_pob\_1, addr\_pob\_2, addr\_str\_1, toilets\_wh, old\_name\_r, old\_name\_f, old\_name\_2, old\_name\_3, old\_name\_d, addr\_pos\_1, short\_na\_3, name\_sv, name\_fi, name\_en, internet\_1, internet\_2, addr\_str\_2, addr\_hou\_1 etc are removed because these attributes are blank and not very useful for the audience. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 10 records.   
- **Consistency**: The dataset is consistent with 49 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:**   
**Organization:** NordRegio   
**Position:** NA  
**Email:** NA  
**Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Finland\_centroids | WGS 1984 | Point | 10 | 49 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full\_id | Text | Full ID |
|  |  |  |  |  | osm\_id | Text | OpenStreetMap ID |
|  |  |  |  |  | osm\_type | Text | OpenStreetMap Type |
|  |  |  |  |  | amenity | Text |  |
|  |  |  |  |  | faculty | Text |  |
|  |  |  |  |  | covered | Text |  |
|  |  |  |  |  | ref | Text |  |
|  |  |  |  |  | man\_made | Text | observatory |
|  |  |  |  |  | access | Text |  |
|  |  |  |  |  | descriptio | Text |  |
|  |  |  |  |  | alt\_name\_e | Text |  |
|  |  |  |  |  | start\_date | Text |  |
|  |  |  |  |  | loc\_name | Text |  |
|  |  |  |  |  | int\_name | Text |  |
|  |  |  |  |  | layer | Text |  |
|  |  |  |  |  | url | Text |  |
|  |  |  |  |  | short\_name | Text |  |
|  |  |  |  |  | ref\_vatin | Text |  |
|  |  |  |  |  | phone\_open | Text | The time window for phone call |
|  |  |  |  |  | wikimedia\_ | Text |  |
|  |  |  |  |  | name\_de | Text |  |
|  |  |  |  |  | addr\_stree | Text |  |
|  |  |  |  |  | isced\_leve | Text | Change it to ice\_level |
|  |  |  |  |  | fax | Text |  |
|  |  |  |  |  | addr\_posta | Text |  |
|  |  |  |  |  | landuse | Text |  |
|  |  |  |  |  | email | Text |  |
|  |  |  |  |  | phone | Text |  |
|  |  |  |  |  | source\_nam | Text |  |
|  |  |  |  |  | internet\_a | Text |  |
|  |  |  |  |  | addr\_place | Text |  |
|  |  |  |  |  | wikipedia | Text |  |
|  |  |  |  |  | wikidata | Text |  |
|  |  |  |  |  | old\_name | Text |  |
|  |  |  |  |  | alt\_name | Text |  |
|  |  |  |  |  | roof\_shape | Text |  |
|  |  |  |  |  | roof\_level | Text |  |
|  |  |  |  |  | building\_l | Text |  |
|  |  |  |  |  | addr\_count | Text |  |
|  |  |  |  |  | wheelchair | Text |  |
|  |  |  |  |  | website | Text |  |
|  |  |  |  |  | type | Text |  |
|  |  |  |  |  | operator | Text |  |
|  |  |  |  |  | name | Text |  |
|  |  |  |  |  | building | Text |  |
|  |  |  |  |  | addr\_postc | Text |  |
|  |  |  |  |  | addr\_city | Text |  |

15. # **Settlements\\Finland\_Merged(Finland\_Univ\_ARTIC)**

**Title**: Finland Merged  
**Abstract**: The "Finland\_Merged" shapefile is a comprehensive geospatial dataset that consolidates various geographic and administrative boundaries across Finland into a single, unified layer. This dataset may include merged data from different sources such as municipal boundaries, regions, land-use zones, and other relevant geographic divisions.   
**Purpose**: The purpose of the "Finland\_Merged" shapefile is to provide a unified geospatial representation of various geographic and administrative boundaries within Finland. This dataset aims to support a variety of applications, including integrated spatial analysis.   
**Keywords:** Finland Merged, environmental management   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 69.757054 degree Bottom: 59.844477 degree Left: 19.830796 degree Right: 29.779513 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: name\_fi, isced\_leve, name\_sv, toilets\_wh, alt\_name\_e, short\_na\_1, short\_na\_2, name\_ru, name\_fr, name\_es, isced\_fiel, addr\_pobox, addr\_pob\_1, addr\_pob\_2, old\_name\_2, old\_name\_3, old\_name\_d, addr\_pos\_1, short\_na\_3, addr\_place etc are removed because these attributes are blank and not very useful for the audience.  

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 238 records.   
- **Consistency**: The dataset is consistent with 21 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Finland\_Merged | WGS 1984 | Point | 238 | 21 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full\_id | Text | Full ID name |
|  |  |  |  |  | osm\_id | Text | OpenStreetMap ID |
|  |  |  |  |  | osm\_type | Text | OpenStreetMap Type |
|  |  |  |  |  | name\_en | Text | English Name |
|  |  |  |  |  | wikipedia | Text |  |
|  |  |  |  |  | wikidata | Text |  |
|  |  |  |  |  | wheelchair | Text | Whether it is user-friendly to wheelchair |
|  |  |  |  |  | name | Text |  |
|  |  |  |  |  | loc\_name | Text |  |
|  |  |  |  |  | int\_name | Text |  |
|  |  |  |  |  | layer | Text |  |
|  |  |  |  |  | url | Text |  |
|  |  |  |  |  | wikimedia\_ | Text |  |
|  |  |  |  |  | old\_name\_r | Text |  |
|  |  |  |  |  | addr\_posta | Text | Postal Code |
|  |  |  |  |  | landuse | Text | Landuse type: Education |
|  |  |  |  |  | source\_nam | Text | Source of information: survey, common knowledge |
|  |  |  |  |  | path | Text |  |

# 

16. # **Settlements\\GreenLand\_Universities** 

**Title**: GreenLand Universities   
**Abstract**: The "Greenland Universities" shapefile is a specialized geospatial dataset that maps the locations and attributes of higher education institutions across Greenland. This dataset includes data points for universities and other institutions offering tertiary education, providing details such as geographic coordinates, institution names, and possibly additional attributes like enrollment size or academic specialties.  
**Purpose**: The purpose of the "Greenland Universities" shapefile is to provide a detailed geospatial representation of universities and other higher education institutions in Greenland. This dataset aims to support a variety of applications, including educational planning and development, research analysis.   
**Keywords:** higher education, greenland universities  
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 69.253357 degree Bottom: 64.168268 degree Left: \-53.651842 degree Right: \-51.696475 degree**

**Spatial Resolution:** 0.000000000000000846837297696301 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: name\_kl, internet\_a, name\_zh, name\_uk, name\_pt, name\_pl, name\_it, name\_is, name\_fr, name\_et, name\_es, name\_da, name\_be, name\_ar, operator etc are removed because these attributes are blank and repetitive. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 6 records.   
- **Consistency**: The dataset is consistent with 21 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Greenland\_Universities | Unknown  | Point | 6 | 21 | FID  | OID  |  |
|  |  |  |  |  | Shape  | Geometry  |  |
|  |  |  |  |  | full\_id  | String  | Full ID name |
|  |  |  |  |  | osm\_id  | String | OpenStreetMap ID |
|  |  |  |  |  | osm\_type  | String  | OpenStreetMap Type |
|  |  |  |  |  | amenity  | String |  |
|  |  |  |  |  | name\_en name  | String | English Name |
|  |  |  |  |  | addr\_unit  | String | unit |
|  |  |  |  |  | addr\_stree  | String  | street |
|  |  |  |  |  | addr\_city  | String | city |
|  |  |  |  |  | wikipedia  | String  |  |
|  |  |  |  |  | wikidata  | String |  |
|  |  |  |  |  | website  | String  |  |
|  |  |  |  |  | layer  | String  |  |
|  |  |  |  |  | path  | String |  |

17. # **Settlements\\Iceland\_point** 

**Title**: Iceland points   
**Abstract**: The "Iceland Point" shapefile is a geospatial dataset that contains point data representing various significant locations across Iceland. This dataset includes points corresponding to cities, towns, landmarks, natural features (such as volcanoes, waterfalls, and glaciers), and infrastructure elements (such as airports and schools).   
**Purpose**: The purpose of the "Iceland Point" shapefile is to provide a detailed geospatial representation of significant point locations within Iceland. This dataset aims to support a wide range of applications, including mapping and navigation.   
**Keywords:** iceland point, geospatial data   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 66.068934 degree Bottom: 63.442923 degree Left: \-23.126112 degree Right: \-20.268816 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** No attributes are removed. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 2 records.   
- **Consistency**: The dataset is consistent with 13 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| iceland\_point | WGS 1984 | Point | 2 | 13  | FID  | OID  |  |
|  |  |  |  |  | Shape  | Geometry  |  |
|  |  |  |  |  | full\_id  | String  | Full ID name |
|  |  |  |  |  | osm\_id  | String | OpenStreetMap ID |
|  |  |  |  |  | osm\_type  | String  | OpenStreetMap Type |
|  |  |  |  |  | amenity  | String |  |
|  |  |  |  |  | operator  | String  |  |
|  |  |  |  |  | addr\_stree  | String | Street number |
|  |  |  |  |  | addr\_postc  | String  |  |
|  |  |  |  |  | addr\_house  | String | House number |
|  |  |  |  |  | addr\_city  | String  |  |
|  |  |  |  |  | name  | String | School Name |
|  |  |  |  |  | alt\_name  | String |  |

# 

18. # **Settlements\\Iceland\_poly(Iceland Universities)**

**Title**: Iceland universities  
**Abstract**: The "Iceland Polygon" shapefile is a geospatial dataset that provides polygonal representations of various geographic, administrative, and land-use boundaries within Iceland. This dataset includes polygons for regions such as municipalities, protected areas, land-use zones, and natural features (e.g., national parks, forests, and bodies of water).  
**Purpose**: The purpose of the "Iceland Polygon" shapefile is to provide a detailed geospatial representation of various polygonal boundaries within Iceland. This dataset aims to support a variety of applications, including land and resource management.   
**Keywords:** iceland polygon, environmental conservation  
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 65.686429 degree Bottom: 64.122586 degree Left: \-21.963143 degree Right: \-18.117967 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree   
**Coordinate Reference System:** WGS 1984  
**Lineage:** Attributes: name\_fa, building\_l, operator, name\_ru, name\_pt, name\_it, name\_fr, name\_es, name\_de, official\_n are removed because these attributes are blank and not very useful for the audience. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 2 records.   
- **Consistency**: The dataset is consistent with 21 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Iceland\_poly | WGS 1984 | Polygon | 2 | 21 | FID  | OID  |  |
|  |  |  |  |  | Shape  | Geometry  |  |
|  |  |  |  |  | full\_id  | String  | Full ID name |
|  |  |  |  |  | osm\_id | String | OpenStreetMap ID |
|  |  |  |  |  | osm\_type  | String  | OpenStreetMap Type |
|  |  |  |  |  | amenity  | String |  |
|  |  |  |  |  | phone  | String |  |
|  |  |  |  |  | email  | String  |  |
|  |  |  |  |  | building  | String |  |
|  |  |  |  |  | int\_name  | String |  |
|  |  |  |  |  | wikipedia  | String  |  |
|  |  |  |  |  | wikidata | String |  |
|  |  |  |  |  | wheelchair  | String  |  |
|  |  |  |  |  | short\_name | String |  |
|  |  |  |  |  | website  | String  |  |
|  |  |  |  |  | type  | String |  |
|  |  |  |  |  | name\_en  | String | English Name |
|  |  |  |  |  | name  | String  |  |
|  |  |  |  |  | addr\_stree | String | street |
|  |  |  |  |  | addr\_postc  | String  | Postal code |
|  |  |  |  |  | addr\_house  | String |  |
|  |  |  |  |  | addr\_city  | String  |  |

# 

19. # **Settlements\\Murmansk\_Universities**

**Title**: Murmansk Universities   
**Abstract**: The "Murmansk Universities" shapefile is a specialized geospatial dataset that maps the locations and attributes of higher education institutions in the Murmansk region of Russia. This dataset includes data points for universities and other institutions offering tertiary education, providing details such as geographic coordinates, institution names, and possibly additional attributes like enrollment size or academic specialties.   
**Purpose**: The purpose of the "Murmansk Universities" shapefile is to provide a detailed geospatial representation of universities and other higher education institutions in the Murmansk region. This dataset aims to support a variety of applications, including educational planning and development.   
**Keywords:** higher education, university locations   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 69.006289 degree Bottom: 68.936666 degree Left: 33.062094 degree Right: 33.102133 degree**

**Spatial Resolution:0.0000000000000888178419700125 Degree**  
**Coordinate Reference System:** WGS 1984  
**Lineage:** No attributes are removed. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 15 records.   
- **Consistency**: The dataset is consistent with 25 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Murmansk\_Universities | WGS 1984 | Point | 15 | 25 | FID  | OID  |  |
|  |  |  |  |  | Shape  | Geometry  |  |
|  |  |  |  |  | full\_id  | String  | Full ID name |
|  |  |  |  |  | osm\_id  | String | OpenStreetMap ID |
|  |  |  |  |  | osm\_type  | String  | OpenStreetMap Type |
|  |  |  |  |  | amenity  | String |  |
|  |  |  |  |  | website  | String  |  |
|  |  |  |  |  | phone  | String |  |
|  |  |  |  |  | opening\_ho   | String  | Opening hours  |
|  |  |  |  |  | barrier  | String | The type of barrier. For example, gate.  |
|  |  |  |  |  | access  | String  |  |
|  |  |  |  |  | name  | String |  |
|  |  |  |  |  | short\_name   | String |  |
|  |  |  |  |  | official\_n   | String  | Official name  |
|  |  |  |  |  | building\_l   | String | Whether there is a building |
|  |  |  |  |  | operator  | String  |  |
|  |  |  |  |  | wikipedia  | String |  |
|  |  |  |  |  | wikidata   | String  |  |
|  |  |  |  |  | old\_name   | String |  |
|  |  |  |  |  | building  | String  |  |
|  |  |  |  |  | addr\_stree  | String | Address street |
|  |  |  |  |  | addr\_house  | String  | Address house |
|  |  |  |  |  | addr\_city  | String | Address city  |
|  |  |  |  |  | layer  | String  |  |
|  |  |  |  |  | path  | String |  |

# 

20. # **Settlements\\Norway\_poly**

**Title**: Norway Polygons   
**Abstract**: The "Norway Polygons" shapefile is a comprehensive geospatial dataset that includes polygonal representations of various geographic, administrative, and land-use boundaries within Norway. This dataset encompasses a wide range of polygons, such as municipal and regional boundaries, protected areas, natural features (e.g., lakes, mountains), and other significant land divisions.  
**Purpose**: The purpose of the "Norway Polygons" shapefile is to provide a detailed geospatial representation of various polygonal boundaries within Norway. This dataset aims to support a variety of applications, including land resource management.   
**Keywords:** land use, protected areas, Norway   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 78.222601 degree Bottom: 58.163185 degree Left: 5.273695 degree Right: 23.674555 degree**

**Spatial Resolution:0.0000000000000888178419700125 Degree**  
**Coordinate Reference System:** WGS 1984  
**Lineage:** Attributes: toilets\_wh, shortest\_n, name\_ko, name\_ru, name\_nn, ssr\_stedsn, ref\_bygnin are removed because these attributes are blank and not very useful for the audience. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 64 records.   
- **Consistency**: The dataset is consistent with 49 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Norway\_poly | WGS 1984 | Point | 64 | 49  | FID  | OID  |  |
|  |  |  |  |  | Shape  | Geometry  |  |
|  |  |  |  |  | full\_id  | String  | Full ID name |
|  |  |  |  |  | osm\_id  | String | OpenStreetMap ID |
|  |  |  |  |  | osm\_type  | String  | OpenStreetMap Type |
|  |  |  |  |  | amenity  | String |  |
|  |  |  |  |  | contact\_ph  | String  | Contact phone number  |
|  |  |  |  |  | roof\_shape  | String |  |
|  |  |  |  |  | roof\_level  | String  |  |
|  |  |  |  |  | building\_l  | String |  |
|  |  |  |  |  | landuse  | String | The landuse type |
|  |  |  |  |  | barrier  | String | The type of barrier. For example, gate.  |
|  |  |  |  |  | isced\_leve  | String  | Change it to ice\_level |
|  |  |  |  |  | loc\_name  | String | Location name |
|  |  |  |  |  | opening\_ho  | String  | Opening hour |
|  |  |  |  |  | fax  | String |  |
|  |  |  |  |  | start\_date  | String  |  |
|  |  |  |  |  | note\_start  | String  | A note for further description |
|  |  |  |  |  | operator\_e  | String  |  |
|  |  |  |  |  | internet\_a  | String |  |
|  |  |  |  |  | operator\_t  | String |  |
|  |  |  |  |  | internet\_1  | String |  |
|  |  |  |  |  | internet\_2  | String  |  |
|  |  |  |  |  | email  | String |  |
|  |  |  |  |  | addr\_house  | String  |  |
|  |  |  |  |  | addr\_count  | String |  |
|  |  |  |  |  | wikipedia  | String  |  |
|  |  |  |  |  | name\_de  | String |  |
|  |  |  |  |  | int\_name  | String  |  |
|  |  |  |  |  | contact\_we  | String | Website contact |
|  |  |  |  |  | contact\_em  | String  | Email contact |
|  |  |  |  |  | wikidata | String |  |
|  |  |  |  |  | short\_name  | String |  |
|  |  |  |  |  | old\_name  | String |  |
|  |  |  |  |  | name\_no  | String |  |
|  |  |  |  |  | name\_en  | String  |  |
|  |  |  |  |  | addr\_stree  | String |  |
|  |  |  |  |  | addr\_postc  | String  |  |
|  |  |  |  |  | addr\_hou\_1  | String |  |
|  |  |  |  |  | addr\_city  | String  |  |
|  |  |  |  |  | wheelchair  | String |  |
|  |  |  |  |  | website  | String  |  |
|  |  |  |  |  | type  | String |  |
|  |  |  |  |  | phone  | String |  |
|  |  |  |  |  | operator  | String  |  |
|  |  |  |  |  | name  | String |  |
|  |  |  |  |  | building  | String |  |
|  |  |  |  |  | alt\_name  | String  | Alternative Name |

# 

21. # **Settlements\\Norway\_Universities(Norway\_Universities\_Artic)**

**Title**: Norway Universities   
**Abstract**: The "Norway Universities" shapefile is a detailed geospatial dataset that maps the locations and attributes of higher education institutions across Norway. This dataset includes points representing universities, colleges, and other institutions offering tertiary education, providing information such as geographic coordinates, institution names, and possibly additional attributes like enrollment size, academic focus, and campus facilities.  
**Purpose**: The purpose of the "Norway Universities" shapefile is to provide a detailed geospatial representation of universities and other higher education institutions in Norway. This dataset aims to support a variety of applications, including educational planning and development.   
**Keywords:** Norway universities, higher education, university locations   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 78.222601 degree Bottom: 58.163185 degree Left: 5.273695 degree Right: 23.674555 degree**

**Spatial Resolution:0.0000000000000888178419700125 Degree**  
**Coordinate Reference System:** WGS 1984  
**Lineage:** Attributes: name\_nb, internet\_a, internet\_1, operator\_t, ssr\_type, ssr\_stedsn, isced\_leve  
, ele, tactile\_pa, isced\_le\_1, loc\_name, opening\_\_1, shortest\_n, name\_ko, name\_ru, name\_nn, internet\_4, internet\_5, addr\_hou\_2, ssr\_sted\_1, addr\_str\_1, addr\_pos\_1, addr\_hou\_3, addr\_cit\_1, ref\_bygnin are removed because these attributes are blank and not very useful for the audience.

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 159 records.   
- **Consistency**: The dataset is consistent with 72 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Norway\_Universities | WGS 1984 | Point | 159 | 72 | FID  | OID  |  |
|  |  |  |  |  | Shape  | Geometry  |  |
|  |  |  |  |  | full\_id  | String | Full name ID  |
|  |  |  |  |  | osm\_id  | String  | OpenStreetMap ID |
|  |  |  |  |  | osm\_type  | String | OpenStreetMap Type |
|  |  |  |  |  | amenity  | String  |  |
|  |  |  |  |  | short\_name  | String |  |
|  |  |  |  |  | addr\_unit  | String  | Housing Unit  |
|  |  |  |  |  | start\_date  | String |  |
|  |  |  |  |  | ref\_toll  | String |  |
|  |  |  |  |  | contact\_we  | String | Website  |
|  |  |  |  |  | charge\_mot  | String  | Charing hour |
|  |  |  |  |  | charge\_m\_1  | String | Hourly pay |
|  |  |  |  |  | charge\_hgv  | String  |  |
|  |  |  |  |  | charge\_h\_1  | String |  |
|  |  |  |  |  | parking  | String  | Type of parking lot: Underground  |
|  |  |  |  |  | layer  | String |  |
|  |  |  |  |  | network  | String |  |
|  |  |  |  |  | bus  | String  |  |
|  |  |  |  |  | traffic\_ca  | String |  |
|  |  |  |  |  | opening\_ho  | String | Opening Hour |
|  |  |  |  |  | addr\_house  | String  |  |
|  |  |  |  |  | phone  | String |  |
|  |  |  |  |  | fax  | String  |  |
|  |  |  |  |  | facebook  | String |  |
|  |  |  |  |  | email  | String  |  |
|  |  |  |  |  | alt\_name  | String | Alternative Name |
|  |  |  |  |  | barrier  | String  |  |
|  |  |  |  |  | access  | String |  |
|  |  |  |  |  | entrance  | String  |  |
|  |  |  |  |  | traffic\_si  | String | Whether it has traffic sign  |
|  |  |  |  |  | button\_ope  | String  | Whether it has button operation  |
|  |  |  |  |  | wikipedia  | String |  |
|  |  |  |  |  | wikidata  | String |  |
|  |  |  |  |  | name\_en  | String |  |
|  |  |  |  |  | wheelchair  | String  |  |
|  |  |  |  |  | website  | String |  |
|  |  |  |  |  | addr\_stree  | String  | street |
|  |  |  |  |  | addr\_postc  | String | Postal code |
|  |  |  |  |  | addr\_hou\_1  | String  | house |
|  |  |  |  |  | addr\_city  | String | City  |
|  |  |  |  |  | train  | String |  |
|  |  |  |  |  | railway\_po  | String  |  |
|  |  |  |  |  | railway  | String |  |
|  |  |  |  |  | public\_tra  | String |  |
|  |  |  |  |  | name  | String | Railway Station Name |
|  |  |  |  |  | crossing\_i  | String  | Whether it has crossing |
|  |  |  |  |  | highway  | String |  |
|  |  |  |  |  | crossing  | String  |  |
|  |  |  |  |  | operator  | String |  |
|  |  |  |  |  | internet\_2  | String  |  |
|  |  |  |  |  | contact\_ph  | String | Contact Phone Number |
|  |  |  |  |  | roof\_shape  | String  |  |
|  |  |  |  |  | roof\_level  | String |  |
|  |  |  |  |  | building\_l  | String  |  |
|  |  |  |  |  | toilets\_wh  | String |  |
|  |  |  |  |  | landuse  | String  | Landuse Type |
|  |  |  |  |  | note\_start  | String | Further Description for schools |
|  |  |  |  |  | operator\_e | String |  |
|  |  |  |  |  | internet\_3  | String  |  |
|  |  |  |  |  | operator\_1  | String | University or School |
|  |  |  |  |  | addr\_count  | String | Country Address |
|  |  |  |  |  | name\_de  | String | Name Description  |
|  |  |  |  |  | int\_name  | String |  |
|  |  |  |  |  | contact\_\_1  | String  |  |
|  |  |  |  |  | contact\_em  | String | Email Contact |
|  |  |  |  |  | old\_name  | String |  |
|  |  |  |  |  | name\_no  | String  |  |
|  |  |  |  |  | name\_en\_1  | String | English Name |
|  |  |  |  |  | type  | String | Geographical Type: point or polygon  |
|  |  |  |  |  | building  | String  |  |
|  |  |  |  |  | path  | String |  |

# 

# 

22. # **Settlements\\Siberia\_Universities**

**Title**: Siberia Universities   
**Abstract**: The "Siberia Universities" shapefile is a comprehensive geospatial dataset that maps the locations and attributes of higher education institutions across the Siberian region of Russia. This dataset includes data points representing universities and other institutions offering tertiary education, providing details such as geographic coordinates, institution names, and potentially additional attributes like enrollment numbers, academic specialties, and campus facilities.  
**Purpose**: The purpose of the "Siberia Universities" shapefile is to provide a detailed geospatial representation of universities and other higher education institutions in the Siberian region. This dataset aims to support a variety of applications, including educational planning and development   
**Keywords:** Siberia universities, higher education, university locations   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 78.222601 degree Bottom: 62.005626 degree Left: \-179.122086 degree Right: 177.529286 degree**

**Spatial Resolution:0.0000000000000888178419700125 Degree**  
**Coordinate Reference System:** WGS 1984  
**Lineage:** Attributes: nat\_name, railway\_po, name\_zh, name\_uk, name\_is, name\_et, name\_da, name\_be, name\_ar, alt\_name\_f, alt\_name\_e, descript\_1, descript\_2, name\_pl, name\_ko, addr\_str\_1, addr\_str\_2, name\_se, name\_ca, int\_name, name\_sv, name\_it, name\_fr, name\_es, name\_no, name\_nn, name\_de, loc\_name, addr\_hou\_1, addr\_regio, internet\_2 are removed because these attributes are blank and not very useful for the audience.

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 264 records.   
- **Consistency**: The dataset is consistent with 34 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Siberia\_Universities3 | WGS 1984 | Point | 264 | 34 | FID | OID |  |
|  |  |  |  |  | Shape  | Geometry |  |
|  |  |  |  |  | full\_id  | String | Full ID |
|  |  |  |  |  | osm\_id  | String  | OpenStreetMap ID  |
|  |  |  |  |  | osm\_type  | String | OpenStreetMap Type |
|  |  |  |  |  | amenity  | String | University/College |
|  |  |  |  |  | vehicle  | String | Empty |
|  |  |  |  |  | lift\_gate\_  | String  | Empty |
|  |  |  |  |  | contact\_yo  | String | Youtube |
|  |  |  |  |  | contact\_fa  | String  | Facebook |
|  |  |  |  |  | addr\_state | String | state |
|  |  |  |  |  | short\_name  | String  |  |
|  |  |  |  |  | old\_name  | String |  |
|  |  |  |  |  | url  | String  |  |
|  |  |  |  |  | addr\_count  | String |  |
|  |  |  |  |  | addr\_postc | String  |  |
|  |  |  |  |  | addr\_city  | String |  |
|  |  |  |  |  | descriptio  | String |  |
|  |  |  |  |  | website | String  |  |
|  |  |  |  |  | addr\_stree  | String |  |
|  |  |  |  |  | addr\_house  | String |  |
|  |  |  |  |  | railway  | String |  |
|  |  |  |  |  | public\_tra  | String  |  |
|  |  |  |  |  | crossing\_i  | String |  |
|  |  |  |  |  | name  | String  |  |
|  |  |  |  |  | landuse  | String  | Landuse Type |
|  |  |  |  |  | place | String  |  |
|  |  |  |  |  | site | String  |  |
|  |  |  |  |  | full\_name  | String  |  |
|  |  |  |  |  | designatio  | String |  |
|  |  |  |  |  | type  | String |  |
|  |  |  |  |  | building  | String |  |
|  |  |  |  |  | layer  | String |  |
|  |  |  |  |  | path  | String  |  |

23. # **Settlements\\Sweden\_Lines**

**Title**: Sweden Lines  
**Abstract**: The "Sweden Lines" shapefile is a geospatial dataset that contains line features representing various linear elements across Sweden. This dataset includes data on roads, highways, railways, rivers, and other important linear infrastructure or natural features. The "Sweden Lines" shapefile serves as a crucial tool for transportation planning, infrastructure management, environmental studies, and geographic analysis.  
**Purpose**: The purpose of the "Sweden Lines" shapefile is to provide a comprehensive geospatial representation of linear features within Sweden. This dataset aims to support a variety of applications, including transportation planning and management.   
**Keywords:** Sweden Lines, linear features, infrastructure   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 60.487938 degree Bottom: 55.607539 degree Left: 11.444624 degree Right: 17.640931 degree**

**Spatial Resolution:0.0000000000000888178419700125 Degree**  
**Coordinate Reference System:** WGS 1984  
**Lineage:** No attributes are removed. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 28 records.   
- **Consistency**: The dataset is consistent with 22 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Sweden\_lines | WGS 1984 | Line | 28 | 22 | FID | OID  |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full\_id  | String |  |
|  |  |  |  |  | osm\_id  | String  |  |
|  |  |  |  |  | osm\_type  | String |  |
|  |  |  |  |  | natural  | String  | Natural scene: costal line |
|  |  |  |  |  | name  | String |  |
|  |  |  |  |  | footway\_su  | String  | Footway material: paving stones |
|  |  |  |  |  | cycleway\_s  | String | Cycleway material: asphalt |
|  |  |  |  |  | segregated  | String  |  |
|  |  |  |  |  | foot  | String | Foot Designated paveway  |
|  |  |  |  |  | bicycle  | String  | Bicycle  Designated paveway |
|  |  |  |  |  | surface  | String |  |
|  |  |  |  |  | lit  | String  |  |
|  |  |  |  |  | highway  | String |  |
|  |  |  |  |  | layer  | String |  |
|  |  |  |  |  | barrier  | String |  |
|  |  |  |  |  | addr\_stree  | String  |  |
|  |  |  |  |  | addr\_postc  | String |  |
|  |  |  |  |  | addr\_house  | String |  |
|  |  |  |  |  | addr\_count  | String | country |
|  |  |  |  |  | addr\_city  | String  | city |

24. # **Settlements\\Sweden\_multipolygons** 

**Title**: Sweden multipolygons   
**Abstract**: The "Sweden multipolygons" shapefile is a comprehensive geospatial dataset that includes multipolygon geometries representing various geographic, administrative, and land-use boundaries within Sweden. This dataset encompasses a wide range of polygonal features, such as national and regional boundaries, municipalities, protected areas, urban zones, and natural features (e.g., lakes, forests).  
**Purpose**: The purpose of the "Sweden multipolygons" shapefile is to provide a detailed geospatial representation of various multipolygonal boundaries within Sweden. This dataset aims to support a variety of applications, including urban and regional planning.   
**Keywords:** Sweden multipolygons, Land Use, Protected Areas   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 67.912113 degree Bottom: 55.589219 degree Left: 11.146164 degree Right: 22.146587 degree**

**Spatial Resolution:0.0000000000000888178419700125 Degree**  
**Coordinate Reference System:** WGS 1984  
**Lineage:** Attributes: internet\_a, toilets\_wh, addr\_munic, addr\_count, name\_zh-Ha  
, name\_zh-\_1, name\_ru, name\_ro, name\_pt, name\_pl, name\_nl, name\_it, name\_fa, name\_et, name\_es, name\_ca, name\_ar, isced\_leve, amenity\_1, noname, name\_ko, name\_fr, wheelcha\_1, is\_in, operator\_t, roof\_colou, name\_de, building\_l, building\_c, name\_sv, name\_en, addr\_hou\_1, addr\_cou\_1 are removed because these attributes are blank and repetitive.

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 14 records.   
- **Consistency**: The dataset is consistent with 56 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| clean\_Sweden\_multipolygons | WGS 1984 | Polygon | 14 | 56 | FID  | OID  |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full\_id | String | Full ID |
|  |  |  |  |  | osm\_id  | String  | OpenStreetMap ID |
|  |  |  |  |  | osm\_type  | String | OpenStreetMap Type |
|  |  |  |  |  | amenity  | String  |  |
|  |  |  |  |  | level  | String |  |
|  |  |  |  |  | indoor  | String  |  |
|  |  |  |  |  | telescope\_  | String |  |
|  |  |  |  |  | telescop\_1  | String  | Telescope range: 120-240MHz |
|  |  |  |  |  | descriptio | String |  |
|  |  |  |  |  | barrier  | String  | Barrier Type |
|  |  |  |  |  | building\_m  | String |  |
|  |  |  |  |  | email | String  |  |
|  |  |  |  |  | roof\_mater  | String  | Roof Material |
|  |  |  |  |  | phone  | String |  |
|  |  |  |  |  | website\_en  | String  |  |
|  |  |  |  |  | height  | String |  |
|  |  |  |  |  | man\_made  | String |  |
|  |  |  |  |  | landuse  | String  | Landuse Type |
|  |  |  |  |  | source\_ref  | String | Source Reference |
|  |  |  |  |  | smoking  | String  |  |
|  |  |  |  |  | opening\_ho  | String | Opening Hour |
|  |  |  |  |  | check\_date  | String |  |
|  |  |  |  |  | layer | String |  |
|  |  |  |  |  | loc\_name\_e  | String |  |
|  |  |  |  |  | alt\_name | String |  |
|  |  |  |  |  | roof\_shape  | String |  |
|  |  |  |  |  | ref  | String  |  |
|  |  |  |  |  | wheelchair  | String |  |
|  |  |  |  |  | start\_date  | String  |  |
|  |  |  |  |  | roof\_level  | String  |  |
|  |  |  |  |  | descript\_1  | String |  |
|  |  |  |  |  | name\_fi  | String |  |
|  |  |  |  |  | int\_name  | String  |  |
|  |  |  |  |  | official\_n  | String |  |
|  |  |  |  |  | contact\_fa  | String  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  | designatio  | String |  |
|  |  |  |  |  | loc\_name  | String  |  |
|  |  |  |  |  | short\_name  | String |  |
|  |  |  |  |  | image  | String  |  |
|  |  |  |  |  | building\_1  | String |  |
|  |  |  |  |  | operator  | String  |  |
|  |  |  |  |  | addr\_house  | String |  |
|  |  |  |  |  | old\_name  | String  |  |
|  |  |  |  |  | building  | String |  |
|  |  |  |  |  | addr\_stree  | String |  |
|  |  |  |  |  | wikipedia  | String  |  |
|  |  |  |  |  | website  | String |  |
|  |  |  |  |  | contact\_we  | String  | Website |
|  |  |  |  |  | contact\_ph  | String | Phone Number |
|  |  |  |  |  | addr\_postc  | String  | Postal Code |
|  |  |  |  |  | addr\_city  | String |  |
|  |  |  |  |  | wikidata  | String  |  |
|  |  |  |  |  | name  | String |  |
|  |  |  |  |  | type  | String |  |

25. # **Settlements\\Sweden\_points**

**Title**: Sweden points  
**Abstract**: The "Sweden Points" shapefile is a geospatial dataset that includes point data representing various significant locations across Sweden. This dataset comprises points for cities, towns, landmarks, natural features (such as mountains, lakes, and forests), infrastructure elements (such as airports, schools, and hospitals), and other notable sites.   
**Purpose**: The purpose of the "Sweden Points" shapefile is to provide a detailed geospatial representation of significant point locations within Sweden. This dataset aims to support a variety of applications, including mapping and navigation.   
**Keywords:** Sweden points, Land Use, Protected Areas, GIS data   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 65.619992 degree Bottom: 55.610590 degree Left: 11.924996 degree Right: 22.144992 degree**

**Spatial Resolution:0.0000000000000888178419700125 Degree**  
**Coordinate Reference System:** WGS 1984  
**Lineage:** Attributes: internet\_a, source\_add, opening\_\_1, operator\_t, isced\_leve, network\_wi, network\_\_1, addr\_hou\_1, is\_in, check\_da\_1, nat\_name, gtfs\_id, tactile\_pa, crossing\_i, name\_sv, name\_fi are removed because these attributes are blank and not very useful for the audience.

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 184 records.   
- **Consistency**: The dataset is consistent with 47 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of record | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Sweden\_points | WGS 1984 | Point | 184 | 47 | FID  | OID  |  |
|  |  |  |  |  | Shape  | Geometry  |  |
|  |  |  |  |  | full\_id  | String  | Full ID |
|  |  |  |  |  | osm\_id  | String | OpenStreetMap ID |
|  |  |  |  |  | osm\_type  | String  | OpenStreetMap Type |
|  |  |  |  |  | amenity  | String |  |
|  |  |  |  |  | parking  | String  |  |
|  |  |  |  |  | fee  | String |  |
|  |  |  |  |  | phone  | String |  |
|  |  |  |  |  | door  | String  |  |
|  |  |  |  |  | ref | String |  |
|  |  |  |  |  | addr\_house  | String  |  |
|  |  |  |  |  | addr\_postc  | String |  |
|  |  |  |  |  | opening\_ho  | String  | Opening Hour |
|  |  |  |  |  | motor\_vehi  | String  |  |
|  |  |  |  |  | material  | String  |  |
|  |  |  |  |  | locked  | String |  |
|  |  |  |  |  | noexit  | String  |  |
|  |  |  |  |  | foot  | String |  |
|  |  |  |  |  | shelter  | String  |  |
|  |  |  |  |  | operator  | String |  |
|  |  |  |  |  | contact\_we  | String | Website |
|  |  |  |  |  | contact\_ph  | String | Phone Number |
|  |  |  |  |  | addr\_city  | String |  |
|  |  |  |  |  | entrance  | String  |  |
|  |  |  |  |  | level  | String  |  |
|  |  |  |  |  | network  | String  |  |
|  |  |  |  |  | local\_ref  | String  | Local reference |
|  |  |  |  |  | addr\_stree  | String |  |
|  |  |  |  |  | addr\_count  | String |  |
|  |  |  |  |  | wheelchair  | String  |  |
|  |  |  |  |  | traffic\_si  | String |  |
|  |  |  |  |  | check\_date  | String |  |
|  |  |  |  |  | button\_ope  | String |  |
|  |  |  |  |  | wikimedia\_  | String |  |
|  |  |  |  |  | name\_en  | String  |  |
|  |  |  |  |  | traffic\_ca  | String |  |
|  |  |  |  |  | crossing\_r  | String  |  |
|  |  |  |  |  | public\_tra  | String |  |
|  |  |  |  |  | bus  | String |  |
|  |  |  |  |  | website  | String  |  |
|  |  |  |  |  | barrier  | String |  |
|  |  |  |  |  | access  | String  |  |
|  |  |  |  |  | highway  | String |  |
|  |  |  |  |  | crossing  | String |  |
|  |  |  |  |  | bicycle  | String  |  |
|  |  |  |  |  | wikipedia  | String |  |
|  |  |  |  |  | wikidata  | String  |  |
|  |  |  |  |  | name  | String |  |

# 

# 

26. # **Settlements\\Nordregio\_settlements\\version1\\Nordregio\_ACPR\_sett\_v1**

**Title**: a\_Nordregion\_ACPR\_sett\_v1  
**Abstract**: This dataset represents population information in the Arctic Circumpolar Permafrost Region at settlement level. It also contains estimates of future of permafrost settlements using projected permafrost extents modeled by Hjort et al. (2018) using Representative Concentration Pathways (RCPs) 2.6, 4.5, and 8.5 for the period 2041–2060.   
**Purpose**: The purpose of this dataset is to provide a detailed geospatial representation of population by country, region, and settlement.   
**Keywords:** Settlements, populations  
**Temporal Extent:** 

* **Date:**   
  * Alaska: July 2017  
  * Canada: 2016  
  * Faroe Islands & Greenland & Iceland & Norway & Svalbard: 1st January 2017  
  * Sweden & Finland: 31st December 2016  
  * Russia: 1st January 2017  
* **Time Period:** NA

**Geographic Extent:** 

* **Bounding Box:**   
  * Top	4,168,410.226000	m  
  * Bottom	\-3,136,893.682600	m  
  * Left	\-4,134,787.023100	m  
  * Right	2,906,267.715800	m

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:**   
**Quality Information:** 

- **Accuracy**:   
- **Completeness:**   
- **Consistency**: 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone**:  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| a\_Nordregion\_ACPR\_sett\_v1.shp | WGS 1984 | Point | 1220 | 20 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID\_Nordre | Integer |  |
|  |  |  |  |  | Cntr | String | Country name |
|  |  |  |  |  | Region | String | Region name |
|  |  |  |  |  | Code | String | Settlement administrative/census code |
|  |  |  |  |  | Sett | String | Settlement name |
|  |  |  |  |  | AT\_COAST | Integer |  |
|  |  |  |  |  | Pop\_2017 | Integer | Population in 2017 |
|  |  |  |  |  | PF\_ext | Integer |  |
|  |  |  |  |  | ON\_PF | Integer | Permafrost settlements |
|  |  |  |  |  | Ic\_26 | Integer | Consensus Index showing zones of hazard potential for 2041–2060 under RCP 2.6 |
|  |  |  |  |  | Ic\_45 | Integer | Consensus Index showing zones of hazard potential for 2041–2060 under RCP 4.5 |
|  |  |  |  |  | Ic\_85 | Integer | Consensus Index showing zones of hazard potential for 2041–2060 under RCP 8.5 |
|  |  |  |  |  | Country | String |  |
|  |  |  |  |  | Lat | Double |  |
|  |  |  |  |  | Lon | Double |  |
|  |  |  |  |  | FID\_arctic | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape\_Leng | Double |  |

27. # **Settlements\\Nordregio\_settlements\\version1\\Nordregio\_ACPR\_sett\_v2**

**Title**: a\_Nordregion\_ACPR\_sett\_v2  
**Abstract**: This dataset represents population information in the Arctic Circumpolar Permafrost Region at settlement level.   
**Purpose**: The purpose of this dataset is to provide a detailed geospatial representation of population by country, region, and settlement.   
**Keywords:** Settlements, populations  
**Temporal Extent:** 

* **Date:**   
  * Alaska: July 2017  
  * Canada: 2016  
  * Faroe Islands & Greenland & Iceland & Norway & Svalbard: 1st January 2017  
  * Sweden & Finland: 31st December 2016  
  * Russia: 1st January 2017  
* **Time Period:** NA

**Geographic Extent:** 

* **Bounding Box:**   
  * Top	81.605737	deg  
  * Bottom	51.411665	deg  
  * Left	\-179.412894	deg  
  * Right	179.354345	deg

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:**   
**Quality Information:** 

- **Accuracy**:   
- **Completeness:**   
- **Consistency**: 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone**:  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| a\_Nordregion\_ACPR\_sett\_v2.shp | WGS 1984 | Point | 1221 | 12 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID\_Nordre | Integer |  |
|  |  |  |  |  | Cntr | String | Country name |
|  |  |  |  |  | Region | String | Region name |
|  |  |  |  |  | Code | String | Settlement administrative/census code |
|  |  |  |  |  | Sett | String | Settlement name |
|  |  |  |  |  | Pop\_2017 | Integer | Population in 2017 |
|  |  |  |  |  | On\_Perma | Integer | Permafrost settlements |
|  |  |  |  |  | FID\_arctic | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape\_Leng | Double |  |

# 

28. # **Mining Locations** 

**Title:** Mining Locations   
**Abstract:** This dataset represents the location and area of mines spread throughout the world as of (2022? From data survey results). It includes information on the size of the mining area in terms of countries the sites are located in instead of sovereign states.  
**Purpose:**The dataset aims to provide precise locational mining data to support Arctic development and environmental initiatives and research .  
**Keywords:** mining, land use, Arctic, countries, GIS  
**Temporal Extent:**  
**Date**: \[Date of data collection\]  
**Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Earth (expressed in WGS 1984 coordinates)

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems**: WGS 1984\]  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: SQLite Database/Geopackage  
* Access Constraints: No metadata is in the original file  
* Use Constraints:

**Metadata Contact:**

* Organization: \[Name of organization responsible for maintaining the dataset\]  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of record | Number of attributes | List of Attributes | Data Type | Notes \- Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| main.mining\_polygons | WGS 1984 | S polygon | 44,929 | 5 | fid | Object ID |  |
|  |  |  |  |  | geom | Geometry |  |
|  |  |  |  |  | ISO3\_CODE | Text | 3 letter country abbreviation |
|  |  |  |  |  | COUNTY\_NAME | Text |  |
|  |  |  |  |  | AREA | Double | Numbers are small, with most being below 5, but the largest being \~2545, but with 6 decimal places. Units aren’t given. |

# 

29. # **Alaskan Airports**

**Title:** Alaskan Airports  
**Abstract:** This dataset represents Airport locations throughout the state of Alaska. It includes information on the location, owner, status, and identifying codes of the airport. .  
**Purpose:**The dataset aims to provide information on Alaskan Airport locations and ownership to assist in transportation decisions in Alaska while dealing with Arctic development.  
**Keywords:** Alaska, Airports, Arctic, FAA\_ID, GIS  
**Temporal Extent:**

* **Date**: March 2025  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.284889 deg; Bottom: 51.877963 deg; Left: \-176.646046 deg; Right: \-130.010426 deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [Alaska Department of Transportation](https://dot.alaska.gov/)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of record | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Airports.shp | WGS 1984 | point | 289 | 12 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | NAME | Text (43) | Full name of airport |
|  |  |  |  |  | OWNER | Text (17) | Who controlls/owns airport |
|  |  |  |  |  | STATUS | Text (20) | Standard or Substandard |
|  |  |  |  |  | REGION | Text (10) | Region of alaska |
|  |  |  |  |  | LAT\_DD | Double (23,15) | latitude |
|  |  |  |  |  | LONG\_DD | Double (23,15) | longitude |
|  |  |  |  |  | FAA\_ID | Text (3) | Identifies airport |

# 

30. # **AHDR Airports**

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
| Airports\_AHDR.shp | WGS 1984 | point | 30 | 42 | FID | Object ID |  |
|  |  |  |  |  | Shape \* | Geometry |  |
|  |  |  |  |  | scalerank | Short |  |
|  |  |  |  |  | featurecla | Text (80) | Says “Airport” for all of them |
|  |  |  |  |  | type | Text (50) | “Mid”, “major”, or “military major”: type of airport |
|  |  |  |  |  | name | Text (200) | Airport name, ex. “Kodiac” or “Iqaluit” |
|  |  |  |  |  | location | Text (50) | “Ramp”, “terminal”, “runway” or “approximate” |
|  |  |  |  |  | iata\_code | Text (254) | Same as “abbrev” attribute, except for the one row in which the abbrev is 4 letters, in which case it is empy |
|  |  |  |  |  | wikipedia | Text (254) | Website link |
|  |  |  |  |  | wikidatid | Text (254) |  |
|  |  |  |  |  | wdid\_score | Short | May relate to waste discharge identification |
|  |  |  |  |  | ne\_id | Long | Natural earth id |

31. # **AHDR Ports**

**Title:** AHDR\_Ports  
**Abstract:** This dataset represents Airport locations throughout the Arctic. It includes information on the name, Natural Earth ID, and in some cases the website of the port.  
**Purpose:**The dataset aims to provide information on Arctic port locations to assist in transportation decisions in the Arctic while dealing with Arctic development.  
**Keywords:** Ports, Arctic, ne\_id, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 78.226111 deg; Bottom: 53.384444 deg; Left: \-165.425147 deg; Right: 177.538634 deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: Considering the high spatial resolution and low tolerance of 0.00000000898315284119521 Degree, this is an accurate dataset.   
* Completeness: Data set lacks an attribute for the nation or area of the Port.   
* Consistency: Not every Port has a website, leading to inconsistent amounts of information for each one. 

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
| AHDR\_Ports.shp | WGS 1984 | point | 52 | 8 | FID | Object ID |  |
|  |  |  |  |  | scalerank | Short |  |
|  |  |  |  |  | featurecla | Text (80) | Each one says “Port” |
|  |  |  |  |  | name | Text (50) | Appears to be name of port |
|  |  |  |  |  | website | Text (254) |  |
|  |  |  |  |  | ne\_id | Long | Natural earth id |

# 

# 

32. # **Railroads**

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
| ne\_10m\_railroads.shp | WGS 1984 | line | 25,413 | 14 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | mult\_track | Short | 2, 1, or 0 |
|  |  |  |  |  | electric | Short | 2, 1, or 0 |
|  |  |  |  |  | category | Short | 0-9 |
|  |  |  |  |  | disp\_scale | Text (5) | 1:10m to 1:80m |
|  |  |  |  |  | featurecla | Text (50) | “railroad” for all of them |
|  |  |  |  |  | scalerank | Short | 4-10 |
|  |  |  |  |  | natlscale | Double (10, 3\) |  |
|  |  |  |  |  | continent | Text (50) | Continent, including oceana |

# 

33. # **Transportation\_Networks/ne\_10m\_roads**

**Title:** ne\_10m\_roads  
**Abstract:** This dataset represents road locations throughout the world at a 10m scale. It includes information on the type of road, country, length, toll information, expressway status, continent, and for many the name of the roads as well.  
**Purpose:**The dataset aims to provide an overview of the global road network to assist with mapping the transit routes for both people and goods.  
**Keywords:** roads, country, expressway GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.177684 deg; Bottom: \-55.112124 deg; Left: \-166.532488 deg; Right: 178.419079 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
“Edited”, “namealt”, “routeraw”, “question”, “ne\_part”, “label”, “label2”, “local”, “localtype” “localalt”, “ignore”, “add”, “rwdb\_rd\_id”, “orig\_fid”, “min\_zoom”, and “min\_label” attributes were deleted.    
**Quality Information:**

* Accuracy:  
* Completeness: Not every road has a name, namealtt, note, level, or prefix  
* Consistency: 

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
| ne\_10m\_roads.shp | WGS 1984 | Line | 56,600 | 33 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | scalerank | Long | From 3 to 10 |
|  |  |  |  |  | featurecla | Text (30) | “Road” or “ferry” |
|  |  |  |  |  | type | Text (50) | “Beltway”, “Bypass”, “Ferry Route”, “Ferry, seasonal”, “Major Highway”, “Road”, “Secondary Highway”, “Track”, or “Unknown” |
|  |  |  |  |  | sov\_a3 | Text (3) | 3- letter country abbreviation |
|  |  |  |  |  | note | Text (50) | Almost all blank, just a select few talk about who operartes the ferry for example |
|  |  |  |  |  | name | Text (25) | Letters or number codes |
|  |  |  |  |  | namealtt | Text (30) | Almost all blank, some say federal, Interstate, State, or A1 |
|  |  |  |  |  | length\_km | Long | Length in km |
|  |  |  |  |  | toll | Short | 1 or 0 |
|  |  |  |  |  | labelrank | Short | 1-8 |
|  |  |  |  |  | prefix | Text (5) | E, I, US, or blank |
|  |  |  |  |  | uident | Long | numbers |
|  |  |  |  |  | continent | Text (50) | continent |
|  |  |  |  |  | expressway | Short | 0 or 1 |
|  |  |  |  |  | level | Text (50) | Blank, “E”, “Federal”, “State”, “Ferry”, “Interstate”, “U/C”, or “Other” |

# 

34. # **Transportation\_Networks/ne\_10m\_roads\_north\_america**

**Title:** ne\_10m\_roads\_north\_america  
**Abstract:** This dataset represents road locations throughout North America at a 10m scale. It includes information on the type of road, country, length, toll information, expressway status, continent, and for many the name of the roads as well.  
**Purpose:**The dataset aims to provide an overview of the global road network to assist with mapping the transit routes for both people and goods.  
**Keywords:** roads, country, expressway GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box:   
  * Top	70.296684	deg  
  * Bottom	51.377332	deg  
  * Left	\-176.764008	deg  
  * Right	\-60.126692	deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy:  
* Completeness: Not every road has a name, namealtt, note, level, or prefix  
* Consistency: 

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

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ne\_10m\_roads\_north\_america.shp | WGS 1984 | Line | 288 | FID | OID |  |
|  |  |  |  | Shape | Geometry |  |
|  |  |  |  | FID\_clean\_ | Integer |  |
|  |  |  |  | class | String |  |
|  |  |  |  | type | String |  |
|  |  |  |  | divided | String |  |
|  |  |  |  | country | String |  |
|  |  |  |  | state | String |  |
|  |  |  |  | note | String |  |
|  |  |  |  | scalerank | SmallInteger |  |
|  |  |  |  | uident | Integer |  |
|  |  |  |  | length | Double |  |
|  |  |  |  | rank | SmallInteger |  |
|  |  |  |  | FID\_arctic | Integer |  |
|  |  |  |  | Id | Integer |  |
|  |  |  |  | Shape\_Leng | Double |  |
|  |  |  |  | Shape\_Area | Double |  |
|  |  |  |  | length\_km | Double |  |

35. # **Arctic Regions**

**Title:** Arctic Regions  
**Abstract:** This dataset represents regions in the Arctic. It includes information on the name of the region, and for some of the regions, the classification of the territory and the country it resides in.   
**Purpose:**The dataset aims to outline the regions of the Arctic visually while providing name information.   
**Keywords:** Arctic, Territory, Russia, Greenland  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 83.658333 deg; Bottom: 83.658333 deg; Left: 51.209721 deg; Right: 180.000000 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
“ID”, “Shape\_Leng”, “Shape\_Area”, “GID\_1”, “NAME\_1”, “NL\_NAME\_1”, “GID\_2”, “NAME\_2”, “NL\_NAME\_2”, “GID\_3”, “NAME\_3”, “VARNAME\_3”, “NL\_NAME\_3”, TYPE\_3, “ENGTYPE\_3”, “CC\_3”, “HASC\_3”, “VARNAME\_1”, “TYPE\_1”, “CC\_1”, “HASC\_1”, and “path” attributes were deleted.   
**Quality Information:**

* Accuracy:  
* Completeness: For the GID\_0, NAME\_0, and ENGTYPE\_1 attributes, only a few rows have data.   
* Consistency: 

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: Tingstad, A., Van Abel, K., Bennett, M.M. *et al.* Divergent trajectories of Arctic change: Implications for future socio-economic patterns. *Ambio* 54, 239–255 (2025). https://doi.org/10.1007/s13280-024-02080-x  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of record | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ArcticRegions.shp | WGS 1984 | Polygon  | 19 | 28 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | GID\_0 | Text (80) | 3-letter code abbreviation of NAME\_0 attribute, or blank |
|  |  |  |  |  | NAME\_0 | Text (80) | Name of region, or blank |
|  |  |  |  |  | ENGTYPE\_1 | Text (80) | “Territory”, “Region”, or blank |
|  |  |  |  |  | layer | Text (254) | Says nation/region place is in |

# 

36. # **NO2 Canada**

**Title:** no2\_canada  
**Abstract:** This raster shows NO2 concentrations over a large portion of Canada and the waters directly surrounding it.   
**Purpose:** This dataset provides reference for areas with abundant NO2 to assist with developmental and environmental decision making.   
**Keywords:** NO2, Arctic, Canada  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 70.095542, Bottom: 59.944579, Left: 59.944579, Right: \-60.456619


**Spatial Resolution**:   
**Coordinate Reference Systems:** GCS\_WGS\_1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**

* Accuracy:  
* Completeness:  
* Consistency: 

**Distribution Information:**

* Format: Raster (TIFF)  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [Copernicus](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_NO2#description)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

# 

37. # **NO2 Canada clipped**

**Title:** NO2 Canada clipped  
**Abstract:** This raster shows NO2 concentrations over much of the land portion of Canada.   
**Purpose:** This dataset provides reference for areas with abundant NO2 to assist with developmental and environmental decision making.   
**Keywords:** NO2, Arctic, Canada  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top 70.095542, Bottom 59.944579, Left \-102.030650, Right \-60.456619

**Spatial Resolution**:   
**Coordinate Reference Systems:** GCS\_WGS\_1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**

* Accuracy:  
* Completeness:  
* Consistency: 

**Distribution Information:**

* Format: Raster (TIFF)  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [Copernicus](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_NO2#description)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

# 

# 

38. # **NO2 Iceland** 

    Title?

**Title:** no2\_icelan  
**Abstract:** This raster shows NO2 concentrations over Iceland and the waters directly surrounding it.   
**Purpose:** This dataset provides reference for areas with abundant NO2 to assist with developmental and environmental decision making.   
**Keywords:** NO2, Arctic, Iceland  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top 67.759922, Bottom 60.528484, Left \-25.745716, Right \-5.524639

**Spatial Resolution**:   
**Coordinate Reference Systems:** GCS\_WGS\_1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**

* Accuracy:  
* Completeness:  
* Consistency: 

**Distribution Information:**

* Format: Raster (TIFF)  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [Copernicus](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_NO2#description)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

# 

39. # **NO2 Iceland Clipped**

**Title:** NO2 Iceland Clipped  
**Abstract:** This raster shows NO2 concentrations over Iceland and the waters directly surrounding it.   
**Purpose:** This dataset provides reference for areas with abundant NO2 to assist with developmental and environmental decision making.   
**Keywords:** NO2, Arctic, Iceland  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 67.759922, Bottom: 60.528484, Left: \-25.745716, Right: \-5.524639


**Spatial Resolution**:   
**Coordinate Reference Systems:** GCS\_WGS\_1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**

* Accuracy:  
* Completeness:  
* Consistency: 

**Distribution Information:**

* Format: Raster (TIFF)  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [Copernicus](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_NO2#description)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

# 

# 

40. # **Administrative Country Boundaries**

**Title:** ne\_10m\_countries  
**Abstract:** This dataset represents country boundaries. It includes information on the population, sovereignty, GDP, development stage, and region of the world of each country.  
**Purpose:**The dataset aims to provide an overview of the demographics of each country and each country's recognized borders, as opposed to those of nations or states.  
**Keywords:** countries, GDP, population, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 83.634101 deg; Bottom: \-90.000000 deg; Left: \-180.000000 deg; Right: 180.000000 deg

**Spatial Resolution**: XY resolution: 0.000000000899322046075566 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
The attributes of Featurecla, scalerank, LABELRANK, ADMO\_DIF, LEVEL, TLC, ADMIN, ADM0\_A3, GEOU\_DIF, GEOUNIT, GU\_A3, SU\_DIF, SUBUNIT, SU\_A3, BRK\_DIFF, NAME, NAME\_LONG, BRK\_A3, BRK\_NAME, BRK\_GROUP, ABBREV, POSTAl, FORMAL\_EN, FORMAL\_FR, NAME\_CIAWF, NOTE\_ADM0, NOTE\_BRK, NAME\_SORT, NAME\_ALT, MAPCOLOR7, MAPCOLOR8, MAPCOLOR9, MAPCOLOR13, GDP\_MD, WOE\_ID\_EH, as well as country names and abbreviations in a vast array of languages, have been deleted from the original dataset to create this cleaned dataset.   
**Quality Information:**

* Accuracy:  
* Completeness: Each row has each attribute, creating a very complete dataset.   
* Consistency: 

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
| ne\_10m\_admin\_0\_countries.shp | WGS 1984 | polygon | 258 | 169 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | SOVEREIGNT | Text (15) | Country it is |
|  |  |  |  |  | SOV\_A3 | Text (3) | 3- letter country abbreviation |
|  |  |  |  |  | TYPE | Text (17) | Status of sovereignty  |
|  |  |  |  |  | POP\_EST | Double (11, 1\) | Estimation of population |
|  |  |  |  |  | POP\_RANK | Short | Number in the 0’s and 10’s |
|  |  |  |  |  | POP\_YEAR | Short | Year population was recorded: 2020 or 201964 |
|  |  |  |  |  | GDP\_YEAR | Short | Year GDP\_MD was recorded |
|  |  |  |  |  | ECONOMY | Text (16) | Ranked from 1-7 with how developed the economy is  |
|  |  |  |  |  | INCOME\_GRP | Text (23) | Ranked from 1-5 with high-low income  |
|  |  |  |  |  | WOE\_ID | Long | 32-bit ID that corresponds to a feature on earth |
|  |  |  |  |  | WOE\_NOTE | Text (167) | Whether the WOE\_ID is an exact match or not |
|  |  |  |  |  | REGION\_UN | Text (10) |  |
|  |  |  |  |  | SUBREGION | Text (25) |  |
|  |  |  |  |  | WIKIDATAID | Text (8) |  |
|  |  |  |  |  | FCLASS\_TLC | Text (21) | Dependency, country etc |

# 

41. # **CS Night Areas**

**Title:** CS Night Areas  
**Abstract:** This dataset represents 6 night areas across the world, including area (in unspecified units) of each night area.   
**Purpose:** The purpose of this dataset is unknown.   
**Keywords:** Night Areas, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:**   
Bounding Box: Top: 2,339,656.188965 m; Bottom: \-1,219,500.000000 m; Left: 742,933.715820 m; Right: 2,921,373.779297 m  
**Spatial Resolution**: XY resolution: 0.0001 Meters  
**Coordinate Reference Systems:** WGS\_1984\_Stereographic\_North\_Pole  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
No attributes were deleted.   
**Quality Information:**

* Accuracy: Without units, it is difficult to understand the content of the Area attribute.   
* Completeness: Each row has data for each attribute.   
* Consistency: 

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| CS\_Night\_Areas.shp | Projected: WGS\_1984\_Arctic\_Polar\_Stereographic GCS: WGS 1984 | polygon | 591 | 5 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Id | Long |  |
|  |  |  |  |  | gridcode | Long |  |
|  |  |  |  |  | Area | Float | Units unspecified |

# 

42. # **CS 500 sub (Nightlights)**

**Title:** cs\_500\_sub  
**Abstract:** This raster provides a cloud-screened (CS) subset of monthly average radiance composite images derived from the Visible Infrared Imaging Radiometer Suite (VIIRS) Day/Night Band (DNB). The data has been corrected for stray light and filtered to remove cloud cover artifacts.   
**Purpose:** This dataset provides reference for quantitative analysis of nighttime light emissions without the noise and artifacts present in the raw VIIRS data, serving as a reliable indicator of human activity and environmental conditions in the Northern Hemisphere.  
**Keywords:**   
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: 2000-2016

**Geographic Extent:** 

* Bounding Box: Top: 3142000.000000, Bottom: \-3140500.000000, Left: \-755500.000000, Right: \-3142000.000000 (no units given)


**Spatial Resolution**: 500 meters  
**Coordinate Reference Systems:** GCS\_WGS\_1984 (Geographic coordinate system), WGS\_1984\_Arctic\_Polar\_Stereographic (Projected Coordinate system)  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**

* Accuracy:  
* Completeness:  
* Consistency: 

**Distribution Information:**

* Format: Raster (TIFF)  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

# 

43. # **CS\_NightMAX (Nightlights)**

**Title:** CS\_NightMAX  
**Abstract:** This raster shows just a solid box of all the same values over part of the Arctic. It is difficult to deduce what information may be gathered from this dataset.    
**Purpose:** This dataset provides reference for….   
**Keywords:**   
**Temporal Extent:**  
**Date**: \[Date of data collection\]  
**Time Period**: \[Start date \- End date\]

**Geographic Extent:**   
Bounding Box: Top: 3091500.000000, Bottom: \-1595500.000000, Left: \-1595500.000000, Right: \-364500.000000 (no units)

**Spatial Resolution**:   
**Coordinate Reference Systems:** GCS\_WGS\_1984 (Geographic coordinate system), WGS\_1984\_Arctic\_Polar\_Stereographic (Projected Coordinate system)   
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**  
Accuracy:  
Completeness:  
Consistency:   
**Distribution Information:**  
Format: Raster (TIFF)  
Access Constraints: \[Describe any restrictions on access\]  
Use Constraints: \[Describe any restrictions on usage\]  
**Metadata Contact:**  
Organization: \[Name of organization responsible for maintaining the dataset\] Veland team  
Position: \[Position of the contact person\]  
Email: \[Contact email address\]  
Phone: \[Contact phone number\]

# 

44. # **CS 500 sub RGB (Nightlights)**

**Title:** CS 500 sub RGB  
**Abstract:** This raster shows….   
**Purpose:** This dataset provides reference for….   
**Keywords:**   
**Temporal Extent:**  
**Date**: \[Date of data collection\]  
**Time Period**: \[Start date \- End date\]

**Geographic Extent:**   
Bounding Box: Top: 3142000.000000, Bottom: \-3140500.000000, Left: \-755500.000000, Right: 3142000.000000 (no units given)

**Spatial Resolution**:   
**Coordinate Reference Systems:** GCS\_WGS\_1984 (Geographic coordinate system), WGS\_1984\_Arctic\_Polar\_Stereographic (Projected Coordinate system)  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**  
Accuracy:  
Completeness:  
Consistency:   
**Distribution Information:**  
Format: Raster (TIFF)  
Access Constraints: \[Describe any restrictions on access\]  
Use Constraints: \[Describe any restrictions on usage\]  
**Metadata Contact:**  
Organization: \[Name of organization responsible for maintaining the dataset\] Veland team  
Position: \[Position of the contact person\]  
Email: \[Contact email address\]  
Phone: \[Contact phone number\]

# 

45. # **CS\_Nights500 (Nightlights)**

**Title:** CS\_Nights500  
**Abstract:** This raster shows just a solid black box of all the same values over part of the Arctic, by Russia. It is difficult to deduce what information may be gathered from this dataset.    
**Purpose:** This dataset provides reference for….   
**Keywords:**   
**Temporal Extent:**  
**Date**: \[Date of data collection\]  
**Time Period**: \[Start date \- End date\]

**Geographic Extent:**   
Bounding Box: Top: 3091500.000000, Bottom: \-1595500.000000, Left: 364500.000000, Right: 3172000.000000 (no units)

**Spatial Resolution**:   
**Coordinate Reference Systems:** GCS\_WGS\_1984 (Geographic coordinate system), WGS\_1984\_Arctic\_Polar\_Stereographic (Projected Coordinate system)   
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**  
Accuracy:  
Completeness:  
Consistency:   
**Distribution Information:**  
Format: Raster (TIFF)  
Access Constraints: \[Describe any restrictions on access\]  
Use Constraints: \[Describe any restrictions on usage\]  
**Metadata Contact:**  
Organization: \[Name of organization responsible for maintaining the dataset\] Veland team  
Position: \[Position of the contact person\]  
Email: \[Contact email address\]  
Phone: \[Contact phone number\]

# 

46. # **CS\_Nights (Nightlights)**

**Title:** CS\_Nights  
**Abstract:** This raster shows just a solid black box of all the same values over part of the Arctic, by Russia. It is difficult to deduce what information may be gathered from this dataset.    
**Purpose:** This dataset provides reference for….   
**Keywords:**   
**Temporal Extent:**  
**Date**: \[Date of data collection\]  
**Time Period**: \[Start date \- End date\]

**Geographic Extent:**   
Bounding Box: Top: 3092000.000000, Bottom: \--1596000.000000, Left: 364000.000000, Right: 3172000.000000 (no units)

**Spatial Resolution**:   
**Coordinate Reference Systems:** GCS\_WGS\_1984 (Geographic coordinate system), WGS\_1984\_Arctic\_Polar\_Stereographic (Projected Coordinate system)   
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**  
Accuracy:  
Completeness:  
Consistency:   
**Distribution Information:**  
Format: Raster (TIFF)  
Access Constraints: \[Describe any restrictions on access\]  
Use Constraints: \[Describe any restrictions on usage\]  
**Metadata Contact:**  
Organization: \[Name of organization responsible for maintaining the dataset\] Veland team  
Position: \[Position of the contact person\]  
Email: \[Contact email address\]  
Phone: \[Contact phone number\]

47. # **OSM Alaska Buildings** 

**Title:** gis\_osm\_buildings\_a\_free\_1  
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
| gis\_osm\_buildings\_a\_free\_1.shp | WGS 1984 | Shapefile, polygon | 143,330 | 7 | FID | double | number |
|  |  |  |  |  | Shape | Polygon |   |
|  |  |  |  |  | osm\_id | Text (12) | Long number |
|  |  |  |  |  | name | Text (100) | Name of building, or blank for most |
|  |  |  |  |  | type | Text (20) | Type of building, but most are blank |

48. # **OSM Alaska Land Use** 

**Title:** gis\_osm\_landuse\_a\_free\_1  
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
| gis\_osm\_landuse\_a\_free\_1 | WGS 1984 | Shapefile, Polygon | 18,272 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 7201-7229: Maybe a land use code? |
|  |  |  |  |  | fclass | Text (28) | Forest, park, retail etc describing land designation. Seems to be tied to code |
|  |  |  |  |  | name | Text (100) | Name of land piece, if applicable |

49. # **OSM Alaska Natural A Features** 

**Title:** gis\_osm\_natural\_a\_free\_1  
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
| gis\_osm\_natural\_a\_free\_1 | D WGS 1984 | Shapefile, Polygon | 4,149 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 4103, 4112, or 4141 |
|  |  |  |  |  | fclass | Text (28) | Beach, cliff, or glacier–correlates to code attribute |
|  |  |  |  |  | name | Text (100) | Name of natural attribute, if applicable |

50. # **OSM Alaska Natural Features** 

**Title:** gis\_osm\_natural\_free\_1  
**Abstract:** This dataset represents natural features in the state of Alaska. All of the entries contain info about the name of the feature, code, and feature type.   
**Purpose:**The dataset aims to provide the locations and identities of natural features throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Nature, Beach, Glacier, Volcano, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 70.170434 deg; Bottom: 51.223554 deg; Left: \-179.109405 deg; Right: \-129.518398 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row has each attribute filled, creating a complete dataset.   
* Consistency: 

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: OpenStreetMap (OSM)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gis\_osm\_natural\_free\_1 | WGS 1984 | Shapefile, Point | 4,876 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm\_id | Text (12) |  |
|  |  |  |  |  | code | Short | One of 8 unique 4-digit codes defining type of land feature |
|  |  |  |  |  | fclass | Text (28) | Beach, cave\_entrance, volcano, cliff, glacier, peak, spring, or tree. Correlates to code attribute |
|  |  |  |  |  | name | Text (100) | Name of feature. Each feature has a name here.  |

51. # **OSM Alaska A Places** 

**Title:** gis\_osm\_places\_a\_free\_1  
**Abstract:** This dataset represents places, such as towns or islands, in the state of Alaska. All of the entries contain info about the name of the feature, code, and feature type. Many also include population data.  
**Purpose:**The dataset aims to provide the locations and identities of places throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Island, Population, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 74.102874 deg; Bottom: 51.214590 deg; Left: \-179.148286 deg; Right: \-124.393980 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row has each attribute filled, creating a complete dataset.   
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
| gis\_osm\_places\_a\_free\_1 | WGS 1984 | Shapefile, Polygon | 1,268 | 7 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of 6 unique 4-digit codes beginning with 1: 1001, 1002, 1003, 1004, 1020, 1050 |
|  |  |  |  |  | fclass | Text (28) | City, hamlet, Island, village, locality, or town. Corresponds to code. |
|  |  |  |  |  | population | Long | Many say 0, max says 569 |
|  |  |  |  |  | name | Text (100) | Name of place. Each row has a name.  |

52. # **OSM Alaska Places** 

**Title:** gis\_osm\_places\_free\_1  
**Abstract:** This dataset represents places, such as cities, towns, or islands, in the state of Alaska. All of the entries contain info about the code and feature type, and nearly all places have a name. Many also include population data.  
**Purpose:**The dataset aims to provide the locations and identities of populous places throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Island, Population, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.360450 deg; Bottom: 51.815832 deg; Left: \-177.947960 deg; Right: \-129.897266 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which 5 rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis\_osm\_places\_free\_1 | WGS 1984 | Shapefile, Point | 1,060 | 7 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of 8 unique 4-digit codes beginning with 1: 1001, 1002, 1003, 1004, 1010, 1020, 1041, 1050 |
|  |  |  |  |  | fclass | Text (28) | City, county, hamlet, Island, village, locality, suburb or town. Corresponds to code. |
|  |  |  |  |  | population | Long | 291,247 as max and 0 for many as min |
|  |  |  |  |  | name | Text (100) | Every place except for 5 have a name.  |

53. # **OSM Alaska A Places of Worship**

**Title:** gis\_osm\_pofw\_a\_free\_1  
**Abstract:** This dataset represents places of worship in the state of Alaska. All of the entries contain info about the code and religion type, and all places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of places of worship throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Worship, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.292610 deg; Bottom: 51.866513 deg; Left: \-176.667003 deg; Right: \-130.019277 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row has each attribute filled, creating a complete dataset.   
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
| gis\_osm\_pofw\_a\_free\_1 | WGS 1984 | Shapefile, Polygon | 383lu | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of 11 unique 4-digit codes, each beginning with 3 |
|  |  |  |  |  | fclass | Text (28) | Religion type of place of worship (Muslim, christian, etc) corresponding to code attribute |
|  |  |  |  |  | name | Text (100) | Name of place of worship. |

54. # **OSM Alaska Places of Worship**

**Title:** gis\_osm\_pofw\_free\_1  
**Abstract:** This dataset represents places of worship in the state of Alaska. All of the entries contain info about the code and religion type, and almost all places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of places of worship throughout Alaska to aid with development and spatial reference.   
**Keywords:** Alaska, OSM, Worship, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 66.898244 deg; Bottom: 51.866767 deg; Left: \-176.666724 deg; Right: \-131.681143 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which 7 rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis\_osm\_pofw\_free\_1 | WGS 1984 | Shapefile, Point | 48 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of 6 unique 4-digit codes, each beginning with 3 |
|  |  |  |  |  | fclass | Text (28) | Religion type of place of worship (christian\_catholic, christian\_lutheran, etc) corresponding to code attribute |
|  |  |  |  |  | name | Text (100) | Name of place of worship. 7 do not have names. |

55. # **OSM Alaska A Places of Interest**

**Title:** gis\_osm\_pois\_a\_free\_1  
**Abstract:** This dataset represents places of public interest in the state of Alaska. All of the entries contain info about the code and feature type, and almost all places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of places of interest throughout Alaska to aid with development, public interest, and spatial reference.   
**Keywords:** Alaska, OSM, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.332432 deg; Bottom: 51.715068 deg; Left: \-177.200597 deg; Right: \-129.896222 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which many rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis\_osm\_pois\_a\_free\_1 | WGS 1984 | Shapefile, Polygon | 6174 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many unique 4-digit identifying codes beginning with 2\. |
|  |  |  |  |  | fclass | Text (28) | Describes the business or public place type (bakery, artwork, university, water\_well, zoo, etc) |
|  |  |  |  |  | name | Text (100) | Name of location. Most places have a name but many are empty |

56. # **OSM Alaska Places of Interest**

**Title:** gis\_osm\_pois\_free\_1  
**Abstract:** This dataset represents places of public interest in the state of Alaska. All of the entries contain info about the code and feature type, and almost all places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of places of interest throughout Alaska to aid with development, public interest, and spatial reference.   
**Keywords:** Alaska, OSM, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.383041 deg; Bottom: 51.847984 deg; Left: \-176.663694 deg; Right: \-129.901862 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which many rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis\_osm\_pois\_free\_1 | WGS 1984 | Shapefile, Point | 4575 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many unique 4-digit identifying codes beginning with 2\. |
|  |  |  |  |  | fclass | Text (28) | Describes the business or public place type (bakery, chemist, artwork, university, water\_well, zoo, etc) |
|  |  |  |  |  | name | Text (100) | Name of location. Most places have a name but many are empty |

57. # **OSM Alaska Railways**

**Title:** gis\_osm\_railways\_free\_1  
**Abstract:** This dataset represents railways in the state of Alaska. All of the entries contain info about the code, existence of bridges and tunnels, and feature type, and many of the railways have a name.   
**Purpose:**The dataset aims to provide the locations and identities of railroads throughout Alaska to aid with development, transportation, and spatial reference.   
**Keywords:** Alaska, OSM, Railways, Trains, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 64.941199 deg; Bottom: 53.883157 deg; Left: \-166.531653 deg; Right: \-131.641250 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which many rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis\_osm\_railways\_free\_1 | WGS 1984 | Shapefile, Polyline | 1144 | 9 | FID | double |  |
|  |  |  |  |  | Shape | Polyline |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 6101, 6106, 6107, or 6108 |
|  |  |  |  |  | fclass | Text (28) | Funicular, minuature\_railway, narrow\_gauge, or rail. Corresponds to code attribute. |
|  |  |  |  |  | name | Text (100) | Name of the railway. Many are blank.  |
|  |  |  |  |  | layer | Double (12, 0\) | \-1, 0, or 1\. Not sure what this corresponds to. |
|  |  |  |  |  | bridge | Text (1) | T or F corresponding to true or false.  |
|  |  |  |  |  | tunnel | Text (1) | T or F corresponding to true or false.  |

58. # **OSM Alaska Roads**

**Title:** gis\_osm\_roads\_free\_1  
**Abstract:** This dataset represents roads in the state of Alaska. All of the entries contain info about the code, existence of bridges and tunnels, and feature type, and most of the roads have a name.   
**Purpose:**The dataset aims to provide the locations and identities of roads throughout Alaska to aid with development, transportation, and spatial reference.   
**Keywords:** Alaska, OSM, Roads, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.386462 deg; Bottom: 51.591498 deg; Left: \-177.200845 deg; Right: \-129.872230 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
The attribute “ref” was deleted because it contained many long codes, or were blank, that are difficult to understand its meaning as they don’t have much in common.

**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which many rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis\_osm\_roads\_free\_1 | WGS 1984 | Shapefile, Polyline | 97,177 | 11 | FID | double |  |
|  |  |  |  |  | Shape | Polyline |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many unique identifying codes, each beginning with 5\. |
|  |  |  |  |  | fclass | Text (28) | Cycleway, path, track\_grade3, busway, etc. Corresponds to code attribute. |
|  |  |  |  |  | name | Text (100) | Name of the road. Many are blank.  |
|  |  |  |  |  | oneway | Text (1) | B, F, or T. Unsure what B corresponds to..maybe both? |
|  |  |  |  |  | maxspeed | Short | Seems to be maxspeed of road, but does not follow even numbers (ex. 88, 96, 104, 64, 72).  |
|  |  |  |  |  | layer | Double (12, 0\) | \-2. \-1, 0, 1, 2, or 5\. Not sure what this corresponds to. |
|  |  |  |  |  | bridge | Text (1) | T or F corresponding to true or false.  |
|  |  |  |  |  | tunnel | Text (1) | T or F corresponding to true or false.  |

59. # **OSM Alaska A Traffic**

**Title:** gis\_osm\_traffic\_a\_free\_1  
**Abstract:** This dataset represents places relating to traffic flow in the state of Alaska. All of the entries contain info about the code and feature type, and almost all places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of places determining traffic flow in Alaska to aid with development, transportation, and spatial reference.   
**Keywords:** Alaska, OSM, Traffic, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.355702 deg; Bottom: 51.715750 deg; Left: \-177.199817 deg; Right: \-129.987828 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which many rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis\_osm\_traffic\_a\_free\_1 | WGS 1984 | Shapefile, Polygon | 6,169 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many 4-digit classifying codes beginning with 5 |
|  |  |  |  |  | fclass | Text (28) | Pier, dam, parking, fuel, marina, etc. Corresponds to code attribute.  |
|  |  |  |  |  | name | Text (100) | Name of the transport-affecting location. Many are blank.  |

60. # **OSM Alaska Traffic**

**Title:** gis\_osm\_traffic\_free\_1  
**Abstract:** This dataset represents places relating to traffic flow in the state of Alaska. All of the entries contain info about the code and feature type, and almost all places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of places determining traffic flow in Alaska to aid with development, transportation, and spatial reference.   
**Keywords:** Alaska, OSM, Traffic, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Min Y: \-400.00 Degree; Max Y: 400.00 Degree; Min X: \-400.00 Degree, Max X: 400.00 Degree

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which many rows are blank, has each attribute filled, creating an almost complete dataset.   
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
| gis\_osm\_traffic\_free\_1 | WGS 1984 | Shapefile, Point | 19,288 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many 4-digit classifying codes beginning with 5 |
|  |  |  |  |  | fclass | Text (28) | Pier, dam, parking, fuel, stop, speed\_cam, marina, etc. Corresponds to code attribute.  |
|  |  |  |  |  | name | Text (100) | Name of the transport-affecting location. Many are blank.  |

61. # **OSM Alaska Transport A**

**Title:** gis\_osm\_transport\_a\_free\_1  
**Abstract:** This dataset represents transportation hubs in the state of Alaska. All of the entries contain info about the code and feature type, and many of the places have a name.   
**Purpose:**The dataset aims to provide the locations and identities of transportation hubs in Alaska to aid with development, transportation, and spatial reference.   
**Keywords:** Alaska, OSM, Transport, Airport, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.288222 deg; Bottom: 51.602441 deg; Left: \-178.664039 deg; Right: \-129.975879 deg

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
| gis\_osm\_transport\_a\_free\_1 | WGS 1984 | Shapefile, Polygon | 692 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many 4-digit classifying codes beginning with 56 |
|  |  |  |  |  | fclass | Text (28) | Airfield, Airport, apron, bus\_station, ferry\_terminal, helipad, or taxi. Corresponds to code attribute.  |
|  |  |  |  |  | name | Text (100) | Name of the transport location. Many are blank.  |

62. # **OSM Alaska Transport**

**Title:** gis\_osm\_transport\_free\_1  
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
| gis\_osm\_transport\_free\_1 | WGS 1984 | Shapefile, Point | 1277 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Point |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | One of many 4-digit classifying codes beginning with 56 |
|  |  |  |  |  | fclass | Text (28) | Airfield, Airport,  bus\_station, bus\_stop, ferry\_terminal, helipad, railway\_halt, railway\_station, or taxi. Corresponds to code attribute.  |
|  |  |  |  |  | name | Text (100) | Name of the transport location. Many are blank.  |

63. # **OSM Alaska Water A**

**Title:** gis\_osm\_water\_a\_free\_1  
**Abstract:** This dataset represents water bodies in the state of Alaska. All of the entries contain info about the code and feature type, and many of the places have a name.   
**Purpose:** The dataset aims to provide the locations and identities of water bodies/sources in Alaska to aid with development, conservation, and spatial reference.   
**Keywords:** Alaska, OSM, Water, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.387297 deg; Bottom: 51.232347 deg; Left: \-179.126616 deg; Right: \-129.518398 deg

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
| gis\_osm\_water\_a\_free\_1 | WGS 1984 | Shapefile, Polygon | 239,264 | 6 | FID | double |  |
|  |  |  |  |  | Shape | Polygon |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 8200, 8201, 8202, 8203, 8211, or 8221\. |
|  |  |  |  |  | fclass | Text (28) | Dock, Glacier, reservoir, wetland, water, or riverbank. Corresponds to code attribute.  |
|  |  |  |  |  | name | Text (100) | Name of the water body. Many are blank.  |

64. # **OSM Alaska Waterways**

**Title:** gis\_osm\_waterways\_free\_1  
**Abstract:** This dataset represents waterways in the state of Alaska. All of the entries contain info about the code and feature type, and many of the waterways have a name.   
**Purpose:** The dataset aims to provide the locations and identities of waterways in Alaska to aid with development, conservation, water drainage, and spatial reference.   
**Keywords:** Alaska, OSM, Water, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.322976 deg; Bottom: 51.610800 deg; Left: \-178.872271 deg; Right: \-129.796996 deg

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
| gis\_osm\_waterways\_free\_1 | WGS 1984 | Shapefile, Polyline | 429,548 | 7 | FID | double |  |
|  |  |  |  |  | Shape | Polyline |  |
|  |  |  |  |  | osm\_id | Text (12) | Long identifying number code |
|  |  |  |  |  | code | Short | 8101, 8102, 8103, or 8104\. |
|  |  |  |  |  | fclass | Text (28) | canal, drain, river, or stream. Corresponds to code attribute.  |
|  |  |  |  |  | width | Long | Width of waterway. Many are 0, and no units are given. Values range from whole numbers 1-10, and 12, 15, 20, 22, 30, and 60\. |
|  |  |  |  |  | name | Text (100) | Name of the waterway. Many are blank.  |

65. # **OSM\\OSM\_Extracted\\Arctic\_Education\_OSM**

**Title:** a\_Arctic\_Education\_OSM  
**Abstract:** This dataset represents the locations of buildings relating to education in the Arctic.   
**Purpose:** The dataset aims to provide the locations and identities of educational buildings in the Arctic to aid with spatial reference.   
**Keywords:** Arctic, Education, OSM  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box:   
  * Top	79.433962	deg  
  * Bottom	51.484202	deg  
  * Left	\-179.126228	deg  
  * Right	179.251994	deg

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
| a\_Arctic\_Education\_OSM.shp | WGS 1984 | Point | 4642 | 13 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID\_Arctic | Integer |  |
|  |  |  |  |  | osm\_id | String |  |
|  |  |  |  |  | code | SmallInteger |  |
|  |  |  |  |  | fclass | String | Type of building (e.g. College, school, university) |
|  |  |  |  |  | name | String | Name of the building |
|  |  |  |  |  | type | String | Type of building (e.g. College, school, university |
|  |  |  |  |  | ORIG\_FID | Integer |  |
|  |  |  |  |  | FID\_arct\_1 | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape\_Leng | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |

# 

66. # **OSM\\OSM\_Extracted\\Arctic\_Healthcare\_OSM**

**Title:** a\_Arctic\_Healthcare\_OSM  
**Abstract:** This dataset represents the locations of buildings relating to healthcare in the Arctic.   
**Purpose:** The dataset aims to provide the locations and identities of healthcare buildings in the Arctic to aid with spatial reference.   
**Keywords:** Arctic, Healthcare, OSM  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box:   
  * Top	78.654815	deg  
  * Bottom	51.485214	deg  
  * Left	\-179.122174	deg  
  * Right	177.693895	deg

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
| a\_Arctic\_Healthcare\_OSM.shp | WGS 1984 | Point | 1763 | 13 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID\_Arctic | Integer |  |
|  |  |  |  |  | osm\_id | String |  |
|  |  |  |  |  | code | SmallInteger |  |
|  |  |  |  |  | fclass | String | Type of building (e.g. clinic, dentist, doctors, hospital) |
|  |  |  |  |  | name | String | Name of the building |
|  |  |  |  |  | type | String | Type of building (e.g. clinic, dentist, doctors, hospital) |
|  |  |  |  |  | ORIG\_FID | Integer |  |
|  |  |  |  |  | FID\_arct\_1 | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape\_Leng | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |

67. # **OSM\\OSM\_Extracted\\Arctic\_Hospitality\_OSM**

**Title:** a\_Arctic\_Hospitality\_OSM  
**Abstract:** This dataset represents the locations of buildings relating to hospitality in the Arctic.   
**Purpose:** The dataset aims to provide the locations and identities of hospitality buildings in the Arctic to aid with spatial reference.   
**Keywords:** Arctic, Hospitality, OSM  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box:  
  * Top	78.655175	deg  
  * Bottom	51.482985	deg  
  * Left	\-174.203331	deg  
  * Right	177.740687	deg

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
| a\_Arctic\_Hospitality\_OSM.shp | WGS 1984 | Point | 2867 | 13 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID\_Arctic | Integer |  |
|  |  |  |  |  | osm\_id | String |  |
|  |  |  |  |  | code | SmallInteger |  |
|  |  |  |  |  | fclass | String | Type of building (e.g. guesthouse, hostel, hotel, motel) |
|  |  |  |  |  | name | String | Name of the building |
|  |  |  |  |  | type | String | Type of building (e.g. guesthouse, hostel, hotel, motel) |
|  |  |  |  |  | ORIG\_FID | Integer |  |
|  |  |  |  |  | FID\_arct\_1 | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape\_Leng | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |

68. # **GEM-GOIT-Oil-NGL-Pipelines-2024-05**

**Title:** oil\_pipelines  
**Abstract:** This dataset represents tracks Oil Infrastructure globally.  
**Purpose:**  
**Keywords:** oil infrastructure  
**Temporal Extent:**

* **Date**: 5/2024  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box: \[Coordinates defining the geographic extent of the dataset\]

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: Recommended Citation: “Global Oil Infrastructure Tracker, Global Energy Monitor, May 2024 release”.

**Metadata Contact:**

* Organization: [Global Energy Monitor](https://globalenergymonitor.org/projects/global-oil-infrastructure-tracker/)  
* Position: Global Oil Infrastructure Tracker: Baird Langenbrunner   
* Email: baird.langenbrunner@globalenergymonitor.org  
* Phone: 415-206-0906

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| oil\_pipelines.shp | WGS 1984 | Shapefile | 1,639 | 48 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | ProjectID | Text | A unique ID for each project (all the phases, segments, expansions, etc. belonging to the same overall pipeline do not necesssarily share a ProjectID, but they should share the same PipelineName) |
|  |  |  |  |  | Fuel | Text | Oil, Gas, or NGL |
|  |  |  |  |  | StartCntry | Text | Country the pipeline starts in |
|  |  |  |  |  | EndCntry | Text | Country the pipeline ends in |
|  |  |  |  |  | Countries | Text | Countries that the pipeline passes through, in order from beginning to end (where possible); note Hong Kong and Macao are recognized as sovereign states here |
|  |  |  |  |  | Wiki | Text | Link to project's GEM.wiki page |
|  |  |  |  |  | PipeName | Text | Name of the pipeline (or pipeline system, when it has multiple pieces, phases, segments, or expansions) |
|  |  |  |  |  | SegName | Text | Name of the pipeline segment (which can be a segment of a bigger pipeline system/network, or an expansion project) |
|  |  |  |  |  | OthEngName | Text | Alternate pipeline names in English, if applicable; if there are multiple, separate by a semicolon (;) |
|  |  |  |  |  | Status | Text | Operating, Proposed, Retired, Construction, Shelved, Cancelled, Idle, or Mothballed If there have been no development updates in the two years following the project's proposal, then the status is assumed to be "Shelved". If there have been no development updates in the 4 years following the project's proposal or longer, the status is assumed to be "Cancelled". If Shelved, Cancelled, or Retired, these are associated with ShelvedYear, CancelledYear, and StopYear |
|  |  |  |  |  | Owner | Text | Auto-filled: direct owner name(s), percent ownership if available; here "owner" means lowest level of ownership that we're able to find in our research. |
|  |  |  |  |  | Parent | Text | Parent company name(s), percent ownership if available; here "parent" means highest level of ownership that we're able to trace (e.g., parent companies or ultimate shareholders). |
|  |  |  |  |  | ParHQCntry | Text | First year operations initiated, or expected to initiate |
|  |  |  |  |  | StartYr1 | Text | Year operations initiated for first expansion project, or expected to initiate, if expansion not listed as separate observation |
|  |  |  |  |  | StartYr2 | Text | Year operations initiated for second expansion project, or expected to initiate, if expansion not listed as separate observation |
|  |  |  |  |  | StartYr3 | Text | Year operations ended (if Status="Mothballed", Status="Idle", or Status="Retired") or the year the project was cancelled (if Status="Cancelled"). If Status="Cancelled" due to 4-year rule\* (as opposed to a formal cancellation), then StopYear="presumed" |
|  |  |  |  |  | StopYr | Text | If Status=Shelved, the year this became true |
|  |  |  |  |  | ShelvedYr | Text | Maximum potential capacity |
|  |  |  |  |  | Capac | Text | If Status=Cancelled, the year this became true |
|  |  |  |  |  | CancelldYr | Text | Units that "Capacity" is reported in (bpd, bcm/year, mtpa, MMcf/d, or TJ/d) |
|  |  |  |  |  | CapacUnits | Text | Capacity converted to billion cubic meters (bcm) per year |
|  |  |  |  |  | CapacBOEd | Text | Capacity converted to barrels of oil equivalent (BOE) per day |
|  |  |  |  |  | LenKwnKm | Text | Publicly available length, converted to km |
|  |  |  |  |  | LenEstKm | Text | Estimated length in km, calulated using route coordinates with Geopandas Python package and taken from "Length Estimates by Pipeline" tab) |
|  |  |  |  |  | LenMergdKm | Text | Merge between LengthKnownKm and LengthEstimateKm (LengthKnownKm is priotized when available; otherwise LengthEstimateKm is used). |
|  |  |  |  |  | Diam | Text | Pipeline's diameter (without units); when multiple values are reported, they are separated by a comma |
|  |  |  |  |  | DiamUnits | Text | Pipeline's diameter units |
|  |  |  |  |  | FuelSource | Text | Name of oil or gas field, or pipeline, the fuel is sourced from |
|  |  |  |  |  | StartLoc | Text | Town, city, or village the pipeline starts in |
|  |  |  |  |  | StartDist | Text | Prefecture or district the pipeline starts in |
|  |  |  |  |  | StartState | Text | State or province pipeline starts in |
|  |  |  |  |  | StartReg | Text | Pipeline's start region. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | EndLoc | Text | Town, city, or village the pipeline ends in |
|  |  |  |  |  | StartSubRe | Text | Pipeline's start subregion. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | EndDist | Text | Prefecture or district the pipeline ends in |
|  |  |  |  |  | EndState | Text | State or province the pipeline ends in |
|  |  |  |  |  | EndReg | Text | Pipeline's end region. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | FID\_1 | Text | Has the project received its Final Investment Decision (FID) yet? (if Status="Proposed" then option: "Pre-FID"/"FID", if Status is anything other than "Proposed", then leave blank) |
|  |  |  |  |  | EndSubRe | Text | Pipeline's end subregion. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | FIDYr | Text | If Pre-FID status, then enter the year FID is expected; if FID already made, then enter year of decision. |
|  |  |  |  |  | OthLanName | Text | Primary name in other relevant search language. |
|  |  |  |  |  | OthLanSeg | Text | Pipeline segment/expansion name in other relevant search languages. |
|  |  |  |  |  | Cost | Text | Cost of the project (either estimated or actual) |
|  |  |  |  |  | CostUnits | Text | Cost units/currency 3-letter code name (USD, EUR, etc.) |
|  |  |  |  |  | CostUSD | Text | Cost of construction converted to USD |
|  |  |  |  |  | LastUpdate | Text | Date this was last checked/updated (filled in by Researcher) |

69. # **GEM-GGIT-Gas-Pipelines-2024-12**

**Title:** gas\_pipelines  
**Abstract:** This dataset represents tracks natural gas transmission pipeline projects globally.  
**Purpose:**  
**Keywords:** gas infrastructure  
**Temporal Extent:**

* **Date**: 12/2024  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box: Top: 73.007222 degree Bottom: \-54.809613 degree Left: \-158.093400 degree Right: 177.125555 degree

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefiles  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: Recommended Citation: “Global Oil Infrastructure Tracker, Global Energy Monitor, May 2024 release”.

**Metadata Contact:**

* Organization: [Global Energy Monitor](https://globalenergymonitor.org/projects/global-gas-infrastructure-tracker/download-data/​)  
* Position: Global Oil Infrastructure Tracker: Baird Langenbrunner   
* Email: baird.langenbrunner@globalenergymonitor.org  
* Phone: 415-206-0906

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| gas\_pipelines.shp | WGS 1984 | Shapefile | 3,908 | 48 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | ProjectID | Text | A unique ID for each project (all the phases, segments, expansions, etc. belonging to the same overall pipeline do not necesssarily share a ProjectID, but they should share the same PipelineName) |
|  |  |  |  |  | Fuel | Text | Oil, Gas, or NGL |
|  |  |  |  |  | StartCntry | Text | Country the pipeline starts in |
|  |  |  |  |  | EndCntry | Text | Country the pipeline ends in |
|  |  |  |  |  | Countries | Text | Countries that the pipeline passes through, in order from beginning to end (where possible); note Hong Kong and Macao are recognized as sovereign states here |
|  |  |  |  |  | Wiki | Text | Link to project's GEM.wiki page |
|  |  |  |  |  | PipeName | Text | Name of the pipeline (or pipeline system, when it has multiple pieces, phases, segments, or expansions) |
|  |  |  |  |  | SegName | Text | Name of the pipeline segment (which can be a segment of a bigger pipeline system/network, or an expansion project) |
|  |  |  |  |  | OthEngName | Text | Alternate pipeline names in English, if applicable; if there are multiple, separate by a semicolon (;) |
|  |  |  |  |  | Status | Text | Operating, Proposed, Retired, Construction, Shelved, Cancelled, Idle, or Mothballed If there have been no development updates in the two years following the project's proposal, then the status is assumed to be "Shelved". If there have been no development updates in the 4 years following the project's proposal or longer, the status is assumed to be "Cancelled". If Shelved, Cancelled, or Retired, these are associated with ShelvedYear, CancelledYear, and StopYear |
|  |  |  |  |  | Owner | Text | Auto-filled: direct owner name(s), percent ownership if available; here "owner" means lowest level of ownership that we're able to find in our research. |
|  |  |  |  |  | Parent | Text | Parent company name(s), percent ownership if available; here "parent" means highest level of ownership that we're able to trace (e.g., parent companies or ultimate shareholders). |
|  |  |  |  |  | StartYr1 | Text | First year operations initiated, or expected to initiate |
|  |  |  |  |  | StartYr2 | Text | Year operations initiated for first expansion project, or expected to initiate, if expansion not listed as separate observation |
|  |  |  |  |  | StartYr3 | Text | Year operations initiated for second expansion project, or expected to initiate, if expansion not listed as separate observation |
|  |  |  |  |  | StopYr | Text | Year operations ended (if Status="Mothballed", Status="Idle", or Status="Retired") or the year the project was cancelled (if Status="Cancelled"). If Status="Cancelled" due to 4-year rule\* (as opposed to a formal cancellation), then StopYear="presumed" |
|  |  |  |  |  | ShelvedYr | Text | If Status=Shelved, the year this became true |
|  |  |  |  |  | Capac | Text | Maximum potential capacity |
|  |  |  |  |  | CancelldYr | Text | If Status=Cancelled, the year this became true |
|  |  |  |  |  | CapacUnits | Text | Units that "Capacity" is reported in (bpd, bcm/year, mtpa, MMcf/d, or TJ/d) |
|  |  |  |  |  | CapacBcm/y | Text | Capacity converted to billion cubic meters (bcm) per year |
|  |  |  |  |  | CapacBOEd | Text | Capacity converted to barrels of oil equivalent (BOE) per day |
|  |  |  |  |  | LenKwnKm | Text | Publicly available length, converted to km |
|  |  |  |  |  | LenEstKm | Text | Estimated length in km, calulated using route coordinates with Geopandas Python package and taken from "Length Estimates by Pipeline" tab) |
|  |  |  |  |  | LenMergdKm | Text | Merge between LengthKnownKm and LengthEstimateKm (LengthKnownKm is priotized when available; otherwise LengthEstimateKm is used). |
|  |  |  |  |  | Diam | Text | Pipeline's diameter (without units); when multiple values are reported, they are separated by a comma |
|  |  |  |  |  | DiamUnits | Text | Pipeline's diameter units |
|  |  |  |  |  | FuelSource | Text | Name of oil or gas field, or pipeline, the fuel is sourced from |
|  |  |  |  |  | StartLoc | Text | Town, city, or village the pipeline starts in |
|  |  |  |  |  | StartDist | Text | Prefecture or district the pipeline starts in |
|  |  |  |  |  | StartState | Text | State or province pipeline starts in |
|  |  |  |  |  | StartReg | Text | Pipeline's start region. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | EndLoc | Text | Town, city, or village the pipeline ends in |
|  |  |  |  |  | StartSubRe | Text | Pipeline's start subregion. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | EndDist | Text | Prefecture or district the pipeline ends in |
|  |  |  |  |  | EndState | Text | State or province the pipeline ends in |
|  |  |  |  |  | EndReg | Text | Pipeline's end region. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | FIDStatus | Text | Has the project received its Final Investment Decision (FID) yet? (if Status="Proposed" then option: "Pre-FID"/"FID", if Status is anything other than "Proposed", then leave blank) |
|  |  |  |  |  | EndSubRe | Text | Pipeline's end subregion. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | FIDYr | Text | If Pre-FID status, then enter the year FID is expected; if FID already made, then enter year of decision. |
|  |  |  |  |  | OthLanName | Text | Primary name in other relevant search language. |
|  |  |  |  |  | OthLanSeg | Text | Pipeline segment/expansion name in other relevant search languages. |
|  |  |  |  |  | Cost | Text | Cost of the project (either estimated or actual) |
|  |  |  |  |  | CostUnits | Text | Cost units/currency 3-letter code name (USD, EUR, etc.) |
|  |  |  |  |  | CostUSD | Text | Cost of construction converted to USD |
|  |  |  |  |  | LastUpdate | Text | Date this was last checked/updated (filled in by Researcher) |

70. # **GEM-GGIT-LNG-Terminals-2024-09**

**Title:** liquefied\_natural\_gas\_terminals  
**Abstract:** This dataset represents tracks liquefied natural gas (LNG) import and export terminals globally.  
**Purpose:**  
**Keywords:** gas infrastructure, liquefied natural gas, terminals  
**Temporal Extent:**

* **Date**: 9/2024  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box: Top: 73.153613 degree Bottom: \-41.576699 degree Left: \-151.388340 degree Right: 154.690296 degree

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** unknown  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefiles  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: Recommended Citation: “Global Oil Infrastructure Tracker, Global Energy Monitor, May 2024 release”.

**Metadata Contact:**

* Organization: [Global Energy Monitor](https://globalenergymonitor.org/projects/global-gas-infrastructure-tracker/download-data/​)  
* Position: Global Oil Infrastructure Tracker: Baird Langenbrunner   
* Email: baird.langenbrunner@globalenergymonitor.org  
* Phone: 415-206-0906


**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| liquefied\_natural\_gas\_terminals.shp | unknown | Shapefile | 1,295 | 23 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | TerminalID | Text | Assigned ID number to every whole terminal. Unique to each distinct terminal. |
|  |  |  |  |  | ProjectID | Text | Assigned ID number to every project within a whole terminal. Unique within each distinct TerminalID. |
|  |  |  |  |  | ComboID | Text | Combined TerminalID and ProjectID to create unique index value for every observation. |
|  |  |  |  |  | Wiki | Text | Link to project's GEM.wiki page |
|  |  |  |  |  | TermName | Text | Terminal name |
|  |  |  |  |  | UnitName | Text | Smaller unit within a terminal (including trains T1, T2; phases Phase 1, Phase 2; expansions; project revivals/recommissions; etc.) |
|  |  |  |  |  | FacilType | Text | Type of facility (import or export terminal) |
|  |  |  |  |  | Status | Text | Operating, Proposed, Retired, Construction, Shelved, Cancelled, Idle, or Mothballed If there have been no development updates in the two years following the project's proposal, then the status is assumed to be "Shelved". If there have been no development updates in the 4 years following the project's proposal or longer, the status is assumed to be "Cancelled" |
|  |  |  |  |  | Country | Text | Country of location; note Hong Kong and Macao are considered separate countries so that their infrastructure can be tracked independently of China |
|  |  |  |  |  | OthLanName | Text | Terminal name in its local language (referring exactly to the OtherLanguageWikiPage) |
|  |  |  |  |  | OthEngName | Text | Alternate terminal names in English (note some Chinese terminals are also included, and these will eventually be moved to an OtherLanguageTerminalName column) |
|  |  |  |  |  | Owner | Text | Owner company name(s), percent ownership if available; here "owner" means lowest level of ownership that we're able to trace. |
|  |  |  |  |  | Parent | Text | Parent company name(s), percent ownership if available, taken from the Parent tab; here "parent" means highest level of ownership that we're able to trace (e.g., parent companies or ultimate shareholders). For state-owned enterprises, we prioritize the name of the company (e.g., PipeChina) or the ministry (e.g., Iran Ministry of Oil) rather than Government of China or Government of Iran. |
|  |  |  |  |  | ParHQCntry | Text | Parents' headquarters countries, listed in order of the parent companies. |
|  |  |  |  |  | Capac | Text | Maximum potential production capacity (if there's a range found in research, the maximum is recorded in the sheet and the range is added to the wiki page) |
|  |  |  |  |  | CapacUnits | Text | Unit that capacity is publicly reported in (mtpa, bcf/d, bcm/year, gal/day) |
|  |  |  |  |  | CapacMtpa | Text | Publicly reported capacity value, converted to mtpa |
|  |  |  |  |  | CapInBcmy | Text | Capacity in bcm/y |
|  |  |  |  |  | PropYr | Text | Year the project was first proposed |
|  |  |  |  |  | PropMo | Text | Month project was proposed |
|  |  |  |  |  | ConstYr | Text | Year construction began (only fill out if construction has already started or been completed, not the expected year of construction start) |

# 

71. # **AMPHIBIANS**

**Title:** iucn\_amphibians  
**Abstract:** This dataset represents the known range of amphibian species from the class Amphibia on the IUCN Red List of Threatened Species, which contains global assessments for more than 169,400 species. More than 87.5% of these (\>148,900 species) have spatial data.  
**Purpose:**  
**Keywords:** amphibian species  
**Temporal Extent:**

* **Date**: March 2025  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box:   
  * Top	3,326,203.364400	m  
  * Bottom	\-3,088,166.420687	m  
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
| iucn\_amphibians.shp | WGS 1984 | Shapefile | 26 | 32 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | id\_no | Integer |  |
|  |  |  |  |  | sci\_name | String |  |
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
|  |  |  |  |  | tax\_comm | String |  |
|  |  |  |  |  | dist\_comm | String |  |
|  |  |  |  |  | generalisd | Integer |  |
|  |  |  |  |  | legend | String |  |
|  |  |  |  |  | kingdom | String |  |
|  |  |  |  |  | phylum | String |  |
|  |  |  |  |  | class | String |  |
|  |  |  |  |  | order\_ | String |  |
|  |  |  |  |  | family | String |  |
|  |  |  |  |  | genus | String |  |
|  |  |  |  |  | category | String |  |
|  |  |  |  |  | marine | String |  |
|  |  |  |  |  | terrestria | String |  |
|  |  |  |  |  | freshwater | String |  |
|  |  |  |  |  | SHAPE\_Leng | Double |  |
|  |  |  |  |  | Shape\_Le\_1 | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |
|  |  |  |  |  | area\_km2 | Double |  |

# 

72. # **MAMMALS**

**Title:** iucn\_mammals  
**Abstract:** This dataset represents the known range of mammal species from the class Mammalia on the IUCN Red List of Threatened Species, which contains global assessments for more than 169,400 species. More than 87.5% of these (\>148,900 species) have spatial data.  
**Purpose:**  
**Keywords:** mammal species  
**Temporal Extent:**

* **Date**: March 2025  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box:   
  * Top	4,392,355.501400	m  
  * Bottom	\-3,323,302.458200	m  
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
| iucn\_mammals.shp | WGS 1984 | Shapefile | 340 | 32 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | id\_no | Integer |  |
|  |  |  |  |  | sci\_name | String |  |
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
|  |  |  |  |  | tax\_comm | String |  |
|  |  |  |  |  | dist\_comm | String |  |
|  |  |  |  |  | generalisd | Integer |  |
|  |  |  |  |  | legend | String |  |
|  |  |  |  |  | kingdom | String |  |
|  |  |  |  |  | phylum | String |  |
|  |  |  |  |  | class | String |  |
|  |  |  |  |  | order\_ | String |  |
|  |  |  |  |  | family | String |  |
|  |  |  |  |  | genus | String |  |
|  |  |  |  |  | category | String |  |
|  |  |  |  |  | marine | String |  |
|  |  |  |  |  | terrestria | String |  |
|  |  |  |  |  | freshwater | String |  |
|  |  |  |  |  | SHAPE\_Leng | Double |  |
|  |  |  |  |  | Shape\_Le\_1 | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |
|  |  |  |  |  | area\_km2 | Double |  |

# 

73. # **PLANTS**

**Title:** iucn\_plants  
**Abstract:** This dataset represents the known range of plant species from the kingdom Plantae on the IUCN Red List of Threatened Species, which contains global assessments for more than 169,400 species. More than 87.5% of these (\>148,900 species) have spatial data.  
**Purpose:**  
**Keywords:** plant species  
**Temporal Extent:**

* **Date**: March 2025  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box:   
  * Top	4,392,355.501400	m  
  * Bottom	\-3,323,302.458200	m  
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
| iucn\_plants.shp | WGS 1984 | Shapefile | 335 | 32 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | id\_no | Integer |  |
|  |  |  |  |  | sci\_name | String |  |
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
|  |  |  |  |  | tax\_comm | String |  |
|  |  |  |  |  | dist\_comm | String |  |
|  |  |  |  |  | generalisd | Integer |  |
|  |  |  |  |  | legend | String |  |
|  |  |  |  |  | kingdom | String |  |
|  |  |  |  |  | phylum | String |  |
|  |  |  |  |  | class | String |  |
|  |  |  |  |  | order\_ | String |  |
|  |  |  |  |  | family | String |  |
|  |  |  |  |  | genus | String |  |
|  |  |  |  |  | category | String |  |
|  |  |  |  |  | marine | String |  |
|  |  |  |  |  | terrestria | String |  |
|  |  |  |  |  | freshwater | String |  |
|  |  |  |  |  | SHAPE\_Leng | Double |  |
|  |  |  |  |  | Shape\_Le\_1 | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |
|  |  |  |  |  | area\_km2 | Double |  |

# 

74. # **REPTILES**

**Title:** iucn\_reptiles  
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
| iucn\_reptiles.shp | WGS 1984 | Shapefile | 10 | 32 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | id\_no | Integer |  |
|  |  |  |  |  | sci\_name | String |  |
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
|  |  |  |  |  | tax\_comm | String |  |
|  |  |  |  |  | dist\_comm | String |  |
|  |  |  |  |  | generalisd | Integer |  |
|  |  |  |  |  | legend | String |  |
|  |  |  |  |  | kingdom | String |  |
|  |  |  |  |  | phylum | String |  |
|  |  |  |  |  | class | String |  |
|  |  |  |  |  | order\_ | String |  |
|  |  |  |  |  | family | String |  |
|  |  |  |  |  | genus | String |  |
|  |  |  |  |  | category | String |  |
|  |  |  |  |  | marine | String |  |
|  |  |  |  |  | terrestria | String |  |
|  |  |  |  |  | freshwater | String |  |
|  |  |  |  |  | SHAPE\_Leng | Double |  |
|  |  |  |  |  | Shape\_Le\_1 | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |
|  |  |  |  |  | area\_km2 | Double |  |

# 

75. # **arctic\_marine\_biodiversity**

**Title:** arctic\_marine\_biodiversity  
**Abstract:** This dataset represents the biodiversity found in the sea ice, water column and sea floor located in Arctic, Pacific and coastal Alaska.  
**Purpose:**  
**Keywords:** arctic ocean, species  
**Temporal Extent:**

* **Date**: March 2018  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box:   
  * Top	4,353,443.345200	m  
  * Bottom	\-2,483,176.805300	m  
  * Left	\-2,907,813.369100	m  
  * Right	2,089,870.704000	m

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
* Use Constraints: 

**Metadata Contact:**

* Organization: Global Biodiversity Information Facility ([GBIF](https://www.gbif.org/dataset/84b72ee4-f762-11e1-a439-00145eb45e9a​))  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| arctic\_marine\_biodiversity.shp | WGS 1984 | Shapefile | 177,351 | 73 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | gbifID | Integer |  |
|  |  |  |  |  | license | String |  |
|  |  |  |  |  | publisher | String |  |
|  |  |  |  |  | institutio | String |  |
|  |  |  |  |  | collection | String |  |
|  |  |  |  |  | basisOfRec | String |  |
|  |  |  |  |  | catalogNum | Integer |  |
|  |  |  |  |  | recordedBy | String |  |
|  |  |  |  |  | occurrence | String |  |
|  |  |  |  |  | eventDate | String |  |
|  |  |  |  |  | startDayOf | Double |  |
|  |  |  |  |  | endDayOfYe | Double |  |
|  |  |  |  |  | year | Double |  |
|  |  |  |  |  | month | Double |  |
|  |  |  |  |  | day | Double |  |
|  |  |  |  |  | continent | String |  |
|  |  |  |  |  | countryCod | String |  |
|  |  |  |  |  | stateProvi | String |  |
|  |  |  |  |  | locality | String |  |
|  |  |  |  |  | decimalLat | Double |  |
|  |  |  |  |  | decimalLon | Double |  |
|  |  |  |  |  | identified | String |  |
|  |  |  |  |  | acceptedNa | Double |  |
|  |  |  |  |  | scientific | String |  |
|  |  |  |  |  | kingdom | String |  |
|  |  |  |  |  | phylum | String |  |
|  |  |  |  |  | class | String |  |
|  |  |  |  |  | order\_ | String |  |
|  |  |  |  |  | family | String |  |
|  |  |  |  |  | genus | String |  |
|  |  |  |  |  | genericNam | String |  |
|  |  |  |  |  | specificEp | String |  |
|  |  |  |  |  | infraspeci | String |  |
|  |  |  |  |  | taxonRank | String |  |
|  |  |  |  |  | taxonomicS | String |  |
|  |  |  |  |  | datasetKey | String |  |
|  |  |  |  |  | publishing | String |  |
|  |  |  |  |  | lastInterp | String |  |
|  |  |  |  |  | depth | String |  |
|  |  |  |  |  | depthAccur | String |  |
|  |  |  |  |  | issue | String |  |
|  |  |  |  |  | hasCoordin | String |  |
|  |  |  |  |  | hasGeospat | String |  |
|  |  |  |  |  | taxonKey | Integer |  |
|  |  |  |  |  | acceptedTa | Double |  |
|  |  |  |  |  | kingdomKey | Integer |  |
|  |  |  |  |  | phylumKey | Double |  |
|  |  |  |  |  | classKey | Double |  |
|  |  |  |  |  | orderKey | Double |  |
|  |  |  |  |  | familyKey | Double |  |
|  |  |  |  |  | genusKey | Double |  |
|  |  |  |  |  | speciesKey | Double |  |
|  |  |  |  |  | species | String |  |
|  |  |  |  |  | acceptedSc | String |  |
|  |  |  |  |  | verbatimSc | String |  |
|  |  |  |  |  | protocol | String |  |
|  |  |  |  |  | lastParsed | String |  |
|  |  |  |  |  | lastCrawle | String |  |
|  |  |  |  |  | repatriate | String |  |
|  |  |  |  |  | isSequence | String |  |
|  |  |  |  |  | gbifRegion | String |  |
|  |  |  |  |  | publishedB | String |  |
|  |  |  |  |  | level0Gid | String |  |
|  |  |  |  |  | level0Name | String |  |
|  |  |  |  |  | level1Gid | String |  |
|  |  |  |  |  | level1Name | String |  |
|  |  |  |  |  | level2Gid | String |  |
|  |  |  |  |  | level2Name | String |  |
|  |  |  |  |  | level3Gid | String |  |
|  |  |  |  |  | level3Name | String |  |
|  |  |  |  |  | iucnRedLis | String |  |

76. # **aga\_arctic\_ak\_vegetation\_2005\_shp**

**Title:** alaska\_vegetation  
**Abstract:** This dataset represents the zonal vegetation within each mapped polygon. There are 5 zones: B — barrens, G — graminoid-dominated tundras, P — prostrate-shrub-dominated tundras, S — erect-shrub-dominated tundras, and W — wetlands. Each zone is subdivided into 15 vegetation mapping units with numeric codes, named according to dominant plant functional types.  
**Purpose:**  
**Keywords:** vegetation, plants, Alaska  
**Temporal Extent:**

* **Date**: November 2020  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box:   
  * Top	3,326,203.693162	m  
  * Bottom	1,736,158.673033	m  
  * Left	\-1,487,557.834344	m  
  * Right	\-395,912.359893	m

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
* Use Constraints: 

**Metadata Contact:**

* Organization: [Alaska Arctic Geoecological Atlas (AAGA)](https://arcticatlas.geobotany.org/catalog/dataset/alaska-arctic-vegetation-map)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| alaska\_vegetation.shp | WGS 1984 | Shapefile | 771 | 31 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | AREA | Double |  |
|  |  |  |  |  | PERIMETER | Double |  |
|  |  |  |  |  | ALASKA3\_ | Integer |  |
|  |  |  |  |  | ALASKA3\_ID | Integer |  |
|  |  |  |  |  | ILUM | Integer |  |
|  |  |  |  |  | ZONE\_ | Integer |  |
|  |  |  |  |  | PERCENTLAK | Integer |  |
|  |  |  |  |  | CALCAREOUS | Integer |  |
|  |  |  |  |  | SOIL | Integer |  |
|  |  |  |  |  | BEDROCK | Integer |  |
|  |  |  |  |  | SURFGEO | Integer |  |
|  |  |  |  |  | PHYTO | Integer |  |
|  |  |  |  |  | ZILUM | Integer |  |
|  |  |  |  |  | MAPPED | Integer |  |
|  |  |  |  |  | SHRUB | Integer |  |
|  |  |  |  |  | TOPO | Integer |  |
|  |  |  |  |  | PHYTO2 | Integer |  |
|  |  |  |  |  | CHEM | Integer |  |
|  |  |  |  |  | LAKEAREA | Double |  |
|  |  |  |  |  | LAKEPIX | Double |  |
|  |  |  |  |  | LAKEPIXCAT | Integer |  |
|  |  |  |  |  | COUNTRY | Integer |  |
|  |  |  |  |  | LANDSCAPE | Integer |  |
|  |  |  |  |  | PHYSIOG | Integer |  |
|  |  |  |  |  | FINAL | Integer |  |
|  |  |  |  |  | VEG | Double |  |
|  |  |  |  |  | COMM | String |  |
|  |  |  |  |  | Shape\_Leng | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |

77. # **World\_ECS\_v2\_20241010/ecs\_v02**

**Title:** extended\_continental\_shelf\_areas  
**Abstract:** This dataset is a polygon layer representing the Extended Continental Shelves, which are the portion of the continental shelf that extends beyond 200 Nautical Miles, as submitted by a State to or recommended by the Commission on the Limits of the Continental Shelf (CLCS), or deposited with the Division for Ocean Affairs and the Law of the Sea (DOALOS), or claimed by (a) a Non-Party State to UNCLOS or (b) a Party State to UNCLOS through mechanisms other than a submission to the CLCS or a deposit to DOALOS.  
**Purpose:**  
**Keywords:** UNCLOS, Extended Continental Shelves, claims  
**Temporal Extent:**

* **Date**: 2024  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box:   
  * Top	3,879,666.141074	m  
  * Bottom	\-2,822,852.135087	m  
  * Left	\-2,992,923.819108	m  
  * Right	1,279,032.561875	m

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** unknown  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefiles  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization: [Marine Regions](https://www.marineregions.org/downloads.php)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| extended\_continental\_shelf\_areas.shp | WGS 1984 | Shapefile | 24 | 73 | Field Name | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
|  |  |  |  |  | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | GEONAME | String |  |
|  |  |  |  |  | POL\_TYPE | String |  |
|  |  |  |  |  | TERRITORY1 | String |  |
|  |  |  |  |  | MRGID\_TER1 | Double |  |
|  |  |  |  |  | ISO\_TER1 | String |  |
|  |  |  |  |  | UN\_TER1 | Double |  |
|  |  |  |  |  | SOVEREIGN1 | String |  |
|  |  |  |  |  | MRGID\_SOV1 | Double |  |
|  |  |  |  |  | ISO\_SOV1 | String |  |
|  |  |  |  |  | UN\_SOV1 | Double |  |
|  |  |  |  |  | TERRITORY2 | String |  |
|  |  |  |  |  | MRGID\_TER2 | Double |  |
|  |  |  |  |  | ISO\_TER2 | String |  |
|  |  |  |  |  | UN\_TER2 | Double |  |
|  |  |  |  |  | SOVEREIGN2 | String |  |
|  |  |  |  |  | MRGID\_SOV2 | Double |  |
|  |  |  |  |  | ISO\_SOV2 | String |  |
|  |  |  |  |  | UN\_SOV2 | Double |  |
|  |  |  |  |  | TERRITORY3 | String |  |
|  |  |  |  |  | MRGID\_TER3 | Double |  |
|  |  |  |  |  | ISO\_TER3 | String |  |
|  |  |  |  |  | UN\_TER3 | Double |  |
|  |  |  |  |  | SOVEREIGN3 | String |  |
|  |  |  |  |  | MRGID\_SOV3 | Double |  |
|  |  |  |  |  | ISO\_SOV3 | String |  |
|  |  |  |  |  | UN\_SOV3 | Double |  |
|  |  |  |  |  | TERRITORY4 | String |  |
|  |  |  |  |  | MRGID\_TER4 | Double |  |
|  |  |  |  |  | ISO\_TER4 | String |  |
|  |  |  |  |  | UN\_TER4 | Double |  |
|  |  |  |  |  | SOVEREIGN4 | String |  |
|  |  |  |  |  | MRGID\_SOV4 | Double |  |
|  |  |  |  |  | ISO\_SOV4 | String |  |
|  |  |  |  |  | UN\_SOV4 | Double |  |
|  |  |  |  |  | TERRITORY5 | String |  |
|  |  |  |  |  | MRGID\_TER5 | Double |  |
|  |  |  |  |  | ISO\_TER5 | String |  |
|  |  |  |  |  | UN\_TER5 | Double |  |
|  |  |  |  |  | SOVEREIGN5 | String |  |
|  |  |  |  |  | MRGID\_SOV5 | Double |  |
|  |  |  |  |  | ISO\_SOV5 | String |  |
|  |  |  |  |  | UN\_SOV5 | Double |  |
|  |  |  |  |  | TERRITORY6 | String |  |
|  |  |  |  |  | MRGID\_TER6 | Double |  |
|  |  |  |  |  | ISO\_TER6 | String |  |
|  |  |  |  |  | UN\_TER6 | Double |  |
|  |  |  |  |  | SOVEREIGN6 | String |  |
|  |  |  |  |  | MRGID\_SOV6 | Double |  |
|  |  |  |  |  | ISO\_SOV6 | String |  |
|  |  |  |  |  | UN\_SOV6 | Double |  |
|  |  |  |  |  | TERRITORY7 | String |  |
|  |  |  |  |  | MRGID\_TER7 | Double |  |
|  |  |  |  |  | ISO\_TER7 | String |  |
|  |  |  |  |  | UN\_TER7 | Double |  |
|  |  |  |  |  | SOVEREIGN7 | String |  |
|  |  |  |  |  | MRGID\_SOV7 | Double |  |
|  |  |  |  |  | ISO\_SOV7 | String |  |
|  |  |  |  |  | UN\_SOV7 | Double |  |
|  |  |  |  |  | TERRITORY8 | String |  |
|  |  |  |  |  | MRGID\_TER8 | Double |  |
|  |  |  |  |  | ISO\_TER8 | String |  |
|  |  |  |  |  | UN\_TER8 | Double |  |
|  |  |  |  |  | SOVEREIGN8 | String |  |
|  |  |  |  |  | MRGID\_SOV8 | Double |  |
|  |  |  |  |  | ISO\_SOV8 | String |  |
|  |  |  |  |  | UN\_SOV8 | Double |  |
|  |  |  |  |  | X\_1 | Double |  |
|  |  |  |  |  | Y\_1 | Double |  |
|  |  |  |  |  | AREA\_KM2 | Double |  |
|  |  |  |  |  | MRGID | Double |  |
|  |  |  |  |  | MRGID\_ECS | Double |  |

# 

78. # **World\_ECS\_v2\_20241010/ecs\_boundaries\_v02**

**Title:** extended\_continental\_shelf\_boundaries  
**Abstract:** This dataset represents the outer limits of the Extended Continental Shelves, which are the portion of the continental shelf that extends beyond 200 Nautical Miles, as submitted by a State to or recommended by the Commission on the Limits of the Continental Shelf (CLCS), or deposited with the Division for Ocean Affairs and the Law of the Sea (DOALOS), or claimed by (a) a Non-Party State to UNCLOS or (b) a Party State to UNCLOS through mechanisms other than a submission to the CLCS or a deposit to DOALOS.  
**Purpose:**  
**Keywords:** UNCLOS, Extended Continental Shelves, claims  
**Temporal Extent:**

* **Date**: 9/2024  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box:   
  * Top	3,835,526.894206	m  
  * Bottom	\-2,823,003.934644	m  
  * Left	\-2,988,887.422427	m  
  * Right	1,148,960.959265	m

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** unknown  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefiles  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization: Marine Regions  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| extended\_continental\_shelf\_boundaries.shp | WGS 1984 | Shapefile | 49 | 42 | Field Name | Data Type | Description |
|  |  |  |  |  | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | LINE\_ID | Double |  |
|  |  |  |  |  | LINE\_NAME | String |  |
|  |  |  |  |  | LINE\_TYPE | String |  |
|  |  |  |  |  | TERRITORY1 | String |  |
|  |  |  |  |  | SOVEREIGN1 | String |  |
|  |  |  |  |  | TERRITORY2 | String |  |
|  |  |  |  |  | SOVEREIGN2 | String |  |
|  |  |  |  |  | TERRITORY3 | String |  |
|  |  |  |  |  | SOVEREIGN3 | String |  |
|  |  |  |  |  | TERRITORY4 | String |  |
|  |  |  |  |  | SOVEREIGN4 | String |  |
|  |  |  |  |  | TERRITORY5 | String |  |
|  |  |  |  |  | SOVEREIGN5 | String |  |
|  |  |  |  |  | TERRITORY6 | String |  |
|  |  |  |  |  | SOVEREIGN6 | String |  |
|  |  |  |  |  | TERRITORY7 | String |  |
|  |  |  |  |  | SOVEREIGN7 | String |  |
|  |  |  |  |  | MRGID\_TER1 | Double |  |
|  |  |  |  |  | MRGID\_SOV1 | Double |  |
|  |  |  |  |  | MRGID\_TER2 | Double |  |
|  |  |  |  |  | MRGID\_SOV2 | Double |  |
|  |  |  |  |  | MRGID\_TER3 | Double |  |
|  |  |  |  |  | MRGID\_SOV3 | Double |  |
|  |  |  |  |  | MRGID\_TER4 | Double |  |
|  |  |  |  |  | MRGID\_SOV4 | Double |  |
|  |  |  |  |  | MRGID\_TER5 | Double |  |
|  |  |  |  |  | MRGID\_SOV5 | Double |  |
|  |  |  |  |  | MRGID\_TER6 | Double |  |
|  |  |  |  |  | MRGID\_SOV6 | Double |  |
|  |  |  |  |  | MRGID\_TER7 | Double |  |
|  |  |  |  |  | MRGID\_SOV7 | Double |  |
|  |  |  |  |  | ORIGIN | String |  |
|  |  |  |  |  | URL1 | String |  |
|  |  |  |  |  | SOURCE1 | String |  |
|  |  |  |  |  | DOC\_DATE | String |  |
|  |  |  |  |  | URL2 | String |  |
|  |  |  |  |  | SOURCE2 | String |  |
|  |  |  |  |  | URL3 | String |  |
|  |  |  |  |  | SOURCE3 | String |  |
|  |  |  |  |  | LENGTH\_KM | Double |  |

79. # **Submarine\_Cables\_and\_Terminals\_\_2018\_-shp**

**Title:** submarine\_cables\_terminals  
**Abstract:** This dataset represents a global network of submarine communication cables and terminals, as of June 2018\.  
**Purpose:**  
**Keywords:** undersea cables, submarine cables  
**Temporal Extent:**

* **Date**: 6/2018  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box:   
  * Top	3,942,636.518955	m  
  * Bottom	\-3,297,134.984163	m  
  * Left	\-2,955,108.357505	m  
  * Right	678,403.174806	m

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** unknown  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefiles  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization: TeleGeography  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| submarine\_cables\_terminals.shp | WGS 1984 | Shapefile | 19 | 11 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | OBJECTID | Integer |  |
|  |  |  |  |  | Name | String |  |
|  |  |  |  |  | Text\_ID | String |  |
|  |  |  |  |  | cable\_id | String |  |
|  |  |  |  |  | length | String |  |
|  |  |  |  |  | ReadyForSe | String |  |
|  |  |  |  |  | owners | String |  |
|  |  |  |  |  | url | String |  |
|  |  |  |  |  | Shape\_\_Len | Double |  |

80. # **Permafrost/PerProb\_**

**Title:** permaf\_pro  
**Abstract:** This raster shows permafrost occurrence probability with fraction values from 0 to 1 assigned to each grid cell with MAGT \< 0°C.  
**Purpose:** This dataset represents permafrost extent from 2000-2016 in the Northern Hemisphere.  
**Keywords:** permafrost  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: 2000-2016  
* 

**Geographic Extent:** 

* Bounding Box: Top: 67.759922, Bottom: 60.528484, Left: \-25.745716, Right: \-5.524639


**Spatial Resolution**:   
**Coordinate Reference Systems:** GCS\_WGS\_1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**

* Accuracy:  
* Completeness:  
* Consistency: 

**Distribution Information:**

* Format: Raster (TIFF)  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [Arctic Permafrost Geospatial Centre](https://apgc.awi.de/dataset/pex)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

81. # **elevation\_1KMmd\_GMTEDmd.tif**

**Title:** topograp\_e  
**Abstract:** This raster represents global topography of elevation at a 1km resolution using a median aggregation. The data is based on the digital elevation model product of global 250 m GMTED2010.  
**Purpose:** This dataset represents elevation topography data.   
**Keywords:** topography, elevation  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box:   
  * Top	4,371,301.402466	m  
  * Bottom	\-3,325,234.013158	m  
  * Left	\-4,312,167.265112	m  
  * Right	3,068,227.954657	m

**Spatial Resolution**: 1 km  
**Coordinate Reference Systems:** WGS\_1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**

* Accuracy:  
* Completeness:  
* Consistency: 

**Distribution Information:**

* Format: Raster (TIFF)  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [EarthEnv](https://www.earthenv.org//topography)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

82. # **GEBCO\_2024\_sub\_ice\_topo** 

**Title:** bathymetry  
**Abstract:** This raster provides global gridded bathymetric data that includes sub-ice topography, representing seafloor elevation beneath permanent ice cover.  
**Purpose:**   
**Keywords:** bathymetry, sub ice  
**Temporal Extent:**

* **Date**: 2019  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box:   
  * Top	4,380,379.995976	m  
  * Bottom	\-4,380,620.004024	m  
  * Left	\-4,379,687.575658	m  
  * Right	4,378,312.424342	m

**Spatial Resolution**:   
**Coordinate Reference Systems:** WGS\_1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].

**Quality Information:**

* Accuracy:  
* Completeness:  
* Consistency: 

**Distribution Information:**

* Format: Raster (netCDF)  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [GEBCO (General Bathymetric Chart of the Oceans)](https://www.gebco.net/data-products/gridded-bathymetry-data)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

83. # **Marine/SSP126/Routes\_SSP126\_2015\_2065**

**Title:** route\_SSP126\_low\_emissions  
**Abstract:** This dataset represents daily navigable Arctic marine shipping routes simulated under the SSP126 emissions scenario, derived from CMIP6 model projections of sea ice concentration and thickness. The routes were generated assuming a non-ice-strengthened vessel traveling between Rotterdam and the Bering Strait. Each route is based on sea ice conditions modeled by one of 14 CMIP6 general circulation models (GCMs) and spans multiple years and days. The dataset includes attributes for date and contributing climate model. These routes reflect potential Arctic accessibility patterns under a specific climate future scenario.  
**Purpose:** To assess Arctic marine accessibility under a **low-emissions**, sustainable development scenario (SSP1-2.6), where rapid global cooperation, renewable energy transition, and climate mitigation limit future warming and sea ice loss.  
**Keywords:** shipping routes, climate model  
**Temporal Extent:**

* **Date**: 2021  
* **Time Period**: 2015-2065

**Geographic Extent:** 

* Bounding Box:   
  * Top	2,635,762.186500	m  
  * Bottom	\-3,321,766.612412	m  
  * Left	\-2,439,534.585600	m  
  * Right	2,011,649.433400	m

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** 

* Projected Coordinate System: North\_Pole\_Lambert\_Azimuthal\_Equal\_Area

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization:   
  * Li, X., & Lynch, A. H. (2023). New insights into projected Arctic sea road: Operational risks, economic values, and policy implications. Climatic Change, 176(30). https://doi.org/10.1007/s10584-023-03505-4  
  * Lynch, A. H., Norchi, C. H., & Li, X. (2022). The interaction of ice and law in Arctic marine accessibility. Proceedings of the National Academy of Sciences, 119(26), e2202720119. https://doi.org/10.1073/pnas.2202720119  
  * Li, X., Stephenson, S. R., Lynch, A. H., Goldstein, M. A., Bailey, D. A., & Veland, S. (2021). Arctic shipping guidance from the CMIP6 ensemble on operational and infrastructural timescales. Climatic Change, 167(1), 23\. https://doi.org/10.1007/s10584-021-03172-3  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| route\_SSP126\_low\_emissions.shp | North\_Pole\_Lambert\_Azimuthal\_Equal\_Area | Shapefile | 64,094 | 7 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Year | String |  |
|  |  |  |  |  | Month | String |  |
|  |  |  |  |  | Day | String |  |
|  |  |  |  |  | Model | String |  |

84. # **Marine/SSP245/Routes\_SSP245\_2015\_2065**

**Title:** route\_SSP245\_moderate\_emissions  
**Abstract:** This dataset represents daily navigable Arctic marine shipping routes simulated under the SSP245 emissions scenario, derived from CMIP6 model projections of sea ice concentration and thickness. The routes were generated assuming a non-ice-strengthened vessel traveling between Rotterdam and the Bering Strait. Each route is based on sea ice conditions modeled by one of 14 CMIP6 general circulation models (GCMs) and spans multiple years and days. The dataset includes attributes for date and contributing climate model. These routes reflect potential Arctic accessibility patterns under a specific climate future scenario.  
**Purpose:** To explore Arctic marine route viability under a **moderate-emissions** scenario (SSP2-4.5), representing a continuation of current socioeconomic and policy trends with limited climate intervention.  
**Keywords:** shipping routes, climate model  
**Temporal Extent:**

* **Date**: 2021  
* **Time Period**: 2015-2065

**Geographic Extent:** 

* Bounding Box:   
  * Top	2,635,762.186500	m  
  * Bottom	\-3,322,039.250716	m  
  * Left	\-2,409,470.792300	m  
  * Right	1,960,996.968800	m

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** 

* Projected Coordinate System: North\_Pole\_Lambert\_Azimuthal\_Equal\_Area

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization:   
  * Li, X., & Lynch, A. H. (2023). New insights into projected Arctic sea road: Operational risks, economic values, and policy implications. Climatic Change, 176(30). https://doi.org/10.1007/s10584-023-03505-4  
  * Lynch, A. H., Norchi, C. H., & Li, X. (2022). The interaction of ice and law in Arctic marine accessibility. Proceedings of the National Academy of Sciences, 119(26), e2202720119. https://doi.org/10.1073/pnas.2202720119  
  * Li, X., Stephenson, S. R., Lynch, A. H., Goldstein, M. A., Bailey, D. A., & Veland, S. (2021). Arctic shipping guidance from the CMIP6 ensemble on operational and infrastructural timescales. Climatic Change, 167(1), 23\. https://doi.org/10.1007/s10584-021-03172-3  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| route\_SSP245\_moderate\_emissions.shp | North\_Pole\_Lambert\_Azimuthal\_Equal\_Area | Shapefile | 66,052 | 7 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Year | String |  |
|  |  |  |  |  | Month | String |  |
|  |  |  |  |  | Day | String |  |
|  |  |  |  |  | Model | String |  |

85. # **Marine/SSP370/Routes\_SSP370\_2015\_2065**

**Title:** route\_SSP370\_high\_emissions  
**Abstract:** This dataset represents daily navigable Arctic marine shipping routes simulated under the SSP370 emissions scenario, derived from CMIP6 model projections of sea ice concentration and thickness. The routes were generated assuming a non-ice-strengthened vessel traveling between Rotterdam and the Bering Strait. Each route is based on sea ice conditions modeled by one of 14 CMIP6 general circulation models (GCMs) and spans multiple years and days. The dataset includes attributes for date and contributing climate model. These routes reflect potential Arctic accessibility patterns under a specific climate future scenario.  
**Purpose:** To investigate Arctic shipping potential under a **high-emissions** scenario (SSP3-7.0), characterized by regional rivalry, reduced international cooperation, and more severe climate impacts.  
**Keywords:** shipping routes, climate model  
**Temporal Extent:**

* **Date**: 2021  
* **Time Period**: 2015-2065

**Geographic Extent:** 

* Bounding Box:   
  * Top	2,635,762.186500	m  
  * Bottom	\-3,322,039.250716	m  
  * Left	\-2,402,954.761900	m  
  * Right	1,938,007.121300	m

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** 

* Projected Coordinate System: North\_Pole\_Lambert\_Azimuthal\_Equal\_Area

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization:   
  * Li, X., & Lynch, A. H. (2023). New insights into projected Arctic sea road: Operational risks, economic values, and policy implications. Climatic Change, 176(30). https://doi.org/10.1007/s10584-023-03505-4  
  * Lynch, A. H., Norchi, C. H., & Li, X. (2022). The interaction of ice and law in Arctic marine accessibility. Proceedings of the National Academy of Sciences, 119(26), e2202720119. https://doi.org/10.1073/pnas.2202720119  
  * Li, X., Stephenson, S. R., Lynch, A. H., Goldstein, M. A., Bailey, D. A., & Veland, S. (2021). Arctic shipping guidance from the CMIP6 ensemble on operational and infrastructural timescales. Climatic Change, 167(1), 23\. https://doi.org/10.1007/s10584-021-03172-3  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| route\_SSP370\_high\_emissions.shp | North\_Pole\_Lambert\_Azimuthal\_Equal\_Area | Shapefile | 68,521 | 7 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Year | String |  |
|  |  |  |  |  | Month | String |  |
|  |  |  |  |  | Day | String |  |
|  |  |  |  |  | Model | String |  |

86. # **Marine/SSP585/Routes\_SSP585\_2015\_2065**

**Title:** route\_SSP585\_worst\_case\_emissions  
**Abstract:** This dataset represents daily navigable Arctic marine shipping routes simulated under the SSP585 emissions scenario, derived from CMIP6 model projections of sea ice concentration and thickness. The routes were generated assuming a non-ice-strengthened vessel traveling between Rotterdam and the Bering Strait. Each route is based on sea ice conditions modeled by one of 14 CMIP6 general circulation models (GCMs) and spans multiple years and days. The dataset includes attributes for date and contributing climate model. These routes reflect potential Arctic accessibility patterns under a specific climate future scenario.  
**Purpose:** To evaluate extreme Arctic accessibility in a **worst-case emissions** scenario (SSP5-8.5), marked by fossil-fueled economic growth, minimal climate policy, and rapid sea ice decline.  
**Keywords:** shipping routes, climate model  
**Temporal Extent:**

* **Date**: 2021  
* **Time Period**: 2015-2065

**Geographic Extent:** 

* Bounding Box:   
  * Top	2,635,762.186500	m  
  * Bottom	\-3,321,766.612412	m  
  * Left	\-2,402,954.761900	m  
  * Right	1,986,312.786500	m

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** 

* Projected Coordinate System: North\_Pole\_Lambert\_Azimuthal\_Equal\_Area

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization:  
  * Li, X., & Lynch, A. H. (2023). New insights into projected Arctic sea road: Operational risks, economic values, and policy implications. Climatic Change, 176(30). https://doi.org/10.1007/s10584-023-03505-4  
  * Lynch, A. H., Norchi, C. H., & Li, X. (2022). The interaction of ice and law in Arctic marine accessibility. Proceedings of the National Academy of Sciences, 119(26), e2202720119. https://doi.org/10.1073/pnas.2202720119  
  * Li, X., Stephenson, S. R., Lynch, A. H., Goldstein, M. A., Bailey, D. A., & Veland, S. (2021). Arctic shipping guidance from the CMIP6 ensemble on operational and infrastructural timescales. Climatic Change, 167(1), 23\. https://doi.org/10.1007/s10584-021-03172-3  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| route\_SSP585\_moderate\_emissions.shp | North\_Pole\_Lambert\_Azimuthal\_Equal\_Area | Shapefile | 73,615 | 7 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Year | String |  |
|  |  |  |  |  | Month | String |  |
|  |  |  |  |  | Day | String |  |
|  |  |  |  |  | Model | String |  |

87. # **Political Boundaries Countries**

**Title:** Political\_Boundaries\_Cleaned  
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
| Political\_Boundaries\_Cleaned.shp | WGS 1984 Web Mercator (auxiliary sphere) | Polygon | 35 | 8 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | COUNTRY | String |  |
|  |  |  |  |  | ISO\_CC | String | 3 letter long abbreviation of the countryr |
|  |  |  |  |  | CONTINENT | String |  |
|  |  |  |  |  | LAND\_TYPE | String | Description of country’s main geography (ex: small island, primary land) |
|  |  |  |  |  | Shape\_Leng | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |

88. # **Global Ship Density \- All Vessels**

**Title:** Shipping\_Route\_Density\_Cleaned  
**Abstract:** This dataset provides a comprehensive spatial representation of global maritime activity by quantifying the intensity of vessel traffic across the world's oceans. Each grid cell's value (represented by the gridcode attribute) indicates the total cumulative number of Automatic Identification System (AIS) positions reported by all vessels within that cell. The dataset was generated from an analysis of hourly AIS positions by the International Monetary Fund (IMF) as part of their World Seaborne Trade Monitoring System, with support from the World Bank's ESMAP and PROBLUE programs.  
**Purpose:** To be used in analysis and visualization. This datatset can be used to summarize the total values within a polygon (using zonal statistics) to obtain statistical measures like minimum, maximum, mean, and standard deviation; this could be useful for comparing different areas.  
**Keywords:** trade, transport, transportatio, offshore wind, seaborne trade, shipping density, shipping routes, vessel traffic, AIS, oceans, marine, marine spatial planning, esri\_oceans  
**Temporal Extent:**

* **Date**: Last updated May 3, 2021  
* **Time Period**: January 2015 \- February 2021

**Geographic Extent:** 

* Bounding Box:   
  * Top	85.003744	deg  
  * Bottom	51.255673	deg  
  * Left	\-180.002618	deg  
  * Right	180.001993	deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** 

* Projected Coordinate System: WGS 1984

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

* Organization:  
  * Primary Data Analysis & Provider: International Monetary Fund (IMF), as part of their World Seaborne Trade Monitoring System.  
  * Supporting Programs: World Bank's ESMAP (Energy Sector Management Assistance Program) and PROBLUE programs.  
  * Compiled & Published by: Esri (within the ArcGIS Living Atlas, linked [here](https://www.arcgis.com/home/item.html?id=2f72eb72cc0b403bb19a7cd1853f3d94)).  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Shipping\_Route\_Density\_Cleaned.shp | WGS 1984 | Polygon | 8,726,963 | 5 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | gridcode | Integer | total number of AIS (Automatic Identification System) positions reported by all vessels within that specific grid cell (or pixel |
|  |  |  |  |  | Shape\_Leng | Double |  |
|  |  |  |  |  | Shape\_Area | Double |  |

89. # **Mineral Resources Data System (Mining)**

**Title:** global\_mineral\_resource\_occurrences  
**Abstract:** This dataset consolidates global mineral resource occurrence information, primarily focusing on the United States, by integrating records from the [USGS's Mineral Resource Data System (MRDS)](https://mrdata.usgs.gov/mrds/) and the U.S. Bureau of Mines' (now USGS) Mineral Availability System/Mineral Industry Locator System (MAS/MILS). Developed over decades, the MRDS aimed for complete U.S. coverage, making its international data less comprehensive. Critically, the information's currency is limited to the original source reports, some of which are no longer available, meaning operational statuses, ownership, production figures, and resource estimates are likely outdated; however, geological characteristics of the mineral resources generally remain accurate.  
**Purpose:** This digest of the complex mineral resources database is intended for use as reference material supporting mineral resource and environmental assessments on local to regional scale worldwide.  
**Keywords:** mine site, mineral deposit areas, mineral resources  
**Temporal Extent:**

* **Date**: 3/15/2016  
* **Time Period**: 

**Geographic Extent:** 

* Bounding Box:   
  * Top	85.003744	deg  
  * Bottom	51.255673	deg  
  * Left	\-180.002618	deg  
  * Right	180.001993	deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** 

* Projected Coordinate System: WGS 1984

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: All features have values for each of the attributes.  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: none  
* Use Constraints: Haddaway, N.R., Smith, A., Taylor, J.J., Andrews, C., Cooke, S.J., Nilsson, A.E. and Lesser, P., 2022\. Evidence of the impacts of metal mining and the effectiveness of mining mitigation measures on social–ecological systems in Arctic and boreal regions: a systematic map. Environmental Evidence, 11(1), 30

**Metadata Contact:**

* Organization: USGS Geology, Energy, and Minerals Science Center  
* Position: Peter N Schweitzer, Geologist  
* Email: pschweitzer@usgs.gov

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| global\_mineral\_resource\_occurrences.shp | WGS 1984 | Point | 13,141 | 5 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | SITE\_NAME | String | Name of the site, deposit, or operation. |
|  |  |  |  |  | DEV\_STAT | String | Status of development of the resource or operation. |
|  |  |  |  |  | CODE\_LIST | String |  |

90. # **Human Activities**

**Title:** clean\_human\_activities  
**Abstract:**   
**Purpose:**   
**Keywords:**   
**Temporal Extent:**

* **Date**:   
* **Time Period**: 

**Geographic Extent:** 

* Bounding Box:   
  * Top	89.949633	deg  
  * Bottom	51.554943	deg  
  * Left	\-179.452701	deg  
  * Right	179.348539	deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** 

* Projected Coordinate System: WGS 1984

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

* Organization: Abbie Tingstad  
  * Chapter 11 of the CPAD book  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| clean\_human\_activities.shp | WGS 1984 | Point | 1,033 | 22 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Original\_n | String |  |
|  |  |  |  |  | Country | String |  |
|  |  |  |  |  | Name\_1 | String |  |
|  |  |  |  |  | Name\_2 | String |  |
|  |  |  |  |  | Name\_3 | String |  |
|  |  |  |  |  | Name\_4 | String |  |
|  |  |  |  |  | Name\_5 | String |  |
|  |  |  |  |  | Name\_6 | String |  |
|  |  |  |  |  | Name\_7 | String |  |
|  |  |  |  |  | Name\_8 | String |  |
|  |  |  |  |  | latitude | Double |  |
|  |  |  |  |  | longitude | Double |  |
|  |  |  |  |  | City\_town\_ | Double |  |
|  |  |  |  |  | Indigenous | Double |  |
|  |  |  |  |  | Resources | Double |  |
|  |  |  |  |  | Mobility | Double |  |
|  |  |  |  |  | Military\_l | Double |  |
|  |  |  |  |  | Natural\_ar | Double |  |
|  |  |  |  |  | Significan | Double |  |
|  |  |  |  |  | Name\_sourc | String |  |

91. # **Arctic Ocean Average Monthly Sea Ice Area**

**Title:** arctic\_sea\_ice\_time\_series  
**Abstract:** This dataset contains average monthly sea ice area for 1978 to present (2025), in square kilometers, by region of the Arctic Ocean. The Arctic is broken up into 14 regions with boundaries defined by the ASINA team using Meier et al. (2007): Baffin Bay, Barents Sea, Beaufort Sea, Bering Sea, Canadian Archipelago, Central Arctic Ocean, Chukchi Sea, East Siberian Sea, Greenland Sea, Hudson Bay, Kara Sea, Laptev Sea, Sea of Okhotsk, and Gulf of St. Lawrence. The data is sourced from the [NSIDC Sea Ice Index](https://nsidc.org/data/seaice_index), which uses passive microwave remote sensing from the DMSP and JAXA Advanced Microwave Scanning Radiometer 2 (AMSR2) satellites.  
**Purpose:** This dataset provides a long-term, consistent record of average monthly sea ice area in specific regions of the Arctic. It allows for the analysis and tracking of changes in Arctic sea ice over time, which is critical for climate research, environmental monitoring, and understanding the impacts of climate change.  
**Keywords:**   
**Temporal Extent:**

* **Date**:   
* **Time Period**: 1978-2025

**Geographic Extent:** 

* Bounding Box:   
  * Top	89.836816	deg  
  * Bottom	39.169437	deg  
  * Left	\-180.000000	deg  
  * Right	179.763242	deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** 

* Projected Coordinate System: WGS 1984

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: Values for 10 months in 1978 and 11 months in 2025 are missing.  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: Fetterer, F., Knowles, K., Meier, W. N., Savoie, M., Windnagel, A. K. & Stafford, T. (2025). Sea Ice Index. (G02135, Version 4). \[Data Set\]. Boulder, Colorado USA. National Snow and Ice Data Center. https://doi.org/10.7265/a98x-0f50. \[describe subset used if applicable\]. Date Accessed 08-13-2025.

**Metadata Contact:**

* Organization: [National Snow and Ice Data Center](https://nsidc.org/sea-ice-today/sea-ice-tools)  
* Position: NSIDC User Services  
* Email: [nsidc@nsidc.org](mailto:nsidc@nsidc.org) 

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| arctic\_sea\_ice\_time\_series.shp | WGS 1984 | Point | 14 | 579 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | region\_nam | String | 1/14 Arctic regions:  Baffin Bay, Barents Sea, Beaufort Sea, Bering Sea, Canadian Archipelago, Central Arctic Ocean, Chukchi Sea, East Siberian Sea, Greenland Sea, Hudson Bay, Kara Sea, Laptev Sea, Sea of Okhotsk, Gulf of St. Lawrence |
|  |  |  |  |  | Jan\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Feb\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Mar\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Apr\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | May\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Jun\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Jul\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Aug\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Sep\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Oct\_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Nov\_1978 | Double |  |
|  |  |  |  |  | Dec\_1978 | Double |  |
|  |  |  |  |  | Jan\_1979 | Double |  |
|  |  |  |  |  | Feb\_1979 | Double |  |
|  |  |  |  |  | Mar\_1979 | Double |  |
|  |  |  |  |  | Apr\_1979 | Double |  |
|  |  |  |  |  | May\_1979 | Double |  |
|  |  |  |  |  | Jun\_1979 | Double |  |
|  |  |  |  |  | Jul\_1979 | Double |  |
|  |  |  |  |  | Aug\_1979 | Double |  |
|  |  |  |  |  | Sep\_1979 | Double |  |
|  |  |  |  |  | Oct\_1979 | Double |  |
|  |  |  |  |  | Nov\_1979 | Double |  |
|  |  |  |  |  | Dec\_1979 | Double |  |
|  |  |  |  |  | ... | Double |  |
|  |  |  |  |  | Jan\_2025 | Double |  |
|  |  |  |  |  | Feb\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Mar\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Apr\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | May\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Jun\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Jul\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Aug\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Sep\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Oct\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Nov\_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Dec\_2025 | String | Data unavailable for this month and year |

