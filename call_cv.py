import cv2

def action(name):

    img = cv2.imread(name, 1)
    cv2.imshow('some', img)
    cv2.waitKey(0)
