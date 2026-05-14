import os
import cv2
import time

def display_sign_language(spoken_text, base_path="ASL/"):
    clean_text = spoken_text.upper().strip()
    
    print("\nAvailable Speeds:")
    print("1: Very Slow (2.0s)")
    print("2: Normal (1.0s)")
    print("3: Fast (0.5s)")
    print("4: Very Fast (0.2s)")
    
    speed_choice = input("Select speed (1-4): ")
    
    speed_map = {"1": 2.0, "2": 1.0, "3": 0.5, "4": 0.2}
    delay = speed_map.get(speed_choice, 1.0)

    for char in clean_text:
        if char == " ":
            char_folder = os.path.join(base_path, "SPACE")
            display_char = "Space"
        else:
            char_folder = os.path.join(base_path, char)
            display_char = char
        
        if os.path.exists(char_folder):
            files = [f for f in os.listdir(char_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
            if files:
                img_path = os.path.join(char_folder, files[0])
                frame = cv2.imread(img_path)
                
                if frame is not None:
                    display_frame = cv2.resize(frame, (600, 600))
                    cv2.rectangle(display_frame, (0, 0), (200, 60), (0, 0, 0), -1)
                    cv2.putText(display_frame, display_char, (20, 45), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)
                    
                    cv2.imshow("Sign Language Translator", display_frame)
                    
                    if cv2.waitKey(int(delay * 1000)) & 0xFF == ord('q'):
                        break
        else:
            print(f"Directory for {char} not found.")

    cv2.destroyAllWindows()

user_input = input("Enter text: ")
display_sign_language(user_input)