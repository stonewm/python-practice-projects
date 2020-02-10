import gzip
import os
import tarfile
import zipfile
from unrar import rarfile # pip install unrar

def decompress_rar(src_file, dest_dir):
    """
    Decompress rar file into destination direction
    """
    rv = (True, '')

    try:
        rar = rarfile.RarFile(src_file)
        rar.extractall(dest_dir)
    except Exception as e:
        rv = (False, e)
        return rv

    return rv


def decompress_tar_and_tgz(src_file, dest_dir):
    """
    Decomporess .tar or .tgz file into destination directory
    """
    rv = (True, '')
    try:
        tar = tarfile.open(src_file)
        names = tar.getnames()
        for name in names:
            tar.extract(name, dest_dir)
        tar.close()
    except Exception as e:
        rv = (False, e)
        return rv

    return rv


def decompress_zip(src_file, dest_dir):
    """
    Decompress .zip file into destination folder
    """
    rv = (True, '')
    try:
        zip_file = zipfile.ZipFile(src_file)
        for name in zip_file.namelist():
            zip_file.extract(name, dest_dir)
        zip_file.close()
    except Exception as e:
        rv = (False, e)
        return rv
    
    return rv

def decompress_gz(src_file, dest_dir):
    """
    Decompress .gz file into destination folder
    """
    rv = (True, "")
    try:
        fname = dest_dir + '/' + os.path.basename(src_file)
        gfile = gzip.GzipFile(src_file)
        open(fname, "w+").write(gfile.read())
        gfile.close()
    except Exception as e:
        rv = (False, e)
        return rv

    return rv


def decompress(src_file, dest_dir):
    fname, ext = os.path.splitext(src_file)

    if ext in ('.tgz', '.tar'):
        decompress_tar_and_tgz(src_file, dest_dir)
    elif ext == '.zip':
        decompress_zip(src_file, dest_dir)        
    elif ext == '.rar':
        decompress_rar(src_file, dest_dir)
    elif ext == '.gz':
        decompress_gz(src_file, dest_dir)


def decompress_folder(src_dir):
    files = os.listdir(src_dir)

    for fname in files: # fname is file name with extension
        name, ext = os.path.splitext(fname) # name is file name without extension
        src_file = os.path.join(src_dir, fname)
        dest_path = os.path.join(src_dir, name)
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)

        decompress(src_file, dest_path)
        print(src_file, 'was decompressed.')


if __name__ == '__main__':
    src_dir = r'D:\BaiduNetdiskDownload\尚硅谷SpringMVC视频'
    decompress_folder(src_dir)
