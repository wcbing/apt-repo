#!/usr/bin/env python3

import sqlite3

# create table
conn = sqlite3.connect("data/deb.db")
conn.execute(
    """
        CREATE TABLE IF NOT EXISTS amd64 (
            name TEXT UNIQUE,
            version TEXT,
            url TEXT
        );
    """
)
conn.execute(
    """
        CREATE TABLE IF NOT EXISTS arm64 (
            name TEXT UNIQUE,
            version TEXT,
            url TEXT
        );
    """
)
conn.execute(
    """
        CREATE TABLE IF NOT EXISTS 'all' (
            name TEXT UNIQUE,
            version TEXT,
            url TEXT
        );
    """
)

conn.commit()
conn.close()
