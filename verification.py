from istacpy.indicators.lite import indicators

from entrypoints import ENTRYPOINTS_TESTING_CALLS


def verify_indicators():
    failing_entrypoints = []
    all_indicators = indicators.get_indicators()
    for indicator_code, _ in all_indicators:
        indicator = indicators.get_indicator(indicator_code)
        try:
            indicator.get_data()
        except Exception:
            failing_entrypoints.append(
                indicator.api_response.get('selfLink', indicator_code)
            )
    return failing_entrypoints


def verify_entrypoints():
    failing_entrypoints = []
    for item in ENTRYPOINTS_TESTING_CALLS:
        f = item[0]
        args = item[1]
        response = f(**args)
        if response is None:
            failing_entrypoints.append(response.get('selfLink', response['code']))
    return failing_entrypoints
