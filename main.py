import threading

import cv2

liste = []
i = 0
def recherche(fichier):
    body_cascade = cv2.CascadeClassifier(fichier)
    cap = cv2.VideoCapture('sample.mp4')

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        body = body_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
        for x, y, w, h in body:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            liste.append(f'id : {i}, x: {x} y: {y}')
            i++
        if cv2.waitKey(1) == ord('q'):
            break
        cv2.imshow('video', frame)
    cap.release()
    cv2.destroyAllWindows()


def collecte():
    while True:
        with open('localisation.txt', 'w') as f:
            for x in liste:
                f.write(f'{x}\n')

        print(liste)


t1 = threading.Thread(target=recherche, args=("./haarcascade_fullbody.xml",))
t2 = threading.Thread(target=collecte, args=())
t1.start()
t2.start()
t1.join()
t2.join()
