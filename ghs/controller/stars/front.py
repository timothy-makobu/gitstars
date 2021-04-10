from typing import Any, Optional, Union

from asyncpg import Record

from ghs.model.database.database import Database


class Pager:

    __slots__ = ("dbh", "offset", "limit", "total_pages")

    def __init__(self, dbh: Database = Database()) -> None:
        self.dbh: Database = dbh
        self.limit: int = 20
        self.offset: int = 0
        self.total_pages: Union[int, Record, None] = None

    async def page(self) -> Any:

        await self.dbh.init_db()

        self.total_pages = await self.dbh.read("SELECT count(*) FROM project")
        self.total_pages = int(self.total_pages[0]["count"]) // self.limit

        for row in await self.dbh.read(
            f"""
                SELECT add_time, project.name, description, pro_lang.name as language, url,
                initial_stars, current_stars, initial_fork_count, current_fork_count
                FROM project
                JOIN pr_pl ON pr_pl.pr_id = project.project_id
                JOIN pro_lang ON pro_lang.language_id = pr_pl.pl_id
                ORDER BY current_stars DESC
                LIMIT {self.limit}
                OFFSET {self.offset}
            """.strip()
        ):
            yield row

        self.offset += 20
