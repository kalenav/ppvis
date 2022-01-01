#include "date_class.h"

Date::Date() {};
Date::Date(int day_in, int month_in, int year_in)
{
	day = day_in;
	month = month_in;
	year = year_in;
}

int Date::getDay() { return day; }
int Date::getMonth() { return month; }
int Date::getYear() { return year; }