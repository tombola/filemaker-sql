from pypika.dialects import MSSQLQuery, MSSQLQueryBuilder
from typing import Any


class FileMakerQuery(MSSQLQuery):
    """
    Defines a query class for use with Microsoft SQL Server.
    """

    @classmethod
    def _builder(cls, **kwargs: Any) -> "FileMakerQueryBuilder":
        return FileMakerQueryBuilder(**kwargs)


class FileMakerQueryBuilder(MSSQLQueryBuilder):
    QUERY_CLS = FileMakerQuery

    def __init__(self, **kwargs: Any) -> None:
        super(MSSQLQueryBuilder, self).__init__(dialect="filemakersql", **kwargs)

        # properties copied from pypika MSSQLQueryBuilder
        self._top: int | None = None
        self._top_with_ties: bool = False
        self._top_percent: bool = False

    def _limit_sql(self) -> str:
        return f" FETCH FIRST {self._limit} ROWS ONLY"
