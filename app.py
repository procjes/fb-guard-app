#!/usr/bin/env python3
# guard.py
# -*- coding: utf-8 -*-

import json
import hashlib
import pg8000
from getpass import getpass
import requests
from datetime import datetime

# ---------- Configuration ----------
DATABASE_CONFIG = {
    'user': 'neondb_owner',
    'password': 'npg_eb9CqgNx6nyK',
    'host': 'ep-orange-cloud-a8bf9lzx-pooler.eastus2.azure.neon.tech',
    'database': 'neondb',
    'ssl_context': True
}
ADMIN_USER = 'admin'
ADMIN_PASS = 'adminpogi'
# -----------------------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def connect():
    return pg8000.connect(**DATABASE_CONFIG)

def init_db():
    with connect() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                ip TEXT NOT NULL,
                created_at_
