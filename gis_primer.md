# GIS File Formats Primer

This document serves as an educational resource and reference for the primary geospatial data formats used in web GIS and the Arctic Map application.

## GIS File Formats

- **GeoJSON** — Standardized in [RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946) [1]. A JSON-based format representing geographical features, their properties, and spatial boundaries. JSON structure: `{ "type":"FeatureCollection", "features":[...] }`, where each feature contains a `geometry` object (type + nested coordinate arrays) and `properties` (metadata/attributes). "Resolution" is determined by coordinate density (e.g., 50k vs. 500 points per coastline—visually similar at overview, but with a ~100x difference in file size).
- **Shapefile** (`.shp/.shx/.dbf/.prj`, usually zipped) — Legacy binary vector format developed by ESRI, described in the [ESRI Shapefile Technical Description](https://www.loc.gov/preservation/digital/formats/fdd/fdd000280.shtml) [2] (Library of Congress reference). It comprises multiple files containing geometry, spatial index, attribute data, and coordinate system projection information. Served by `zip_shapefiles.py` / `zip_downloads.py`.
- **GeoPackage (.gpkg) / SQLite** — An open, standards-based, platform-independent, portable, self-describing, compact format defined by the [Open Geospatial Consortium (OGC)](https://www.geopackage.org/) [3]. It is implemented as an SQLite database container holding vector feature layers, tile matrix sets of imagery, and metadata. `cpad.sqlite` in the project is intended to be a GeoPackage database.
- **GeoTIFF / raster** — Standard TIFF image files with embedded spatial metadata (georeferencing) describing pixel grids (e.g., `topograp_e` 1km elevation). Modern cloud architectures leverage the [OGC Cloud Optimized GeoTIFF (COG) specification](https://docs.ogc.org/is/21-026/21-026.html) [4] for HTTP range requests. Not currently in the local cache; handled via a separate raster path.
- **Vector Tiles (.mvt/.pbf / .mbtiles)** — Pre-chopped, zoom-leveled binary tiles containing vector data clipped to tile boundaries, conforming to the [Mapbox Vector Tile Specification](https://github.com/mapbox/vector-tile-spec) [5]. MBTiles is a SQLite-based specification for storing these tiles. Typically built from GeoJSON/GeoPackage via tools like [Tippecanoe](https://github.com/felt/tippecanoe) [6]. This is the primary "webtiles" path.
- **Raster Webtiles (XYZ PNG)** — A Tile Map Service (TMS) or XYZ `{z}/{x}/{y}.png` scheme serving pre-rendered pixel tiles for raster layers, mapped using the Mapbox `type: "raster"` source.

## References

1. **GeoJSON Format Specification (RFC 7946)**: [RFC 7946 - The GeoJSON Format](https://datatracker.ietf.org/doc/html/rfc7946)
2. **ESRI Shapefile Format**: [Library of Congress - ESRI Shapefile Format description](https://www.loc.gov/preservation/digital/formats/fdd/fdd000280.shtml)
3. **OGC GeoPackage Standard**: [OGC GeoPackage Encoding Standard](https://www.geopackage.org/)
4. **OGC Cloud Optimized GeoTIFF (COG) Standard**: [OGC COG Standard Specification](https://docs.ogc.org/is/21-026/21-026.html)
5. **Mapbox Vector Tile Specification**: [Mapbox Vector Tile Spec on GitHub](https://github.com/mapbox/vector-tile-spec)
6. **Tippecanoe Tool**: [Felt Tippecanoe GitHub Repository](https://github.com/felt/tippecanoe)
