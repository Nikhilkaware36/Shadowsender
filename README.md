💀 ShadowSender - Anonymous Scare Mail Tool 💀

 

Created by: Nikhil Santosh KawareGitHub: @Nikhilkaware36

⚠️ Disclaimer

This tool is developed strictly for educational and demonstration purposes only. Do not use it for illegal or malicious purposes. The creator is not responsible for any misuse of this tool.

🚀 Introduction

ShadowSender allows you to send anonymous scare mails using either saved SMTP credentials or saved email credentials (like Gmail,protonmail , etc).

Perfect for:

Cybersecurity awareness demos

Testing mail spoofing setups

Educational training

📁 Folder Structure

    Shadowsender/
    ├── login/
    │   ├── my-mails.txt      # Saved email credentials
    │   └── my-smtp.txt       # Saved SMTP config
    ├── uninstall.sh          # Script to clean up the tool
    ├── requirements.txt      # Python dependencies
    ├── shadow.py             # Main tool script
    └── README.md             # Project documentation

🛠️ Installation

🔸 Step 1: Clone the Repository
    
    git clone https://github.com/Nikhilkaware36/Shadowsender.git
    cd Shadowsender

🔸 Step 2: Install Dependencies

    pip install -r requirements.txt

🔸 Step 3: Add Your Credentials

Option 1: Gmail credentials (login/my-mails.txt)

    EMAIL=myemail@gmail.com
    PASSWORD=my-app-password

Option 2: SMTP credentials (login/my-smtp.txt)

    HOST=test.io
    PORT=2525
    USERNAME=test@1234
    PASSWORD=test@1234

Note: Gmail requires App Passwords if 2FA is enabled.

🎯 How to Use

    python shadow.py

It will prompt you to use saved credentials.

Enter recipient, subject, and message.

Choose a theme or type your own.

🧽 Uninstall Tool

To remove all tool files from your system:

    chmod +x uninstall.sh
    ./uninstall.sh


✨ Author

Nikhil KawareGitHub: @Nikhilkaware36

Happy Hacking! 😈

