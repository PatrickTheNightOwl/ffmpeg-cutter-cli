import os
import subprocess
import shutil
import webbrowser
from tkinter import Tk, filedialog

def cut_video_with_note():
    root = Tk()  # Create a GUI window
    root.withdraw()  # Hide the GUI window, only show the file dialog
    
    # Step 1: Select the video file
    filepath = filedialog.askopenfilename(
        title="Select a video file",
        filetypes=[("Video files", "*.mp4 *.mkv *.mov")]
    )
    if not filepath:
        print(" No video selected. Exiting.")
        return

    # Step 2: Select the folder to save the output
    savingfolder = filedialog.askdirectory(
        title="Select a folder to save the new video"
    )
    if not savingfolder:
        print(" No folder selected. Exiting.")
        return

    print(f"\n Selected video: {filepath}")

    # Step 3: Enter trimming details
    start_time = input(" Enter start time (hh:mm:ss): ")
    end_time = input(" Enter end time (hh:mm:ss): ")
    name = input(" Enter output file name: ").strip()
    if name.endswith(".mp4"):
        name = name[:-4]
    ext = ".mp4"

    output_video = os.path.join(savingfolder, f"{name}{ext}")

    # Step 4: Run FFmpeg to cut the video
    cmd = [
        "ffmpeg",
        "-y",
        "-i", filepath,
        "-ss", start_time,
        "-to", end_time,
        "-c:v", "libx264", "-preset", "slow", "-crf", "18",
        "-c:a", "copy",
        output_video
    ]

    print("\n Processing video...")
    subprocess.run(cmd)

    print(f"\n Done! Saved video at: {output_video}\n")

if __name__ == "__main__":
    if shutil.which('ffmpeg') is None:
        print("FFmpeg is not installed on your system.")
        print("Please install FFmpeg to enable full functionality.")
        while True:
            choice = input("Open FFmpeg download page? [Y/n]: ").strip().lower()
            if choice in ["y", "yes", ""]:
                webbrowser.open("https://ffmpeg.org/download.html")
                break
            elif choice in ["n", "no"]:
                print("❌ Cannot proceed without FFmpeg. Exiting.")
                exit()
            else:
                print("Please enter a valid answer.")
    else:
        while True:
            cut_video_with_note()
            loop = input("Cut another video? (y/n): ").strip().lower()
            if loop != "y":
                print("👋 Goodbye!")
                break
