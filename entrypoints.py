from istacpy.indicators import systems, geographic
from istacpy.statisticalresources import cubes
from istacpy.structuralresources import (
    category as cat,
    classifications as cla,
    concepts as con,
    datastructures as ds,
    variables as var,
)

ENTRYPOINTS_TESTING_CALLS = (
    # ============================================================
    (systems.get_indicators_systems, dict()),
    (systems.get_indicators_systems_code, dict(indicatorsystemcode='C00075H')),
    (
        systems.get_indicators_systems_code_instances,
        dict(
            indicatorsystemcode='C00075H',
            q='id EQ "INDICADORES_MUNICIPALES"',
            order='id ASC',
            fields='+data',
            representation='GEOGRAPHICAL[35003|35005], MEASURE[ABSOLUTE]',
        ),
    ),
    (
        systems.get_indicators_systems_code_instances_code,
        dict(
            indicatorsystemcode='C00075H',
            indicatorinstancecode='21af0477-d63b-493b-ad02-4ab181547223',
        ),
    ),
    (
        systems.get_indicators_systems_code_instances_code_data,
        dict(
            indicatorsystemcode='C00075H',
            indicatorinstancecode='21af0477-d63b-493b-ad02-4ab181547223',
        ),
    ),
    # ============================================================
    (geographic.get_indicators_geographic_granularities, dict()),
    (
        geographic.get_indicators_geographical_values,
        dict(geographicalgranularitycode='REGIONS', subjectcode='061'),
    ),
    (geographic.get_indicators_subjects, dict()),
    (geographic.get_indicators_time_granularities, dict()),
    # ============================================================
    (
        cubes.get_statisticalresources_datasets,
        dict(orderby='id ASC', query='name ILIKE "PASAJEROS"'),
    ),
    (
        cubes.get_statisticalresources_datasets_agency,
        dict(agencyid='ISTAC', orderby='id ASC', query='name ILIKE "PASAJEROS"'),
    ),
    (
        cubes.get_statisticalresources_datasets_agency_resource,
        dict(
            agencyid='ISTAC',
            resourceid='C00017A_000001',
            orderby='id ASC',
            query='name ILIKE "PASAJEROS"',
        ),
    ),
    (
        cubes.get_statisticalresources_datasets_agency_resource_version,
        dict(
            agencyid='ISTAC',
            resourceid='C00017A_000001',
            version='2.2',
            dim='TIME_PERIOD:2010',
            fields='-metadata',
        ),
    ),
    # ============================================================
    (
        cat.get_structuralresources_categorisations,
        dict(query='name LIKE "CAT"', orderby='id ASC'),
    ),
    (
        cat.get_structuralresources_categorisations_agency,
        dict(agencyid='ISTAC', query='name LIKE "CAT"', orderby='id ASC'),
    ),
    (
        cat.get_structuralresources_categorisations_agency_resource,
        dict(
            agencyid='ISTAC', resourceid='cat2', query='name LIKE "CAT"', orderby='id ASC'
        ),
    ),
    (
        cat.get_structuralresources_categorisations_agency_resource_version,
        dict(agencyid='ISTAC', resourceid='cat2', version='01.000'),
    ),
    (
        cat.get_structuralresources_category_schemes,
        dict(query='name ILIKE "OPERACIONES"', orderby='id ASC'),
    ),
    (
        cat.get_structuralresources_category_schemes_agency,
        dict(agencyid='ISTAC', query='name ILIKE "OPERACIONES"', orderby='id ASC'),
    ),
    (
        cat.get_structuralresources_category_schemes_agency_resource,
        dict(
            agencyid='ISTAC',
            resourceid='TEMAS_CANARIAS',
            query='name ILIKE "OPERACIONES"',
            orderby='id ASC',
        ),
    ),
    (
        cat.get_structuralresources_category_schemes_agency_resource_version,
        dict(agencyid='ISTAC', resourceid='TEMAS_CANARIAS', version='01.000'),
    ),
    (
        cat.get_structuralresources_category_schemes_agency_resource_version_categories,
        dict(
            agencyid='ISTAC',
            resourceid='TEMAS_CANARIAS',
            version='01.000',
            query='name ILIKE "COMERCIO"',
            orderby='id ASC',
        ),
    ),
    (
        cat.get_structuralresources_category_schemes_agency_resource_version_categories_id,
        dict(
            agencyid='ISTAC',
            resourceid='TEMAS_CANARIAS',
            version='01.000',
            categoryid='060',
        ),
    ),
    # ============================================================
    (
        cla.get_structuralresources_codelist_families,
        dict(orderby='id ASC', query='id EQ 2090'),
    ),
    (cla.get_structuralresources_codelist_families_id, dict(id='CODELIST_ID')),
    (
        cla.get_structuralresources_codelists,
        dict(query='name ILIKE "AEROPUERTOS"', orderby='id ASC'),
    ),
    (
        cla.get_structuralresources_codelists_agency,
        dict(agencyid='ISTAC', query='name ILIKE "AEROPUERTOS"', orderby='id ASC'),
    ),
    (
        cla.get_structuralresources_codelists_agency_resource,
        dict(
            agencyid='ISTAC',
            resourceid='CL_AEROPUERTOS',
            query='name ILIKE "AEROPUERTOS"',
            orderby='id ASC',
        ),
    ),
    (
        cla.get_structuralresources_codelists_agency_resource_version,
        dict(agencyid='ISTAC', resourceid='CL_AEROPUERTOS', version='01.002'),
    ),
    (
        cla.get_structuralresources_codelists_agency_resource_version_codes,
        dict(
            agencyid='ISTAC',
            resourceid='CL_AEROPUERTOS',
            version='01.002',
            query='name ILIKE "AEROPUERTOS"',
            orderby='id ASC',
            fields='+open',
        ),
    ),
    (
        cla.get_structuralresources_codelists_agency_resource_version_codes_codeid,
        dict(
            agencyid='ISTAC',
            resourceid='CL_AEROPUERTOS',
            version='01.002',
            codeid='ES_GCFV',
        ),
    ),
    # ============================================================
    (con.get_structuralresources_concept_types, dict()),
    (
        con.get_structuralresources_concept_schemes,
        dict(query='name ILIKE "TRANSPORTE"', orderby='id ASC'),
    ),
    (
        con.get_structuralresources_concept_schemes_agency,
        dict(agencyid='ISTAC', query='name ILIKE "TRANSPORTE"', orderby='id ASC'),
    ),
    (
        con.get_structuralresources_concept_schemes_agency_resource,
        dict(
            agencyid='ISTAC',
            resourceid='CSM_C00017A',
            query='name ILIKE "TRANSPORTE"',
            orderby='id ASC',
        ),
    ),
    (
        con.get_structuralresources_concept_schemes_agency_resource_version,
        dict(
            agencyid='ISTAC',
            resourceid='CSM_C00017A',
            version='01.000',
        ),
    ),
    (
        con.get_structuralresources_concept_schemes_agency_resource_version_concepts,
        dict(
            agencyid='ISTAC',
            resourceid='CSM_C00010A_SIE',
            version='01.000',
            query='name ILIKE "TASA"',
            orderby='id ASC',
            fields='+description',
        ),
    ),
    (
        con.get_structuralresources_concept_schemes_agency_resource_version_concepts_id,
        dict(
            agencyid='ISTAC',
            resourceid='CSM_C00010A_SIE',
            version='01.000',
            conceptid='ELECTORES',
        ),
    ),
    # ============================================================
    (
        ds.get_structuralresources_content_constraints,
        dict(query='name ILIKE "AFILIACIONES"', orderby='id ASC'),
    ),
    (
        ds.get_structuralresources_content_constraints_agency,
        dict(agencyid='ISTAC', query='name ILIKE "AFILIACIONES"', orderby='id ASC'),
    ),
    (
        ds.get_structuralresources_content_constraints_agency_resource,
        dict(
            agencyid='ISTAC',
            resourceid='CSM_C00010A_SIE',
            query='name ILIKE "AFILIACIONES"',
            orderby='id ASC',
        ),
    ),
    (
        ds.get_structuralresources_content_constraints_agency_resource_version,
        dict(agencyid='ISTAC', resourceid='CSM_C00010A_SIE', version='01.000'),
    ),
    (
        ds.get_structuralresources_content_constraints_agency_resource_version_regions,
        dict(
            regioncode='0001',
            agencyid='ISTAC',
            resourceid='CSM_C00010A_SIE',
            version='01.000',
        ),
    ),
    (
        ds.get_structuralresources_data_structures,
        dict(query='name ILIKE "ELECCIONES"', orderby='id ASC'),
    ),
    (
        ds.get_structuralresources_data_structures_agency,
        dict(agencyid='ISTAC', query='name ILIKE "ELECCIONES"', orderby='id ASC'),
    ),
    (
        ds.get_structuralresources_data_structures_agency_resource,
        dict(
            agencyid='ISTAC',
            resourceid='DSD_C00010A_00001',
            query='name ILIKE "ELECCIONES"',
            orderby='id ASC',
        ),
    ),
    (
        ds.get_structuralresources_data_structures_agency_resource_version,
        dict(agencyid='ISTAC', resourceid='DSD_C00010A_00001', version='01.001'),
    ),
    # ============================================================
    (
        var.get_structuralresources_variable_families,
        dict(query='name ILIKE "SALUD"', orderby='id ASC'),
    ),
    (var.get_structuralresources_variable_families_id, dict(id='VRF_DEMOGRAFICAS')),
    (
        var.get_structuralresources_variable_families_id_variables,
        dict(id='VRF_DEMOGRAFICAS', query='name ILIKE "EDAD"', orderby='id ASC'),
    ),
    (
        var.get_structuralresources_variables,
        dict(query='name ILIKE "IDIOMA"', orderby='id ASC'),
    ),
    (var.get_structuralresources_variables_id, dict(id='VR_IDIOMA')),
    (
        var.get_structuralresources_variableelements,
        dict(variableid='VR_SEXO', query='name ILIKE "MUJER"', orderby='id ASC'),
    ),
    (
        var.get_structuralresources_variableelements_resource,
        dict(variableid='VR_SEXO', resourceid='FEMALE'),
    ),
    (
        var.get_structuralresources_geoinfo,
        dict(
            variableid='VR_TERRITORIO',
            resourceid='MUN_ICOD_VINOS',
            fields='-geometry',
            orderby='id ASC',
        ),
    ),
)
