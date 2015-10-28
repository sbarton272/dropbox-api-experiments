import dropbox
import config
import pprint

dbx = dropbox.Dropbox(config.ACCESS_TOK)

def dirSize(curDir):
    size = 0
    children = []
    for entry in dbx.files_list_folder(curDir).entries:
        if type(entry) == dropbox.files.FileMetadata:
            size += entry.size / 1000
        elif type(entry) == dropbox.files.FolderMetadata:
            child = dirSize(entry.path_lower)
            size += child['sz']
            children.append(child)

    # Convert size from Bytes to MB
    return {'sz' : size, 'path': curDir, 'chld' : children}


sizes = dirSize('')

pp = pprint.PrettyPrinter(indent=1)
pp.pprint(sizes)
