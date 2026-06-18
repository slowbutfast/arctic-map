#!/usr/bin/env python3
"""
process_metadata.py - Clean, match, filter, and split Arctic Map metadata for Dify RAG indexing.

Reads:
  - CPAD Datasets Theme & Subtheme Organization V2 - CPAD WebGIS App.csv  (83 active layers)
  - Meta Data based on ISO 19115 Standards.md                         (91 records)
  - active_layers_production.txt                                      (reference hierarchy)

Generates:
  - map-docs/cleaned_metadata/<layer_name>.md  for each of 83 active layers
  - map-docs/cleaned_metadata/_index.md        master directory
"""

import csv
import os
import re
import sys

MAP_DOCS_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(MAP_DOCS_DIR, "cleaned_metadata")
CSV_PATH = os.path.join(MAP_DOCS_DIR, "CPAD Datasets Theme & Subtheme Organization V2 - CPAD WebGIS App.csv")
MD_PATH = os.path.join(MAP_DOCS_DIR, "Meta Data based on ISO 19115 Standards.md")


# =============================================================================
# 1. Parse CSV
# =============================================================================
def parse_csv(path):
    rows = []
    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            theme = row["theme"].strip()
            subtheme = row["subtheme"].strip()
            layer_name = row["layer_name"].strip()
            display_name = row["display_name"].strip()
            rows.append({"theme": theme, "subtheme": subtheme, "layer_name": layer_name, "display_name": display_name})
    print(f"[CSV] Loaded {len(rows)} active layers")
    return rows


# =============================================================================
# 2. Parse MD file – split into individual records, keyed by Title
# =============================================================================
def parse_md(path):
    """Return dict: normalized_title -> {title, raw_text}"""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split on section headers like "# 1. # **Something**" or "# 1. # Something"
    pattern = r'^#\s+\d+\.\s+#\s+\*{0,2}(.+?)\*{0,2}\s*$'
    sections = re.split(pattern, text, flags=re.MULTILINE)

    records = {}
    # sections[0] is preamble (before first match)
    # then alternating: title, body
    for i in range(1, len(sections), 2):
        if i + 1 >= len(sections):
            break
        raw_title = sections[i].strip()
        body = sections[i + 1].strip()
        # Extract the **Title:** from the body for reliable matching
        title_match = re.search(r'\*\*Title:\*\*\s*(.+?)(?:\n|$)', body)
        md_title = title_match.group(1).strip() if title_match else raw_title

        records[md_title] = {"raw_title": raw_title, "md_title": md_title, "body": body}

    print(f"[MD] Parsed {len(records)} metadata records")
    return records


# =============================================================================
# 3. Manual alias map for mismatched names
# =============================================================================
# Maps CSV layer_name -> MD record title
MANUAL_ALIASES = {
    "a_clean_gl_geonames": "GreenLand Geonames",
    "a_clean_ne_10m_railroads": "Railroads",
    "iceland_poly": "Iceland universities",
    "a_gis_osm_places_a_free_1": "gis_osm_places_a_free_1",
    "clean_human_activities": "clean_human_activities",
    "a_clean_arctic_regions": "Arctic Regions",
    "a_clean_alaskan_airports": "Alaskan Airports",
    "clean_airports_ahdr": "Airports AHDR",
    "a_clean_ports_ahdr": "AHDR_Ports",
    "shipping_route_density_cleaned": "Shipping_Route_Density_Cleaned",
    "political_boundaries_cleaned": "Political_Boundaries_Cleaned",
    "arctic_sea_ice_time_series": "arctic_sea_ice_time_series",
    "global_mineral_resource_occurrences": "global_mineral_resource_occurrences",
}


def find_md_record(layer_name, md_records):
    """Try to find the MD record matching a given layer_name."""
    # Direct alias lookup
    if layer_name in MANUAL_ALIASES:
        alias = MANUAL_ALIASES[layer_name]
        if alias in md_records:
            return md_records[alias]

    # Try matching Title to layer_name
    for rec_title, rec in md_records.items():
        rec_clean = rec_title.lower().replace(" ", "_").replace("-", "_")
        ln_clean = layer_name.lower()
        if rec_clean == ln_clean:
            return rec
        if rec_clean.endswith(ln_clean) or ln_clean.endswith(rec_clean):
            return rec

    # Fuzzy: find any MD record whose title contains significant parts of the layer name
    ln_lower = layer_name.lower()
    for rec_title, rec in md_records.items():
        rl = rec_title.lower()
        # Extract meaningful tokens
        if any(token in rl for token in ln_lower.split("_") if len(token) > 3):
            return rec

    return None


# =============================================================================
# 4. Clean backslash-escaped underscores
# =============================================================================
def clean_escaped_underscores(text):
    return text.replace("\\_", "_")


# =============================================================================
# 5. Build output for a single layer
# =============================================================================
def build_metadata_text(layer_info, md_body):
    """Prepend CSV header fields to the metadata body, with cleaned underscores."""
    theme = layer_info["theme"]
    subtheme = layer_info["subtheme"]
    display_name = layer_info["display_name"]
    layer_name = layer_info["layer_name"]

    header = f"---\nTheme: {theme}\nSubtheme: {subtheme}\nDisplay Name: {display_name}\nLayer Name: {layer_name}\n---\n\n"
    body_clean = clean_escaped_underscores(md_body)
    return header + body_clean


# =============================================================================
# 6. Generate yearly route files (inherit from SSP126 low emissions)
# =============================================================================
YEARLY_ROUTES = [
    ("route_ssp126_2015", "SSP 126 Low Emission Scenario for 2015"),
    ("route_ssp126_2016", "SSP 126 Low Emission Scenario for 2016"),
    ("route_ssp126_2017", "SSP 126 Low Emission Scenario for 2017"),
    ("route_ssp126_2018", "SSP 126 Low Emission Scenario for 2018"),
    ("route_ssp126_2019", "SSP 126 Low Emission Scenario for 2019"),
    ("route_ssp126_2020", "SSP 126 Low Emission Scenario for 2020"),
]


def generate_yearly_routes(parent_body):
    """Generate yearly route metadata files inheriting from SSP126 parent."""
    parent_clean = clean_escaped_underscores(parent_body)
    # Replace title references
    parent_clean = parent_clean.replace("route_SSP126_low_emissions", "route_ssp126_{year}")
    parent_clean = parent_clean.replace("SSP126 Shipping Routes Low Emissions Scenario", "SSP 126 Low Emission Scenario for {year}")
    # Modify abstract to specify year
    lines = parent_clean.split("\n")
    abstract_line = None
    purpose_line = None
    for i, line in enumerate(lines):
        if line.startswith("**Abstract:**") and "2015-2065" in line:
            abstract_line = i
        if line.startswith("**Purpose:**") and "low-emissions" in line.lower():
            purpose_line = i

    results = []
    for layer_name, display_name in YEARLY_ROUTES:
        year = layer_name.split("_")[-1]
        text = parent_clean.replace("{year}", year)
        if abstract_line is not None:
            lines_copy = text.split("\n")
            lines_copy[abstract_line] = lines_copy[abstract_line].replace(
                "2015–2065", year
            ).replace("2015-2065", year)
            text = "\n".join(lines_copy)
        header = (
            f"---\nTheme: Infrastructure\nSubtheme: Shipping Routes\n"
            f"Display Name: {display_name}\nLayer Name: {layer_name}\n---\n\n"
        )
        results.append((layer_name, header + text))
    return results


# =============================================================================
# 7. Generate cpad_arctic_base.md
# =============================================================================
CPAD_ARCTIC_BASE = """---

Theme: Socioeconomic
Subtheme: Administrative & Geographic Boundaries
Display Name: CPAD Arctic Base Boundaries
Layer Name: cpad_arctic_base
---

**Title:** CPAD Arctic Base Boundaries

**Abstract:** This dataset defines the spatial boundary of the Arctic region as used by the Circumpolar Arctic Development (CPAD) Project. It encompasses the geographic area of interest for all CPAD analyses and mapping activities, covering Arctic and sub-Arctic regions across North America, Europe, and Asia. The boundary serves as the fundamental spatial reference for the CPAD project's data collection, analysis, and visualization efforts.

**Purpose:** To provide a standardized project boundary that defines the spatial extent of the CPAD project's area of interest, ensuring consistency across all mapped layers and analyses within the Arctic Map Dataset Explorer.

**Keywords:** CPAD, Arctic boundary, project boundary, Arctic region

**Temporal Extent:**
- **Date:** NA
- **Time Period:** NA

**Geographic Extent:**
- **Bounding Box:**
  - Top: 85.0 deg
  - Bottom: 50.0 deg
  - Left: -180.0 deg
  - Right: 180.0 deg

**Spatial Resolution:** N/A
**Coordinate Reference System:** WGS 1984

**Lineage:** The boundary was defined by the CPAD project team based on the project's scope and research objectives. It incorporates commonly accepted Arctic delimitations including the Arctic Circle (66.5°N) and sub-Arctic transition zones relevant to the project's thematic focus areas.

**Quality Information:**
- **Accuracy:** The boundary represents a generalized project area of interest.
- **Completeness:** The boundary encompasses all regions covered by CPAD's active layers.
- **Consistency:** The boundary is consistently applied across all CPAD project analyses.

**Distribution Information:**
- **Format:** Shapefile
- **Access Constraints:** No constraints
- **Use Constraints:** No constraints

**Metadata Contact:**
- **Organization:** Circumpolar Arctic Development (CPAD) Project
- **Position:** NA
- **Email:** NA
- **Phone:** NA

**Data Dictionary:**
| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :--------- | :---------------- | :----------- | :---------------- | :------------------ | :----------------- | :-------- | :---------- |
| cpad_arctic_base.shp | WGS 1984 | Polygon | 1 | 3 | FID | Object ID | |
| | | | | | Shape | Geometry | |
| | | | | | Name | Text | CPAD Arctic Base Boundary |
"""


# =============================================================================
# 8. Generate _index.md
# =============================================================================
def generate_index(all_layers):
    """Generate master index file grouped by Theme and Subtheme."""
    lines = [
        "# Arctic Map Dataset Explorer - Layer Directory\n",
        "This index organizes all available layers by Theme and Subtheme. Use this file as a directory to discover datasets.\n",
    ]

    # Group by theme then subtheme
    from collections import OrderedDict
    groups = OrderedDict()
    for lyr in all_layers:
        theme = lyr["theme"]
        subtheme = lyr["subtheme"]
        groups.setdefault(theme, OrderedDict())
        groups[theme].setdefault(subtheme, [])
        groups[theme][subtheme].append(lyr)

    for theme, subthemes in groups.items():
        lines.append(f"## {theme}\n")
        for subtheme, layers in subthemes.items():
            lines.append(f"### {subtheme}\n")
            for lyr in layers:
                lines.append(f"- **{lyr['display_name']}** (`{lyr['layer_name']}`)")
            lines.append("")
        lines.append("")

    return "\n".join(lines)


# =============================================================================
# 9. Main
# =============================================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    csv_layers = parse_csv(CSV_PATH)
    md_records = parse_md(MD_PATH)

    # Build a fast lookup: layer_name -> csv row
    csv_by_name = {r["layer_name"]: r for r in csv_layers}

    # Track stats
    matched = 0
    unmatched_csv = []
    generated_yearly = []
    generated_cpad = False
    written_files = []

    # Find SSP126 parent record for yearly route generation
    ssp126_parent = None
    for rec_title, rec in md_records.items():
        if "SSP126" in rec_title or "low_emissions" in rec_title:
            ssp126_parent = rec["body"]
            break
    if not ssp126_parent:
        # Fallback: search in body texts
        for rec_title, rec in md_records.items():
            if "route_SSP126_low_emissions" in rec["body"]:
                ssp126_parent = rec["body"]
                break

    for lyr in csv_layers:
        ln = lyr["layer_name"]

        # Yearly routes
        if ln.startswith("route_ssp126_") and ln != "route_SSP126_low_emissions":
            if ssp126_parent:
                yearly_results = generate_yearly_routes(ssp126_parent)
                for yln, ytext in yearly_results:
                    if yln == ln:
                        fpath = os.path.join(OUTPUT_DIR, f"{yln}.md")
                        with open(fpath, "w", encoding="utf-8") as f:
                            f.write(ytext)
                        written_files.append(yln)
                        generated_yearly.append(yln)
                        print(f"  [YEARLY] Generated {yln}.md")
                continue
            else:
                print(f"  [WARN] No SSP126 parent found for {ln}, skipping")
                continue

        # CPAD Arctic Base
        if ln == "cpad_arctic_base":
            fpath = os.path.join(OUTPUT_DIR, f"{ln}.md")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(CPAD_ARCTIC_BASE)
            written_files.append(ln)
            generated_cpad = True
            print(f"  [CPAD] Generated {ln}.md")
            continue

        # Normal matching
        rec = find_md_record(ln, md_records)
        if rec:
            text = build_metadata_text(lyr, rec["body"])
            fpath = os.path.join(OUTPUT_DIR, f"{ln}.md")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(text)
            written_files.append(ln)
            matched += 1
            print(f"  [MATCH] {ln}.md <- '{rec['md_title']}'")
        else:
            unmatched_csv.append(ln)
            print(f"  [UNMATCHED] {ln}")

    # Generate _index.md
    index_text = generate_index(csv_layers)
    index_path = os.path.join(OUTPUT_DIR, "_index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_text)
    written_files.append("_index.md")

    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"  CSV active layers:       {len(csv_layers)}")
    print(f"  MD records parsed:       {len(md_records)}")
    print(f"  Matched via MD:          {matched}")
    print(f"  Yearly routes generated: {len(generated_yearly)}")
    print(f"  CPAD generated:          {generated_cpad}")
    print(f"  Total files written:     {len(written_files)} (incl. _index.md)")
    if unmatched_csv:
        print(f"  UNMATCHED CSV entries:   {len(unmatched_csv)}")
        for u in unmatched_csv:
            print(f"    - {u}")
    print(f"\nOutput directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()