[app]
title               = FacebookGuardCLI
package.name        = fbguard
package.domain      = com.example
source.include_exts = py,kv
entrypoint          = main.py

requirements        = python3,kivy,requests,pg8000
android.permissions = INTERNET

version             = 0.1
orientation         = portrait

[buildozer]
log_level           = 2
warn_on_root        = 1
