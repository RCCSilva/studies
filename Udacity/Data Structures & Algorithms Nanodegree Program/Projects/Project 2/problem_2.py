import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if suffix is None:
        raise TypeError('suffix must not be None. It should be a valid string')

    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return None

    contents = map(lambda x: os.path.join(path, x), os.listdir(path))

    result = []
    for content in contents:
        r = find_files(suffix, content)
        if r:
            result += r

    return result


def test():
    '''
    This tests assumes that you have the example folder downloaded and set on the same directory of this file.
    If you don't have it, download it on https://s3.amazonaws.com/udacity-dsand/testdir.zip
    '''

    # Test 1 - Test find .c files
    c_files = find_files('.c', './testdir')
    assert set(c_files) == {'./testdir/t1.c', './testdir/subdir1/a.c',
                            './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c'}

    # Test 2 - Test find .h files
    h_files = find_files('.h', './testdir')
    assert set(h_files) == {'./testdir/t1.h', './testdir/subdir1/a.h',
                            './testdir/subdir5/a.h', './testdir/subdir3/subsubdir1/b.h'}

    # Test 3 - Given non existing extension .py, return empty list
    empty_list = find_files('.py', './testdir')
    assert empty_list == []

    # Test 3 - Given empty extension .py, return all files list
    empty_list = find_files('', './testdir')
    assert set(empty_list) == {'./testdir/t1.c', './testdir/subdir1/a.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c',
                               './testdir/t1.h', './testdir/subdir1/a.h', './testdir/subdir5/a.h', './testdir/subdir3/subsubdir1/b.h',
                               './testdir/subdir4/.gitkeep', './testdir/subdir2/.gitkeep'}

    # Test 3 - Given None existing extension .py, return empty list
    try:
        empty_list = find_files(None, './testdir')
        assert False
    except TypeError as ex:
        assert str(ex) == 'suffix must not be None. It should be a valid string'


if __name__ == "__main__":
    print(f'Starting "{__file__}" tests... ', end='')
    test()
    print('Finished!')
