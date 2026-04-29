import asyncpg
from config import DB_URL

pool = None

async def connect():
    global pool
    pool = await asyncpg.create_pool(DB_URL)

async def execute(query, *args):
    async with pool.acquire() as conn:
        return await conn.execute(query, *args)

async def fetch(query, *args):
    async with pool.acquire() as conn:
        return await conn.fetch(query, *args)

async def fetchrow(query, *args):
    async with pool.acquire() as conn:
        return await conn.fetchrow(query, *args)


async def init_db():
    await execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id BIGINT PRIMARY KEY,
        name TEXT,
        age INT,
        city TEXT,
        gender TEXT,
        search TEXT,
        about TEXT,
        photo TEXT,
        agreed BOOLEAN DEFAULT FALSE
    );
    """)
