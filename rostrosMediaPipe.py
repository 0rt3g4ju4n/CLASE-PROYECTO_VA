import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5) as face_detection:
    image = cv2.imread('rostro.jpg')
    height, width, _ = image.shape
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)
    print("Detections:", results.detections)
   
    if results.detections is not None:
        for detection in results.detections:
            # Bounding Box
            print(int(detection.location_data.relative_bounding_box.xmin * width))
            xmin = int(detection.location_data.relative_bounding_box.xmin * width)
            ymin = int(detection.location_data.relative_bounding_box.ymin * height)
            w = int(detection.location_data.relative_bounding_box.width * width)
            h = int(detection.location_data.relative_bounding_box.height * height)
            cv2.rectangle(image, (xmin, ymin), (xmin + w, ymin + h), (0, 255, 0), 2)
            # Ojo derecho
            x_RE = int(detection.location_data.relative_keypoints[0].x * width)
            y_RE = int(detection.location_data.relative_keypoints[0].y * height)
            cv2.circle(image, (x_RE, y_RE), 1, (0, 0, 255), 5)
            # Ojo izquierdo
            x_LE = int(detection.location_data.relative_keypoints[1].x * width)
            y_LE = int(detection.location_data.relative_keypoints[1].y * height)
            cv2.circle(image, (x_LE, y_LE), 1, (255, 0, 255), 5)
            # Punta de la nariz
            x_NT = int(detection.location_data.relative_keypoints[2].x * width)
            y_NT = int(detection.location_data.relative_keypoints[2].y * height)
            cv2.circle(image, (x_NT, y_NT), 1, (255, 0, 0), 5)
            # Centro de la boca
            x_MC = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.MOUTH_CENTER).x * width)
            y_MC = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.MOUTH_CENTER).y * height)
            cv2.circle(image, (x_MC, y_MC), 1, (0, 255, 0), 5)
            # Trago de la oreja derecha
            x_RET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.RIGHT_EAR_TRAGION).x * width)
            y_RET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.RIGHT_EAR_TRAGION).y * height)
            cv2.circle(image, (x_RET, y_RET), 1, (0, 255, 255), 5)
            # Trago de la oreja izquierda
            x_LET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.LEFT_EAR_TRAGION).x * width)
            y_LET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.LEFT_EAR_TRAGION).y * height)
            cv2.circle(image, (x_LET, y_LET), 1, (255, 255, 0), 5)
 
    cv2.imshow("Image", image)
    cv2.waitKey(0)
cv2.destroyAllWindows()