# curator
Organize and archive pictures and videos.

This project is indefinitely on ice, but will be picked up again in the future.

Goal usage:
```
    $ curate destination \
          source1 source2 source3 \
          -d/--date "10-10-10" \
          -m/--method "copy" \
          -u/--unknown-extensions "ignore" \
          -a/--title-format "{year}-{month}_{title}" \
          -i/--item-format "{initials}_{sequence}.{extension}"
```
