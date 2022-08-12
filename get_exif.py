import pandas as pd
import PIL.Image
#pd.set_option('display.max_columns', 500)
train=pd.read_csv('train_plates.csv')
test=pd.read_csv('test_plates.csv')

print(len(train))
custom_data=[]
import PIL.ExifTags
trgt_keys=['ResolutionUnit', 'ExifOffset', 'Make', 'Model', 'Software', 'Orientation', 'DateTime', 'XResolution', 'YResolution', 'HostComputer', 'ExifVersion', 'ShutterSpeedValue', 'DateTimeOriginal', 'DateTimeDigitized', 'ApertureValue', 'BrightnessValue', 'ExposureBiasValue', 'MeteringMode', 'Flash', 'FocalLength', 'ColorSpace', 'ExifImageWidth', 'DigitalZoomRatio', 'FocalLengthIn35mmFilm', 'OffsetTime', 'OffsetTimeOriginal', 'OffsetTimeDigitized', 'SubsecTimeOriginal', 'SubsecTimeDigitized', 'ExifImageHeight', 'SensingMethod', 'ExposureTime', 'FNumber', 'SceneType', 'ExposureProgram', 'ISOSpeedRatings', 'ExposureMode', 'WhiteBalance', 'LensMake', 'LensModel', 'CompositeImage', 1, 2, 3, 4, 5, 6, 12, 13, 16, 17, 23, 24, 31, '21_gps', '22_gps', '23_gps', '41_gps', '42_gps', '43_gps', 'lens1', 'lens2', 'lens3', 'subjcloc1', 'subjcloc2', 'subjcloc3', 'subjcloc4', 'image_name']

for i in range(len(train)):
    if i==0:
        if 'heic' in train['image_name'][i]:
            img = PIL.Image.open('train/' + train['image_name'][i][:-5] + '.jpg')
            mode = 1
        else:
            img = PIL.Image.open('train/' + train['image_name'][i])
        exif_data = img._getexif()
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }
        exif.update(exif['GPSInfo'])
        del exif['GPSInfo']
        #print(exif)
        exif['21_gps']=exif[2][0]
        exif['22_gps'] = exif[2][1]
        exif['23_gps'] = exif[2][2]
        exif['41_gps']=exif[4][0]
        exif['42_gps'] = exif[4][1]
        exif['43_gps'] = exif[4][2]
        del exif['MakerNote']
        exif['lens1']=exif['LensSpecification'][0]
        exif['lens2'] = exif['LensSpecification'][1]
        exif['lens3'] = exif['LensSpecification'][2]
        del exif['LensSpecification']
        exif['subjcloc1']=exif['SubjectLocation'][0]
        exif['subjcloc2'] = exif['SubjectLocation'][1]
        exif['subjcloc3'] = exif['SubjectLocation'][2]
        exif['subjcloc4'] = exif['SubjectLocation'][3]
        del exif['SubjectLocation']
        exif['image_name']=train['image_name'][i]
        dels = []
        for key in exif.keys():
            if key not in trgt_keys:
                dels.append(key)
        for i in dels:
            del exif[i]
        df=pd.DataFrame(exif)[:1]
        #print(df)

        #exit(0)
        #temp_df=temp_df.drop_duplicates()
    else:
        try:
            mode=0
            if 'heic' in train['image_name'][i]:
                img = PIL.Image.open('train/'+train['image_name'][i][:-5]+'.jpg')
                mode=1
            else:
                img = PIL.Image.open('train/'+train['image_name'][i])
            exif_data = img._getexif()
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in PIL.ExifTags.TAGS
            }
            exif.update(exif['GPSInfo'])
            del exif['GPSInfo']
            #print(exif)
            exif['21_gps']=exif[2][0]
            exif['22_gps'] = exif[2][1]
            exif['23_gps'] = exif[2][2]
            exif['41_gps']=exif[4][0]
            exif['42_gps'] = exif[4][1]
            exif['43_gps'] = exif[4][2]
            del exif['MakerNote']
            exif['lens1']=exif['LensSpecification'][0]
            exif['lens2'] = exif['LensSpecification'][1]
            exif['lens3'] = exif['LensSpecification'][2]
            del exif['LensSpecification']
            exif['subjcloc1']=exif['SubjectLocation'][0]
            exif['subjcloc2'] = exif['SubjectLocation'][1]
            exif['subjcloc3'] = exif['SubjectLocation'][2]
            exif['subjcloc4'] = exif['SubjectLocation'][3]
            del exif['SubjectLocation']
            exif['image_name']=train['image_name'][i]
            dels=[]
            for key in exif.keys():
                if key not in trgt_keys:
                    dels.append(key)
            for i in dels:
                del exif[i]
            #print(exif)
            temp_df=pd.DataFrame(exif)
            temp_df=temp_df.iloc[0]
            df=df.append(temp_df)
        except PIL.UnidentifiedImageError:
            print('-------')
            pass
    print(len(df))
    #exit(0)
print(len(train.columns),len(train))
train=train.merge(df,on='image_name')
print(train)
print(len(train.columns),len(train))
train.to_csv('train_exif.csv',index=False)
print('tr_')


for i in range(len(test)):
    if i==0:
        if 'heic' in test['image_name'][i]:
            img = PIL.Image.open('test/' + test['image_name'][i][:-5] + '.jpg')
            mode = 1
        else:
            img = PIL.Image.open('test/' + test['image_name'][i])
        exif_data = img._getexif()
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }
        exif.update(exif['GPSInfo'])
        del exif['GPSInfo']
        #print(exif)
        exif['21_gps']=exif[2][0]
        exif['22_gps'] = exif[2][1]
        exif['23_gps'] = exif[2][2]
        exif['41_gps']=exif[4][0]
        exif['42_gps'] = exif[4][1]
        exif['43_gps'] = exif[4][2]
        del exif['MakerNote']
        exif['lens1']=exif['LensSpecification'][0]
        exif['lens2'] = exif['LensSpecification'][1]
        exif['lens3'] = exif['LensSpecification'][2]
        del exif['LensSpecification']
        exif['subjcloc1']=exif['SubjectLocation'][0]
        exif['subjcloc2'] = exif['SubjectLocation'][1]
        exif['subjcloc3'] = exif['SubjectLocation'][2]
        exif['subjcloc4'] = exif['SubjectLocation'][3]
        del exif['SubjectLocation']
        exif['image_name']=test['image_name'][i]
        dels = []
        for key in exif.keys():
            if key not in trgt_keys:
                dels.append(key)
        for i in dels:
            del exif[i]
        df=pd.DataFrame(exif)[:1]
        #print(df)

        #exit(0)
        #temp_df=temp_df.drop_duplicates()
    else:
        try:
            mode=0
            if 'heic' in test['image_name'][i]:
                img = PIL.Image.open('test/'+test['image_name'][i][:-5]+'.jpg')
                mode=1
            else:
                img = PIL.Image.open('test/'+test['image_name'][i])
            exif_data = img._getexif()
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in PIL.ExifTags.TAGS
            }
            exif.update(exif['GPSInfo'])
            del exif['GPSInfo']
            #print(exif)
            exif['21_gps']=exif[2][0]
            exif['22_gps'] = exif[2][1]
            exif['23_gps'] = exif[2][2]
            exif['41_gps']=exif[4][0]
            exif['42_gps'] = exif[4][1]
            exif['43_gps'] = exif[4][2]
            del exif['MakerNote']
            exif['lens1']=exif['LensSpecification'][0]
            exif['lens2'] = exif['LensSpecification'][1]
            exif['lens3'] = exif['LensSpecification'][2]
            del exif['LensSpecification']
            exif['subjcloc1']=exif['SubjectLocation'][0]
            exif['subjcloc2'] = exif['SubjectLocation'][1]
            exif['subjcloc3'] = exif['SubjectLocation'][2]
            exif['subjcloc4'] = exif['SubjectLocation'][3]
            del exif['SubjectLocation']
            exif['image_name']=test['image_name'][i]
            dels=[]
            for key in exif.keys():
                if key not in trgt_keys:
                    dels.append(key)
            for i in dels:
                del exif[i]
            temp_df=pd.DataFrame(exif)
            temp_df=temp_df.iloc[0]
            df=df.append(temp_df)
        except PIL.UnidentifiedImageError:
            print(test['image_name'][i])
            pass
    #exit(0)
print(len(test.columns))
print(len(test))
test=test.merge(df,on='image_name')
print(len(test.columns))
print(len(test))
test.to_csv('test_exif.csv',index=False)
