import boto3
import csv
import re
import pickle
from tqdm import tqdm
import os

file_names = []
cards_dict = {}


#Get the abbrievated list of all sets
with open("setList", "rb") as f:
    sets = pickle.load(f)


sacnnedCards = open("scannedCards.txt", "a")
scannedCardsDict = open("scannedCardsDict.txt", "a")



failed = 0
success = 0
total = 0

dir = "processed_cards"

rek = boto3.client("rekognition")

for filename in tqdm(os.listdir(dir)):
    f = os.path.join(dir, filename)
    if os.path.isfile(f):
        total += 1
        try:
            with open(f, "rb") as photo:
                resp = rek.detect_text(Image={"Bytes": photo.read()})

            resp = resp["TextDetections"]

            ftext = str(resp[0]['DetectedText'])

            i = 1

            while(ftext.isnumeric() or len(str(ftext)) == 1):
                # print("number")
                ftext = str(resp[i]['DetectedText'])
                i += 1
                if (i > 5):
                    ftext = str(resp[0]['DetectedText'])
                    break

            
            if ftext in cards_dict:
                cards_dict[ftext] += 1
            else:
                cards_dict[ftext] = 1

            string = ftext + "\n"

            sacnnedCards.write(string)

            success += 1
        except:
            failed += 1




success_rate = success / total

for cardName in cards_dict:
    string = str(cards_dict[cardName]) + " " + cardName + "\n"
    try:
        scannedCardsDict.write(string)
    except:
        print("could not write '" + string + "' to file") 


sacnnedCards.close()
scannedCardsDict.close()

print(f"success = {success}, failed = {failed}, sucess rate = {success_rate}")


       
        # number = re.search("\d\d\d?\/\d\d\d?", text)
        # if number:
        #     print(number.group(0))


# reponse = detect_labels(file_names[0], BUCKET_NAME)

# ftext = str(response[0]['DetectedText'])

# print(ftext)