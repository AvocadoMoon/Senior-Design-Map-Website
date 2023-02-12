-- Need to add authorization levels

CREATE SCHEMA IF NOT EXISTS "map-data"
    AUTHORIZATION postgres;

GRANT USAGE ON SCHEMA "Map Data" TO pg_read_all_data;

GRANT ALL ON SCHEMA "Map Data" TO postgres;

CREATE TABLE IF NOT EXISTS "map-data"."time-stamps"
(
    utc_timestamp timestamp without time zone,
    local_timestamp timestamp without time zone
);

CREATE TABLE IF NOT EXISTS "map-data"."device-info"(
    caid "char"[],
    id_type "char"[],
    brands "char"[]
);

CREATE TABLE IF NOT EXISTS "map-data"."location"(
    location_name "char"[],
    naics_code bigint,
    top_category "char"[],
    sub_category "char"[],
    street_address "char"[],
    city "char"[],
    state "char"[],
    zip_code "char"[],
    minimum_dwell bigint,
    safegraph_place_id "char"[],
    geohash_5 "char"[],
    census_block_group "char"[],
    placekey_id "char"[]
);


GRANT SELECT ON TABLE "map-data"."time-stamps", "map-data"."device-info", "map-data"."location" TO "map-data-reader";

ALTER TABLE IF EXISTS "map-data"."time-stamps"
    OWNER to postgres;
	
ALTER TABLE IF EXISTS "map-data"."device-info"
    OWNER to postgres;

ALTER TABLE IF EXISTS "map-data"."location"
    OWNER to postgres;
