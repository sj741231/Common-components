# -*-coding=utf8-*-

import datetime
import time
import pytz


def get_local_timezone():
    """
    Get Local timezone name
    :return:
    """
    return time.strftime('%Z', time.localtime())


def get_datetime_timezone(interval_hours=None):
    """
    Get timezone from datetime.timezone
    :param interval_hours: Hours, example: CTS(Asia/Shanghai) +8
    :return: timezone object of UTC or specified timezone
    """
    if isinstance(interval_hours, int):
        return datetime.timezone(datetime.timedelta(hours=interval_hours))
    else:
        return datetime.timezone.utc


def get_pytz_timezone(timezone=None):
    """
    Get timezone object
    :param timezone: The string of timezone, example: Asia/Shanghai
    :return: timezone object of UTC or specified timezone
    """
    if timezone:
        return pytz.timezone(timezone)
    else:
        return pytz.timezone('UTC')


def get_tzname_from_country(country_code):
    """
    Get timezone name by country code
    :param country_code: country code, example: 'cn','us','jp'
    :return: timezone name list
    """
    return pytz.country_timezones(country_code)


def get_all_timezones():
    """
    Get all timezones list
    :return:
    """
    return pytz.all_timezones


def get_common_timezones():
    """
    Get common timezones list
    :return:
    """
    return pytz.common_timezones


def get_timezone_now(tz=None):
    """
    Get datetime object
    :param tz: timezone object
    :return: datetime object
    """
    return datetime.datetime.now(tz=tz)


def convert_timezone(dt, tz=None):
    """
    Convert the timezone of datetime object
    :param dt: datetime object
    :param tz: timezone object
    :return: converted datetime object
    """
    return dt.astimezone(tz=tz)


if __name__ == "__main__":
    print("###" * 30)
    china = get_pytz_timezone(timezone="Asia/Shanghai")
    print(f"China Timezone: {china}")
    china_tz = get_timezone_now(tz=china)
    print(f"China Now: {china_tz}")

    print("***" * 30)
    japan_tz = get_datetime_timezone(interval_hours=9)
    print(f"Japan Timezone: {japan_tz}")
    japan_time = convert_timezone(china_tz, tz=japan_tz)
    print(f"Japan Now: {japan_time}")

    print("***" * 30)
    utc = get_pytz_timezone(timezone='UTC')
    print(f"UTC Timezone: {utc}")
    utc_tz = convert_timezone(china_tz, tz=utc)
    print(f"UTC Now: {utc_tz}")

    print("***" * 30)
    print(f"cn timezone name: {get_tzname_from_country(country_code='cn')}")
    print(f"jp timezone name: {get_tzname_from_country(country_code='jp')}\n")

    print("###" * 30)
    print(f"Local timezone: {get_local_timezone()}\n")

    print("###" * 30)
    print(f"All timezones: {get_all_timezones()}\n")

    print("###" * 30)
    print(f"Common timezone: {get_common_timezones()}\n")

    print("###" * 30)