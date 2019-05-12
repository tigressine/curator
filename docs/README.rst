curator
----
Organize and archive photos and videos with this simple Python script. I wrote this because I was sick of manually renaming photos and videos in my personal photo archive. This script can be called like this:
::
  # python3 curator.py <destination> <sources...> [--flag argument]

flags
-----
Here is a list of all available options/flags:

``--year YEAR``
  The year that your photos and videos were taken.
``--month MONTH``
  The month that your photos and videos were taken. Must be in integer format (i.e. 1-12). Zeros are prepended to single-digit month numbers automatically.
``--title TITLE``
  The title for the destination directory. Defaults to ``Album``.
``--initials INITIALS``
  The initials that this script should use to name each photo and video. If not given, this script will pull all of the capital letters from the title and use those letters as the initials.
  
examples
----
Here are some basic usage examples:
::
  # Copy all media from 'source1' and 'source2' into 'destination'
  python3 curator.py destination source1 source2

  # Copy all media from 'my album' into 'dest' and set the folder
  # date as May, 2016
  python3 curator.py dest "my album" --year 2016 --month 5
  
  # Copy all media from 'source' into 'dest' with the custom album
  # name 'My Big Fat Greek Wedding'
  python3 curator.py dest source --title "My Big Fat Greek Wedding"
  
  # Copy all media from 'source1' and 'source2' into 'archive' with
  # the custom name 'Family Trip' and with the initials 'FAMTRIP'
  python3 curator archive source1 source2 --title "Family Trip" --initials FAMTRIP
