from PIL import Image


DATE = '20220108'
VENUE = 'my-venue'


HOUR_LIST = ['1205', '1240', '1315', '1350', '1500', '1535']
ADJUSTED_HOUR_LIST = []

for n in range(len(HOUR_LIST)):
    adjusted_hour = int(HOUR_LIST[n])
    ADJUSTED_HOUR_LIST.append(adjusted_hour)

print(ADJUSTED_HOUR_LIST)

for n in range(len(HOUR_LIST)):
    image1 = Image.open(fr'{VENUE}_{DATE}_{HOUR_LIST[n]}.png')
    im1 = image1.convert('RGB')
    im1.save(f'{VENUE}_{DATE}_{ADJUSTED_HOUR_LIST[n]}.pdf')
    curl = fr'curl --include -H "API-KEY: 01511c49-22ae-45ca-8f86-c2d0a8eafb53"  --request POST https://www.racingtv.com/api/sectional  --form "sectional_document[pdf]=@{VENUE}_{DATE}_{ADJUSTED_HOUR_LIST[n]}.pdf"'
    print(curl)

# curl = f'curl --include -H "API-KEY: 01511c49-22ae-45ca-8f86-c2d0a8eafb53"  --request POST https://www.racingtv.com/api/sectional  --form "sectional_document[pdf]=@{VENUE}_{DATE}_{ADJUSTED_HOUR_LIST[0]}.pdf"'
# print(curl)

# curl --include -H "API-KEY: 01511c49-22ae-45ca-8f86-c2d0a8eafb53"  --request POST https://www.racingtv.com/api/sectional  --form "sectional_document[pdf]=@hamilton-park_20210609_1645.pdf"
