Used for recognizing magic the gathering card names, but can be used for other TCG as well.

Upload pictures into a "cards" folder, and use the crop script to crop the pictures to just include the card name, this will speed up the process, but is not neccesary.

The local script takes the pictures from the local directory "processed_cards" and runs them trough the AWS image rekonition service to find text within the image. After finding the text some processing is done to remove as many false positives as possible.
