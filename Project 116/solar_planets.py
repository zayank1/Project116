import cv2
img = cv2.imread("solar-system.jpg")



cv2.putText(img,
            "sun",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )
cv2.putText(img,
            "mercury",
            (110,250),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.4,
            color=(255,255,255)
            )
cv2.putText(img,
            "venus",
            (190,260),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )
cv2.putText(img,
            "earth",
            (280,270),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.6,
            color=(255,255,255)
            )
cv2.putText(img,
            "mars",
            (385,260),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )
cv2.putText(img,
            "jupiter",
            (530,380),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )
cv2.putText(img,
            "saturn",
            (750,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.8,
            color=(255,255,255)
            )
cv2.putText(img,
            "uranus",
            (940,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.8,
            color=(255,255,255)
            )
cv2.putText(img,
            "neptune",
            (1100,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.8,
            color=(255,255,255)
            )

cv2.imshow("output",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)