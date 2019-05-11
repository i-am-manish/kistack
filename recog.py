import cv2

def numrecog(name):
    image = cv2.imread(name, 0)
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    edges = cv2.Canny(image, 100, 200)
    cv2.imshow('kistack', edges)
    cv2.waitKey(0)
