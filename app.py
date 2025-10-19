import customtkinter as ctk
import speedtest
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Internet Speed Test")
app.geometry("420x380")

def test_speed():
    result_label.configure(text="Testing...", text_color="yellow")
    app.update_idletasks()
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        ping = st.results.ping
        result_label.configure(
            text=f"Download: {download:.2f} Mbps\nUpload: {upload:.2f} Mbps\nPing: {ping:.0f} ms",
            text_color="lightgreen"
        )
    except Exception as e:
        result_label.configure(text=f"Error: {e}", text_color="red")

def run_test():
    threading.Thread(target=test_speed, daemon=True).start()

title = ctk.CTkLabel(app, 
                     text="🌐 Internet Speed Test", 
                     font=("Segoe UI", 26, "bold"))
title.pack(pady=25)

test_button = ctk.CTkButton(app, 
                            text="Start Test", 
                            command=run_test, 
                            height=50, width=220, 
                            corner_radius=20, 
                            font=("Segoe UI", 18, "bold"))
test_button.pack(pady=15)

result_label = ctk.CTkLabel(app, 
                            text="Click to test speed", 
                            font=("Segoe UI", 18, "bold"))
result_label.pack(pady=40)

app.mainloop()
