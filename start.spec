# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['start.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('C:\Schulprojekt\\datasources\\articles.xlsx', 'datasources/'),
        ('C:\Schulprojekt\\datasources\\customer_data.csv', 'datasources/'),
        ('C:\Schulprojekt\\datasources\\db.sqlite3', 'datasources/'),
        ('C:\Schulprojekt\\datasources\\mock_articles.xlsx', 'datasources/'),
        ('C:\Schulprojekt\\datasources\\orders.sqlite3', 'datasources/'),
        ('C:\Schulprojekt\\datasources\\vehicles.sqlite3', 'datasources/'),
        ('C:\Schulprojekt\\versandplanung\\resources\\templates', 'versandplanung/resources/templates'),
    ],
    hiddenimports=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'versandplanung.vehicles',
        'versandplanung.orders',
        'versandplanung.index',
        'versandplanung.tasks',
        'versandplanung.customer',
        'versandplanung.articles',
        'versandplanung.order_detail'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['C:\Schulprojekt\docs'],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='versandplanung',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
