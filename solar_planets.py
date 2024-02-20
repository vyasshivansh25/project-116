import cv2

cv2.imread("solar-system.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HESHEY_COMPLAX,
            0.5,
            (255,255,255)
            ),
cv2.putText(img,
            "Mercuary",
            (40,300),
            cv2.FONT_HESHEY_COMPLAX,
            0.5,
            (1,1,1)
            ),
cv2.putText(img,
            "Mars",
            (60,300),
            cv2.FONT_HESHEY_COMPLAX,
            0.5,
            (50,50,50))
cv2.putText(img,
            "Earth",
            (80,300),
            cv2.FONT_HESHEY_COMPLAX,
            0.5,
            (100,100,100)),
cv2.putText(img,
            "Neptune",
            (100,300),
            cv2.FONT_HESHEY_COMPLAX,
            0.5,
            (150,150,150)),
cv2.putText(img,
            "Venus",
            (120,300),
            cv2.FONT_HESHEY_COMPLAX,
            0.5,
            (200,200,200)),
cv2.putText(img,
            "Urenus",
            (140,300),
            cv2.FONT_HESHEY_COMPLAX,
            0.5,
            (225,225,225)),
cv2.putText(img,
            "Jupiter",
            (160,300),
            cv2.FONT_HESHEY_COMPLAX,
            0.5,
            (115,115,115)),
cv2.putText(img,
            "Saturn",
            (180,300),
            cv2.FONT_HESHEY_COMPLAX,
            0.5,
            (65,65,65))

cv2.imwrite("Solar_systemwithname.jpg",img)