import os
import time
import subprocess
import pygetwindow as gw
import pyperclip
import keyboard

# ✅ Define the path of Google Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# ✅ Check if Google Chrome exists
if not os.path.exists(chrome_path):
    print(f"❌ Google Chrome was not found at the path:\n{chrome_path}")
    exit()

# ✅ Open TikTok profile page
tiktok_profile_url = "https://www.tiktok.com/profile"
try:
    subprocess.Popen([chrome_path, tiktok_profile_url], shell=True)
    print("✅ TikTok profile page opened!")
except Exception as e:
    print(f"❌ An error occurred while trying to open the browser: {e}")
    exit()

# ✅ Wait for Chrome to load and maximize the window
time.sleep(5)
chrome_window = None
for window in gw.getWindowsWithTitle("Google Chrome"):
    chrome_window = window
    break

if chrome_window:
    chrome_window.maximize()  # Set Chrome to full screen mode
    print("✅ Google Chrome window maximized!")

# ✅ Wait for the website to load completely
print("⏳ Waiting for 5 seconds until the site is fully loaded. If the page takes longer than 5 seconds to load, the program won't work...")
time.sleep(5)

# ✅ Open DevTools and run JavaScript to click on the "Reposts" button
keyboard.press_and_release("ctrl+shift+i")  # Open DevTools
time.sleep(2)
keyboard.press_and_release("ctrl+shift+j")  # Switch to Console
time.sleep(1)

# ✅ Solve "allow pasting" issue
pyperclip.copy("allow pasting")  # Copy the command
keyboard.press_and_release("ctrl+v")  # Paste the command in the Console
time.sleep(1.3)
keyboard.press_and_release("enter")  # Execute the command

# ✅ Copy JavaScript code to open the Reposts tab
js_code_open_reposts = """
let interval = setInterval(() => {
    let repostTab = document.querySelector('p[data-e2e="repost-tab"]');
    if (repostTab) {
        repostTab.click();  // Click on the Reposts tab
        console.log("✅ Reposts tab clicked!");
        clearInterval(interval); // Stop the interval after finding the button
    } else {
        console.log("❌ Button not found yet...");
    }
}, 1000); // Check every second
"""
pyperclip.copy(js_code_open_reposts)  # Copy the code

# ✅ Paste the code into DevTools
keyboard.press_and_release("ctrl+v")
time.sleep(0.5)
keyboard.press_and_release("enter")  # Execute the code

# Wait until the Reposts tab is opened
time.sleep(5)

# ✅ Copy JavaScript code to find the first image in Reposts
js_code_find_image = """
let interval = setInterval(() => {
    const firstRepostImage = document.querySelector('.css-1mdo0pl-AVideoContainer'); // Find the first image in the Reposts section
    if (firstRepostImage) {
        console.log("✅ First image in Reposts found");
        firstRepostImage.click();  // Click on the image
        console.log("✅ First image in Reposts clicked!");
        clearInterval(interval); // Stop the interval after finding the image
    } else {
        console.log("❌ Image not found yet...");
    }
}, 1000); // Check every second
"""
pyperclip.copy(js_code_find_image)  # Copy the code

# ✅ Paste the code into DevTools
keyboard.press_and_release("ctrl+v")
time.sleep(1)
keyboard.press_and_release("enter")  # Execute the code

# Start the repeating process (unfollow repost then next)
repost_count = 0
while True:  # Infinite loop until the user presses F1 to stop the program
    if keyboard.is_pressed('*'):  # Check if the user pressed F1
        print(f"✅ Unfollow reposted from {repost_count} videos successfully!")
        break  # Stop the loop when F1 is pressed

    # Click on the <path fill="#FFC300"> (unfollow repost)
    setTimeout_js = """
    setTimeout(() => {
        let element = document.querySelector('path[fill="#FFC300"]');
        if (element) {
            // Access the parent element that contains the path
            let svgElement = element.closest('svg');  // Get the SVG containing the path
            if (svgElement) {
                // Create a click event
                let clickEvent = new MouseEvent('click', {
                    bubbles: true,
                    cancelable: true,
                    view: window
                });

                // Dispatch the event to the parent element
                svgElement.dispatchEvent(clickEvent);
                console.log("✅ Click event dispatched to the parent element!");
            } else {
                console.log("❌ Parent element not found!");
            }
        } else {
            console.log("❌ Element not found!");
        }
    }, 2000);  // Delay for 2 seconds before trying again
    """
    pyperclip.copy(setTimeout_js)  # Copy the code
    keyboard.press_and_release("ctrl+v")
    time.sleep(0.5)
    keyboard.press_and_release("enter")  # Execute the code

    # Wait a few seconds after unfollowing repost
    time.sleep(0.5)

    # Click on the next button (move to the next video)
    next_video_js = """
    let interval = setInterval(() => {
        const nextVideoButton = document.querySelector('button[data-e2e="arrow-right"]'); // Find the next video button
        if (nextVideoButton) {
            nextVideoButton.click();  // Click the button
            console.log("✅ Next video button clicked!");
            clearInterval(interval); // Stop the interval after finding the button
        } else {
            console.log("❌ Button not found yet...");
        }
    }, 1000); // Check every second
    """
    pyperclip.copy(next_video_js)  # Copy the next video code
    keyboard.press_and_release("ctrl+v")
    time.sleep(0.5)
    keyboard.press_and_release("enter")  # Execute the code

    repost_count += 1  # Update the counter for the videos from which repost was unfollowed

    # Wait a few seconds before starting the next iteration
    time.sleep(5)  # You can adjust this time as needed
