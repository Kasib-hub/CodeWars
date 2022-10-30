def increment_string(strng):
    # grab the char before the ending nums
    head = strng.rstrip('0123456789')
    
    tail = strng[len(head):]
    
    if tail == '':
        return strng+"1"
    
    # zfill prepends zeros to a string to reach specified lenght
    return head + str(int(tail) + 1).zfill(len(tail)) 

print(increment_string('foo')) # foo1
print(increment_string('foobar001')) # foobar002
print(increment_string('foobar1')) # foobar2
print(increment_string('foobar00')) # foobar01
print(increment_string('foobar99')) # foobar100
print(increment_string('foobar099')) # foobar100
print(increment_string('fo99obar99')) # fo99obar100 
print(increment_string('')) # "1"
