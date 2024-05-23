#share_incident.py
import tkinter as tk
import Harresment_Details
def si():
    def submit():
        if consent_check:
            # Add code to save data here
            print("Data Providing Page Loaded")
            Harresment_Details.hd()
        else:
            print("Please provide consent.")

    # Create main window
    root2 = tk.Tk()
    root2.title("Share Incident")

    # Create first label
    label1 = tk.Label(root2, text="Share Incident", font=("Helvetica", 18))
    label1.pack(pady=20)

    # Create second label
    label2 = tk.Label(root2, text="We understand it is difficult to recall one's traumatic experiences."
                                 "\nIf you feel uncomfortable at any time, know that you can exit."
                                 "\nIf you do not hit the submit button, your data will not be saved."
                                 "\n"
                                 "\nEven though you are sharing your experience anonymously."
                                 "\nWe need your consent to include your experience in our database of crowd source data", font=("Helvetica", 12))
    label2.pack(pady=10)

    # Create consent checkbox
    consent_var = tk.BooleanVar()
    consent_check = tk.Checkbutton(root2, text="I consent to share my incident", variable=consent_var)
    consent_check.pack(pady=5)

    # Create submit button
    submit_button = tk.Button(root2, text="Next", command=submit)
    #if(submit_button):
    submit_button.pack(pady=10)
    root2.mainloop()

    #submit_button.pack(pady=10)

   # root2.mainloop()