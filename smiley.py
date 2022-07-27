
from configparser import NoSectionError
from urllib.parse import _NetlocResultMixinBytes


def count_smileys(arr):
    eyes = ':;'
    nose = '~-'
    mouth = 'D)'
    count = 0
    for face in arr:
        if face[0] in eyes:
            if face[1] in nose:
                if face[2] in mouth:
                        count += 1
            elif face[1] in mouth:
                    count += 1
    return count

    

print(count_smileys([':)',':(',':D',':O',':;']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))