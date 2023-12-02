import datetime

from pypika.terms import Function


class FMDate(Function):
    """
    Allows insertion of date into query in FM format.
    ie `DATE 01/12/2024` rather than `DATE(01/12/2024)`
    Uses todays date if no date is supplied.
    """

    def __init__(self, date=None, alias=None):
        if not date:
            date = datetime.datetime.now()
        super(FMDate, self).__init__("DATE", date, alias=alias)
        if isinstance(date, datetime.date):
            print("DATE")
            self.date = date
        elif isinstance(date, str):
            self.date = datetime.datetime.strptime(date, "%Y/%m/%d")

    @property
    def _fm_date_string(self):
        return self.date.strftime("%Y/%m/%d")

    def get_function_sql(self, **kwargs) -> str:
        # DATE 2024/12/01
        return f"{self.name} '{self._fm_date_string}'"
