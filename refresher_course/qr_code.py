import hashlib
import datetime
import qrcode


def qr_code_function(ob):
    # Convert the date object to a string and encode it
    date_str = str(ob.jshshr).encode('utf-8')
    # Create a hash object using the SHA-256 algorithm
    hash_object = hashlib.md5()
    # Update the hash object with the encoded date string
    hash_object.update(date_str)
    # Get the hexadecimal representation of the hash
    hex_digest = hash_object.hexdigest()
    # Print the hash
    # Importing library
    # Data to be encoded
    data = f'https:www.ilmiymarkaz.com/{hex_digest}/'
    # Encoding data using make() function
    img = qrcode.make(data)
    # Saving as an image file
    img.save(f'media/qr_codes/{hex_digest}.png')
    return hex_digest
