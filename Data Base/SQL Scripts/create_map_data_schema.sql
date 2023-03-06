-- Need to add authorization levels

CREATE SCHEMA IF NOT EXISTS "map-data"
    AUTHORIZATION postgres;

GRANT USAGE ON SCHEMA "Map Data" TO pg_read_all_data;

GRANT ALL ON SCHEMA "Map Data" TO postgres;

CREATE TABLE IF NOT EXISTS "map-data"."time-stamps"
(
    utc_timestamp timestamp without time zone,
    caid "char"[],
    
    minimum_dwell bigint,
    local_timestamp timestamp without time zone
);

CREATE TABLE IF NOT EXISTS "map-data"."device-info"(
    caid "char"[],
    utc_timestamp timestamp without time zone,

    id_type "char"[],
    brands "char"[]
);

CREATE TABLE IF NOT EXISTS "map-data"."zone-location"(
    utc_timestamp timestamp without time zone,
    caid "char"[],

    top_category "char"[],
    sub_category "char"[],
    safegraph_place_id "char"[],
    location_name "char"[],
    geohash_5 "char"[],
    naics_code bigint,
    census_block_group "char"[],
    placekey_id "char"[]
);

CREATE TABLE IF NOT EXISTS "map-data"."address-location"(
    utc_timestamp timestamp without time zone,
    caid "char"[],

    street_address "char"[],
    city "char"[],
    state "char"[],
    zip_code "char"[]
);


GRANT SELECT ON TABLE "map-data"."time-stamps", "map-data"."device-info", "map-data"."location" TO "map-data-reader";

ALTER TABLE IF EXISTS "map-data"."time-stamps"
    OWNER to postgres;
	
ALTER TABLE IF EXISTS "map-data"."device-info"
    OWNER to postgres;

ALTER TABLE IF EXISTS "map-data"."location"
    OWNER to postgres;
