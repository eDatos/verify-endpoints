from istacpy.indicators.lite import indicators


def verify_indicators():
    all_indicators = indicators.get_indicators()
    for indicator_code, _ in all_indicators:
        indicator = indicators.get_indicator(indicator_code)
        try:
            indicator.get_data()
        except Exception as err:
            print(f'{indicator_code} is not available ({err})')
            break


if __name__ == "__main__":
    verify_indicators()
