from file_transfer import receive_file

if __name__ == '__main__':
    while True:
        try:
            receive_file(3389, 'images/init_images/source_image.jpg')
        except Exception as e:
            print(e)
            continue