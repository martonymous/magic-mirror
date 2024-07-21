from file_transfer import receive_file

if __name__ == '__main__':
    while True:
        try:
            receive_file(12345, 'audio.txt')
        except Exception as e:
            print(e)
            continue