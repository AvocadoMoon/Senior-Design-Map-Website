var wms_layers = [];


        var lyr_OpenStreetMap_0 = new ol.layer.Tile({
            'title': 'OpenStreetMap',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: ' ',
                url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
            })
        });
var format_converted_shape_1 = new ol.format.GeoJSON();
var features_converted_shape_1 = format_converted_shape_1.readFeatures(json_converted_shape_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_converted_shape_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_converted_shape_1.addFeatures(features_converted_shape_1);
var lyr_converted_shape_1 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_converted_shape_1, 
                style: style_converted_shape_1,
                interactive: true,
    title: 'converted_shape<br />\
    <img src="styles/legend/converted_shape_1_0.png" /> Full-Service Restaurants<br />\
    <img src="styles/legend/converted_shape_1_1.png" /> Limited-Service Restaurants<br />\
    <img src="styles/legend/converted_shape_1_2.png" /> Snack and Nonalcoholic Beverage Bars<br />\
    <img src="styles/legend/converted_shape_1_3.png" /> <br />'
        });

lyr_OpenStreetMap_0.setVisible(true);lyr_converted_shape_1.setVisible(true);
var layersList = [lyr_OpenStreetMap_0,lyr_converted_shape_1];
lyr_converted_shape_1.set('fieldAliases', {'field_1': 'field_1', 'Unnamed_ 0': 'Unnamed_ 0', 'utc_timest': 'utc_timest', 'local_time': 'local_time', 'caid': 'caid', 'id_type': 'id_type', 'location_n': 'location_n', 'top_catego': 'top_catego', 'sub_catego': 'sub_catego', 'street_add': 'street_add', 'city': 'city', 'state': 'state', 'naics_code': 'naics_code', 'brands': 'brands', 'zip_code': 'zip_code', 'minimum_dw': 'minimum_dw', 'safegraph_': 'safegraph_', 'geohash_5': 'geohash_5', 'census_blo': 'census_blo', 'placekey': 'placekey', 'latitude': 'latitude', 'longitude': 'longitude', 'utc_dateti': 'utc_dateti', 'local_date': 'local_date', });
lyr_converted_shape_1.set('fieldImages', {'field_1': 'Hidden', 'Unnamed_ 0': 'Hidden', 'utc_timest': 'Hidden', 'local_time': 'Hidden', 'caid': 'Hidden', 'id_type': 'Hidden', 'location_n': 'TextEdit', 'top_catego': 'TextEdit', 'sub_catego': 'TextEdit', 'street_add': 'TextEdit', 'city': 'TextEdit', 'state': 'TextEdit', 'naics_code': 'Hidden', 'brands': 'Hidden', 'zip_code': 'TextEdit', 'minimum_dw': 'Hidden', 'safegraph_': 'Hidden', 'geohash_5': 'Hidden', 'census_blo': 'Hidden', 'placekey': 'Hidden', 'latitude': 'TextEdit', 'longitude': 'TextEdit', 'utc_dateti': 'TextEdit', 'local_date': 'TextEdit', });
lyr_converted_shape_1.set('fieldLabels', {'location_n': 'inline label', 'top_catego': 'inline label', 'sub_catego': 'inline label', 'street_add': 'inline label', 'city': 'inline label', 'state': 'inline label', 'zip_code': 'inline label', 'latitude': 'inline label', 'longitude': 'inline label', 'utc_dateti': 'inline label', 'local_date': 'inline label', });
lyr_converted_shape_1.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});