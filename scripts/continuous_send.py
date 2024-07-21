from file_transfer import send_file

if __name__ == '__main__':
    while True:
        try:
            send_file('81.205.194.201', 56789, 'outputs/img2img-samples/samples/mirror.png')
        except Exception as e:
            print(e)