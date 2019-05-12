curator
----
Organize and archive photos and videos with this simple Python script. I wrote this because I was sick of manually renaming photos and videos in my personal photo archive. Automate everything! This script can be called like this:
::
  # python3 curator.py <destination> <sources...> [--flags arguments]

flags
-----
Here is a list of all available options/flags:

``--year YEAR``
  The year that these photos and videos were taken.
``--month MONTH``
  The month that these photos and videos were taken. Must be in integer format (i.e. 1-12). Zeros are prepended to single-digit month numbers automatically.
``--title TITLE``
  The title for the destination directory. Defaults to ``Album``.
``--initials INITIALS``
  The initials that this script should use to name each photo and video. If not given, this script will pull all of the capital letters from the title and use those as the initials.
  
examples
----

::
  # Copy all photos and videos from source1 and source2 into destination
  python3 curator.py destination source1 source2
