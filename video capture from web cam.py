import cv2
capture = cv2.VideoCapture(0)
while (True):
    ret, frame = capture.read(0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    cv2.imshow('image', gray)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
