from istacpy.indicators import systems

ENTRYPOINTS_TESTING_CALLS = (
    (systems.get_indicators_systems, {}),
    (systems.get_indicators_systems_code, dict(indicatorsystemcode='C00075H')),
)
