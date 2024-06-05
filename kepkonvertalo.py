import numpy as np
from PIL import Image
import math

#image in matrix out
def image_to_matrix(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    matrix = np.array(grayscale_image)
    return matrix

character=r" `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
values=[0, 0.0751, 0.0829, 0.0848, 0.1227, 0.1403, 0.1559, 0.185, 0.2183, 0.2417, 0.2571, 0.2852, 0.2902, 0.2919, 0.3099, 0.3192, 0.3232, 0.3294, 0.3384, 0.3609, 0.3619, 0.3667, 0.3737, 0.3747, 0.3838, 0.3921, 0.396, 0.3984, 0.3993, 0.4075, 0.4091, 0.4101, 0.42, 0.423, 0.4247, 0.4274, 0.4293, 0.4328, 0.4382, 0.4385, 0.442, 0.4473, 0.4477, 0.4503, 0.4562, 0.458, 0.461, 0.4638, 0.4667, 0.4686, 0.4693, 0.4703, 0.4833, 0.4881, 0.4944, 0.4953, 0.4992, 0.5509, 0.5567, 0.5569, 0.5591, 0.5602, 0.5602, 0.565, 0.5776, 0.5777, 0.5818, 0.587, 0.5972, 0.5999, 0.6043, 0.6049, 0.6093, 0.6099, 0.6465, 0.6561, 0.6595, 0.6631, 0.6714, 0.6759, 0.6809, 0.6816, 0.6925, 0.7039, 0.7086, 0.7235, 0.7302, 0.7332, 0.7602, 0.7834, 0.8037, 0.9999]

for i in range(len(values)):
    values[i]=int(values[i]*10000*255)

#pixel to character takes an in from 0 to 255 and prints a character
def printer(pixel):
    #pixel=255-pixel
    pixel=pixel*10000
    diff=[]
    for x in range(len(values)):
        diff.append(abs(pixel-values[x]))
    for x in range(len(diff)):
        if diff[x]==min(diff):
            print(character[x], end='')

image_path = r'probakep.jpg'
matrix = image_to_matrix(image_path)

primes1=[]
primes2=[]

for i in range(2, matrix.shape[0]):
    if matrix.shape[0]%i==0:
        if i not in primes1:
            primes1.append(i)

for i in range(2, matrix.shape[1]):
    if matrix.shape[1]%i==0:
        if i not in primes2:
            primes2.append(i)

primes=[]
for i in primes1:
    if i in primes2:
        primes.append(i)
print("The amount of downscaling can be one of these numbers or the multiplication of them:")
print(primes)
leméretezés=int(input("How many times do you want to downscale the image? (maximum 100): "))
print("What y transform do you want to use to counteract the stretching of the characters?")
num=int(input("y transform: "))

x=matrix.shape[1]/leméretezés;
y=matrix.shape[0]/leméretezés;
print(x, y)

extrastep=int(matrix.shape[0]/((matrix.shape[0]-matrix.shape[0]%(num*leméretezés))/num/leméretezés))
db=int(matrix.shape[0]%(num*leméretezés))
print(extrastep, db)

if db==0:
    for i in range(0, matrix.shape[0], int(leméretezés)):
        for j in range(0, matrix.shape[1], int(leméretezés)):
            avg = 0
            for k in range(int(leméretezés)):
                for l in range(int(leméretezés)):
                    avg += matrix[i + k][j + l]
            printer(avg / (leméretezés  * leméretezés))
        print()

# kellene db darabszor extrastep+1 méretű sort átlagolni, majd utána simán extrastep méretű sort átlagolni de fasz tudja már mi történik itt legjobb lenne újraírni a végét
while db>0:
    for i in range(db*extrastep, extrastep+1):
        for j in range(0, matrix.shape[1], int(leméretezés)):
            avg = 0
            for k in range(int(extrastep+1)):
                for l in range(int(leméretezés)):
                    avg += matrix[i + k][j + l]
            printer(avg / ((extrastep+1)  * leméretezés))
        print()
    db=db-1

for i in range(db*extrastep, matrix.shape[0], extrastep):
    for j in range(0, matrix.shape[1], int(leméretezés)):
        avg = 0
        for k in range(int(extrastep)):
            for l in range(int(leméretezés)):
                avg += matrix[i + k][j + l]
        printer(avg / (leméretezés  * leméretezés))
    print()

