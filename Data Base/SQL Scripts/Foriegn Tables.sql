CREATE EXTENSION IF NOT EXISTS file_fdw;

CREATE SERVER IF NOT EXISTS veraset_data FOREIGN DATA WRAPPER file_fdw;

CREATE SCHEMA IF NOT EXISTS "map-data"
    AUTHORIZATION db_user;

GRANT USAGE ON SCHEMA "map-data" TO read_sdp;

GRANT ALL ON SCHEMA "map-data" TO postgres;


CREATE FOREIGN TABLE IF NOT EXISTS "map-data"."all-data"(
    csv_index int,
    utc_timestamp text,
    local_timestamp text,
    caid text,
    id_type text,
    location_name text,
    top_category text,
    sub_category text,
    street_address text,
    city text,
    states text,
    naics_code bigint,
    brands text,
    zip_code text,
    minimum_dwell decimal,
    safegraph_place_id text,
    geohash_5 text,
    census_block_group text,
    placekey text
) SERVER veraset_data
OPTIONS (filename 'D:\Home\School\CS\3 Concentration and High Level Courses\CS Senior Design\Senior-Design-Map-Website\testCSV.csv', format 'csv', header 'true')