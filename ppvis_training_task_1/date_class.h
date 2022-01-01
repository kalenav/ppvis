class Date
{
private:
	int day = 1;
	int month = 1;
	int year = 2000;
public:
	Date();
	Date(int day_in, int month_in, int year_in);
	int getDay();
	int getMonth();
	int getYear();
};