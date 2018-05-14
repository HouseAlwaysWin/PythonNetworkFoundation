import argparse


def decodeToBytes(input_bytes):
    input_chars = input_bytes.decode('utf-16')
    print(repr(input_chars))
    return input_chars


def encodeToChar(input_char):
    output_bytes = input_char.encode('utf-8')
    with open('eagle.txt', 'wb') as f:
        f.write(output_bytes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='decode input bytes and encode output character')
    parser.add_argument('-b', metavar='bytes code', type=bytes,
                        default=b'\xff\xfe4\x001\x004\x00\x00i\x00s\x00\x00i\x00n\x00.\x00')
    args = parser.parse_args()
    input = decodeToBytes(args.b)
    encodeToChar(input)