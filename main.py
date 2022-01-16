import threading

import cv2

#tableau dans lequel est enregistré les personnes
liste = []

#id des personnes
i = 0

#fonction qui recherche les personnes
def recherche(fichier):

    #le modèle a rechercher dans la vidéo
    body_cascade = cv2.CascadeClassifier(fichier)

    #la vidéo en question
    cap = cv2.VideoCapture('sample.mp4')

    #boucle de recherche
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        body = body_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
        #dessin des rectangles
        for x, y, w, h in body:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            #les ajoutes au tableau
            liste.append(f'id : {i}, x: {x} y: {y}')
            i = i+1
        if cv2.waitKey(1) == ord('q'):
            break
        #affiche la vidéo
        cv2.imshow('video', frame)
    cap.release()
    cv2.destroyAllWindows()

#fonction de collecte des données depuis le tableau vers le fichier texte
def collecte():
    while True:
        with open('localisation.txt', 'w') as f:
            for x in liste:
                f.write(f'{x}\n')

        print(liste)

#lancement des threads
t1 = threading.Thread(target=recherche, args=("./haarcascade_fullbody.xml",))
t2 = threading.Thread(target=collecte, args=())
t1.start()
t2.start()
t1.join()
t2.join()
