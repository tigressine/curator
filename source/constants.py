"""
"""
import utilities

TRANSFER_METHOD = utilities.copy_method
HANDLE_UNKNOWN_FILETYPES_METHOD = utilities.ignore_unknown_filetypes_method
KNOWN_IMAGE_TYPES = {
    'bmp',
    'png',
    'jpg',
    'jpeg',
    'tiff',
}
KNOWN_VIDEO_TYPES = {
    'mp4',
    'avi',
    'mov',
    'wmv',
}
DIRECTORY_NAME_FORMAT = '{year}-{month} {name}'
FILE_NAME_FORMAT = '{initials}_{number}.{filetype}'
