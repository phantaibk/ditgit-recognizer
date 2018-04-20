import numpy as np
from scipy.misc.pilutil import Image
import imageio
import xlwt
import cv2
import scipy.misc as mi
from keras.models import model_from_json 

def reStoreModel():
    
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    return loaded_model

def getDigit1(image):
    test = np.asarray(image)
    test.setflags(write=1)
    for x in test:
        i = 0
        for y in x:
            t = 255 - y
            x[i] = t
            i += 1
    for x in test:
        i = 0
        for y in x:
            if y < 40:
                x[i] = 0
            i += 1
    test[0] = 0
    test[1] = 0
    test[2] = 0
    test[3] = 0
    for x in test:
        i = 0
        x[0] = 0
        x[1] = 0
        x[2] = 0
        x[len(x)-1] = 0
        x[len(x)-2] = 0
        x[len(x)-3] = 0
        i += 1
        
    # xoa duong ke ngang
    arr = []
    for x in test:
        i = 3
        j = 0
        if x[3] > 30 or x[4] > 30 or x[5] > 30:
            a = 0
            for y in x:
                if a < 40:
                    x[i] = 0
                    arr[i] = 0
                else:
                    arr[i] = x[i]
                    break
                # print(arr)
                i += 1
                if i > len(x) - 1:
                    break
                else:
                    a = arr[i]
                    # print(a)
            k = len(x) - 3
            for y in x:
                if arr[k - j] < 40:
                    x[k - j] = 0
                    arr[k - j] = 0
                else:
                    arr[k - j] = x[k - j]
                    break
                # print(arr)
                j += 1
        else:
            arr.clear()
            for y in x:
                arr.append(y)
                i += 1
    
    # tinh kich thuoc so
    pixel_a = 0
    i = 0
    for column in test.T:
        j = 0
        for x in column:
            if j > len(column) - 5:
                break
            if x > 30:
                pixel_a = i
                break
            j += 1
        if pixel_a > 0:
            break
        i += 1
    digit_width = 0
    i = 0
    for column in test.T:
        if i < pixel_a + 13:
            i += 1
            continue
        j = 0
        for x in column:
            if j < 3:
                j += 1
                continue
            if j == len(column) - 12:
                break
            if x == 0:
                check = 1
                j += 1
                continue
            else:
                check = 0
                break
        if check == 1:
            digit_width = 5
            break
        else:
            digit_width = 13
            break
        i += 1
    pixel_b = 0
    i = 0
    for column in test.T:
        if i < pixel_a + digit_width:
            i += 1
            continue
        j = 0
        for x in column:
            if j < 3:
                j += 1
                continue
            if j == len(column) - 13:
                break
            if x == 0:
                check = 1
                j += 1
                continue
            else:
                check = 0
                break
        if check == 1:
            pixel_b = i
            break
        i += 1
    if pixel_b > pixel_a + 30:
        pixel_b = pixel_a + 20
        
    # get digit
    test_width = len(test[0])
    for column in test.T:
        test_weight = len(column)
        break
    # digit1 = np.empty((0,20), int)
    digit1 = []
    i = 0
    k = 1
    for x in test:
        if i < 3:
            i += 1
            continue
        j = 0
        arr1 = []
        for y in x:
            if j < pixel_a - 3:
                j += 1
                continue
            arr1.append(y)
            j += 1
            if j == pixel_b:
                arr1.append(0)
                arr1.append(0)
                arr1.append(0)
                break
        if i > test_weight - 4:
            arr1[pixel_b - pixel_a + 2] = 0
        digit1.append(arr1)
        # digit1 = np.append(digit1, arr1[0], axis=0)
        i += 1
    arr2 = []
    for x in arr1:
        arr2.append(0)
    digit1.append(arr2)
    digit1.append(arr2)
    # imageio.imwrite('input/digit1.jpg', np.asarray(digit1))
    mi.imsave('input/digit1.jpg', digit1)
# =============================================================================
#     digit_img = Image.open('input/digit1.jpg').convert('L')
#     digit_arr = np.asarray(digit_img)     
#     digit_arr.setflags(write=1)
# =============================================================================
    
def getDigit2(image):
    test = np.asarray(image)
    test.setflags(write=1)
    for x in test:
        i = 0
        for y in x:
            t = 255 - y
            x[i] = t
            i += 1
    for x in test:
        i = 0
        for y in x:
            if y < 40:
                x[i] = 0
            i += 1
    test[0] = 0
    test[1] = 0
    test[2] = 0
    test[3] = 0
    for x in test:
        i = 0
        x[0] = 0
        x[1] = 0
        x[2] = 0
        x[len(x)-1] = 0
        x[len(x)-2] = 0
        x[len(x)-3] = 0
        i += 1
        
    # xoa duong ke ngang
    arr = []
    for x in test:
        i = 3
        j = 0
        if x[3] > 30 or x[4] > 30 or x[5] > 30:
            a = 0
            for y in x:
                if a < 40:
                    x[i] = 0
                    arr[i] = 0
                else:
                    arr[i] = x[i]
                    break
                # print(arr)
                i += 1
                if i > len(x) - 1:
                    break
                else:
                    a = arr[i]
                    # print(a)
            k = len(x) - 3
            for y in x:
                if arr[k - j] < 40:
                    x[k - j] = 0
                    arr[k - j] = 0
                else:
                    arr[k - j] = x[k - j]
                    break
                # print(arr)
                j += 1
        else:
            arr.clear()
            for y in x:
                arr.append(y)
                i += 1
    
    # tinh kich thuoc so
    pixel_a = 0
    i = 0
    for column in reversed(test.T):
        j = 0
        for x in column:
            if j > len(column) - 5:
                break
            if x > 30:
                pixel_a = i
                break
            j += 1
        if pixel_a > 0:
            break
        i += 1
    digit_width = 0
    i = 0
    for column in reversed(test.T):
        if i < pixel_a + 13:
            i += 1
            continue
        j = 0
        for x in column:
            if j < 3:
                j += 1
                continue
            if j == len(column) - 12:
                break
            if x == 0:
                check = 1
                j += 1
                continue
            else:
                check = 0
                break
        if check == 1:
            digit_width = 5
            break
        else:
            digit_width = 13
            break
        i += 1
    pixel_b = 0
    i = 0
    for column in reversed(test.T):
        if i < pixel_a + digit_width:
            i += 1
            continue
        j = 0
        for x in column:
            if j < 3:
                j += 1
                continue
            if j == len(column) - 13:
                break
            if x == 0:
                check = 1
                j += 1
                continue
            else:
                check = 0
                break
        if check == 1:
            pixel_b = i
            break
        i += 1
    if pixel_b > pixel_a + 30:
        pixel_b = pixel_a + 20
        
    # get digit
    test_width = len(test[0])
    for column in reversed(test.T):
        test_weight = len(column)
        break
    digit = []
    i = 0
    k = 1
    for x in test:
        if i < 3:
            i += 1
            continue
        j = 0
        arr1 = []
        for y in reversed(x):
            if j < pixel_a - 3:
                j += 1
                continue
            arr1.append(y)
            j += 1
            if j == pixel_b:
                arr1.append(0)
                arr1.append(0)
                arr1.append(0)
                break
        if i > test_weight - 4:
            arr1[pixel_b - pixel_a + 2] = 0
        digit.append(arr1)
        # digit1 = np.append(digit1, arr1[0], axis=0)
        i += 1
    arr2 = []
    for x in arr1:
        arr2.append(0)
    digit.append(arr2)
    digit.append(arr2)
    imageio.imwrite('input/digit2.jpg', np.asarray(digit))
    # mi.imsave('input/digit2.jpg', digit)
# =============================================================================
#     digit_img = Image.open('input/digit2.jpg').convert('L')
#     digit_arr = np.asarray(digit_img)
#     digit_arr.setflags(write=1)
# =============================================================================
    
def recognizeDigit(cnnModel, digit_location):
    digit_img = Image.open(digit_location).convert('L')
    digit_arr = np.asarray(digit_img)
    digit_arr.setflags(write=1)
    digit_arr = cv2.resize(digit_arr, (28, 28))
    digit_arr[0] = 0
    digit_arr[1] = 0
    digit_arr[2] = 0
    for x in digit_arr:
        i = 0
        for y in x:
            if y < 30:
                x[i] = 0
            i += 1
# =============================================================================
#     arr = []
#     for x in digit1_arr:
#         i = 0
#         if x[27] > 30:
#             x[27] = 0
#             x[26] = 0
#             for y in x:
#                 if arr[25 - i] < 70:
#                     x[25 - i] = 0
#                     arr[25 - i] = 0
#                 else:
#                     arr[25 - i] = x[25 - i]
#                     break
#                 i += 1
#         else:
#             arr.clear()
#             for y in x:
#                 arr.append(y)
# =============================================================================
    
    # img = np.zeros((20,20,3), np.uint8)
    # mi.imsave('test.jpg', test)
    
    digit_arr = digit_arr / 255.0
    digit_arr = digit_arr.reshape(-1,28,28,1)
    # predict results
    results = cnnModel.predict(digit_arr)
    # select the indix with the maximum probability
    accuracy  = np.amax(results,axis = 1)
    results = np.argmax(results,axis = 1)
    ketqua = [results[0], accuracy[0]]
    # results = pd.Series(result,name="Label")
    return ketqua
    
model = reStoreModel()
direction = 'input/pic.png'
input_img = Image.open(direction).convert('L')

# =============================================================================
# img = input_img.crop((585, 675, 653, 701))
# getDigit1(img)
# getDigit2(img)
# digit1_location = 'input/digit1.jpg'
# digit2_location = 'input/digit2.jpg'
# digit1 = recognizeDigit(model, digit1_location)
# digit2 = recognizeDigit(model, digit2_location)
# if digit2[0] != 0:
#     digit2[0] = 5
# print("Ket qua: %s,%s (%s)" %(digit1[0], digit2[0], digit1[1]))
# =============================================================================

coordinates = []
result = []
digit_arr = [2,4,2,5,6,7,3,3,6,2,3,4,7,5,5,3,5,7,6,5,9,4,5,1,6,5]
coordinates.append([582, 48, 650, 74])
coordinates.append([582, 74, 651, 100])
coordinates.append([582, 127, 651, 152]) #2
coordinates.append([583, 153, 651, 178])
coordinates.append([583, 178, 651, 204]) #xsthap
coordinates.append([583, 204, 651, 230])
coordinates.append([583, 231, 651, 257])
coordinates.append([583, 257, 651, 282])
coordinates.append([583, 283, 651, 309])
coordinates.append([584, 336, 651, 362])
coordinates.append([584, 361, 652, 388])
coordinates.append([584, 388, 652, 414])
coordinates.append([584, 414, 652, 440]) #xsthap
coordinates.append([584, 440, 652, 466])
coordinates.append([584, 466, 652, 492])
coordinates.append([584, 492, 653, 518])
coordinates.append([585, 518, 653, 544])
coordinates.append([585, 570, 653, 596])
coordinates.append([585, 596, 653, 622])
coordinates.append([585, 622, 653, 648])
coordinates.append([585, 648, 653, 675]) #xsthap
coordinates.append([585, 675, 653, 701])
coordinates.append([585, 701, 653, 728])
coordinates.append([585, 727, 653, 754]) #xsthap
coordinates.append([585, 753, 654, 780]) #xsthap
coordinates.append([585, 780, 654, 806])

book = xlwt.Workbook()
sh = book.add_sheet("Sheet 1")
sh.write(0, 0, 'STT')
sh.write(0, 1, 'Diem')
sh.write(0, 2, 'Do chinh xac')
sh.write(0, 3, 'Ghi chu')
i = 1
for x in coordinates:
    img = input_img.crop(x)
    getDigit1(img)
    getDigit2(img)
    digit1_location = 'input/digit1.jpg'
    digit2_location = 'input/digit2.jpg'
    digit1 = recognizeDigit(model, digit1_location)
    digit2 = recognizeDigit(model, digit2_location)
    if digit2[0] != 0:
        digit2[0] = 5
    sh.write(i, 0, i)
    sh.write(i, 1, str(str(digit1[0]) + ',' + str(digit2[0])))
    sh.write(i, 2, str(round(digit1[1], 4)))
    if digit1[1] < 0.5:
        sh.write(i, 3, 'xac xuat thap')
    # print("Ket qua: %s,%s (%s)" %(digit1[0], digit2[0], digit1[1]))
    i += 1
    
book.save('output/result.xls')

# =============================================================================
# for x in coordinates:
#     img1 = img.crop(x)
#     digit = recognizeDigit(model, img1)
#     result.append(digit)
# # np.set_printoptions(threshold=np.nan)
# i = 0
# for x in result:
#     if x[0] == digit_arr[i] and x[1] >= 0.5:
#         print(x)
#     elif x[0] == digit_arr[i] and x[1] < 0.5:
#         print("%s --> xác suất thấp" %x)
#     elif x[0] != digit_arr[i] and x[1] > 0.5:
#         print("%s --> sai(%s), xác suất cao" %(x, digit_arr[i]))
#     else:
#         print("%s --> sai(%s)" %(x, digit_arr[i]))
#     i += 1
# =============================================================================
    
