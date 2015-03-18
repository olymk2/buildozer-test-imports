[app]

title = TestImports
package.name = testimports
package.domain = org.testimports
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,glsl,so,6
#version.regex = __version__ = ['"](.*)['"]
version = 1.2.0
#version.filename = %(source.dir)s/main.py

#, --allow-external ctypes --allow-unverified ctypes ctypes
#freetype-py, cairo
requirements = kivy==master, freetype, freetype-py

# (str) Supported orientation (one of landscape, portrait or all)
orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

android.api = 14
android.minapi = 14
android.sdk = 21
android.ndk = 9d
android.branch = feature/freetype


[buildozer]
builddir = /opt/buildozer/testimports
log_level = 2
