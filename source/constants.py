"""
"""
import utilities

KNOWN_IMAGE_TYPES = {
    "bmp",
    "png",
    "jpg",
    "jpeg",
    "tiff",
}
KNOWN_VIDEO_TYPES = {
    "mp4",
    "avi",
    "mov",
    "wmv",
}

DEFAULT_TITLE = "album"
DEFAULT_TITLE_FORMAT = "{year}-{month}_{title}"
DEFAULT_ITEM_FORMAT = "{initials}_{sequence}.{extension}"
DEFAULT_TRANSFER_METHOD = "copy"
TRANSFER_METHOD_CHOICES = {
    "copy",
    "move",
}
DEFAULT_UNKNOWN_EXTENSION_HANDLER = "ignore"
UNKNOWN_EXTENSION_HANDLER_CHOICES = {
    "copy",
    "move",
    "ignore",
}
