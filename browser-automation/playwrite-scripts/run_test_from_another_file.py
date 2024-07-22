import test_image_upload_another_file

def main():

    print("Running...")
    success = test_image_upload_another_file.run_test("https://www.reduceimages.com/")
    if success:
        print("Script ran successfully with no errors.")
    else:
        print("Script encountered errors.")

if __name__ == "__main__":
    main()