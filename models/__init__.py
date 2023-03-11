#!/usr/bin/python3
"""
AirBnB console replication
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
