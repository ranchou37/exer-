[app]
title = HelloTest
package.name = hellotest
package.domain = org.test

source.dir = .
source.include_exts = py

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

[buildozer]
log_level = 2

[android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
