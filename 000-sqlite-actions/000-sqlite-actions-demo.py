#!/usr/bin/env python
import sqlite3, re, json
conn = sqlite3.connect(":memory:")

# Simple example of a UDF
conn.create_function(
    "split",
    2,
    lambda pattern, string: json.dumps(re.split(pattern, string)))
cursor = conn.execute(
    r"SELECT key, value FROM json_each(split('\W+', 'the cat'));")


# File metadata UDF
def file_size(name):
    ''' Stub to find a file's size '''
    return 8282
def file_perm(name):
    ''' Stub to find a file's permissions '''
    return 640

conn.execute("CREATE TABLE filenames(name TEXT)")
conn.executemany("INSERT INTO filenames(name) VALUES (?)", [["foo"], ["bar"], ["baz"]])
names = conn.execute("SELECT name FROM filenames;").fetchall()
cursor.executemany(
    "INSERT INTO file_status(size, perm, name) VALUES (?,?,?);",
    # This whole list goes into memory before we start
    [[file_size(name), file_perm(name), name]
        for name in names
    ]
)

conn.create_function("file_size", 1, file_size)
conn.create_function("file_perm", 1, file_perm)
cursor.execute(
    # This is evaluated as we go
    """INSERT INTO file_status(size, perm, name)
    SELECT file_size(name), file_perm(name), name
    FROM filenames;"""
)