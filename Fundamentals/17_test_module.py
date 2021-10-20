print("Test module's name: {}".format(__name__))


if __name__ == '__main__':
    print("My test module was run directly")
else:
    print("My test module was run from import")
