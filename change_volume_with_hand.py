import cv2
import mediapipe as mp
import pyautogui
import speech_recognition as sr
import keyboard

# ? Multithreading


class GestureControl:
    def __init__(self) -> None:
        pass


# It pauses for very long even after speaking
# It is working very slow I need to speed it up
# def takeCommand(required_words):
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 0.5
#         r.energy_threshold = 494
#         r.adjust_for_ambient_noise(source, duration=1.5)
#         audio = r.listen(source)

#     try:
#         print("Recognizing..")
#         query = r.recognize_google(audio, language="en-in")
#         # Should take other languages also
#         # Set a keyword for it
#         # Should have other options to use like openai and whisper and azure speech recognition if the user wants
#         print(f"User said: {query}\n")

#         # Check if any of the required words are present in the user's command
#         if any(word in query.lower() for word in required_words):
#             print("Required words found in the user's command.")
#         else:
#             print("Required words not found in the user's command.")

#     except Exception as e:
#         # Handle speech recognition errors
#         print("Error recognizing speech:", e)
#         return "None"

#     return query


# # Example usage:
# required_words = ["weather", "temperature", "joke"]
# user_command = takeCommand(required_words)


# TODO: Start listening in the background
# TODO: Should have a optiion to mute
# TODO: Should not acclerate the volume decreasing (Not good)
# TODO: Should use if GPU: use GPU else CPU
# TODO: It should have a option to pop the camera and not pop the camera
# TODO: It should always run in the background (SOLVED) and (STARTUP at boot) solved
# TODO: Should make a package out of it, compiled into .exe file (SOLVED) TODO: At last

(
    x1,
    y1,
    x2,
    y2,
) = (
    0,
    0,
    0,
    0,
)
webcam = cv2.VideoCapture(0)

my_hands = mp.solutions.hands.Hands()  # capture hands
drawing_utils = mp.solutions.drawing_utils  # draw points in hand

mute_state = False  # Variable to track mute state

while True:
    _, image = webcam.read()
    image = cv2.flip(image, 1)  # 0 = x axis and 1 = y axis
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmarks in enumerate(landmarks):
                x = int(landmarks.x * frame_width)
                y = int(landmarks.y * frame_height)
                if id == 8:  # forefinger id is 8
                    cv2.circle(
                        img=image,
                        center=(x, y),
                        radius=8,
                        color=(0, 255, 255),
                        thickness=3,
                    )
                    x1 = x
                    y1 = y
                if id == 4:  # thumb id is 4
                    cv2.circle(
                        img=image,
                        center=(x, y),
                        radius=8,
                        color=(0, 0, 255),
                        thickness=3,
                    )
                    x2 = x
                    y2 = y

        dist = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (0.5)) // 4
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
        # if dist > 20:
        #     pyautogui.press("volumeup")
        # # elif dist < 8:
        # #     pyautogui.press("volumedown")
        # elif dist < 20:
        #     pyautogui.press("mute")

        if dist > 22:
            keyboard.press_and_release("volume up")
            mute_state = False  # Unmute when adjusting volume
        elif dist < 10 and not mute_state:
            keyboard.press_and_release("volume mute")
            mute_state = True
            # ? Learn more about CONSTANTS, what are those and how to go on with them.
            # ? Will mute_state will be considered a CONSTANT here? how and why? it changes it's value constantly but
            # Set mute state to True to avoid continous muting
        # else:
        #     keyboard.press_and_release("volume down")

    cv2.imshow("Hand volume control using Python", image)
    key = cv2.waitKey(10)
    if key == 27:  # 27 is ASCII of ESC key
        break

webcam.release()
cv2.destroyAllWindows()
