from istacpy.indicators.lite import indicators

from entrypoints import ENTRYPOINTS_TESTING_CALLS


def verify_indicators():
    '''Verify all available indicator codes using the istacpy lite module'''
    failing_entrypoints = []
    all_indicators = indicators.get_indicators()
    for indicator_code, _ in all_indicators:
        try:
            indicator = indicators.get_indicator(indicator_code)
            indicator.get_data()
        except Exception:
            failing_entrypoints.append(
                indicator.api_response.get('selfLink', indicator_code)
            )
    return failing_entrypoints


def verify_entrypoints():
    '''Verify a bunch of entrypoints using different arguments on each call'''
    failing_entrypoints = []
    for item in ENTRYPOINTS_TESTING_CALLS:
        f = item[0]
        args = item[1]
        try:
            f(**args)
        except Exception as err:
            failing_entrypoints.append(err.requested_url)
    return failing_entrypoints
