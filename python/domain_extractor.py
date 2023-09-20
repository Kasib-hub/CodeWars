# Description: Extracts the domain name from a URL

def domain_name(url):
    # list of strings to remove from url
    junk = [ "www.", "https://", "http://"]

    # list of indices of periods in url
    indices = []
    
    # iterate through junk and remove from url
    for strng in junk:
        url = url.replace(strng, "")
    
    # iterate through the resulting url and find indices of periods
    for i, char in enumerate(url):
        if char == ".":
            indices.append(i)
    
    # if there are two periods, return the substring between the first and second
    return url[0 : indices[0]]