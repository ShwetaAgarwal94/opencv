#Task 4.1
import numpy
import cv2
photo = numpy.zeros([200,200,3])
p1 = (50,130)
p2 = (150,130)
p3 = (100,75)
triangle = numpy.array([p1,p2,p3])
photo1 = cv2.fillPoly(photo, [triangle], color = (0,0,255))
photo[130:200, 50:150] = [255,0,0]
photo[160:200,90:110] = [0,255,0]
cv2.imshow('hii',photo)
cv2.waitKey()==13
cv2.destroyAllWindows()
