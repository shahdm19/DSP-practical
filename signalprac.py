import cv2 

def process_video(input_path):

    cap = cv2.VideoCapture(r"D:\XO XO\Uni projects\30FPS Video.mp4")
    
    frames = []
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
            
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        yuv_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2YUV)
        
        frames.append(yuv_frame)
    
    cap.release()
    return frames

video_frames = process_video(r"D:\XO XO\Uni projects\30FPS Video.mp4")  

def classify_frames(frames, i_frame_interval=10):
    frame_types = []
    
    for i, frame in enumerate(frames):
        if i % i_frame_interval == 0:
            frame_types.append('I')
        else:
            frame_types.append('P')
    
    return frame_types

video_path = r"D:\XO XO\Uni projects\30FPS Video.mp4"
frames = process_video(video_path)

print("\n[Video Processing Check]")
print(f"Total frames: {len(frames)}")
if len(frames) > 0:
    print(f"First frame dimensions: {frames[0].shape}")  
    print(f"Frame data type: {frames[0].dtype}")        
else:
    print("Warning: No frames loaded! Check video path.")
    
    
frame_types = classify_frames(frames)
print("\n[Frame Classification Check]")
print(f"First 15 frame types: {frame_types[:15]}")
print(f"Total I-frames: {frame_types.count('I')}")
print(f"Total P-frames: {frame_types.count('P')}")

